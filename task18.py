n = int(input("Enter a natural N: "))

a = []

for i in range(n):
    a.append(int(input(f"Enter an integer A{i}: ")))

x = int(input("Enter an integer X: "))

delta = abs(a[0]-x)
close_el = a[0]

for el in a:
    if abs(el-x) < delta:
        close_el = el
print(f"The closest element in array A to number {x} is {close_el}.")
