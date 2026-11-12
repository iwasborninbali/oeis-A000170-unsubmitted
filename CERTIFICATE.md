# Verification certificate

## Claim

Simkin's exponential theorem implies the weak limit α−1 and forces any strong-form constant to be exp(α−1). The reported refined numerical estimates give approximately 0.944 and 2.570.

## Evidence

| What | Path | Author and date | Coverage | Result |
|---|---|---|---|---|
| Derivation | [proof.md](proof.md) | OpenAI Codex, 2026-11-13, from Simkin's theorem | Both implications | Exact consequences |
| Independent arithmetic check | [verification/check.py](verification/check.py) | OpenAI Codex, 2026-11-13 | Conversion of reported endpoints | 0.944 and 2.570 |

The arithmetic checker shares reported endpoints but no code with the source answer. It does not independently derive these endpoints.

## Replayed for this repository

2026-11-13, macOS local workstation: `python3 verification/check.py`; see [verification/logs/check.txt](verification/logs/check.txt) for the complete output.

## Not covered

Simkin's theorem and the reported numerical optimization were not independently reproved or certified. The strong asymptotic remains unproved here. Finite decimal computation cannot certify the input bounds.

## Guide's independent check

pending

## Verdict

partial — the numerical conversion was independently replayed; the numerical estimates and the theorem are external inputs, not independently certified here.
