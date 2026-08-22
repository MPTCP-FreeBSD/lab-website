---
title: Tour
date: 2022-10-24
type: landing

# Rebuilt to match the rest of the site: a `dc_banner` header followed by
# alternating photo-and-text splits, the same `dc_about` block the home page
# uses. `image.position` flips the photo side and `design.css_class:
# dc-band-white` flips the band colour, so the sequence alternates on both.
#
# This replaces a fullscreen `slider` block. That slider set
# `slide_height: 100vh` but each slide carried an 80px heading, 30px body copy
# AND a 1400px-wide photo - far more than 100vh could hold - so the text was
# pushed up under the navbar and the images ran off the bottom of the slide.
# The content is all preserved below, just laid out so it fits.

sections:

  - block: dc_banner
    content:
      title: Tour the lab
      text: >
        A look inside the IoT & Software Engineering Lab - where we work,
        how we work together, and the people behind the research.

  - block: dc_about
    content:
      eyebrow: The lab
      title: Where research meets real-world systems
      text: |
        We blend innovation, collaboration and technology to turn ideas into
        working systems. Our researchers build and test connected infrastructure
        end to end - from protocol design through to deployment - and take that
        work to international standards bodies and conferences.
      image:
        filename: ietf_group_photo.jpg
        alt: Lab members at an IETF meeting
    design:
      css_class: dc-band-white

  - block: dc_about
    content:
      eyebrow: Workshops & collaboration
      title: Students, researchers and partners in the same room
      text: |
        Our students, researchers and industry partners work side by side
        through hands-on workshops, hackathons and live demonstrations. It is
        where research questions meet practical constraints, and where a good
        portion of our project work begins.
      image:
        filename: workshop_group_photo.jpg
        alt: Lab members at a workshop on the Burwood campus
        position: left

  - block: dc_about
    content:
      eyebrow: Our culture
      title: Behind every connected system is a connected team
      text: |
        From whiteboards to lunch tables, the lab runs on collaboration and
        shared goals. We mark the milestones together - and the people who make
        the work happen are the reason it holds together.
      image:
        filename: coders.jpg
        alt: Lab members at a team lunch
      link:
        label: Meet the team
        url: /people/
    design:
      css_class: dc-band-white
---
