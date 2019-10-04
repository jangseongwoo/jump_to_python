def main():
    with open("new_file.txt", "w") as f:
        for i in range(11, 20):
            data= "{} line .\n".format(i)
            f.write(data)
    

    f = open("new_file.txt", "r")
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()

if __name__ == '__main__':
    main()
    