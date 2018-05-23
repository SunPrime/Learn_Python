class A:
    count = 0

    def __init__(self):
        A.count += 1

    @staticmethod
    def method():
        return A.count

for i in range(10):
    A()

print(A.method())