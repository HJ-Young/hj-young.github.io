---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

Education
======

- **M.Eng. in Software Engineering**, Peking University, 2024–2027
  - Ranked **1/4200** in the comprehensive entrance evaluation
  - PKU Academic Excellence Award
- **B.Eng. in Software Engineering**, Nanjing University, 2020–2024
  - National Scholarship (3rd class)

Experience
======

- **StepFun — Foundation Models**, Agent RL Research Intern (2026-04 – present), Beijing
  - Advisor: [Ruihang Miao](https://dblp.org/pid/244/7389.html). Post-training of Step3.6 / Step4 to improve agentic capability using real production traffic.
  - Built a multi-turn RL framework on VeRL with user-simulator rollouts and token-level masking / advantage estimation.
  - Designed turn-level and session-level reward functions (rule-based + generative); reward redesign yielded a **28.1% relative improvement** over the initial version.

- **Meituan — Longcat Interaction**, Foundation Algorithm Research Intern (2025-10 – 2026-04), Beijing
  - Advisor: [Jingqing Ruan](https://scholar.google.com/citations?user=L_C8xRkAAAAJ&hl=zh-CN). Post-training of Meituan's in-house Longcat base model to improve persuasion ability in real sales scenarios.
  - Multi-turn RL framework on VeRL supporting rollouts with simulated users and per-token mask / advantage.
  - Reward design combining turn-level (rule-based) and session-level (generative) signals; +28.1% relative gain over the initial reward.

- **Microsoft Research Asia — DKI Excel Research**, Research Intern (2025-04 – 2025-10), Beijing
  - Advisor: [Ran Jia](https://scholar.google.com/citations?user=yIBo3fgAAAAJ&hl=zh-CN). RLHF, Excel agents, Deep Research.
  - Qwen-32B GRPO training for Python / Formula instruction control in Excel: built a multi-turn tool-use pipeline on VeRL with fine-grained rewards, **+17% accuracy** over GPT-o4-mini.
  - Pivot-table dataset: defined a schema covering all operations, built a batched generation pipeline, collected 20k high-quality samples.
  - Search benchmark: built a semi-automated pipeline for evaluating large-scale search agents using Wikidata and curated sources with a voting-based validator.

- **Baidu — TPG**, LLM Algorithm Intern (2024-09 – 2025-03), Beijing
  - Advisor: Ziwei Jin. LoRA fine-tuning, GraphRAG, retrieval-augmented systems.
  - Text2Gremlin: LoRA-fine-tuned Qwen2.5-Coder on a curated 60k-from-480k dataset, lifting task accuracy from 70% to **87.2%**.
  - RAG pipeline: introduced Text2Gremlin + intent classification, compressed QA latency from 9s to 3s in 60% of business scenarios and extended RAG to simple-reasoning queries.
  - Proposed a chunk-Graph RAG combining GraphRAG and chunk-RAG for specific business scenarios.

Selected Publications
======

- **WavefrontDiffusion: Dynamic Decoding Schedule for Improved Reasoning.** Haojin Yang, R. Hu, Z. Sun, R. Zhou, Y. Cai, Y. Wang. *ICLR 2026* (Poster).
- **Harmonizing Dense and Sparse Signals in Multi-turn RL: Dual-Horizon Credit Assignment for Industrial Sales Agents.** Haojin Yang, A. Jian, X. Huang, Y. Wang, W. Zhang, K. Zeng, X. Cai, J. Ruan. *ACL 2026* (Poster).
- **Asymmetric On-Policy Distillation: Bridging Exploitation and Imitation at the Token Level.** N. Jia, Haojin Yang (co-first), X. Ma, J. Lian, S. Zhang, W. Zhang, K. Zeng, X. Cai, Z. Sun. *EMNLP 2026 Findings*.
- **VADE: Variance-Aware Dynamic Sampling via Online Sample-Level Difficulty Estimation for Multimodal RL.** Z. Hu, J. Qiu, T. Bai, Haojin Yang, B. Yuan, Q. Jing, C. He, W. Zhang. *CVPR 2026 Findings*.
- **TRUST-SQL: Tool-Integrated Multi-Turn Reinforcement Learning for Text-to-SQL over Unknown Schemas.** A. Jian, X. Zhang, W. Du, J. Ruan, J. Pei, W. Zhang, K. Zeng, X. Cai. *EMNLP 2026* (Main).

Awards
======

- **PKU Academic Excellence Award**, 2025 — Peking University.
- **National Scholarship (3rd class)**, 2023 — Ministry of Education, China.
- **PKU SSM Graduate Entrance — Ranked 1/4200**, 2024 — Peking University. Initial-exam score 436; ranked 1st in the comprehensive evaluation among ~4200 candidates.

Skills
======

- **Programming**: Python, Java, C++, Shell
- **ML / RL**: PyTorch, VeRL, GRPO, RLHF, Multi-turn RL, Diffusion LMs, LoRA

Languages
======

- Chinese — Native speaker
- English — CET-6 632 (proficient)

Research Interests
======

Reinforcement learning, multi-turn agentic RL, diffusion language models, credit assignment, tool use.
