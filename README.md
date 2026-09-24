# Angus Barlow — barlowa124

Biological data → predictive ML → scientific agents → independently checkable execution → regulated biopharma software.

I build life-science software where the evidence is inspectable: frozen splits, deterministic computation, machine-checked claims, replayable runs, and explicit abstention when the data does not support a result.

Currently focused on the intersection of **trustworthy AI and human-relevant preclinical models** — New Approach Methodologies (NAMs), computational toxicology, and ML tooling for drug discovery that reduces reliance on animal testing.

## Projects

| Repository | What it is | What to look at |
|---|---|---|
| [oncology-coscientist](https://github.com/barlowa124/oncology-coscientist) | Cohort-agnostic TCGA survival analysis (Cox PH, Random Survival Forest) with LangGraph agents that draft reports while a deterministic verifier binds every number in the prose to the computation — and to the model it is attributed to. Human approval gate, replayable transcripts. | The "What the verifier caught" section: fabricated cohort sizes, invented metrics for abstained models, misattributed model blocks. |
| [bioprocess-decision-runtime](https://github.com/barlowa124/bioprocess-decision-runtime) | Independently executable, bit-exact specification of a fixed Gemma 3 270M checkpoint — all 18 layers, full 262,144-logit vocabulary projection — with predeclared held-outs, replay, and a preserved failure where token agreement hid 49 differing logits. Plus an advisory-only evidence-bound policy runtime for a synthetic bioprocess scenario. | Results-at-a-glance table; `docs/EXPERIMENT_LOG.md` for the full record. |
| [cultivated-meat-multiomic](https://github.com/barlowa124/cultivated-meat-multiomic) | Methods demonstration: RNA + metabolic-flux clustering, 30-gene panel selection, calibration, conformal prediction, ablation and drift monitoring on public data; cross-species checks on bovine and porcine muscle. | Data-provenance section (explicit about the stand-in dataset); integration benchmark. |
| [labStackDev](https://github.com/barlowa124/labStackDev) | Production-style RNA-seq quantification pipelines (Salmon, STAR+Salmon hybrid, pyDESeq2, METAFlux), validated at r = 0.984 against a CLC baseline. | Pipeline README with timings and validation. |
| [qms-ai-system-resume](https://github.com/barlowa124/qms-ai-system-resume) | Fail-closed deployment assessment engine and hardened reference architecture for AI in regulated quality systems. | Threat model and assessment engine tests. |

## Scope statements I hold to

- Verified computation is not verified science: reproducing a calculation says nothing about whether the model or the hypothesis is right.
- Research and education use only. Nothing here is validated for GMP, clinical, or manufacturing decisions.
- Failures are kept, not deleted. Rejected runs and abstentions are part of the evidence record.
