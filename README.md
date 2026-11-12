# OEIS A000170: asymptotic constants (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted.** (replaced by the registry tool)
<!-- oeis-status:end -->

## Definition

For n≥0, a(n) is the number of ways to place n mutually nonattacking queens on an n by n chessboard. The empty board has one configuration; the offset is 0.

## Terms / result

No terms change. The live [A000170](https://oeis.org/A000170), read 2026-11-13, contains Benoit Cloitre's Nov 10 2002 formula: `Strong conjecture: there is a constant c around 2.54 such that a(n) is asymptotic to n!/c^n; weak conjecture: lim_{n -> infinity} (1/n) * log(n!/a(n)) = constant = 0.90....` The same entry already states Simkin's theorem (Peter Luschny, Oct 07 2021) and its root-limit consequence (Vaclav Kotesovec, Jan 01 2023). The weak limit is α−1≈0.944; any strong-form constant must be exp(α−1)≈2.570. The strong asymptotic itself does not follow.

## How it was obtained

Subtract the logarithm of Simkin's asymptotic from Stirling's formula; see [proof.md](proof.md). Michael Simkin, *The number of n-queens configurations*, Advances in Mathematics 427 (2023), 109127, [doi:10.1016/j.aim.2023.109127](https://doi.org/10.1016/j.aim.2023.109127), [arXiv:2107.13460](https://arxiv.org/abs/2107.13460), establishes the exponential rate. Nobel, Agrawal and Boyd, *Computing tighter bounds on the n-queens constant via Newton's method*, Optimization Letters 17 (2023), 1229–1240, [doi:10.1007/s11590-022-01933-2](https://doi.org/10.1007/s11590-022-01933-2), report a sharper numerical interval, used for the decimals here. The source answer reports that its numerical optimization is not fully rationally certified.

## Verification

The proof derives both consequences from Simkin's theorem; a separate decimal calculation checks the conversion of the reported numerical endpoints. The theorem's proof and numerical optimization were not reverified. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Simkin established the exponential rate; the entry already includes it. Nobel, Agrawal and Boyd supplied the refined numerical estimates. The lab's ChatGPT answer and guide derived the consequences. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 verification/check.py` (under one second). Expected output:

```text
reported numerical alpha interval minus one: 0.944000752 0.944001082
exponential endpoints: 2.570243784010330841065142834030005699274 2.570244632190919514263754224455811086006
```

## Provenance

Source: `projects/science/athanor-oeis`, commit `11b7ea9cc6f4c0057731d8e36c023f8b36e7c27f`, `tasks/2026-11-12-A000170-queens-asymptotic/answers/2026-11-12-chatgpt.md`. Proof and checker were written for this repository.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
