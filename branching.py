#Welcome python
r = "morning"

count = 0
while count <= 5:
    print(count)
    count += 1

count = 0
while count <= 10:
    print(f"Count: {count}")
    count += 1

rice = ["grain", "tiny","starch", "sweet", "food"]

for x in rice:
    if x == "starch":
        print("Same as carb")
        continue
    if x == "sweet":
        break

    print(x)

People = ["John", "Paul", "Sara", "Susan"]

for persons in People:
    if persons == "Sara":
        break
    print(f"Current Person: {persons}")


#function
def name(female ="Georgia",male="George"):
    real = f"{female} and {male} are twin sibling"
    return real

print(name())    
#if, elif, else:
r= 67
bee = 43

if 
    