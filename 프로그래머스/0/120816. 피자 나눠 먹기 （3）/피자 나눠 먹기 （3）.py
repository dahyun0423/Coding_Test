#머쓱이네가 조각 수로 잘라 줄 수 있는 것 : 2 ~ 10조각까지 = slice
# n명의 사람이 최소 한조각 이상 피자먹으려면? 최소 몇판의 피자? 대답은 = pizza

def solution(slice, n):
    pizza = n / slice
    if (n % slice) != 0:
        pizza += 1
    return int(pizza)