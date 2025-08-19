from datetime import datetime

valid_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        date_input = input("Date: ").strip()

        try:
            date = datetime.strptime(date_input, "%m/%d/%Y")
            print(date.strftime("%Y-%m-%d"))
            break
        except ValueError:
            pass

        try:
            date = datetime.strptime(date_input, "%B %d, %Y")
            print(date.strftime("%Y-%m-%d"))
            break
        except ValueError:
            pass

        print("Invalid date format. Please enter a valid date.")

if __name__ == "__main__":
    main()
