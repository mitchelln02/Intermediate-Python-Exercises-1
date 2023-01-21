x = 1
total = 0
while x != 6:
    value = (float(input(f"Enter interger #{x}: ")))
    if value % 1 == 0:
         total = total + value
         x = x + 1
    else:
        print("Try again")

total = int(total)
print(f"The sum is {total} ")
