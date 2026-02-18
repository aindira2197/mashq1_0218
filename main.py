# 1
n = int(input())
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)

# 2
n = int(input())
for i in range(n, 0, -1):
    line = ""
    for j in range(i):
        line += "#"
    print(line)

# 3
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 4
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()

# 5
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
