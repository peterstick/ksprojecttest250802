

score = int(input("점수를 내놓거라 닝겐"))


if score < 0 and score > 100:
    print("말같은 소리를 해라 닝겐")
if score >= 80:
    print("합격이다 닝겐")
elif score >= 60:
    print("기회를 한번 더 주지 닝겐")
else:
    print("강해져서 돌아와라 닝겐")



#while True:
 #   user_input = input("값을내놔러ㅏ")
#
 #   if user_input.lower() == "z":
  #      break


input_number = int(input("수를 내놔라"))
index =0

while index < input_number:
    print(index)
    index += 1