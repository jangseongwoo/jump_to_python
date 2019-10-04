def main():
    result = 0

    for number in range(1001):
        if number % 3 == 0:
            result += number

    print(result)

if __name__ == '__main__':
    main()
    