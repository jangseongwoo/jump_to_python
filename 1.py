import random

def main():
    a = list()
    for i in range(0,12):
        a.append(random.randint(1, 10000))
    
    for i in range(0,12):
        print(a[i])
    
    
    
    b = list()

    for j in range(12, 24):
        b.append(random.randint(1, 10000))

    print("###")
    for i in range(0,12):
        print(b[i])
    
    # a.sort()
    # b.sort()
    c = a+b
    
    c.sort()
    c.reverse()
    print(c)

if __name__ == "__main__":
    main()