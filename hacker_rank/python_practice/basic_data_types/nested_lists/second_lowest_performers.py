""""
NESTED LISTS

Given the names and grades for each student in a class of N students, store them
in a nested list and print the name(s) of any student(s) having the second
lowest grade.

NOTE: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.

EXAMPLE:
    - records = [
        ["chi", 20.0],
        ["beta", 50.0],
        ["alpha", 50.0]
    ]

"""

def find_second_lowest_performers(nested_students_scores):
    scores_lst = []
    student_scores_dict = {}
    lowest_score = None
    second_lowest_score = None
        
    for i in range(0, len(nested_students_scores)):
        student_info_lst = nested_students_scores[i]
        # print("student_info_lst = ", student_info_lst)
        student_str = student_info_lst[0]
        # print("student_str = ", student_str)
        score_float = student_info_lst[1]
        # print("score_float = ", score_float)
        
        # append a score to the total list of scores
        scores_lst.append(score_float)
        # print("scores_lst = ", scores_lst)
        
        # add a student's name to the existing list of students with a particular score in the
        # 'student_scores_dict'.
        # print("student_scores_dict[str(score_float)] = ", student_scores_dict[str(score_float)])
        if score_float in student_scores_dict.keys():
            student_scores_dict[score_float].append(student_str)    
        else:
            student_scores_dict[score_float] = [student_str]

        # print("student_scores_dict = ", student_scores_dict)
        
    # sort list of scores in ascending order
    sorted_scores_lst = sorted(scores_lst)
    # print("sorted_scores_lst = ", sorted_scores_lst)
    
    for j in range(0, len(sorted_scores_lst)):
        score = sorted_scores_lst[j]
        # print("score = ", score)
        # print("lowest_score = ", lowest_score)
        if lowest_score is None:
            lowest_score = score
            # print("UPDATED lowest_score = ", lowest_score)
        else:
            # print("second_lowest_score = ", second_lowest_score)
            if score > lowest_score:
                second_lowest_score = score
                # print("UPDATED second_lowest_score = ", second_lowest_score)
                break
            
    second_lowest_performers = student_scores_dict[second_lowest_score]      
    # print("second_lowest_performers = ", second_lowest_performers)
            
    sorted_second_lowest_performers = sorted(second_lowest_performers)
    # print("sorted_second_lowest_performers = ", sorted_second_lowest_performers)
    
    return sorted_second_lowest_performers
