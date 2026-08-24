# hj-young.github.io

Personal academic website of **Haojin Yang (杨昊锦)** — M.Eng. student in Software Engineering at Peking University. Live at [hj-young.github.io](https://hj-young.github.io).

Built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) fork of the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) Jekyll theme.

## Content locations

| What            | Where                               |
| --------------- | ----------------------------------- |
| Bio / news      | `_pages/about.md`                   |
| Publications    | `_publications/*.md`                |
| CV              | `_pages/cv.md`                      |
| Navigation      | `_data/navigation.yml`              |
| Site config     | `_config.yml`                       |
| Layouts / theme | `_layouts/`, `_includes/`, `_sass/` |

## Local preview

Requires Ruby 3.x with Bundler.

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

## Scholar citation counts

`.github/workflows/update-citations.yml` runs Mon/Wed/Fri and calls
`bin/update_scholar_citations.py` to refresh the `citations` field on each
`_publications/*.md` file from Google Scholar. Trigger manually via the Actions
tab.
