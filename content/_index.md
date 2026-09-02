---
title: IoT & Software Engineering Lab
summary: >
  We design, build and evaluate connected systems - advancing IoT,
  networking and software engineering research in partnership with
  government, industry and community.
date: 2022-10-24
type: landing

# Section order mirrors the reference site's own home page
# (cybercentre.org.au), module for module:
#
#   .module-hero-slider          -> dc_hero
#   .module-featured-media       -> dc_about
#   .module-proof-points         -> omitted; the lab has no verified figures
#   .module-research-areas       -> dc_areas
#   .module-featured-projects    -> dc_projects
#   .module-latest-news          -> omitted; no news section on this site
#   .subscribe-banner            -> omitted; see the note above `dc_cta`
#   .cta-primary.footer-cta      -> dc_cta
#   .site-footer                 -> the site-wide footer, on every page
#                                   (layouts/partials/components/footers/)
#
# Each block partial documents its own options in
# layouts/partials/blocks/, and its styling in assets/scss/custom.scss §13–19.

sections:

  # The reference's hero puts the centre's own name in the headline with a
  # one-sentence mission statement under it. Same shape here.
  - block: dc_hero
    content:
      title: IoT & Software Engineering Lab
      text: >
        We design, build and evaluate connected systems - advancing IoT,
        networking and software engineering research in partnership with
        government, industry and community.
      image:
        filename: workshop_group_photo.jpg
        alt: Members of the IoT and Software Engineering Lab

  - block: dc_about
    content:
      eyebrow: About the lab
      title: >
        The lab works at the forefront of connected and software-intensive
        systems
      text: |
        Our research spans embedded and networked systems, software engineering
        practice, and the measurement of how both behave once deployed. We work
        with government, industry and community partners to take approaches
        from prototype through to operation - creating demonstrable innovations
        and commercialisable intellectual property, and publishing the results.
      image:
        filename: ietf_group_photo.jpg
        alt: Lab members at the IETF meeting
      link:
        label: Meet the team
        url: /people/

  # The four areas are the ones already documented in content/research/_index.md.
  - block: dc_areas
    content:
      eyebrow: Research areas
      items:
        - title: 6G Communications and Networking
          text: >
            Pioneering next-generation communication technologies to support
            ultra-fast, reliable and secure networks for IoT devices.
          link: /research/
        - title: IoT Platforms and Interoperability
          text: >
            Developing seamless IoT platforms that let different devices and
            systems work together, creating smarter environments and industries.
          link: /research/
        - title: IoT Cooperation, Sensing and Analytics
          text: >
            Using IoT sensors to gather real-time data, with advanced analytics
            to improve decision-making and outcomes across sectors.
          link: /research/
        - title: AI-Driven Data Transport Protocols
          text: >
            Innovating AI-based solutions for optimising data transport, and the
            speed, efficiency and reliability of IoT communications.
          link: /research/

  # `section` is the content/ directory name and is case-sensitive - the
  # project folder is `content/Projects`, capital P.
  - block: dc_projects
    content:
      eyebrow: Flagship projects
      section: Projects
      count: 3
      link:
        label: View all projects
        url: /projects/

  # `dc_subscribe` (the reference's `.subscribe-banner`) is deliberately not
  # listed: the closing CTA is the only thing the home page carries below the
  # projects block, and everything after it now lives in the site-wide footer.
  # The block still exists at layouts/partials/blocks/dc_subscribe.html - add
  # it back here with a real form `action` if a mailing list is ever set up.
  - block: dc_cta
    content:
      title: Collaborate with us
      text: >
        The lab engages with industry and government through collaborative
        research projects that have real-world impact, and our graduate research
        program supports candidates working on connected and software-intensive
        systems.
      buttons:
        - label: Get in touch
          url: /contact/
---
