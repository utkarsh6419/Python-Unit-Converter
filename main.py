"""Convert three common sets of units."""


def main():
    print("1) km to miles  2) kg to pounds  3) Celsius to Fahrenheit")
    choice = input("Choose: ").strip()
    try:
        value = float(input("Value: "))
    except ValueError:
        print("Enter a valid number.")
        return
    if choice == "1":
        print(f"{value * 0.621371:.2f} miles")
    elif choice == "2":
        print(f"{value * 2.20462:.2f} pounds")
    elif choice == "3":
        print(f"{value * 9 / 5 + 32:.2f} °F")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
