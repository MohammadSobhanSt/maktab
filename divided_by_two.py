#  question 1

def divide_by_two(n, k):

    for i in range(k):
        n = n // 2
    return n


def main():
    n = int(input("enter a number: "))
    k = int(input("how many you want to Division? "))

    result = divide_by_two(n, k)

    print(result)


if __name__ == "__main__":
    main()
