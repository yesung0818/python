def pos(m):
    n= int(input(m))
    while (n<=0):
        n=int(input("양수를 입력하시오:"))
    return n
def area(w,h):
    return w*h
w=pos("사각형의 가로:")
h=pos("사각형의 세로:")
print("면적=",area(w,h))
            
