def main():
    student_score_list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    student_score_sum = 0

    for student_score in student_score_list:
        student_score_sum += student_score
    
    print(student_score_sum/len(student_score_list))


if __name__ == '__main__':
    main()
    