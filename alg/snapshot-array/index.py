class SnapshotArray:
    def __init__(self, n):
        self.snaps = [[None for _ in range(n)]]

    def set(self, index, val):
        l = len(self.snaps)
        self.snaps[l - 1][index] = val

    def snap(self) -> int:
        l = len(self.snaps)
        self.snaps = self.snaps + [self.snaps[l-1][:]]
        return l - 1

    def get(self, index, snapid):
        return self.snaps[snapid][index]

sol = SnapshotArray(3)
sol.set(0, 5)
print(sol.snap())
sol.set(0, 6)
print(sol.get(0, 0))
