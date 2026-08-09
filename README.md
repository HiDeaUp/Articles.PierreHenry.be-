# articles.pierrehenry.be

Minimal Hugo site for articles.pierrehenry.be, using the fantastic clean and [minimalist](https://medium.com/pierrewriter/%EF%B8%8Fim-a-minimalist-for-years-why-i-m-freaking-love-it-2f9f8ac8041) [hugo-bearblog](https://github.com/janraasch/hugo-bearblog) theme.

## What This Repo Contains

This repository holds the French-language articles Pierre-Henry Soria writes on a daily basis. I love writing: it is how I explain, test, and develop my ideas.

The site publishes French articles with an emphasis on:

- Tech and software engineering
- Digital nomad work and travel
- Money and wealth
- Time management, tasks, productivity, and time blocking
- Entrepreneurship

The content import is automated from the source markdown archive at `~/Code/youtube-to-medium-blog-posts-automation/articles`.

## Local Development

Install Hugo first:

```bash
brew install hugo
```

Import the French articles into the Hugo content folder:

```bash
python3 scripts/import_articles.py --clean
```

Run the site locally:

```bash
hugo server
```

Build the production site:

```bash
hugo build
```

## Content Rules

The importer keeps only French-ready markdown files with structured metadata, normalizes their Hugo front matter, removes duplicated opening headings, strips leftover promotional clutter, and promotes the target niches on the homepage via priority tags.

## Founder

[![Pierre-Henry Soria](https://s.gravatar.com/avatar/a210fe61253c43c869d71eaed0e90149?s=200 "Pierre-Henry Soria - Software AI Engineer")](https://pierrehenry.dev)

**Pierre-Henry Soria**

Passionate software AI engineer building intelligent systems to solve real-world problems.

☕️ Enjoying this project? [Buy me a coffee](https://ko-fi.com/phenry) to support more AI innovations!

[![BlueSky](https://img.shields.io/badge/BlueSky-000000?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/pierrehenry.dev "Follow Me on BlueSky")
[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/phenrysay "Follow Me on X")
[![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "Follow Me on GitHub")
# Articles.PierreHenry.be-
