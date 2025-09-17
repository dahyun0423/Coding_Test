# 피자 6조각으로 잘라줘. 
# 나눠 먹을 사람 n명 
# n명이 주문한 피자를 남기지않고 모두 같은 수의 피자조각을 먹어야해
# 최소 몇판?
def solution(n):
    pizza = 1 #최소 1판부터 시작
    while True:
        if(pizza * 6) % n ==0: #전체 조각이 n명에게 딱 나눠떨어지면
            return pizza       #그때의 피자 판 수 반환
        pizza += 1