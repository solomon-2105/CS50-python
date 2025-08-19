def main():
    items = {}
    try:
        while True:
            item = input().strip().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
    except EOFError:
        print()
    for item in sorted(items):
        print(f"{items[item]} {item.upper()}")
if __name__ == "__main__":
    main()
