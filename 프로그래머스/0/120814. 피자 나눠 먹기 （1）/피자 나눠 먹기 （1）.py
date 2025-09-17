#피자를 무조건 7조각으로 짤라줘야만 해.
#나눠 먹을 사람 n이 주어졌어? 
#이 사람들은 다 한조각 이상 먹기위해 필요한 피자 수 = pizza
def solution(n):
    pizza = n / 7
    if n % 7 != 0 :
        pizza += 1
    return int(pizza)