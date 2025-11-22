x= 6 #대입연산자
y=       4


#조건연산자
z = x == y
print("x == y : ", z)

z = x != y
print("x != y : ", z)
z = x > y
print("x > y : ", z)
z = x >= y
print("x >= y : ", z)
z = x<y
print("x < y : ", z)
z = x<=y
print("x <= y : ", z)

#사칙연산
z = x + y
print("x + y : ", z)
z = x - y
print("x - y : ", z)
z = x*y
print("x * y : ", z)
z= x / y
print("x / y : ", z)

z = x%y
print("x % y : ", z)
z = x // y
print("x // y : ", z)

z = x ** y
print("x ** y : ", z)



str_x = "hello"
str_y = "python"

str_z = str_x + str_y
print("str_x+str_y : ", str_z)


str_z = str_x*2
print("str_x*2 : ", str_z)



delayed_effect_skill_a = "" #snake case
delayedEffectSkillA = ""#camelCase


array_x = [12314, 12344]
array_y = [123567, 213123]

array_z = array_x + array_y
print("array_x + array_y : ", array_z)

array_z = array_x*2
print("array_x *2 : ", array_z)

array_z = array_x* array_y[0]
print("array_x + array_y[0] : ", array_z)

reportCard   = {
    "국어" : 3,
    "수학" : 2,
    "영어" : 6,
    "물리" : 4,
    "화학" : 2,
    "생명과학" : 5,
}

canApply = reportCard["국어"] <= 3 and reportCard["수학"] <= 3 and reportCard["영어"] <= 3
print("지원가능여부 : ", canApply)

#3합6
totalScore = reportCard["국어"]+reportCard["수학"]+reportCard["영어"] <= 6
print("3합6 : ", totalScore)

#과학 영재반
can_apply_for_the_gifted = reportCard["물리"] ==1 or reportCard["화학"] ==1 or reportCard["생명과학"] == 1
print("영재반 지원가능여부 :", can_apply_for_the_gifted


      