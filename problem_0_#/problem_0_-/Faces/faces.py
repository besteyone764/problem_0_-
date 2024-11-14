def main():
    # prompt user to enter a greeting and emoticon
    combined_input = input("Please enter a greeting and a emoticon ('Hello :)') or ('Goodbye :(')   ")

    greeting, emoticon = combined_input.split(maxsplit=1)

    combined_input = greeting + " " + emoticon

    if convert(combined_input):
        print(f"Hello \U0001F642")
    elif greeting == "Goodbye" and emoticon == ":(":
        print(f"Gooddbye \U0001F641")
    else:
        print(f"Hello \U0001F642 , Gooddbye \U0001F641")


def convert(combined_input):
    if combined_input == 'Hello :)':
        return True
    else:
        return False

if __name__ == '__main__':
    main()