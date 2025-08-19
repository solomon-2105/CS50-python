a=input("Input: ")
b=""
c=['a','e','i','o','u']
for i in a:
    if i.lower() in c:
        continue
    b+=i
print(f"Output: {b}")
