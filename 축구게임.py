import random
Options = ["왼쪽","중앙","오른쪽"]
while True :
    Computer_choice = random.choice(Options)
    user_choice = input("어디를 공격하시겠어요?(왼쪽,중앙,오른쪽)" )
    if Computer_choice==user_choice :
        print("패널티 킥을 실패하였습니다.")
    else :
        print("패널티 킥을 성공하였습니다.")
    
