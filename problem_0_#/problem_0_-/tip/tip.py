def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))


    tip = dollars * percent
    print(f"leave ${tip:.2f}")


def dollars_to_float(dollars_to_float):
    # enter dollars in format $##.##
    if dollars_to_float.startswith("$"):
        return float (dollars_to_float.strip("$"))


def percent_to_float(percent_to_float):
    if percent_to_float.endswith("%"):
        return float (percent_to_float.strip("%")) / 100



if __name__ == '__main__':
    main()



