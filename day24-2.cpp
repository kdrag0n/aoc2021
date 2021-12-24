#include "bits/stdc++.h"

using namespace std;

static int hash_zd(int z, int d) {
    int h = 17;
    h *= 31;
    h += z;
    h *= 31;
    h += d;
    h *= 31;
    return h;
}

#include "day24-2-prog.h"

static __attribute__((noinline)) unsigned long long got_zero(int res, int best, int d0, int d1, int d2, int d3, int d4, int d5, int d6, int d7, int d8, int d9, int d10, int d11, int d12, int d13) {
    string ns = to_string(d0) + to_string(d1) + to_string(d2) + to_string(d3) + to_string(d4) + to_string(d5) + to_string(d6) + to_string(d7) + to_string(d8) + to_string(d9) + to_string(d10) + to_string(d11) + to_string(d12) + to_string(d13);
    cout << "FOUND ZERO: " << ns << '\n';
    unsigned long long n = stoull(ns);
    if (n > best) {
        return n;
    }
    return 0;
}

int main(int argc, char **argv) {
    unsigned long long i = 0;
    unsigned long long best = 0;
    for (int d0 = 1; d0 <= 9; d0++) {
    auto z0 = run_prog0(0, d0);
    for (int d1 = 1; d1 <= 9; d1++) {
    auto z1 = run_prog1(z0, d1);
    for (int d2 = 1; d2 <= 9; d2++) {
    auto z2 = run_prog2(z1, d2);
    for (int d3 = 1; d3 <= 9; d3++) {
    auto z3 = run_prog3(z2, d3);
    for (int d4 = 1; d4 <= 9; d4++) {
    auto z4 = run_prog4(z3, d4);
    for (int d5 = 1; d5 <= 9; d5++) {
    auto z5 = run_prog5(z4, d5);
    for (int d6 = 1; d6 <= 9; d6++) {
    auto z6 = run_prog6(z5, d6);
    for (int d7 = 1; d7 <= 9; d7++) {
    auto z7 = run_prog7(z6, d7);
    for (int d8 = 1; d8 <= 9; d8++) {
    auto z8 = run_prog8(z7, d8);
    for (int d9 = 1; d9 <= 9; d9++) {
    auto z9 = run_prog9(z8, d9);
    for (int d10 = 1; d10 <= 9; d10++) {
    auto z10 = run_prog10(z9, d10);
    for (int d11 = 1; d11 <= 9; d11++) {
    auto z11 = run_prog11(z10, d11);
    for (int d12 = 1; d12 <= 9; d12++) {
    auto z12 = run_prog12(z11, d12);
    for (int d13 = 1; d13 <= 9; d13++) {
    auto z13 = run_prog13(z12, d13);
        if (i % 1000000000 == 0) {
            cerr << i << '\n';
        }

        int res = z13;
        if (res == 0) {
            int nb = got_zero(res, best, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13);
            if (nb != 0) {
                best = nb;
            }
        }
        i++;
    }}}}}}}}}}}}}}
    return 0;
}
