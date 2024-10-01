class Stats:
    def __init__(self, Data: list):
        if not all(isinstance(x, (int, float)) for x in Data):
            raise ValueError("Data list must only contain integers or floats.")
        self.Data = Data

    def sum(self) -> float:
        if not self.Data:
            return None
        return sum(self.Data)

    def mean(self) -> float:
        if not self.Data:
            return None
        return self.sum() / len(self.Data)

    def min(self) -> float:
        if not self.Data:
            return None
        return min(self.Data)

    def max(self) -> float:
        if not self.Data:
            return None
        return max(self.Data)

# Example Input
data = [10, 20, 30, 40, 50]

# Example Usage
stats = Stats(data)
print(stats.sum())   # Output: 150
print(stats.mean())  # Output: 30.0
print(stats.min())   # Output: 10
print(stats.max())   # Output: 50
