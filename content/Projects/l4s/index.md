---
title: Implementing an Experience-driven Low Latency, Low Loss, and Scalable Throughput (L4S) Internet Service Architecture using FreeBSD

# `type` now cascades from content/Projects/_index.md as `project`, which routes
# this page to layouts/project/single.html. The previous `type: page` +
# `layout: page` forced Hugo Blox's generic article layout instead.

# summary: A research project enhancing low-latency, lossless, and scalable internet service delivery using the FreeBSD networking stack.

# Rendered as outline arrow buttons under the overview, matching the reference
# site's `.button-group > .arrow-btn--outline`. Replaces the shields.io badge
# that used to sit in the body, which pulled an image off an external host.
links:
  - label: Go to project site
    url: https://apnic.foundation/projects/implementing-an-experience-driven-l4s-internet-service-architecture-in-freebsd/

abstract: |
  This project, supported by the APNIC Foundation, focuses on implementing the IETF-defined L4S (Low Latency, Low Loss, Scalable Throughput) architecture within the FreeBSD kernel to support real-time, congestion-aware internet applications. The work involves modifying queue management systems and using reinforcement learning to dynamically optimize performance for modern digital services including cloud gaming, real-time video, and industrial IoT.

date: 2025-05-12

featured: true

image:
  caption: 'Implementation of L4S in FreeBSD for next-generation low-latency networking.'
  focal_point: Right
  filename: l4s-networking.jpg

projects: []

tags: ["L4S", "FreeBSD", "Internet Architecture", "Networking", "QoS", "QoE"]

url_pdf: ""
url_slides: ""
url_code: ""
url_video: ""
---

<!-- ## 

**A research initiative by the IoT & Software Engineering Lab, supported by the APNIC Foundation**

--- -->

<!-- <div style="margin-top: 1em;">
  <a href="https://apnic.foundation/projects/implementing-an-experience-driven-l4s-internet-service-architecture-in-freebsd/" target="_blank" class="button primary">Go to Project Site</a>
</div> -->



### Project Overview 


This project explores the integration of Deep Reinforcement Learning (DRL) and Large Language Models (LLMs) with the Low Latency, Low Loss, and Scalable Throughput (L4S) architecture to improve Internet congestion control. Hosted by the lab and funded by the APNIC Foundation, the project implements modular congestion control algorithms within FreeBSD, evaluates them on custom-built testbeds, and disseminates experimental results, software and datasets to the wider community.

<a class="poster-embed" href="Poster_LLM-L4S.pdf" target="_blank" rel="noopener">
  <img src="poster-llm-l4s.jpg" alt="LLM-L4S project poster. Opens the PDF in a new tab." width="1600" height="960">
</a>

---

### Key Outcomes

- DRL-based Multipath TCP (MPTCP) and AQM modules implemented in FreeBSD  
- Public testbed infrastructure available for reproducible experimentation  
- Peer-reviewed publications and ongoing contributions in academic/industry conferences  
- Student internships, mentoring, and curriculum integration for skill development  
- Ongoing industry and research partnerships  

---

### Open Source Software and Datasets

All source code and supporting data from this project have been made openly available to support reproducibility and collaboration:

- Experimental L4S testbed setup: [MPTCP-FreeBSD/FreeBSD-L4S-Experiments](https://github.com/MPTCP-FreeBSD/FreeBSD-L4S-Experiments)  
- DRL-enhanced congestion control stack for FreeBSD: [MPTCP-FreeBSD/FreeBSD-DRL-L4S](https://github.com/MPTCP-FreeBSD/FreeBSD-DRL-L4S)  
- Predictive congestion marking using LLMs: [MPTCP-FreeBSD/L4S-LLM](https://github.com/MPTCP-FreeBSD/L4S-LLM)  
- Adaptive TCP fairness via fine-tuned LLMs: [MPTCP-FreeBSD/LLM-TCP](https://github.com/MPTCP-FreeBSD/LLM-TCP)  
- AQM decision models powered by LLM-based inference: [MPTCP-FreeBSD/AQM-LLM](https://github.com/MPTCP-FreeBSD/AQM-LLM)  

---

### Publications

<!-- - **Pokhrel et al.**, “DDPG-MPCC: An experience driven multipath performance oriented congestion control,” *Future Internet*, Feb. 2024. [DOI](https://doi.org/10.3390/fi16020037)  
- **Shrestha et al.**, “On the fairness of Internet congestion control over WiFi with deep reinforcement learning,” *Future Internet*, Sept. 2024. [DOI](https://doi.org/10.3390/fi16090330)  
- **Satish et al.**, “AQM in L4S with A3C: A FreeBSD networking stack perspective,” *Future Internet*, Aug. 2024. [DOI](https://doi.org/10.3390/fi16080265)  
- **Pokhrel et al.**, “Multipath TCP implementation under FreeBSD-13 for pluggable ML models,” *Computer Networks*, 2024. [DOI](https://doi.org/10.1016/j.comnet.2024.110671)  
- **Shrestha et al.**, “Adapting LLMs for improving TCP fairness over WiFi,” *arXiv*, Dec. 2024. [arXiv:2412.18200](https://arxiv.org/abs/2412.18200)  
- **Satish et al.**, “Distilling LLMs for network AQM,” *arXiv*, Jan. 2025. [arXiv:2501.16734](https://arxiv.org/abs/2501.16734)   -->


<!-- - S. R. Pokhrel, J. Kua, D. Satish, S. Ozer, J. Howe, and A. Walid., **“DDPG-MPCC: An experience driven multipath performance oriented congestion control,** Future Internet, vol. 16, no. 2, p. 37, Feb. 2024. [Online]. Available: https://doi.org/10.3390/fi16020037
- Shrestha, S.K., Pokhrel, S.R. and Kua, J., **"On the Fairness of Internet Congestion Control over WiFi with Deep Reinforcement Learning"**. Future Internet, 16(9), p.330, Sept. 2024. [Online]. Available: https://doi.org/10.3390/fi16090330  
- Satish, D., Kua, J. and Pokhrel, S., **"Active Queue Management in L4S with Asynchronous Advantage Actor-Critic: A FreeBSD Networking Stack Perspective"**, Aug. 2024. [Online]. Available: https://doi.org/10.3390/fi16080265
- Pokhrel, S.R., Kua, J., Fleming, B., Ozer, S., Howe, J. and Walid, A., **"Multipath TCP implementation under FreeBSD-13 for pluggable machine learning models"**. Computer Networks, 252, p.110671, 2024. [Online]. Available: https://doi.org/10.1016/j.comnet.2024.110671
- Shrestha, S.K., Pokhrel, S.R. and Kua, J., **"Adapting Large Language Models for Improving TCP Fairness over WiFi"**. *arXiv preprint arXiv:2412.18200*., Dec. 2024. [Online]. Available: https://arxiv.org/abs/2412.18200
- Satish, D., Pokhrel, S.R., Kua, J. and Walid, A., **“Distilling Large Language Models for Network Active Queue Management”**. *arXiv preprint arXiv:2501.16734.*, Jan. 2025. [Online]. Available: https://arxiv.org/abs/2501.16734 -->

- S. R. Pokhrel, J. Kua, D. Satish, S. Ozer, J. Howe, and A. Walid, **“DDPG-MPCC: An experience driven multipath performance oriented congestion control,”** Future Internet, vol. 16, no. 2, p. 37, Feb. 2024. [Online]. Available: https://doi.org/10.3390/fi16020037
- S. K. Shrestha, S. R. Pokhrel, and J. Kua, **“On the fairness of internet congestion control over WiFi with deep reinforcement learning,”** Future Internet, vol. 16, no. 9, p. 330, Sept. 2024. [Online]. Available: https://doi.org/10.3390/fi16090330
- D. Satish, J. Kua, and S. R. Pokhrel, **“Active Queue Management in L4S with Asynchronous Advantage Actor-Critic: A FreeBSD Networking Stack Perspective,”** Future Internet, vol. 16, no. 8, p. 265, Aug. 2024. [Online]. Available: https://doi.org/10.3390/fi16080265
- S. R. Pokhrel, J. Kua, B. Fleming, S. Ozer, J. Howe, and A. Walid, **“Multipath TCP implementation under FreeBSD-13 for pluggable machine learning models,”** Computer Networks, vol. 252, p. 110671, 2024. [Online]. Available: https://doi.org/10.1016/j.comnet.2024.110671
- S. K. Shrestha, S. R. Pokhrel, and J. Kua, **“Adapting large language models for improving TCP fairness over WiFi,”** *arXiv preprint arXiv:2412.18200*, Dec. 2024. [Online]. Available: https://arxiv.org/abs/2412.18200
- D. Satish, S. R. Pokhrel, J. Kua, and A. Walid, **“Distilling large language models for network active queue management,”** *arXiv preprint arXiv:2501.16734*, Jan. 2025. [Online]. Available: https://arxiv.org/abs/2501.16734

---

### Sponsors

<div class="sponsor-logos">
  <a href="https://www.isif.asia/" target="_blank" rel="noopener">
    <img src="isif_logo.webp" alt="ISIF Asia">
  </a>
  <a href="https://apnic.foundation/" target="_blank" rel="noopener">
    <img src="apnic_logo.webp" alt="APNIC Foundation">
  </a>
</div>

---

### Get Involved

Interested in collaborating or learning more? Our project continues to grow through academic and industry partnerships, conference engagement, and educational outreach.


- **Contact:** [jonathan.kua@deakin.edu.au](mailto:jonathan.kua@deakin.edu.au)
- **Contact:** [shiva.pokhrel@deakin.edu.au](mailto:shiva.pokhrel@deakin.edu.au)



