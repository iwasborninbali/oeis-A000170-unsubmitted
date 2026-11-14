#!/usr/bin/env python3
"""Independent exact-rational Taylor enclosure of exp(alpha-1)."""
from fractions import Fraction
from time import perf_counter

LOW = Fraction(1944000752, 10**9)
HIGH = Fraction(1944001082, 10**9)


def enclosure(x, degree):
    """For 0 <= x <= 1, sum(t_0..t_m) < exp(x) < sum+2*t_(m+1)."""
    assert 0 <= x <= 1
    term = Fraction(1)
    partial = term
    for k in range(1, degree + 1):
        term *= x / k
        partial += term
    omitted = term * x / (degree + 1)
    return partial, partial + 2 * omitted


def certified_truncation(bounds, decimals=80):
    lo, hi = bounds
    radix = 10**decimals
    p, q = (lo.numerator * radix // lo.denominator,
            hi.numerator * radix // hi.denominator)
    assert p == q, 'Taylor enclosure does not determine last digit'
    return f'{p // radix}.{p % radix:0{decimals}d}'


def main():
    t = perf_counter()
    assert HIGH - LOW == Fraction(330, 10**9)
    lo_x, hi_x = LOW - 1, HIGH - 1
    lo_bound = enclosure(lo_x, 90)
    hi_bound = enclosure(hi_x, 90)
    assert lo_bound[1] < hi_bound[0]
    print('source alpha endpoints (assumed, not certified):', str(float(LOW)), str(float(HIGH)))
    print('alpha minus one exactly:', str(lo_x), str(hi_x))
    print('exp(lower alpha minus one), first 80 DECIMAL digits (rigorously enclosed):',
          certified_truncation(lo_bound))
    print('exp(upper alpha minus one), first 80 DECIMAL digits (rigorously enclosed):',
          certified_truncation(hi_bound))
    mid = enclosure((lo_x + hi_x) / 2, 90)
    print('exp(midpoint alpha minus one), 80 digits:', certified_truncation(mid))
    prev = None
    for i in range(1001):
        x = lo_x + (hi_x - lo_x) * Fraction(i, 1000)
        lower, upper = enclosure(x, 90 if i in (0, 1000) else 40)
        assert lo_bound[0] <= lower and upper <= hi_bound[1]
        if prev is not None:
            assert prev < lower, 'mesh enclosures not strictly ordered'
        prev = upper
    print('mesh: 1001 exact rational values of alpha on inclusive source interval')
    print('mesh: PASS, all 1001 exp intervals ordered and within endpoint enclosures')
    print('endpoint order: 90; mesh order: 40; all arithmetic Fraction exact')
    print('wall_clock_seconds: %.6f' % (perf_counter() - t))


if __name__ == '__main__':
    main()
