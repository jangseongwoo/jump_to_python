def main():
    average = 0
    sum = 0 
    count = 0
    while True:
        number = input("number : ")
        count += 1
        sum += number
        average = sum / count
        print(average)


if __name__ == '__main__':
    main()
    