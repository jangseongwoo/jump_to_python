def main():
    input_string = input()

    with open("new_file.txt", "a") as file:
        file.write(input_string)
    
    with open("new_file.txt", "r") as file:
        print(file.readline())

if __name__ == '__main__':
    main()
    