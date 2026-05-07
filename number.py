num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT Prime")
            break
    else:
        print(num, "is Prime")
else:
    print(num, "is NOT Prime")
