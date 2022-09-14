eng = int(input("영어 점수 입력: "))
math = int(input("수학 점수 입력: "))
total = eng+math

if total<110:
    print("불합격: 총합 점수가 부족합니다.")
elif eng>=40 and math >=40:
    print("합격")
elif eng >=40 and math <40:
    print("불합격: 수학 점수가 부족합니다.")
else:
    print("불합격: 영어 점수가 부족합니다.")
