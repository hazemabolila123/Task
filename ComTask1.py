

# Example 5

MyList = []
n = int(input("How many Word you will enter ? "))

for i in range(0, n):
    item = input(f"Enter the element no {i + 1} : ")
    MyList.append(item)

else:

    print("-" * 50)
    for element in MyList:
        if len(element) <= 10:
            print(f"{element}".lower())

        else:
            print(f"{element[0]}{len(element) - 2}{element[-1]}".lower())

print("." * 50)

# Example6

n = int(input("Please enter the numbre of problems? : "))
counter = 0
for i in range(0, n):
    x = input()
    if x.count('1') >= 2:
        counter += 1
print(f"The numbre of problems will be solved = {counter} ")


print("." * 50)

# Example 7


# Example 8
Square_x, Square_y = map(int, input().split())
print((Square_x*Square_y) / 2)
