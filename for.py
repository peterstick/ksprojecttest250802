#수학점수
test=[{'answer': [1,3,2,4,5,3,1,2,3,4]},
 {'answer': [1,5,3,2,3,1,4,5,3,3]},
 {'answer': [1,2,3,4,5,4,3,2,1,2]},
 {'answer': [1,3,2,4,5,3,2,5,5,4]},
 {'answer': [1,3,2,3,4,2,5,1,2,2]},
 {'answer': [1,3,3,5,2,3,1,2,2,2]},]

a=[3,3,2,4,5,3,1,2,3,4]
correct_answer=[1,3,2,4,5,3,1,2,3,4]

for(student, correct) in zip(a, correct_answer):
    print(student , '/', correct)

score=0

for i in range(len(a)):
    if a[i] == correct_answer[i]:
        score = score + 10

print(score)

#나는버러지
# score = 100
# for i in correct_answer:
#     if i not in a:
#         score = score - 10
