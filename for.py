#수학점수
test = [
    {
        'name': 'aaa',
        'number': 10101,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'bbb',
        'number': 10102,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ccc',
        'number': 10103,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },    {
        'name': 'ddd',
        'number': 10104,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'eee',
        'number': 10105,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    }
]


student_answer=[3,3,2,4,5,3,1,2,3,4]
math_answer=[1,3,2,4,5,3,1,2,3,4]

# for(student, correct) in zip(a, correct_answer):
#     print(student , '/', correct)

def get_score(student_answer, math_answer):
    #학생 점수구하기 문항당10점


    score=0

    for i in range(len(student_answer)):
        if student_answer[i] == math_answer[i]:
            score = score + 10

    return score

score = get_score(student_answer, math_answer)
print(score)


for student in test:
    score = get_score(student, correct_answer)
    print(score)








#나는버러지
# score = 100
# for i in correct_answer:
#     if i not in a:
#         score = score - 10
