#!/usr/bin/env python3
"""Cross-repo vendored-parity check.

Every component below is deliberately vendored (not depended on) across
portfolio repos. Each repo's own test suite pins the digest on its side;
this script is the single command a reviewer can run from a checkout
forest to verify all copies at once.

Usage:
    python3 tools/check_vendored_parity.py [--root DIR]

--root defaults to the directory containing this repo's checkout, i.e.
the directory holding sibling clones of the portfolio repos. Exit status
is 1 if any copy is missing or differs from the pinned digest.
"""
import argparse
import hashlib
import sys
from pathlib import Path

# component name -> (pinned sha256, [repo/relative/path, ...])
VENDORED = {
    "claims.py (claims verifier, ported from oncocs verifier)": (
        "475eb4a6a338e363374c0810bf8f3861aec16cd41ae0c4ec2e0fbb54a6cc74a2",
        [
            "bio-qc/scrna_qc/src/scrna_qc/claims.py",
            "bio-qc/statgen/src/statgen/claims.py",
            "llm-posttraining/evals/claims.py",
            "mol-ml/comp_tox_pipeline/src/comp_tox/claims.py",
        ],
    ),
    "conformal.py (canonical conformal helpers)": (
        "fcba54721a3f106e3864ab43ad0cb61caf273c41426d7bfa649b542f5f72af00",
        [
            "bio-qc/cultivated_meat_multiomic/conformal.py",
            "bio-qc/scrna_qc/src/scrna_qc/conformal.py",
            "mol-ml/comp_tox_pipeline/src/comp_tox/eval/conformal_shared.py",
            "protein-ml/protein_stability_uncertainty/src/protstab/conformal.py",
        ],
    ),
    "esm_cache.py (content-addressed ESM-2 embedding cache)": (
        "2c80f1d43fffe47c126ce70e0f7342ced3458a3d902105c6275cacc338295531",
        [
            "mol-ml/dti_fusion/src/dti_fusion/esm_cache.py",
            "protein-ml/active_learning_loop/src/al_loop/esm_cache.py",
            "protein-ml/protein_design_ops/src/design_ops/esm_cache.py",
        ],
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path,
        default=Path(__file__).resolve().parents[2],
        help="directory holding the sibling repo checkouts")
    root = parser.parse_args().root

    drifted, missing, checked = [], [], 0
    for component, (pin, paths) in VENDORED.items():
        print(component)
        for rel in paths:
            path = root / rel
            if not path.exists():
                missing.append(rel)
                print(f"  MISSING  {rel}")
                continue
            digest = sha256(path)
            checked += 1
            status = "ok" if digest == pin else "DRIFTED"
            if digest != pin:
                drifted.append(rel)
            print(f"  {status:8} {rel}")
    print(f"\n{checked} files checked against pinned digests.")
    if missing:
        print(f"missing: {len(missing)} file(s)")
    if drifted:
        print("drifted:")
        for rel in drifted:
            print(f"  {rel}")
        return 1
    if missing:
        return 1
    print("All vendored copies match the pinned digests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
