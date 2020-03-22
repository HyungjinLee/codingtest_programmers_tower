def solution(heights):
    answer = [0] * len(heights) # 정답을 기록할 공간 할당
    
    for i in range (len(heights)-1,-1,-1) : # 맨뒤 탑부터 순차적으로 검사
        for j in range (i-1,-1,-1) : # 바로 전부터 하나씩 거꾸로 검사
            if heights[j] > heights[i] : 
                answer[i] = j+1
                break
        else :
            answer[i] = 0
    return answer