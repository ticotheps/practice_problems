"""
FINDING THE PERCENTAGE

The provided code stub will read in a dictionary containing key/value pairs of
name:[scores] for a list of students. Print the average of the scores array for
the student name provided, showing the 2 places after the decimal.

Example:
    - scores = {
        'alpha': [20, 30, 40],
        'beta': [30, 50, 70]
    }
    - query_name = 'beta'
    - beta's average score is (30 + 50 + 70)/3 = 50.0
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    queried_student_scores = None
    
    total_of_scores = 0
    
    avg_score = 0
    
    # search through key in 'student_marks' dict for match with 'query_name'
    for key in student_marks:
        # if there is a match, store the associated list of scores in a new
        # variable
        if key == query_name:
            # store the queried student's index from "student_marks" in the
            # 'queried_student_scores' variable
            queried_student_scores = student_marks[key]
            
    for score in queried_student_scores:
        total_of_scores += score
    # add the scores within that list to find a sum total of all the
    # scores
    


    # divide the sum total by the number of elements in the list to get the
    # average score for the queried student
    avg_score = float(total_of_scores/len(queried_student_scores))
    
    float_avg_score = "{:.2f}".format(avg_score)

    # print the average score
    print(float_avg_score)    
    