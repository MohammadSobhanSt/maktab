# question 2

def get_birthday():
    birthday = input("enter your birth date: ")
    return birthday


def parse_birthday(birthday):

    if len(birthday) == 8:
        year = (birthday[:2])
        month = (birthday[2:4])
        day = (birthday[4:])

    elif len(birthday) == 6:
        year = (birthday[:2])
        month = (birthday[2:4])
        day = (birthday[4:])

    else:
        raise ValueError("this birth date isn't right")

    if year == 0:
        year = 1400

    return year, month, day


def main():
    birthday = get_birthday()

    year, month, day = parse_birthday(birthday)

    print("saal:", year)
    print("maah:", month)
    print("rooz: ", day)


if __name__ == "__main__":
    main()

