# 509. Fibonacci Number

## Problem Description
The Fibonacci numbers, commonly denoted F(n), form a sequence such that each number is the sum of the two preceding ones, starting from 0 and 1.

* F(0) = 0
* F(1) = 1
* F(n) = F(n - 1) + F(n - 2), for n > 1.

**Goal:** Given an integer 'n', calculate F(n).

---

## Solution Approach: Iterative Dynamic Programming (Tabulation)

This solution uses an iterative (bottom-up) approach, which is the most optimal way to solve the standard Fibonacci problem. It is considered a form of Dynamic Programming (Tabulation) where we only store the two previous results needed for the next calculation, rather than building a full array.

1.  **Base Case Handling:** Checks for F(0) and F(1) and returns `n`.
2.  **State Initialization:** Uses two variables, `a` and `b`, initialized to 0 and 1, to represent the current state (F(i-2) and F(i-1)).
3.  **Shifting Pointers:** In each loop iteration, the sum `a + b` calculates the new Fibonacci number, and the pointers are shifted (`a` takes the old `b`'s value, and `b` takes the new sum) to prepare for the next step.
4.  **Final Result:** The variable `b` holds the final calculated value of F(n).

---

## Complexity Analysis

Based on the submission statistics:

### Time Complexity: O(n)
* The solution involves a single loop that runs exactly `n-1` times. Since the number of operations grows linearly with the input `n`, the time complexity is linear.
* The code achieved a runtime of **15 ms**, beating **75.19%** of other Python submissions.

### Space Complexity: O(1)
* The solution only uses a fixed, constant number of variables (`n`, `a`, `b`, and the loop counter `i`), regardless of the size of the input `n`.
* The code achieved a memory usage of **12.40 MB**, beating **80.32%** of other Python submissions.
