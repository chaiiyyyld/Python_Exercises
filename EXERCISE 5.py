user = list(map(int, input("Enter 6 numbers: ").split()))
user_2 = list(map(int, input("Enter 5 number: ").split()))
common = []
for num in user:
    if num in user_2 and num not in common:
        common.append(num)
print("First list: ", user)
print("Second list: ",  user_2)

print("Common numbers: " , common)