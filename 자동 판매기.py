x =int(input("투입한 돈: "))
y = int(input("물건값: "))
z = x-y
print("거스름돈:", z)
c500 = z//500
z = z % 500
c100 = z//100
print("500원 동전의 개수:", c500)
print("100원 동전의 개수:", c100)
