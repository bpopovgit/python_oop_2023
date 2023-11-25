class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            idx = self.i % len(self.sequence)
            self.i += 1
            return self.sequence[idx]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
print("\n========================")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')


