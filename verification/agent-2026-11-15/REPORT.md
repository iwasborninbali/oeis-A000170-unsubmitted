# Independent verification — 2026-11-15

Source audited: supplied ZIP of `iwasborninbali/oeis-A000170-unsubmitted`, GitHub commit [`aed937ad048d5cb50b8166bdc61e2022f9537acb`](https://github.com/iwasborninbali/oeis-A000170-unsubmitted/commit/aed937ad048d5cb50b8166bdc61e2022f9537acb). Read `README.md`, `CERTIFICATE.md`, `PRIOR-ART.md`, `proof.md`, `verification/check.py`, and `verification/logs/check.txt`. The supplied archive has **no `programs/` directory**. This is a fresh analysis, not an adoption of the earlier certificate.

## Claim

**Exactly as scoped in `CERTIFICATE.md`:** Simkin's exponential theorem implies the weak limit `alpha - 1` and forces any strong-form constant to be `exp(alpha - 1)`; the reported refined numerical estimates give approximately `0.944` and `2.570`.

This **does not** assert `Q(n) ~ n!/c^n`, nor does it establish the reported numerical bounds on `alpha` independently.

## Proof check

**Referee verdict: correct (conditional on the stated published theorem); no invalid implication, no fatal gap.** `proof.md` is only seven physical lines, so the following checks exhaust its substantive steps:

1. **Line 3, `Q(n)=a(n)`: correct.** The OEIS and Simkin count the same nonattacking-queen configurations.
2. **Line 3, Simkin's `Q(n)=((1+o(1))n exp(-alpha))^n`: correct as a *cited external theorem*, not an original proof.** This is the central non-elementary imported result; its 60-page proof was **not independently re-proved**. *Status:* no gap in deduction, but fatal to a claim of self-contained or independently certified proof. *Remedy:* explicitly retain the Simkin citation, or independently referee that full theorem.
3. **Line 3, taking logarithms: correct, with an implicit positivity condition.** Write `epsilon_n -> 0`; then `log Q(n)=n log n-alpha*n+n log(1+epsilon_n)` and `log(1+epsilon_n)=o(1)`. For all sufficiently large `n`, `1+epsilon_n>0`, hence `Q(n)>0`. *Status:* fixable expository omission, not a mathematical error. *Remedy:* add these two sentences.
4. **Line 3, Stirling's formula: correct.** `log(n!)=n log n-n+O(log n)=n log n-n+o(n)`; known theorem, no conjecture. *Status:* no gap.
5. **Lines 3–5, subtraction and division: correct.** `log(n!/Q(n))=(alpha-1)n+o(n)` and the weak limit is exactly `alpha-1`. *Status:* no gap.
6. **Line 7, conditional strong asymptotic: correct, with implicit eventual positivity.** If `Q(n)/(n!/c^n)->1` and `c>0`, then the logarithm of that ratio is `o(1)`. Therefore `log(n!/Q(n))=n log c+o(1)`, and comparison of limits forces `c=exp(alpha-1)`. *Status:* fixable expository omission; the strong asymptotic itself is **not proved**. *Remedy:* spell out the ratio and `log(1+o(1))=o(1)`; do not invert the implication.
7. **Line 7, numeric `alpha≈1.944001`, `0.944001`, `2.570244`: correctly computed from *reported* numerical inputs, but not an independently established interval for the true constant.** The 2023 Nobel–Agrawal–Boyd paper reports `alpha in [1.944000752, 1.944001082]`, from floating-point optimization, and expressly says its rational-certification step was **not performed** (Section 3.3). *Status:* fixable as a clearly attributed approximate numerical statement; **fatal to any claim of fully certified bounds without additional work**. *Remedy:* independently construct feasible rational primal and dual witnesses with rigorous transcendental error bounds, or weaken the wording to numerical estimates.
8. **Line 7, Simkin's older `1.942 ± 0.003`: accurately quotes the paper abstract, though the theorem states a sharper `1.94 < alpha < 1.9449`.** *Status:* no error; cite the sharper theorem to avoid giving a misleading impression of precision.

There is **no unproved conjecture used in the derivation**. In particular, Cloitre's stronger `Q(n) ~ n!/c^n` conjecture is not used. The two independent-certification limitations are the published Simkin theorem and the reported numerical optimization; they are already disclaimed by `CERTIFICATE.md`. Importantly, `((1+o(1))n e^{-alpha})^n` is only an **exponential-rate** asymptotic, not a multiplicative `1+o(1)` asymptotic to `(n e^{-alpha})^n`.

## Independent computation

Two programs were written from scratch; neither imports or copies code from this repository:

- [`interval_check.py`](interval_check.py): exact rational fractions, Taylor polynomial with 90 terms for endpoint/midpoint `exp`, and rigorous positive-tail bound `0 < R_m < 2*x^(m+1)/(m+1)!` for `0 <= x <= 1`. At each endpoint and midpoint, the same first **80 decimal digits** are forced by lower and upper rational bounds. Checks **1,001** evenly spaced rational `alpha` values (inclusive), with 40-term Taylor bounds in the interior, requiring all the resulting exponential intervals to be strictly ordered and inside the certified endpoint enclosures. This checks *arithmetic given the assumed input endpoints*, not the correctness of those inputs or the limiting theorem. Runtime: **0.352511 s** wall clock. Output: [`interval_check.log`](interval_check.log).
- [`queens_count.cpp`](queens_count.cpp): standalone C++17 recursive row-by-row bit-set search tracking occupied columns and two diagonals, using vertical reflection on the first row. Built with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic`; checks every `Q(n)` for **`0 <= n <= 17`** against the published OEIS A000170 terms, all matching. `Q(17)=95815104`. The counted runs took approximately **26.2 s total**; `n=17` alone took **22.463710 s**. Output: [`queens_count.log`](queens_count.log). A separate exploratory `n=18` run exceeded an approximately 200 s execution limit without a complete result and is **not claimed as verified**.

The **exact reported endpoint transformation** (not a rigorously certified bound on the actual `alpha`) is

```
alpha input: [1.944000752, 1.944001082]
alpha - 1:   [0.944000752, 0.944001082]
exp(low-1):  2.57024378401033084106514283403000569927406958843870000567373420443972812769151757...
exp(high-1): 2.57024463219091951426375422445581108600595954406942453217017001962680324376039758...
mesh:        1001/1001 rational inputs, ordering/enclosure PASS
n range:     0..17, all 18 known exact counts match A000170
```

SHA-256 of **local program source and recorded output bytes**:

| File | SHA-256 |
| --- | --- |
| `interval_check.py` | `8cca0295eb4317caa5f8fa1b8d49a9feb804987e80418f5f515f9a0f82cf1f63` |
| `interval_check.log` | `779f91c6144875b7cf73584efdbdd447bc13a980130ea8f2783aaa1c72f17d38` |
| `queens_count.cpp` | `f5299b4a53550330dddf024c726715942ce434543122196c99dc6450403ff248` |
| `queens_count.log` | `932dff99dd51abb7624b98914924adbb660678e3db37b79a1cfd5440fbd0fb4e` |

The log is evidence of the specified run; per-`n` timing changes on rerun and so does the log's SHA-256. The 80 decimal digits are *truncations*, not independently asserted correctly-rounded 80-digit decimal approximations.

## Prior art

**The claimed implication is already in the literature or immediately implied by it; the numerical values are not new.** Sources verified by search on 2026-11-15:

1. **[OEIS A000170](https://oeis.org/A000170)**: Cloitre's dated Nov 10, 2002 weak/strong conjectures (`0.90`, `2.54`); Luschny, Oct 7, 2021 cites Simkin's theorem; Kotesovec, Jan 1, 2023 explicitly gives `lim a(n)^(1/n)/n = exp(-A359441)`. Applying Stirling is immediate. The entry's own cross-references include [A319284](https://oeis.org/A319284) (backtrack-tree diagonal), [A260318](https://oeis.org/A260318), [A260319](https://oeis.org/A260319), [A260320](https://oeis.org/A260320) (symmetry decomposition), and [A348129](https://oeis.org/A348129). They do not appear to contribute a competing stronger asymptotic.
2. **[OEIS A359441](https://oeis.org/A359441)** (Kotesovec, Jan 1, 2023): *the* n-queens constant, already carrying the more precise numerical estimates `1.944000752019729...` and `1.9440010813092217...` and the exact root-limit identity for A000170. This is direct, dated prior art for the numeric constant and exponential rate.
3. **[Michael Simkin, arXiv:2107.13460](https://arxiv.org/abs/2107.13460)**, journal version *Advances in Mathematics* **427** (2023), 109127, [DOI](https://doi.org/10.1016/j.aim.2023.109127): proves the root-limit / exponential-rate theorem; theorem 1.1 gives `1.94 < alpha < 1.9449`. Its proof was not re-refereed here.
4. **[Parth Nobel, Akshay Agrawal, Stephen Boyd, arXiv:2112.03336](https://arxiv.org/abs/2112.03336)**, *Optimization Letters* **17** (2023), 1229–1240, [DOI](https://doi.org/10.1007/s11590-022-01933-2), [author-hosted full article](https://stanford.edu/~boyd/papers/pdf/n_queens.pdf): reports the refined endpoints directly. Its Section 3.3 notes that converting the floating-point calculation into a rigorous rational certificate was not done.
5. **[Math Stack Exchange question 1485740](https://math.stackexchange.com/questions/1485740/how-can-i-calculate-the-total-number-of-unique-solutions-for-the-n-queen-puzzle)**: an **April 21, 2025 comment by Travis Willse explicitly writes `c=e^(alpha-1)=2.57024...`**. Thus even the converted constant is not novel. The comment loosely says this “confirms” the old strong conjecture; this inference is *not valid* from the exponential-rate theorem alone. The updated answer also has an apparent typo A000710 for A000170.
6. **[MathOverflow question 322132](https://mathoverflow.net/questions/322132/lower-bound-on-the-number-of-solutions-of-n-queens-problem)** (2019): predates Simkin, discusses older exponential lower bounds and cites Rivin–Vardi–Zimmermann, *American Mathematical Monthly* **101** (1994), 629–639 (zbMATH identifier **ZBL0825.68479**), and [Luria arXiv:1705.05225](https://arxiv.org/abs/1705.05225). No earlier proof of the stated exact alpha-conversion found there.
7. **[B. Green, open problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)** (recent document), problem 97: cites Simkin and Nobel–Agrawal–Boyd and says the stronger asymptotic, rather than an asymptotic for its logarithm, remains open; consistent with the certificate's explicit limitation.
8. **[Liu, Liao, Wang, *Physical Review E* 114 (2026), 034125](https://doi.org/10.1103/cx7m-n3d5)**: references Simkin and the refined approximately 1.94400 constant. It does not establish novelty for this contribution; its abstract uses `~` informally for the exponential-rate conclusion, so it cannot be used as proof of the stronger `n!/c^n` equivalence.

**History search:** Attempted OEIS's [A000170 history endpoint](https://oeis.org/history?seq=A000170) and [A359441 history endpoint](https://oeis.org/history?seq=A359441); both returned HTTP 403 through the available browser. Consequently the entire edit-by-edit history could not be inspected; the **dated historical annotations visible in the entries** were inspected instead. **zbMATH search:** searched the indexed domain `zbmath.org` for Simkin (2023) and Nobel–Agrawal–Boyd (2023), and the names/titles on the general web; no accessible specific zbMATH record for these two articles surfaced. The MathOverflow source supplies the older 1994 zbMATH identifier. **MathOverflow/MSE search:** searched for `n-queens`, `asymptotic`, `Simkin`, `alpha`, `2.57024`, `0.944`; the 2025 MSE occurrence above is decisive, and no separate prior proof of a strong-form equivalence was located. Searches do not establish absolute absence of other sources.

## Verdict

**PARTIAL — mathematics of the stated *conditional consequences* is correct; independently verified arithmetic and finite examples; originality is disproved by dated prior art.** A fully independent certificate would need (i) an independent check/refereeing of Simkin's global asymptotic theorem and (ii) certified rational primal/dual bounds for the large numerical convex optimizations if the refined interval is to be asserted rigorously. Neither has been done. A strong-form asymptotic `Q(n)~n!/c^n` is neither claimed nor established. Nothing in this review warrants changing A000170's integer terms or claiming a new theorem.
