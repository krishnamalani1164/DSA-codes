class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0  # no overlap
        if l <= start and end <= r:
            return self.tree[node]  # total overlap
        mid = (start + end) // 2
        left = self.query(2 * node + 1, start, mid, l, r)
        right = self.query(2 * node + 2, mid + 1, end, l, r)
        return left + right  # partial overlap

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

# Usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

# Query sum from index 1 to 3
print("Query(1,3):", seg_tree.query(0, 0, seg_tree.n - 1, 1, 3))  # Output: 15

# Update index 1 to value 10
seg_tree.update(0, 0, seg_tree.n - 1, 1, 10)

# Query again
print("Query(1,3) after update:", seg_tree.query(0, 0, seg_tree.n - 1, 1, 3))  # Output: 22
