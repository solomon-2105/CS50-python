a=input("camelCase: ")
b=""
for i in a:
    if i.isupper():
        b+="_"+i.lower()
    else:
        b+=i
print(f"snake_case: {b}")

