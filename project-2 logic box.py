print("welcome")
print(" PATTERN LOGIC")
print("Find the hidden pattern")

n = int(input("Enter a number: "))

for i in range(1, n + 1):

    if i % 3 == 0:
        for j in range(i):
            print("@", end=" ")
    elif i % 2 == 0:
        for j in range(i):
            print("#", end=" ")
    else:
        for j in range(i):
            print("*", end=" ")

    print()
    
print(" BUTTERFLY PATTERN")
print("Find the hidden pattern")

n = int(input("Enter a number: "))

for i in range(1, n + 1):

    if i % 2 == 0:
        for j in range(i):
            print("#", end=" ")
    else:
        for j in range(i):
            print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    if i % 2 == 0:
        for j in range(i):
            print("#", end=" ")
    else:
        for j in range(i):
            print("*", end=" ")

    print()

    
