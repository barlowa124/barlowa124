# Angus Barlow (barlowa124)

Biological data → predictive ML → scientific agents → independently checkable execution → regulated biopharma software.

I build life-science software where the evidence is inspectable: frozen splits, deterministic computation, machine-checked claims, replayable runs and explicit abstention when the data does not support a result.

Currently focused on **trustworthy AI and human-relevant preclinical models**: New Approach Methodologies (NAMs), computational toxicology, and ML tooling for drug discovery that reduces reliance on animal testing.

Related projects are grouped into monorepos — each subdirectory is a self-contained package with its own tests, config, and full commit history. The original repos are archived with pointers, so old links still resolve.

## Bioinformatics and assay data — [bio-qc](https://github.com/barlowa124/bio-qc) + [lab-informatics](https://github.com/barlowa124/lab-informatics)

| Repository | What it is |
|---|---|
| [cytof-qc](https://github.com/barlowa124/bio-qc/tree/main/cytof_qc) | Mass-cytometry benchmark: FCS parsing, channel/event QC, Leiden clustering on all 167k events of Levine_13dim with agreement scored on the 81.7k labeled subset (ARI 0.867). Merged and missed populations reported per gate. |
| [labStackDev](https://github.com/barlowa124/lab-informatics/tree/main/labStackDev) | RNA-seq quantification pipelines (Salmon, STAR+Salmon hybrid, pyDESeq2, METAFlux) validated at r = 0.984 against a CLC baseline, plus a SQLite LIMS with a hash-chained audit log. |
| [organoid-qc](https://github.com/barlowa124/bio-qc/tree/main/organoid_qc) | Organoid fidelity scoring vs CELLxGENE reference centroids, reported per cluster with unmapped fractions, plus an Opentrons Flex dosing protocol validated by the official Protocol Engine. |
| [cultivated-meat-multiomic](https://github.com/barlowa124/cultivated-meat-multiomic) | RNA + metabolic-flux clustering, 30-gene panel selection, conformal prediction, and drift monitoring on public data with cross-species checks. |

## Protein engineering and ML — [protein-ml](https://github.com/barlowa124/protein-ml)

| Repository | What it is |
|---|---|
| [protein-diffusion](https://github.com/barlowa124/protein-ml/tree/main/protein_diffusion) | Conditional DDPM over the GB1 fitness landscape scored against the measured oracle. The v1 model memorized (46% copied rows); v2 fitness conditioning steers measurably (80% fit vs 4% random). DDP, FastAPI service, Flax/JAX port matching torch to 3e-6. [Weights on HF](https://huggingface.co/barlowa/protein-ddpm-landscapes). |
| [active-learning-loop](https://github.com/barlowa124/protein-ml/tree/main/active_learning_loop) | GP-UCB acquisition vs a 20-seed random baseline on two measured landscapes (GB1, AAV2). ~79x top-100 enrichment on GB1; AAV2 holds ~8x with overlapping AUBC bands, reported as a partial replication. ESM-2 embeddings lose to one-hot, committed as a negative finding. |
| [protein-stability-uncertainty](https://github.com/barlowa124/protein-ml/tree/main/protein_stability_uncertainty) | Sequence to melting-point regression on the Meltome atlas (27,951 proteins) with a homology-separated split. Marginal conformal coverage (0.90) hides a 0.96 → 0.85 gradient across distance; Mondrian calibration recovers flat coverage. |
| [protein-design-ops](https://github.com/barlowa124/protein-ml/tree/main/protein_design_ops) | ProteinMPNN generation + ESM-2 rescoring + ESMFold pLDDT screen with pinned-seed provenance. The reproducibility caveat caught upstream `--seed 0` silently randomizing. |
| [dti-fusion](https://github.com/barlowa124/mol-ml/tree/main/dti_fusion) | Drug-target interaction on DAVIS (fingerprints + ESM-2), modality-ablated on held-out proteins. Fusion wins ranking/MSE; drug-only edges MAE. |

## Trustworthy ML and scientific agents — [trust-tools](https://github.com/barlowa124/trust-tools)

| Repository | What it is |
|---|---|
| [oncology-coscientist](https://github.com/barlowa124/oncology-coscientist) | TCGA survival analysis (Cox PH, RSF) where LangGraph agents draft reports and a deterministic verifier binds every number to its computation. See "What the verifier caught": fabricated cohort sizes and invented metrics for abstained models. |
| [llm-posttraining](https://github.com/barlowa124/llm-posttraining) | SFT + hand-rolled DPO + GRPO on SmolLM2-135M for abstention vs fabrication. DPO collapses deployed behavior at 100% train accuracy; shaped GRPO repairs it. Checkpoints published, including the collapsed one. |
| [bioprocess-decision-runtime](https://github.com/barlowa124/bioprocess-decision-runtime) | Bit-exact re-execution spec of a fixed Gemma 3 270M checkpoint with predeclared held-outs, plus a preserved failure where token agreement hid 49 differing logits. |
| [qms-ai-system-resume](https://github.com/barlowa124/qms-ai-system-resume) | Fail-closed deployment assessment engine and hardened architecture for AI in regulated quality systems. |
| [agent-trajectory-audit](https://github.com/barlowa124/trust-tools/tree/main/agent_trajectory_audit) | Oversight applied to my own coding-agent sessions: normalizes transcripts to an event stream and flags where actions diverge from stated plans (unbacked test/deploy claims, dropped plan items, out-of-scope writes). `trajaudit redteam` runs an adversarial battery against its own detectors — two evasion classes found and fixed on first run, one residual documented openly. |
| [inference-receipts](https://github.com/barlowa124/trust-tools/tree/main/inference_receipts) | Hash-bound receipts for LLM calls (weights, input, settings, output, chain link) with live replay verification. Committed example replays two real SmolLM2-135M calls bit-exact and catches a tampered receipt. |
| [eval-harness](https://github.com/barlowa124/trust-tools/tree/main/eval_harness) | Task-spec eval runner with hash-chained result logs; `sweep` runs one battery across staged checkpoints — the training-run-assessment shape. Committed artifact: a 3-stage SmolLM2 sweep where DPO collapsed abstention to 0.13 while answer generation degenerated at every stage. |
| [agent-monitor](https://github.com/barlowa124/trust-tools/tree/main/agent_monitor) | The audit moved upstream: a pre-execution policy gate on tool calls. Every allow/flag/block decision lands as a hash-chained event record. |
| [model-serve](https://github.com/barlowa124/trust-tools/tree/main/model_serve) | Serving slice: queued micro-batched inference, shadow comparison of a candidate against production, hash-bound record per response. |
| [receipt-report](https://github.com/barlowa124/trust-tools/tree/main/receipt_report) | Audit documents generated from the other packages' chains — verifies integrity first, then recomputes every reported number from the records. |

## Lab software and pipelines — [mol-ml](https://github.com/barlowa124/mol-ml) + [lab-informatics](https://github.com/barlowa124/lab-informatics)

| Repository | What it is |
|---|---|
| [comp-tox-pipeline](https://github.com/barlowa124/mol-ml/tree/main/comp_tox_pipeline) | Reproducible Tox21 evaluation: scaffold-split LR/RF/GIN with calibration, conformal coverage, and applicability-domain conditioning. The NR-ER applicability-domain inversion only surfaced because out-of-domain metrics were measured. |
| [lab-instrument-gateway](https://github.com/barlowa124/lab-informatics/tree/main/lab_instrument_gateway) | SCPI-style instrument driver against an emulated bioreactor over TCP: timeouts, reconnects, error-register polling, typed readings to SQLite, FastAPI dashboard, fault injection for failure-path tests. |
| [dockops](https://github.com/barlowa124/mol-ml/tree/main/dockops) | Docking pipeline ops: DUD-E staging, Vina backend, AFDB-vs-PDB structure QC that correctly argues against docking the AF model for EGFR, per-run provenance manifests. |
| [vector-db-mcp](https://github.com/barlowa124/vector-db-mcp) | Local vector DB over MCP (stdio) with flat/IVF/HNSW scans. Committed benchmark shows exact flat wins at this scale; two construction bugs were caught by recall measurement. |

## Upstream contributions

- **scverse/scanpy** (open): [PR #4383](https://github.com/scverse/scanpy/pull/4383) keeps a user-supplied `hue` in `sc.pl.violin` instead of dropping it or erroring. [PR #4385](https://github.com/scverse/scanpy/pull/4385) fixes multi-column `groupby` crashing on non-string observations across the BasePlot family.
- **OpenADMET/openadmet-models** (open): PRs [#607](https://github.com/OpenADMET/openadmet-models/pull/607), [#608](https://github.com/OpenADMET/openadmet-models/pull/608), [#609](https://github.com/OpenADMET/openadmet-models/pull/609), [#610](https://github.com/OpenADMET/openadmet-models/pull/610). The last exposes `n_jobs` on the splito-based splitters.
- **chaidiscovery/chai-lab** (open): [PR #431](https://github.com/chaidiscovery/chai-lab/pull/431) reports pTM as the aggregate score for single-chain inputs, where the ipTM-based headline understated confidence.
- [TDC fork](https://github.com/barlowa124/TDC): tested fix for silent dataset-name substitution plus an AnnData getter/split API. [ProteinMPNN](https://github.com/barlowa124/ProteinMPNN): effective-seed visibility fix filed as [issue #154](https://github.com/dauparas/ProteinMPNN/issues/154).

## How the pieces connect

The repos are standalone, but a few components are shared deliberately so results cross-check each other:

- **ESM-2** is the protein encoder in three places with honestly split outcomes: it drives rescoring in protein-design-ops and the target encoder in dti-fusion, and in active-learning-loop it loses to one-hot on GB1, kept as a committed negative result.
- **The GB1 measured landscape** is the fitness oracle in both protein-diffusion and active-learning-loop, so the generation-steering and acquisition-enrichment numbers are comparable across repos.
- **AnnData/scanpy** underlies cytof-qc and organoid-qc. The upstream scanpy PRs came from plotting bugs hit in that workflow, not from drive-by contributions.
- **Claims bound to computation**: oncology-coscientist's verifier, the bioprocess runtime's replay certificates, protein-design-ops' pinned-seed provenance, and comp-tox's applicability-domain conditioning are the same discipline applied at different layers.
- **Shared conventions, vendored not depended on**: a common provenance schema (`docs/PROVENANCE.md`) is adopted by oncology-coscientist, bioprocess-decision-runtime, dockops, labStackDev and comp-tox-pipeline. A canonical conformal helper with parity tests runs in comp-tox-pipeline, protein-stability-uncertainty and cultivated-meat-multiomic. One content-addressed ESM-2 cache is vendored into protein-design-ops, dti-fusion and active-learning-loop.
- **Cross-repo flows**: lab-instrument-gateway captures feed bioprocess-decision-runtime's `capture-scenario` evaluator. job-watch's repost detection and oncology-coscientist's `embed` retrieval mode can both dispatch to vector-db-mcp's E5 embedder while keeping dependency-free defaults. qms-ai-system-resume's deployment instrument has a committed worked assessment of oncology-coscientist (verdict: BLOCKING_FINDINGS, as designed for a research tool).

## Scope statements I hold to

- Verified computation is not verified science: reproducing a calculation says nothing about whether the model or the hypothesis is right.
- Research and education use only. Nothing here is validated for GMP, clinical or manufacturing decisions.
- Rejected runs, abstentions and failures are part of the evidence record.
