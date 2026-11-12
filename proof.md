# Consequence of Simkin's theorem

Let Q(n)=a(n). Simkin's theorem states Q(n)=((1+o(1)) n exp(−α))^n. Thus log Q(n)=n log n−αn+o(n). Stirling's formula gives log(n!)=n log n−n+o(n). Subtraction and division by n yield

lim (1/n) log(n!/Q(n))=α−1.

If the stronger relation Q(n)~n!/c^n holds for a fixed positive c, then log(n!/Q(n))=n log c+o(1), so log c=α−1 and c=exp(α−1). This establishes necessity, not the stronger relation. The reported numerical estimate α≈1.944001 yields α−1≈0.944001 and exp(α−1)≈2.570244. Simkin's own α=1.942±0.003 is less precise. The refined numerical estimate is not certified by this argument.
