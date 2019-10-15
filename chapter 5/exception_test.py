class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass



def main():
    eagle = Eagle()
    eagle.fly()


if __name__ == '__main__':
    main()
    