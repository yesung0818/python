H,M = map(int,input().split())
(0<=H<=23, 0<=M<=59)
if M>=45 :
    print(H,M-45)
elif H>0 and M<45 :
    print(H-1,M+15)
else :
    print(23,M+15)
