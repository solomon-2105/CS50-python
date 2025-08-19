from fractions import Fraction

def main():
    while True:
        try:
            brr = input("Fraction: ")
            grr = Fraction(brr)
            if 0 <= grr <= 1:
                percentage = round(grr * 100)
                if percentage>=99: print("F")
                elif percentage<=1: print("E")
                else:print(f"{percentage}%")
                break
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

main()
