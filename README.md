# IoT & Software Engineering Research Lab Website

Source for the lab website: team, projects, and publications.

**Live site:** [https://mptcp-freebsd.github.io/lab-website/](https://mptcp-freebsd.github.io/lab-website/)

---

## Stack

- [Hugo](https://gohugo.io/) **extended** (CI uses **0.165.0**)
- [Hugo Blox Builder](https://hugoblox.com/) (`blox-bootstrap/v5`)
- Markdown content, SCSS in `assets/scss/custom.scss`
- GitHub Pages via `.github/workflows/hugo.yml`

---

## Develop locally

### Prerequisites

- [Hugo extended](https://gohugo.io/installation/) 0.165.x (the `extended` build is required for SCSS)
- [Go](https://go.dev/dl/) 1.15+ (Hugo modules)
- Git

Confirm:

```bash
hugo version   # should say "extended"
go version
```

### Run

```bash
git clone https://github.com/MPTCP-FreeBSD/lab-website.git
cd lab-website
hugo mod get
hugo server -D --bind 127.0.0.1 --port 1313 --disableFastRender
```

Open [http://127.0.0.1:1313/lab-website/](http://127.0.0.1:1313/lab-website/). The `/lab-website/` prefix matches the GitHub Pages project URL (`baseURL` in `hugo.yaml`).

`--disableFastRender` rebuilds the whole page on save, which is what you want when editing layouts or SCSS.

### Production build (optional)

```bash
hugo --gc --minify
```

Output lands in `public/` (gitignored). CI does this on every push to `main`.

---

## Config YAML

Hugo reads everything under `config/_default/`. Edit these; do not add a root `config.yaml`.

### `config/_default/hugo.yaml`

Site-wide Hugo settings.

| Key | What it is |
| --- | --- |
| `title` | Browser tab / default site name |
| `baseURL` | Public origin. **Must** stay `https://mptcp-freebsd.github.io/lab-website/` while the site is a project Pages site, or asset URLs break. The Actions workflow also passes `--baseURL` from Pages. |
| `pagination.pagerSize` | Items per page on listings (projects, publications) |
| `permalinks` | URL shapes for authors, tags, categories, publication types |
| `outputs` | `JSON` is omitted on purpose (search is off). Add it back only if search is re-enabled. |
| `taxonomies` | `tags`, `categories`, `publication_types`, `authors` |

### `config/_default/params.yaml`

Hugo Blox / site chrome: appearance, header, footer, features.

| Block | What it is |
| --- | --- |
| `appearance` | `theme_day: lab` and **empty** `theme_night` keep the site light-only. `font: lab` selects Figtree + Open Sans. |
| `marketing.seo` | Organisation name for metadata. Analytics IDs go here if needed. |
| `header.navbar` | Logo, alignment (`r` = right), no search, no day/night switcher, highlight the active nav item. |
| `footer` | Selects `layouts/partials/components/footers/lab.html`. Acknowledgement of Country, footer Contact URL (`/contact/`), which menu to mirror (`main`), copyright notice. |
| `locale` | Date format (`Jan 2, 2006`). |
| `features.search.provider` | Empty = search off. Keep in sync with `header.navbar.show_search`. |
| `features.avatar.shape` | `square` (no round portraits). |
| `features.repository` | Placeholder GitHub URL for “edit this page” style links if you turn those on. |

Footer copy (acknowledgement, copyright) is edited here, not in the HTML partial.

### `config/_default/menus.yaml`

Navbar (and footer nav, which mirrors `main`).

```yaml
main:
  - name: "Publications"
    url: "publication"  # path under the site; no leading slash needed except Home
    weight: 50           # lower = further left
```

Home must stay `url: "/"`. Weights control order.

### `config/_default/languages.yaml`

Language packs. Only `en` is enabled (`languageCode: en-us`). Uncomment the `zh` (or other) stub to add a second language and a matching `contentDir`.

### `config/_default/module.yaml`

Hugo modules. The theme is:

```yaml
imports:
  - path: github.com/HugoBlox/hugo-blox-builder/modules/blox-bootstrap/v5
```

Version is pinned in `go.mod`. Run `hugo mod get` after changing this.

### `.github/workflows/hugo.yml`

GitHub Actions: build Hugo **0.165.0 extended** and deploy to Pages.

- **Triggers:** push to `main`, or **Run workflow** in the Actions tab
- **Jobs:** `build` (install Hugo → checkout → `hugo --minify`) then `deploy`
- **Hugo version:** `HUGO_VERSION` at the top of the `build` job — bump this if you upgrade Hugo locally
- Pages source is **GitHub Actions** (repo Settings → Pages)

A custom domain needs `static/CNAME` plus a `baseURL` change in `hugo.yaml`.

---

## Content

All of this is Markdown under `content/`. Front matter is YAML.

| Path | Page | Notes |
| --- | --- | --- |
| `content/_index.md` | Home | Landing page. `sections:` lists blocks (`dc_hero`, `dc_about`, `dc_areas`, `dc_projects`, `dc_cta`). Block options are documented in `layouts/partials/blocks/`. |
| `content/tour/index.md` | Tour | `dc_banner` + repeating `dc_about` photo/text splits. |
| `content/people/index.md` | People | Banner + people widget. Groups come from each author’s `user_groups`. |
| `content/authors/<Name>/` | Profiles | `_index.md` + `avatar.jpg` / `.jpeg`. `user_groups` must match a group listed on the People page (e.g. `Principal Investigator`, `Researchers`, `Alumni`). |
| `content/Projects/` | Projects | `_index.md` lists them. Each project is `content/Projects/<slug>/` (page bundle: `index.md`, images, PDFs). `cascade.type: project` is set on the listing so singles use `layouts/project/single.html`. |
| `content/publication/` | Publications | One folder per paper (`index.md`). Listing filters live in `layouts/section/publication.html`. |
| `content/contact/index.md` | Contact | Banner + `dc_contacts` (names, emails, phones). |

Homepage images are loaded from `assets/media/` (see `dc_hero` / `dc_about` `image.filename`). Page-bundle images sit next to that page’s `index.md`.

### Adding a person

1. Create `content/authors/Firstname/_index.md` (copy an existing profile).
2. Add `avatar.jpg` or `avatar.jpeg` in the same folder.
3. Set `user_groups` to a group that already appears on `content/people/index.md`.

### Adding a project

```
content/Projects/my-project/
  index.md
  cover.jpg
```

Keep `image.filename` and `abstract` (or `summary`) in the front matter so the listing card has a picture and blurb.

### Publications from Google Scholar

`getpublications.py` pulls papers for the Scholar IDs in that file and writes under `content/publication/`. Needs `requests` and `scholarly`. Review the generated Markdown before committing.

---

## Theme and layouts

| File | Role |
| --- | --- |
| `assets/scss/custom.scss` | All custom CSS. Loaded last, so it wins over Bootstrap and Hugo Blox. Palette is `$brand-*` / `$accent-*` at the top. |
| `data/themes/lab.toml` | Colour tokens Hugo Blox injects. Keep in sync with `custom.scss` if you retune the palette. |
| `data/fonts/lab.toml` | Figtree headings, Open Sans body; fonts are self-hosted in `static/fonts/`. |
| `layouts/partials/blocks/` | Homepage / landing blocks (`dc_hero`, `dc_banner`, `dc_cta`, …). |
| `layouts/partials/components/headers/navbar.html` | Navbar, including which item is `active`. |
| `layouts/partials/components/footers/lab.html` | Footer markup. Copy comes from `params.yaml`. |
| `layouts/section/projects.html` | Projects listing. |
| `layouts/section/publication.html` | Publications listing + filters. |
| `layouts/project/single.html` | Individual project page. |

The site is **light-only**. Do not set `appearance.theme_night` in `params.yaml` or the OS dark-mode switcher will repaint the whole site.

Do not set `design.background.color` on homepage blocks — it paints over the section bands.

---

## Deploy

Push to `main`. Actions builds and publishes to [https://mptcp-freebsd.github.io/lab-website/](https://mptcp-freebsd.github.io/lab-website/).

To ship a Hugo upgrade, change `HUGO_VERSION` in `.github/workflows/hugo.yml` and match it locally.

---

## License

MIT. See [LICENSE.md](LICENSE.md).

Maintained by the IoT & Software Engineering Research Lab.
