def main():
    sum_of_three_and_five_multiple = 0

    for i in range(2, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_three_and_five_multiple += i

    print(sum_of_three_and_five_multiple)


if __name__ == "__main__":
    main()