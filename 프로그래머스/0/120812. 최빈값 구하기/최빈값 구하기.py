def solution(array):
    #최빈값 = 가장 많이 등장하는 값. 등장 횟수 비교해야지
    #f(x) = x
    #값마다 몇 번 나왔는가? 먼저 계산. 그 중 제일 큰 횟수 값 픽
    #배열->빈도분포->최댓값찾기->답 ㄱㄱ
    freq = {} #값 빈도 저장하기
    for i in array:
        freq[i] = freq.get(i,0)+1
    maximum = max(freq.values())
    
    candidates = []
    for key, value in freq.items():
        if value == maximum:
            candidates.append(key)
    if len(candidates)==1:
        return candidates[0]
    else:
        return -1
        