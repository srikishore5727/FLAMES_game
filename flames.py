name1 = input("Enter the first name: ").lower()
name2 = input("Enter the second name: ").lower()

for char in name1:
    if char in name2:
        name1 = name1.replace(char, "", 1)
        name2 = name2.replace(char, "", 1)

total = len(name1 + name2)

result = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

while len(result) > 1:   
    index = (total % len(result)) - 1
    if index < 0:
        index = len(result) - 1
    result = result[index+1:] + result[:index]

print("According to FLAMES, the relationship status is:", result[0])
