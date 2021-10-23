# Example2 :

Mylist = []
Size = int(input("Please enter the numbre of students : "))

for i in range(0, Size):
    print(f"Enter the score of student no {i+1} : ")
    item = int(input())
    Mylist.append(item)

else:
    print(f"All student scores are {Mylist} ")
    print(f"The maximum score is {max(Mylist)}")


print("." * 50)

# Example3

MyString = input("Please enter the string\n ")
print(MyString.swapcase())

print("." * 50)

# Example4
print('-'.join(input("PLease enter the string :\n ").split()))
