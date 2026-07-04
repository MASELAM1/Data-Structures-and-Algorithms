# Complexity Cheat Sheet

Quick reference for common data structure operations (average case unless noted).

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Dynamic Array (list/vector) | O(1) | O(n) | O(n) amortized | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Hash Map | — | O(1) | O(1) | O(1) |
| Binary Search Tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap (binary) | — | O(n) | O(log n) | O(log n) (root) |

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

## Notes

- Add topic-specific notes here as separate files, e.g. `graph-traversal.md`, `dp-patterns.md`, `two-pointer-technique.md`.
- Keep entries short — this folder is a quick-reference, not a textbook.
