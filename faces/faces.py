def convert(a):
    a=a.replace(":)","🙂")
    a=a.replace(":(","🙁")
    return a
a=input()
print(convert(a))

