import sys

cases = int(input().rstrip())
for i in range (cases):
    line = sys.stdin.readline().rstrip()
    num1, num2 = (int(val) for val in line.split(" "))
    Sum = num1 + num2
    prod = num1*num2
    print(Sum, prod)
