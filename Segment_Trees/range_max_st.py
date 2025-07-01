class SegmentTreeMax:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('-inf')] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('-inf')  # No overlap
        if l <= start and end <= r:
            return self.tree[node]  # Total overlap
        mid = (start + end) // 2
        left = self.query(2 * node + 1, start, mid, l, r)
        right = self.query(2 * node + 2, mid + 1, end, l, r)
        return max(left, right)  # Partial overlap

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

# Example usage:
arr = [2, 1, 5, 3, 9, 7]
seg_tree = SegmentTreeMax(arr)

print("Max from index 1 to 4:", seg_tree.query(0, 0, seg_tree.n - 1, 1, 4))  # Output: 9

# Update index 2 to 10
seg_tree.update(0, 0, seg_tree.n - 1, 2, 10)

print("Max from index 1 to 4 after update:", seg_tree.query(0, 0, seg_tree.n - 1, 1, 4))  # Output: 10
