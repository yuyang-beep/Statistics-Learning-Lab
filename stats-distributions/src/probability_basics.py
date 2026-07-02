class SampleSpace:
    def __init__(self, outcomes):
        self.omega = set(outcomes)

    def P(self, event):
        return len(event) / len(self.omega)

    def union(self, A, B):
        return A | B

    def intersect(self, A, B):
        return A & B

    def complement(self, A):
        return self.omega - A
    
    def inclusion_exclusion(self, A, B):
        return self.P(A) + self.P(B) - self.P(self.intersect(A, B))

if __name__ == "__main__":
    cards = SampleSpace(range(1, 14))
    A = {1, 2, 3}
    B = {1, 11, 12, 13}

    print(cards.P(A))
    print(cards.P(B))
    print(cards.inclusion_exclusion(A, B))