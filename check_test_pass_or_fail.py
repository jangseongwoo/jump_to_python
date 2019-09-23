def main():
    student_score_list = [60, 30, 70, 23, 99, 88]
    number = 0 


    #### for in
    for student_score in student_score_list:
        number += 1
        if student_score > 60:
            print("{} student is pass".format(number))
        else:
            print("{} student is fail".format(number))

    #### for range
    for number in range(len(student_score_list)):
        if student_score_list[number] > 60:
            print("{} student is pass".format(number))
        else:
            print("{} student is fail".format(number))

if __name__ == '__main__':
    main()
    