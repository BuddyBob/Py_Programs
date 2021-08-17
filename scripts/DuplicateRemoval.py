head = [1,2,2]
numbers = []

class Solution():
    def __init__(self, head,numbers):
        self.head = head
        self.numbers = numbers
    def __str__(self):
        for i in range(len(self.head)):
            if self.head[i] not in self.numbers:
                self.numbers.append(self.head[i])
        return str(self.numbers)
conversion = Solution(head,numbers)
print(conversion)
