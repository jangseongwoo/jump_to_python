def main():
    coffee = 10

    while coffee > 0:
        money = int(input())
        if money == 300:
            print("take coffe")
            coffee -= 1
        elif money > 300:
            print("take coffe")
            print("give you left money {}".format(money - 300))
            coffee -= 1
        else:
            print("money not enough.")

    print("coffee is sold out")

if __name__ == '__main__':
    main()
    