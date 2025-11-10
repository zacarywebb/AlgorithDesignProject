# COP4533 – Programming Project: Greedy & Dynamic Programming

## Overview
This project explores different algorithmic approaches to the **Vault Selection Problem**, where given `n` vaults with assigned values, the goal is to choose a subset so that no two selected vaults are within `k` positions of each other while maximizing the total value.

The work is divided into two milestones:

- **Milestone 1:** Focused on designing and analyzing two *greedy algorithms* for simplified versions of the problem.  
- **Milestone 2:** Extended the problem to the general case using *dynamic programming* approaches with increasing efficiency.

---

## Implementations

| Program | Description | Complexity |
|----------|--------------|-------------|
| `program1.py` | Greedy solution for ascending values (S1). | Θ(n) |
| `program2.py` | Greedy solution for unimodal values (S2). | Θ(n) |
| `program3.py` | Exhaustive recursive search (baseline). | Θ(2ⁿ) |
| `program4A.py` | Top-down recursive DP with memoization. | Θ(n²) |
| `program4B.py` | Bottom-up iterative DP checking all valid indices. | Θ(n²) |
| `program5.py` | Optimized linear-time DP. | Θ(n) |

---

## Key Takeaways
- Greedy algorithms work well only under special structural assumptions (sorted or unimodal data).  
- Dynamic programming generalizes the solution, trading memory for massive speed gains.  
- Quadratic DP (4A, 4B) validated the theory, and the linear version (5) showed how much efficiency can improve.  
- Implementation details matter — 4B was about **36× faster** than 4A despite the same asymptotic complexity.

---

**Authors:**  
Zacary Webb  
Jevan Tenaglia
