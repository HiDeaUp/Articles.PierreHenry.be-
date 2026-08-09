#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path


DEFAULT_SOURCE = Path.home() / "Code" / "youtube-to-medium-blog-posts-automation" / "articles"
DEFAULT_TARGET = Path(__file__).resolve().parent.parent / "content" / "blog"

ENGLISH_MARKERS = {
    "the", "and", "you", "your", "with", "that", "this", "from", "for", "are",
    "have", "will", "more", "than", "when", "what", "work", "time", "life", "can",
    "focus", "build", "better", "engineer", "software", "travel", "money", "productivity",
    "habit", "habits", "project", "projects", "business", "future", "today", "people",
    "great", "simple", "learn", "using", "without", "start", "stop", "into", "want",
}

FRENCH_MARKERS = {
    "le", "la", "les", "de", "des", "du", "un", "une", "et", "en", "à", "au",
    "que", "pour", "avec", "dans", "est", "pas", "plus", "comment", "faire", "tout",
    "bien", "vie", "temps", "sur", "ton", "ta", "ses", "pourquoi", "réussir", "grâce",
    "mieux", "jour", "jours", "être", "comme", "par", "sans", "encore", "cela", "quand",
    "nous", "vous", "mon", "tes", "leurs", "avoir", "travail", "projet", "idées",
}

PRIORITY_TOPICS = {
    "tech": {
        "software engineering", "software engineer", "developer", "developers", "coding", "code",
        "programming", "ai", "copilot", "cursor", "mcp", "claude", "chatgpt", "react",
        "python", "terminal", "repository", "codebase", "data science", "electron",
    },
    "nomad": {
        "travel", "travelling", "traveling", "nomad", "digital nomad", "remote work", "remote",
        "location independence", "expat", "airport", "backpack", "kuala lumpur", "thailand", "vietnam",
    },
    "money": {
        "money", "salary", "pay", "negotiation", "income", "freelance", "freelancer", "revenue",
        "pricing", "finance", "financial", "invest", "investing", "rich", "wealth", "bonus",
        "contract", "equity", "stock options", "esop", "isop",
    },
    "wealth": {
        "wealth", "rich", "invest", "investing", "assets", "capital", "financial freedom",
        "net worth", "lifestyle inflation",
    },
    "self-transcendence": {
        "self transcendence", "self-transcendence", "self realization", "self-realization",
        "meaning", "purpose", "inner peace", "mindfulness", "gratitude", "presence",
        "fulfillment", "fulfilment", "higher self", "spiritual growth", "transcendence",
        "self awareness", "self-awareness",
    },
    "time management": {
        "time management", "schedule", "scheduling", "calendar", "plan your week", "weekly plan",
        "daily plan", "priorities", "priority", "organize", "organise", "planning",
    },
    "tasks": {
        "tasks", "task", "to-do", "todo", "checklist", "execute", "execution", "finish what you start",
    },
    "productivity": {
        "productivity", "focus", "deep work", "pomodoro", "efficiency", "efficient", "organize",
        "workflow", "workload", "system", "systems",
    },
    "time blocking": {
        "time blocking", "time boxing", "timeboxing", "time-boxing", "time-blocking",
    },
    "entrepreneurship": {
        "entrepreneur", "entrepreneurship", "solopreneur", "startup", "saas", "business", "audience",
        "offer", "freelance", "brand", "side business", "side hustle",
    },
}

HEADING_REPLACEMENTS = {
    "tl;dr / key takeaways": "## Key Takeaways",
    "tl;dr & key takeaways": "## Key Takeaways",
    "key takeaways": "## Key Takeaways",
    "tl;dr": "## Key Takeaways",
    "actions list": "## Action Steps",
    "action steps": "## Action Steps",
    "ask yourself": "## Reflection",
    "what about you": "## Reflection",
    "what about you?": "## Reflection",
}

PROMO_MARKERS = {
    "book.ph7.me",
    "podcasts.ph7.me",
    "masterclass.ph7.me",
    "ko-fi.com/phenry",
    "retainr.io",
    "substack.com/@pierrehenry",
    "open-source projects i've built",
    "open source projects i've built",
    "subscribe to my youtube channel",
    "support my work with a coffee",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import French markdown articles into Hugo blog posts.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Source article directory")
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET, help="Target Hugo content/blog directory")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--clean", action="store_true", help="Delete previously generated blog posts before importing")
    mode.add_argument("--only-new", action="store_true", help="Import only articles that do not already exist in the target")
    parser.add_argument(
        "--include-slug",
        action="append",
        default=[],
        help="Import only an article with this slug derived from its optimized title. Repeat for curated batches.",
    )
    return parser.parse_args()


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    raw_front_matter = parts[0].removeprefix("---\n")
    body = parts[1]
    data: dict[str, str] = {}
    for raw_line in raw_front_matter.splitlines():
        if not raw_line.strip() or ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    return cleaned or "article"


def escape_toml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def normalize_publication_date(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?", value):
        offset = datetime.now().astimezone().strftime("%z")
        return f"{value}{offset[:3]}:{offset[3:]}"
    return value or "1970-01-01T00:00:00Z"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[^\W\d_]+(?:['’][^\W\d_]+)?", text.lower(), flags=re.UNICODE)


def has_valid_title(value: str) -> bool:
    plain_title = re.sub(r"[*_`#:\[\]]", "", value).strip()
    words = tokenize(plain_title)
    return len(words) >= 3 and plain_title.lower() not in {"title", "untitled"}


def normalize_keyword_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def looks_french(path: Path, metadata: dict[str, str], body: str) -> bool:
    if "en" in path.parts:
        return False

    sample = " ".join(
        [
            metadata.get("optimized_title", ""),
            metadata.get("tags", ""),
            body[:4000],
        ]
    )
    tokens = tokenize(sample)
    if len(tokens) < 80:
        return False

    french_hits = sum(token in FRENCH_MARKERS for token in tokens)
    english_hits = sum(token in ENGLISH_MARKERS for token in tokens)

    if french_hits < 16:
        return False
    if english_hits > french_hits:
        return False

    return True


def split_tags(raw_tags: str) -> list[str]:
    tags = [tag.strip().lower() for tag in raw_tags.split(",") if tag.strip()]
    seen: set[str] = set()
    unique_tags: list[str] = []
    for tag in tags:
        if tag not in seen:
            unique_tags.append(tag)
            seen.add(tag)
    return unique_tags


def detect_priority_topics(title: str, tags: list[str], body: str) -> list[str]:
    haystack = normalize_keyword_text(" ".join([title, " ".join(tags), body[:4000]]))
    topics: list[str] = []
    for topic, keywords in PRIORITY_TOPICS.items():
        if any(normalize_keyword_text(keyword) and f" {normalize_keyword_text(keyword)} " in f" {haystack} " for keyword in keywords):
            topics.append(topic)
    return topics


def strip_leading_heading_block(body: str, page_title: str) -> str:
    lines = body.splitlines()
    index = 0

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            index += 1
            continue
        break

    # Source articles often begin with a decorative topic label before a heading
    # that repeats the page title and an unreliable generated subtitle.
    if (
        index < len(lines)
        and re.fullmatch(r"\*\*[^*]+\*\*", lines[index].strip())
    ):
        index += 1
        while index < len(lines) and not lines[index].strip():
            index += 1

    if index >= len(lines):
        return body.strip()

    heading_match = re.match(r"^#{1,6}\s+(.*)$", lines[index].strip())
    if not heading_match or slugify(heading_match.group(1).strip(" *_")) != slugify(page_title):
        return body.strip()

    index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    if index < len(lines):
        subtitle_match = re.match(r"^#{3,6}\s+(.*)$", lines[index].strip())
        if subtitle_match:
            index += 1
            while index < len(lines) and not lines[index].strip():
                index += 1

    return "\n".join(lines[index:]).strip()


def strip_malformed_media_blocks(body: str) -> str:
    return re.sub(
        r"(?ms)^!\[\((?:.*?)\]\([^\n]+\)\s*\n\*.*?\*\s*\n*",
        "",
        body,
    )


def normalize_sections(body: str) -> str:
    normalized_lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            normalized_lines.append(f"## {stripped[2:]}")
            continue
        plain_label = stripped.strip("*_ ").rstrip(":").lower()
        if plain_label in HEADING_REPLACEMENTS:
            normalized_lines.append(HEADING_REPLACEMENTS[plain_label])
            continue
        heading_match = re.match(r"^#{1,6}\s+\*?(.*?)\*?$", stripped)
        if heading_match:
            label = heading_match.group(1).strip().strip("*_ ").lower()
            replacement = HEADING_REPLACEMENTS.get(label)
            if replacement:
                normalized_lines.append(replacement)
                continue
        normalized_lines.append(line)

    text = "\n".join(normalized_lines)
    text = re.sub(r"(?m)^https://(?:www\.)?youtube\.com/watch\?v=.*$\n?", "", text)
    text = re.sub(r"(?m)^https://youtu\.be/.*$\n?", "", text)
    text = re.sub(r"(?m)^(👋|📺|⚡️).*\n?", "", text)
    text = re.sub(r"(?mi)^and \[retainr\.io\].*\n?", "", text)
    text = re.sub(r"(?mi)^🤖\s+.*$\n?", "", text)
    text = re.sub(r"(?ms)\n*---\s*\n###\s*Kicker:\s*\n.*\Z", "", text)
    text = re.sub(r"(?ms)\n*###\s*Kicker:\s*\n.*\Z", "", text)
    text = re.sub(r"\n(?:---\s*\n){2,}", "\n---\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    kept_chunks: list[str] = []
    saw_prose = False
    for chunk in re.split(r"\n\s*\n", text):
        stripped_chunk = chunk.strip()
        lowered_chunk = stripped_chunk.lower()
        if stripped_chunk == "---" and not saw_prose:
            continue
        if stripped_chunk and any(marker in lowered_chunk for marker in PROMO_MARKERS):
            continue
        if stripped_chunk and stripped_chunk != "---" and not stripped_chunk.startswith("!["):
            if not (stripped_chunk.startswith("*") and stripped_chunk.endswith("*")):
                saw_prose = True
        kept_chunks.append(stripped_chunk)

    text = "\n\n".join(chunk for chunk in kept_chunks if chunk)
    text = re.sub(r"\A(?:---\s*)+", "", text)
    text = re.sub(r"(?:\s*---)+\s*\Z", "", text)
    text = re.sub(r"\n(?:---\s*\n){2,}", "\n---\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[`*_>#-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def escape_shortcode_value(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().replace("\\", "\\\\").replace('"', "&#34;")


def normalize_alt_text(value: str, fallback: str) -> str:
    alt = re.sub(r"\s*(?:-|--|—)\s*Photo by\s+.*?(?:\s+on\s+Unsplash)?\s*$", "", value, flags=re.I)
    alt = re.sub(r"\s+", " ", alt).strip()
    if not alt or alt.lower().startswith("photo by") or len(alt) > 180:
        return fallback
    return alt


def make_figure_shortcode(src: str, alt: str, title: str, caption: str) -> str:
    return (
        f'{{{{< figure src="{escape_shortcode_value(src)}" '
        f'alt="{escape_shortcode_value(alt)}" '
        f'title="{escape_shortcode_value(title)}" '
        f'caption="{escape_shortcode_value(caption)}" >}}}}\n\n'
    )


def convert_markdown_images(body: str, page_title: str) -> str:
    image_pattern = re.compile(
        r'(?ms)^!\[(?P<alt>.*?)\]\((?P<src>\S+?)(?:\s+"(?P<title>[^"]*)")?\)\s*$'
    )
    image_with_caption_pattern = re.compile(
        r'(?ms)^!\[(?P<alt>.*?)\]\((?P<src>\S+?)(?:\s+"(?P<title>[^"]*)")?\)\s*\n'
        r'(?P<caption>\*.*?\*|[^\n]*Photo by[^\n]*)\s*$'
    )

    def replacement(match: re.Match[str]) -> str:
        raw_alt = match.group("alt")
        title = match.group("title") or page_title
        raw_caption = match.groupdict().get("caption") or ""
        caption = raw_caption.strip().strip("*").strip()
        alt = normalize_alt_text(raw_alt, page_title)
        if not caption:
            credit_match = re.search(r"(?:-|--|—)\s*(Photo by\s+.*)$", raw_alt, flags=re.I)
            caption = credit_match.group(1) if credit_match else alt
        return make_figure_shortcode(match.group("src"), alt, title, caption)

    parts = re.split(r"(?ms)(^```.*?^```)", body)
    for index in range(0, len(parts), 2):
        parts[index] = image_with_caption_pattern.sub(replacement, parts[index])
        parts[index] = image_pattern.sub(replacement, parts[index])
    return "".join(parts)


def extract_summary(body: str) -> str:
    for chunk in re.split(r"\n\s*\n", body):
        stripped = chunk.strip()
        if not stripped:
            continue
        if stripped.startswith(("![", "#", "*")):
            continue
        if stripped == "---":
            continue
        summary = strip_markdown(stripped)
        if len(summary) >= 40:
            return summary[:197].rstrip() + ("..." if len(summary) > 197 else "")
    return ""


def normalize_body(body: str, page_title: str) -> str:
    cleaned = body.lstrip()
    cleaned = strip_malformed_media_blocks(cleaned)
    cleaned = strip_leading_heading_block(cleaned, page_title)
    cleaned = normalize_sections(cleaned)
    return cleaned.strip() + "\n"


def render_front_matter(metadata: dict[str, str], title: str, slug: str, tags: list[str], summary: str, priority_topics: list[str]) -> str:
    lines = [
        "+++",
        f'title = "{escape_toml(title)}"',
        f'slug = "{escape_toml(slug)}"',
        f'date = "{escape_toml(normalize_publication_date(metadata.get("date", "")))}"',
        "draft = false",
    ]

    if summary:
        lines.append(f'description = "{escape_toml(summary)}"')
        lines.append(f'summary = "{escape_toml(summary)}"')

    if tags:
        rendered_tags = ", ".join(f'"{escape_toml(tag)}"' for tag in tags)
        lines.append(f"tags = [{rendered_tags}]")

    if priority_topics:
        lines.append("priority = true")
        rendered_topics = ", ".join(f'"{escape_toml(topic)}"' for topic in priority_topics)
        lines.append(f"priority_topics = [{rendered_topics}]")

    original_title = metadata.get("original_title")
    if original_title:
        lines.append(f'original_title = "{escape_toml(original_title)}"')

    medium_url = metadata.get("medium_url")
    if medium_url:
        lines.append(f'source_medium = "{escape_toml(medium_url)}"')

    youtube_url = metadata.get("youtube_url")
    if youtube_url:
        lines.append(f'source_youtube = "{escape_toml(youtube_url)}"')

    lines.append("+++")
    return "\n".join(lines)


def ensure_clean_target(target: Path) -> None:
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)
        return
    for child in target.glob("*.md"):
        if child.name.startswith("_"):
            continue
        child.unlink()


def import_articles(source: Path, target: Path, clean: bool, only_new: bool, include_slugs: set[str]) -> None:
    if clean:
        ensure_clean_target(target)
    else:
        target.mkdir(parents=True, exist_ok=True)

    imported = 0
    skipped = 0
    skipped_existing = 0
    skipped_not_selected = 0
    priority_count = 0
    topic_counter: Counter[str] = Counter()
    slug_counter: Counter[str] = Counter()

    for path in sorted(source.rglob("*.md")):
        if path.name == ".gitkeep":
            continue

        text = path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)

        title = metadata.get("optimized_title", "").strip()
        if not has_valid_title(title) or not looks_french(path, metadata, body):
            skipped += 1
            continue

        article_slug = slugify(title)
        if include_slugs and article_slug not in include_slugs:
            skipped_not_selected += 1
            continue

        tags = split_tags(metadata.get("tags", ""))
        normalized_body = normalize_body(body, title)
        destination = target / f"{article_slug}.md"
        if only_new and destination.exists():
            skipped_existing += 1
            continue

        summary = extract_summary(normalized_body)
        priority_topics = detect_priority_topics(title, tags, normalized_body)
        cleaned_body = convert_markdown_images(normalized_body, title)
        for topic in priority_topics:
            if topic not in tags:
                tags.append(topic)
        tags = sorted(dict.fromkeys(tags))

        slug = article_slug
        slug_counter[slug] += 1
        if slug_counter[slug] > 1:
            slug = f"{slug}-{slug_counter[slug]}"

        front_matter = render_front_matter(metadata, title, slug, tags, summary, priority_topics)
        destination = target / f"{slug}.md"
        if only_new and destination.exists():
            skipped_existing += 1
            continue
        destination.write_text(f"{front_matter}\n\n{cleaned_body}", encoding="utf-8")

        imported += 1
        if priority_topics:
            priority_count += 1
            topic_counter.update(priority_topics)

    print(f"Imported {imported} French articles into {target}")
    print(f"Skipped {skipped} files that were non-French, incomplete, or intentionally excluded")
    if only_new:
        print(f"Skipped {skipped_existing} articles already present in the target")
    if include_slugs:
        print(f"Skipped {skipped_not_selected} articles outside the curated selection")
    print(f"Priority articles: {priority_count}")
    if topic_counter:
        print("Priority topic counts:")
        for topic, count in topic_counter.most_common():
            print(f"  - {topic}: {count}")


def main() -> None:
    args = parse_args()
    import_articles(
        args.source.resolve(),
        args.target.resolve(),
        args.clean,
        args.only_new,
        set(args.include_slug),
    )


if __name__ == "__main__":
    main()
