def main():
    tree_hit = 1
    while tree_hit <= 10:
        print("tree hit : {}".format(tree_hit))
        if tree_hit == 10:
            print("tree is go away")
        tree_hit += 1

if __name__ == "__main__":
    main()