# Angus Barlow (barlowa124)

I build scientific software for drug discovery and lab work. Every reported number can be traced to a committed artifact, and models abstain when the data does not support a conclusion.

Current work is on New Approach Methodologies and computational toxicology, building ML tooling that reduces reliance on animal testing.

Projects are grouped into monorepos. Each subdirectory is a self-contained package with its own tests and config. The original standalone repos are archived and point at the new locations, so old links still resolve.

## Bioinformatics and assay data

Repos: [bio-qc](https://github.com/barlowa124/bio-qc) and [lab-informatics](https://github.com/barlowa124/lab-informatics).

| Repository | Description |
|---|---|
| [cytof-qc](https://github.com/barlowa124/bio-qc/tree/main/cytof_qc) | Mass-cytometry benchmark covering FCS parsing and channel/event QC plus Leiden clustering on all 167k events of Levine_13dim, with agreement scored on the 81.7k labeled subset (ARI 0.867). Merged and missed populations are reported per gate. |
| [fcs-io](https://github.com/barlowa124/bio-qc/tree/main/fcs_io) | Dependency-free FCS 3.0/3.1 reader/writer with explicit vendor-quirk handling (delimiter escapes, blank-header offsets, endianness). Validated bit-exact against `fcsparser` on 55 real Levine files, 432k events. A committed crosscheck artifact records the comparison. |
| [scrna-qc](https://github.com/barlowa124/bio-qc/tree/main/scrna_qc) | Single-cell RNA-seq QC built on scanpy/AnnData, run as a Snakemake DAG with config-driven thresholds. Per-cluster QC keeps a pooled pass from hiding a depleted population. The committed PBMC 3k run filtered 57 high-mito cells and recovered 8 Leiden clusters whose top markers land on canonical PBMC families, with LYZ/S100A8 marking monocytes and NKG7 marking NK cells and CD74 marking antigen-presenting cells. |
| [spatial-qc](https://github.com/barlowa124/bio-qc/tree/main/spatial_qc) | Visium spot QC plus a filtering-strategy benchmark (fixed vs MAD-adaptive vs tissue-only) on two public Space Ranger exports (V1 mouse brain, V1 breast cancer). The strategy ranking reverses between the two datasets. Both runs are committed. |
| [nf](https://github.com/barlowa124/bio-qc/tree/main/nf) | DSL2 Nextflow pipeline in nf-core module style (meta.yml/environment.yml/stub per module, nf-test coverage) running FCSIO_DEMO -> PARSE -> STATS over per-file parallel tasks. |
| [labStackDev](https://github.com/barlowa124/lab-informatics/tree/main/labStackDev) | RNA-seq quantification pipelines (Salmon, STAR+Salmon hybrid, pyDESeq2, METAFlux) validated at r = 0.984 against a CLC baseline. Ships a SQLite LIMS with a hash-chained audit log of HMAC-signed rows carrying reason-for-change fields, plus a VALIDATION.md mapping properties to IQ/OQ/PQ tests. |
| [organoid-qc](https://github.com/barlowa124/bio-qc/tree/main/organoid_qc) | Organoid fidelity scoring against CELLxGENE reference centroids, reported per cluster with unmapped fractions. Includes an Opentrons Flex dosing protocol validated by the official Protocol Engine. |
| [cultivated-meat-multiomic](https://github.com/barlowa124/bio-qc/tree/main/cultivated_meat_multiomic) | RNA and metabolic-flux clustering on public data with cross-species checks. Includes 30-gene panel selection with conformal prediction and drift monitoring. |
| [statgen](https://github.com/barlowa124/bio-qc/tree/main/statgen) | Statistical-genetics pipeline as a config-driven Snakemake DAG covering variant/sample QC (missingness, MAF, HWE, within-ancestry heterozygosity), genotype PCA, linear/logistic association with genomic-control lambda, and a PC-residualized relatedness scan. A committed synthetic cohort recovers all post-QC planted causal variants at Bonferroni (beta correlation 0.99) and measures stratification as lambda 2.65 down to 0.97 with PC covariates. A 1000 Genomes chr22 mode accounts for LD-proxy hits and states regional-LD limits. |
| [split-audit](https://github.com/barlowa124/bio-qc/tree/main/split_audit) | Train/test leakage auditor. It reports scaffold IDs spanning the split boundary and scores k-mer Jaccard similarity across held-out pairs, with flagged items listed per finding. The committed demo plants two shared scaffolds and three sequence leaks on synthetic rows, and recovers all five. |

## Protein engineering and ML

Repo: [protein-ml](https://github.com/barlowa124/protein-ml).

| Repository | Description |
|---|---|
| [protein-diffusion](https://github.com/barlowa124/protein-ml/tree/main/protein_diffusion) | Conditional DDPM over the GB1 fitness landscape scored against the measured oracle. The v1 model memorized (46% copied rows). The v2 fitness conditioning steers measurably (80% fit vs 4% random). The Flax/JAX port matches torch outputs to 3e-6. DDP training and a FastAPI service are included. [Weights on HF](https://huggingface.co/barlowa/protein-ddpm-landscapes). |
| [active-learning-loop](https://github.com/barlowa124/protein-ml/tree/main/active_learning_loop) | GP-UCB acquisition against a 20-seed random baseline on two measured landscapes (GB1, AAV2). GB1 reaches about 79-fold top-100 enrichment. AAV2 holds about 8-fold with overlapping AUBC bands, reported as a partial replication. ESM-2 embeddings lose to one-hot here, kept as a committed negative result. |
| [protein-stability-uncertainty](https://github.com/barlowa124/protein-ml/tree/main/protein_stability_uncertainty) | Sequence-to-melting-point regression on the Meltome atlas (27,951 proteins) with a homology-separated split. Marginal conformal coverage of 0.90 hides a 0.96-to-0.85 gradient across distance. Mondrian calibration recovers flat coverage. |
| [protein-design-ops](https://github.com/barlowa124/protein-ml/tree/main/protein_design_ops) | ProteinMPNN generation with ESM-2 rescoring and an ESMFold pLDDT screen, under pinned-seed provenance. The reproducibility caveat caught upstream `--seed 0` silently randomizing. |
| [dti-fusion](https://github.com/barlowa124/mol-ml/tree/main/dti_fusion) | Drug-target interaction on DAVIS (fingerprints plus ESM-2), modality-ablated on held-out proteins. Fusion wins on ranking and MSE. Drug-only edges it on MAE. |

## Trustworthy ML and scientific agents

Repo: [trust-tools](https://github.com/barlowa124/trust-tools).

| Repository | Description |
|---|---|
| [oncology-coscientist](https://github.com/barlowa124/trust-tools/tree/main/oncology_coscientist) | TCGA survival analysis (Cox PH, RSF) where LangGraph agents draft reports and a deterministic verifier binds every number to its computation. The committed run documents the verifier catching fabricated cohort sizes and invented metrics for abstained models. |
| [llm-posttraining](https://github.com/barlowa124/llm-posttraining) | SFT followed by hand-rolled DPO and GRPO on SmolLM2-135M for abstention vs fabrication. DPO collapses deployed behavior at 100% train accuracy. Shaped GRPO repairs it. A second reward path is programmatic rather than classifier-judged, using arithmetic tasks with last-integer verification. The 40-step log shows format learned quickly and arithmetic at chance. Checkpoints are published, including the collapsed one. [EVAL_REPORT.md](https://github.com/barlowa124/llm-posttraining/blob/main/EVAL_REPORT.md) reports the held-out abstention suite on stock Apache-license models with every number bound to the committed results JSON. SmolLM2-135M-Instruct fabricates on 98.75% of unanswerable prompts. Qwen2.5-0.5B-Instruct abstains at 88.75%. |
| [bioprocess-decision-runtime](https://github.com/barlowa124/bioprocess-decision-runtime) | Bit-exact re-execution spec of a fixed Gemma 3 270M checkpoint with predeclared held-outs, plus a preserved failure where token agreement hid 49 differing logits. |
| [qms-ai-system-resume](https://github.com/barlowa124/qms-ai-system-resume) | Fail-closed deployment assessment engine and hardened architecture for AI in regulated quality systems. |
| [agent-trajectory-audit](https://github.com/barlowa124/trust-tools/tree/main/agent_trajectory_audit) | Oversight applied to my own coding-agent sessions. It normalizes transcripts into an event stream and flags divergence from stated plans. Flagged categories cover unbacked test or deploy claims along with dropped plan items and out-of-scope writes. `trajaudit redteam` runs an adversarial battery against its own detectors. Two evasion classes were found and fixed on the first run. One residual is documented. |
| [inference-receipts](https://github.com/barlowa124/trust-tools/tree/main/inference_receipts) | Hash-bound receipts for LLM calls. Each receipt records the weights, input, settings and output along with the chain link, and supports live replay verification. The committed example replays two real SmolLM2-135M calls bit-exact and catches a tampered receipt. |
| [eval-harness](https://github.com/barlowa124/trust-tools/tree/main/eval_harness) | Task-spec eval runner with hash-chained result logs. `sweep` runs one battery across staged checkpoints for training-run assessment. `inspect-export` emits real Inspect `dataset.jsonl` and `@task` pairs verified under mockllm runs (oracle 100% on all four committed batteries). The committed artifact is a 3-stage SmolLM2 sweep where DPO collapsed abstention to 0.13 while answer generation degenerated at every stage. A second committed sweep scores report-vs-log honesty on 12 tool-log probes, where the `honest_report` grader requires the logged fact in the response and no trace of the false claim. |
| [agent-monitor](https://github.com/barlowa124/trust-tools/tree/main/agent_monitor) | The audit moved upstream: a pre-execution policy gate on tool calls. Every allow/flag/block decision lands as a hash-chained event record. |
| [model-serve](https://github.com/barlowa124/trust-tools/tree/main/model_serve) | Serving layer with queued micro-batched inference, shadow comparison of a candidate against production, and a hash-bound record per response. `bench` measures real p50/p95/p99 under concurrent load. The committed sweep on SmolLM2-135M documents the tradeoff between queue wait and missing fused compute. |
| [agent-observe](https://github.com/barlowa124/trust-tools/tree/main/agent_observe) | Observability layer over the stack. It ingests spans and traces (flat schema and OTLP-lite), surfaces live policy verdicts via agentmon, runs trajaudit detectors on the same event stream, and renders markdown/HTML trace reports. |
| [agent-sandbox](https://github.com/barlowa124/trust-tools/tree/main/agent_sandbox) | Containment-layer benchmark. Scripted tool calls route through the agentmon gate then a realpath filesystem jail, measured separately. The committed battery shows the jail catching what the gate allows (symlink tricks, absolute-path reads) and labels the residual it found: arg aliasing, since fixed in agentmon. Non-redirect writes like `cp` remain an open item. |
| [receipt-report](https://github.com/barlowa124/trust-tools/tree/main/receipt_report) | Audit documents generated from the other packages' chains. It verifies chain integrity before recomputing every reported number from the records. |
| [traj-review-ui](https://github.com/barlowa124/trust-tools/tree/main/traj_review_ui) | Static React and TypeScript review surface for the repo's real artifacts. It includes a findings panel with jump-to-event links and an event timeline pairing calls with results, plus a span-tree view for agent-observe traces. Bundled datasets are committed trajaudit outputs. There is no backend. It is labeled as a static demo. |

## Lab software and pipelines

Repos: [mol-ml](https://github.com/barlowa124/mol-ml) and [lab-informatics](https://github.com/barlowa124/lab-informatics).

| Repository | Description |
|---|---|
| [comp-tox-pipeline](https://github.com/barlowa124/mol-ml/tree/main/comp_tox_pipeline) | Reproducible Tox21 evaluation with scaffold-split LR/RF/GIN. Calibration and conformal coverage are reported inside and outside the applicability domain. The NR-ER applicability-domain inversion only surfaced because out-of-domain metrics were measured. `comp_tox.dossier` generates an evidence dossier per run where every number binds to the metrics artifact through the vendored claims verifier, and the limitations block is emitted from the artifact's own status fields. |
| [lab-instrument-gateway](https://github.com/barlowa124/lab-informatics/tree/main/lab_instrument_gateway) | SCPI-style instrument driver against an emulated bioreactor over TCP. Handles timeouts and reconnects while polling the error register. Readings land typed in SQLite behind a FastAPI dashboard, with fault injection for failure-path tests. |
| [analytics](https://github.com/barlowa124/lab-informatics/tree/main/analytics) | dbt/DuckDB warehouse over the LIMS registry and lablink capture events. A staging-to-marts flow guarded by 65 schema tests plus four domain tests covering audit-sequence contiguity and lock signing along with alarm-to-reading joins. Seeds are generated by driving the real services. Docs publish to Pages automatically. |
| [deploy](https://github.com/barlowa124/lab-informatics/blob/main/docker-compose.yml) | One-image deployment for the lab-informatics stack. A Dockerfile plus compose services run lablink (API on :8000), a LIMS demo run, and the dbt build with docs on :8080. `compose run verify` executes all three test suites inside the image. |
| [dockops](https://github.com/barlowa124/mol-ml/tree/main/dockops) | Docking pipeline ops: DUD-E staging, Vina backend, AFDB-vs-PDB structure QC that correctly argues against docking the AF model for EGFR, and per-run provenance manifests. |
| [vector-db-mcp](https://github.com/barlowa124/vector-db-mcp) | Local vector DB over MCP (stdio) with flat/IVF/HNSW scans. The committed benchmark shows flat exact search beating the indexes on the benchmarked corpus. Two construction bugs were caught by recall measurement. |

## Upstream contributions

- **scverse/scanpy** (open): [PR #4383](https://github.com/scverse/scanpy/pull/4383) keeps a user-supplied `hue` in `sc.pl.violin` instead of dropping it or erroring. [PR #4385](https://github.com/scverse/scanpy/pull/4385) fixes multi-column `groupby` crashing on non-string observations across the BasePlot family.
- **OpenADMET/openadmet-models** (open): PRs [#607](https://github.com/OpenADMET/openadmet-models/pull/607), [#608](https://github.com/OpenADMET/openadmet-models/pull/608), [#609](https://github.com/OpenADMET/openadmet-models/pull/609), [#610](https://github.com/OpenADMET/openadmet-models/pull/610). The last exposes `n_jobs` on the splito-based splitters.
- **chaidiscovery/chai-lab** (open): [PR #431](https://github.com/chaidiscovery/chai-lab/pull/431) reports pTM as the aggregate score for single-chain inputs, where the ipTM-based headline understated confidence. [PR #432](https://github.com/chaidiscovery/chai-lab/pull/432) persists the PAE/PDE/pLDDT matrices in Python-mode `scores.npz`.
- **UKGovernmentBEIS/inspect_evals** (open): [PR #2583](https://github.com/UKGovernmentBEIS/inspect_evals/pull/2583) registers [inspect-case-bench](https://github.com/barlowa124/inspect-case-bench), a port of CASE-Bench (ICML 2025, context-aware safety judgment vs human majority labels, 900 samples). Full two-model `.eval` run logs included per the register's evidence requirement.
- [TDC fork](https://github.com/barlowa124/TDC): tested fix for silent dataset-name substitution plus an AnnData getter/split API. [ProteinMPNN](https://github.com/barlowa124/ProteinMPNN): effective-seed visibility fix filed as [issue #154](https://github.com/dauparas/ProteinMPNN/issues/154).

## How the pieces connect

The repos are standalone, but a few components are shared on purpose so results cross-check each other.

- **ESM-2** is the protein encoder in three places with mixed outcomes. It drives rescoring in protein-design-ops and encodes targets in dti-fusion. In active-learning-loop it loses to one-hot on GB1, kept as a committed negative result.
- **The GB1 measured landscape** is the fitness oracle in both protein-diffusion and active-learning-loop, so the generation-steering and acquisition-enrichment numbers are comparable across repos.
- **AnnData/scanpy** is the shared base for the four QC packages (scrna-qc, organoid-qc, spatial-qc, cytof-qc). The upstream scanpy PRs came from plotting bugs hit in that workflow.
- **Claims bound to computation.** The claims verifier is ported from oncology-coscientist's draft verifier and vendored into bio-qc's scrna-qc and statgen as well as comp-tox-pipeline and llm-posttraining's eval report. `python3 tools/check_vendored_parity.py` in this repo checks all four claims copies plus the shared conformal and ESM-2 files against pinned digests in one run. The bioprocess runtime's replay certificates and protein-design-ops' pinned-seed provenance apply the same discipline, as does comp-tox's applicability-domain conditioning.
- **Shared conventions, vendored.** A common provenance schema (`docs/PROVENANCE.md`) is adopted by oncology-coscientist, bioprocess-decision-runtime, dockops, labStackDev and comp-tox-pipeline. A canonical conformal helper with parity tests runs in comp-tox-pipeline, protein-stability-uncertainty and cultivated-meat-multiomic. One content-addressed ESM-2 cache is vendored into protein-design-ops, dti-fusion and active-learning-loop.
- **Cross-repo flows.** lab-instrument-gateway captures feed bioprocess-decision-runtime's `capture-scenario` evaluator. job-watch's repost detection and oncology-coscientist's `embed` retrieval mode can both dispatch to vector-db-mcp's E5 embedder while keeping dependency-free defaults. qms-ai-system-resume's deployment instrument has a committed worked assessment of oncology-coscientist (verdict: BLOCKING_FINDINGS, as designed for a research tool).

## Scope

- Verified computation is not verified science: reproducing a calculation says nothing about whether the model or the hypothesis is right.
- Research and education use only. Nothing here is validated for GMP, clinical or manufacturing decisions.
- Rejected runs, abstentions and failures are part of the evidence record.
