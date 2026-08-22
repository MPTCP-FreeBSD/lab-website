
# IoT & Software Engineering Lab Website

This repository contains the source code for the **IoT and Software Engineering Lab** website, showcasing our team, projects, publications, and lab activities.

🔗 **Live Site**: not yet configured - set `baseURL` in `config/_default/hugo.yaml`.

---

## 🔍 About the Lab

The IoT Lab is committed to advancing the field of Internet of Things (IoT) and software systems through cutting-edge research, real-world innovation, and academic collaboration. Our key focus areas include:

- Edge computing and embedded systems  
- Smart cities and sensor networks  
- Industrial IoT and autonomous systems  
- Privacy-aware and sustainable technologies

---

## 📁 Site Structure

- `/content/people/` – Team profiles
- `/content/projects/` – Ongoing and past research projects
- `/content/publication/` – Research papers and publications
- `/content/news/` – Announcements and events
- `/static/media/` – Lab images, figures, and media assets

---

## 🛠️ Tech Stack

- [Hugo](https://gohugo.io/) + [Hugo Blox Builder](https://hugoblox.com/)
- Markdown for content
- GitHub Pages for deployment

---

## 🎨 Theme

The site runs a custom light theme. Four files control it:

| File | Purpose |
| --- | --- |
| `data/themes/lab.toml` | Base colour tokens Hugo Blox feeds into its SCSS (primary, links, menu, section backgrounds) |
| `data/fonts/lab.toml` | Font pack - Figtree headings, Open Sans body, both self-hosted from `static/fonts/`; no Google Fonts request |
| `assets/scss/custom.scss` | All component styling: navbar, hero, cards, buttons, listings, footer. Compiled last, so it overrides Bootstrap and Hugo Blox |
| `config/_default/params.yaml` | Selects the two packs under `appearance:` |

The site is **light-only**. `appearance.theme_day` is set to `lab` and
`appearance.theme_night` is intentionally left empty: Hugo Blox only enables
the day/night switcher when both a day *and* a night theme exist, and setting
both would let the visitor's OS `prefers-color-scheme` repaint the whole site.

Palette: slate `#334155` carries headings, navigation and the news band; blue
`#0ea5e9` carries the closing CTA field, buttons and the project-card arrows.
Blue is only ever used as a *field* colour under dark type - it measures
2.8:1 on white and fails as text.

To retune the palette, edit the `$brand-*` / `$accent-*` variables in §1 of
`assets/scss/custom.scss` and mirror any changes in `data/themes/lab.toml`.

> Avoid setting `design.background.color` on homepage blocks - it paints an
> inline background over the theme's own section bands.

---

## 🚀 Deployment

The site is deployed via **GitHub Pages** using the workflow at `.github/workflows/hugo.yml`. Changes pushed to the `main` branch will be automatically built and published to the origin configured as `baseURL` in
`config/_default/hugo.yaml`. A custom domain also needs a `static/CNAME` file
holding that hostname.

GitHub Pages must be enabled once, under repo **Settings → Pages → Source → GitHub Actions**.

---

## 📬 Contributions

For updates to team members, projects, or publications, please open a Pull Request or contact the site maintainers.

---

## 📄 License

This website is open source and distributed under the [MIT License](LICENSE).

---

**Maintained by the IoT & Software Engineering Lab**
