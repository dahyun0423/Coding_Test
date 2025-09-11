import math 

def solution(numer1, denom1, numer2, denom2):
    #1) 공통분모(lcm) = (a*b) //gcd(a,b)
    low = denom1 * denom2 // math.gcd(denom1, denom2)
    #2) 통분 후 분자의 합
    first = numer1 * (low // denom1)
    second = numer2 *(low // denom2)
    high = first + second
    #3) 기약분수로 약분
    g=math.gcd(high,low)
    answer = [high//g,low//g]
    
    return answer