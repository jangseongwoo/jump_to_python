def main():
    a = 0
    while a < 99:
        a += 1
        if a % 2 == 0:
            continue
        else:
            print(a)


if __name__ == '__main__':
    main()
    