// Independent direct row-by-row bit-set enumeration, no repository code.
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>

static std::uint64_t visit(std::uint64_t columns, std::uint64_t rising,
                           std::uint64_t falling, std::uint64_t board) {
    if (columns == board) return 1;
    std::uint64_t choices = board & ~(columns | rising | falling);
    std::uint64_t total = 0;
    while (choices) {
        const std::uint64_t square = choices & (~choices + 1ULL);
        choices -= square;
        total += visit(columns | square, ((rising | square) << 1) & board,
                       (falling | square) >> 1, board);
    }
    return total;
}

static std::uint64_t count_queens(int n) {
    if (n == 0) return 1;
    const std::uint64_t board = (1ULL << n) - 1ULL;
    std::uint64_t ans = 0;
    // Reflect the first queen about the vertical center line.
    for (int j = 0; j < n / 2; ++j) {
        const std::uint64_t bit = 1ULL << j;
        ans += 2 * visit(bit, (bit << 1) & board, bit >> 1, board);
    }
    if (n % 2) {
        const std::uint64_t bit = 1ULL << (n / 2);
        ans += visit(bit, (bit << 1) & board, bit >> 1, board);
    }
    return ans;
}

int main(int argc, char** argv) {
    const int end = (argc > 1) ? std::atoi(argv[1]) : 18;
    if (end < 0 || end > 20) return 2;
    std::cout << "method: direct 64-bit occupancy/diagonal DFS; first-row reflection\n";
    for (int n = 0; n <= end; ++n) {
        const auto start = std::chrono::steady_clock::now();
        const auto count = count_queens(n);
        const double elapsed = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - start).count();
        std::cout << "n=" << std::setw(2) << n << " Q=" << count
                  << " seconds=" << std::fixed << std::setprecision(6)
                  << elapsed << '\n' << std::flush;
    }
}
