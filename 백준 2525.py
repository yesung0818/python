h,m= map(int,input().split())
time=int(input())

if(time+m)//60:
    h+=(time+m)//60
    m=(time+m)%60
else:
    m+=time

while h>23:
    hour%=24
print(h,m)
