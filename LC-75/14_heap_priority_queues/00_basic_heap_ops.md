Default heap = MINHEAP

| Operation Type | Function                | Description                                                                 | Time Complexity  |
|----------------|-------------------------|-----------------------------------------------------------------------------|------------------|
| Build Heap     | heapq.heapify(x)        | Convert list `x` into a valid min‑heap in place.                            | O(n)             |
| Insert         | heapq.heappush(h, item) | Push `item` onto heap `h` while maintaining heap property.                  | O(log n)         |
| Remove         | heapq.heappop(h)        | Pop and return the smallest element from heap `h`.                          | O(log n)         |
| Push + Pop     | heapq.heappushpop(h, x) | Push `x`, then pop and return the smallest element (more efficient combo).  | O(log n)         |
| Pop + Push     | heapq.heapreplace(h, x) | Pop smallest element, then push `x` (heap size unchanged).                  | O(log n)         |
| k Smallest     | heapq.nsmallest(k, it)  | Return the `k` smallest elements from iterable `it`.                        | O(n log k)       |
| k Largest      | heapq.nlargest(k, it)   | Return the `k` largest elements from iterable `it`.                         | O(n log k)       |
| Peek           | h[0]                    | Access smallest element without removing it.                                | O(1)             |
