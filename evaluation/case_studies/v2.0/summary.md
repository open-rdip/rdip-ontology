# Summary of Case Studies (v2.0)
## Answering Competency Questions 1–11

> **Ontology version:** RDIP v2.0  
> **Namespace:** `https://w3id.org/rdip/`  
> **CQ coverage:** CQ1–CQ7 (refined) · CQ8 Hyperparameters · CQ9 Computing Environment · CQ10 Evaluation Results · CQ11 Dataset Lineage

**What is new in v2.0 relative to v1.0:**

| New CQ | Capability Added |
|---|---|
| CQ8 | Exact hyperparameters and random seeds per activity |
| CQ9 | OS, GPU, CUDA version, Docker image digest per activity |
| CQ10 | Named evaluation metrics (AUC, mAP, F1…) with split labels |
| CQ11 | Full dataset derivation chain: raw source → processed artefact |

Additionally, v1.0 activities are re-typed more precisely (e.g. qualitative coding → `rdip:DataAnalysisActivity`; image preprocessing → `rdip:DataProcessingActivity`), activity sequencing is captured with `rdip:precedes`/`rdip:follows`, and software dependency graphs are added.

---

# Cross-Case Summary — Full CQ Coverage (v2.0)

| CQ | ChitwanAI (CS) | NepalStartups (Business) | ThaiMedAI (Medical) |
|---|---|---|---|
| **CQ1** Software used to generate dataset | YOLOv8 8.0.1 + Roboflow | NVivo 14.23.0 | OpenCV 4.9.0 |
| **CQ2** Methods used (with DOI) | COCO protocol (doi ✅) | Braun & Clarke (doi ✅) | CNN protocol (doi ✅ + Nextflow ✅) |
| **CQ3** Publication → PI | Dr. R. N. Sharma | Dr. L. K. Shrestha | Dr. P. Kittipong |
| **CQ4** Access level + landing page + license | open / ✅ / CC-BY | restricted / ✅ / CC-BY-NC | restricted-controlled / ✅ / CC-BY-NC |
| **CQ5** Co-outputs | article | article | software + article |
| **CQ6** Person roles | PI + Annotator | PI + Research Assistant | PI + Data Collector + Software Engineer |
| **CQ7** Full chain | 4 rows | 2 rows | 3 rows (training activity) |
| **CQ8** Hyperparameters + seed | LR, batch, epochs, seed(42) | *(no params — qualitative)* | LR, batch, epochs, dropout, seed(2025) |
| **CQ9** Computing environment | RTX 3090 / CUDA 12.1 / Ubuntu 22.04 | *(no env — qualitative)* | A100 80GB / CUDA 12.2 / Docker digest |
| **CQ10** Evaluation results | mAP@0.5=0.873, precision=0.891 | identified_themes=6 | AUC=0.961, sens=0.923, spec=0.947 |
| **CQ11** Dataset lineage | Raw JPEG → Annotated COCO JSON | Raw DOCX → Anonymized DOCX | Raw DICOM → Anonymized PNG |

> **Observations:**
> - CQ8 and CQ9 correctly return empty results for the business case study — qualitative research has no GPU or hyperparameters. The ontology handles this gracefully via OPTIONAL patterns.
> - CQ10 demonstrates that "evaluation results" work for both quantitative metrics (CS/Medical) and qualitative analytic counts (Business).
> - CQ11 closes the provenance gap identified in the v1 review: every project now has a traceable raw → processed dataset derivation chain using `rdip:derivedFrom` (subPropertyOf `prov:wasDerivedFrom`).
