from decimal import Decimal, getcontext
getcontext().prec = 40
lo, hi = Decimal('1.944000752'), Decimal('1.944001082')
print('reported numerical alpha interval minus one:', lo-1, hi-1)
print('exponential endpoints:', (lo-1).exp(), (hi-1).exp())
