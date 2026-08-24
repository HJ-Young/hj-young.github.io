---
title: "WavefrontDiffusion: Dynamic Decoding Schedule for Improved Reasoning"
collection: publications
category: conferences
permalink: /publication/2026-wavefront
excerpt: 'A dynamic wavefront decoding mechanism for diffusion language models. Outperforms BlockDiffusion on GSM8K, HumanEval and additional math/code reasoning benchmarks at the same compute budget.'
date: 2026-04-24
venue: 'International Conference on Learning Representations (ICLR)'
citation: 'Haojin Yang, R. Hu, Z. Sun, R. Zhou, Y. Cai, Y. Wang. &quot;WavefrontDiffusion: Dynamic Decoding Schedule for Improved Reasoning.&quot; <i>ICLR 2026</i> (Poster).'
---

Standard diffusion language models suffer from globally unconstrained decoding that accumulates early errors, while block diffusion sacrifices semantic coherence at hard block boundaries. We propose a dynamic wavefront mechanism inspired by physical wave propagation: an active token frontier expands outward from already-decoded positions, with adaptive Expand and confidence-based Prune steps. On GSM8K, HumanEval, and three additional math/code reasoning benchmarks, WavefrontDiffusion surpasses BlockDiffusion across the board while keeping compute on par. We introduce the MHCO metric to quantify boundary-induced reasoning violations and show consistent gains in BERTScore semantic consistency.
