---
title: "Achieving high performance content streaming with adaptive chunklets and active queue management"
authors:
  - Jonathan Kua
year: "2019"
date: "2019-01-01"
publication_types: ["article-journal"]  # Journal Article
publication_type_label: "Journal Article"
 #s
publisher: "Association for Computing Machinery (ACM)"
volume: "15"
issue: "4"
pages: "1-24"
doi: "10.1145/3344381"
abstract: "             Commercial streaming services such as Netflix and YouTube use proprietary HTTP-based adaptive streaming (HAS) techniques to deliver content to consumers worldwide. MPEG recently developed Dynamic Adaptive Streaming over HTTP (DASH) as a unifying standard for HAS-based streaming. In DASH systems, streaming clients employ adaptive bitrate (ABR) algorithms to maximise user Quality of Experience (QoE) under variable network conditions. In a typical Internet-enabled home, video streams have to compete with diverse application flows for the last-mile Internet Service Provider (ISP) bottleneck capacity. Under such circumstances, ABR algorithms will only act upon the fraction of the network capacity that is available, leading to possible QoE degradation. We have previously explored             <jats:italic>chunklets</jats:italic>             as an approach orthogonal to ABR algorithms, which uses parallel connections for intra-video chunk retrieval. Chunklets effectively make more bandwidth available for ABR algorithms in the presence of cross-traffic, especially in environments where Active Queue Management (AQM) schemes such as Proportional Integral controller Enhanced (PIE) and FlowQueue-Controlled Delay (FQ-CoDel) are deployed. However, chunklets consume valuable server/middlebox resources which typically handle hundreds of thousands of requests/connections per second. In this article, we propose             <jats:italic>‘adaptive chunklets’</jats:italic>             -- a novel chunklet enhancement that dynamically tunes the number of concurrent connections. We demonstrate that the combination of adaptive chunklets and FQ-CoDel is the most effective strategy. Our experiments show that adaptive chunklets can reduce the number of connections by almost 30% and consume almost 8% less bandwidth than fixed chunklets while providing the same QoE.           "
cited_by: "0"
tags:
  - 
url_pdf: "https://figshare.swinburne.edu.au/articles/thesis/Achieving_high_performance_content_streaming_with_adaptive_chunklets_and_active_queue_management/26280550"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
slides: ""
---
