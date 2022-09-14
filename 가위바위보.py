def gbb(a,b,x,y):
    if (x=="바위" and y=="가위") or (x=="가위" and y=="보") or (x=="보" and y=="바위"):
        print(a,"가 이겼습니다")
    elif (x=="바위" and y=="보") or (x=="가위" and y=="바위") or (x=="보" and y=="가위"):
        print(b,"가 이겼습니다!")
    else:
        print("비겼습니다")

a,b=input().split()
x,y=input().split()
gbb(a,b,x,y)
