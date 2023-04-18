n = int(input("Enter a natural N: "))

a = []

for i in range(n):
    a.append(int(input(f"Enter an integer A{i}: ")))

x = int(input("Enter an integer X: "))

print(f"Number {x} meets in array A {a.count(x)} times.")
