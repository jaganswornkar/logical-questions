    n = int(input('enter the number of students : '))
    student_marks = {}
    for _ in range(n):
        name, *line = input('enter the name and marks of student (space separated)').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('enter the name of student for query')

    query_marks = student_marks[query_name]
    total_marks = sum(query_marks) 
    avg_mark = float(total_marks)/len(query_marks)
    avg_mark = format(avg_mark, '.2f')  # formating 2 digits after decimal
    

    print(avg_mark)