def solution(heights):
    answer = [0] * len(heights) # ������ ����� ���� �Ҵ�
    
    for i in range (len(heights)-1,-1,-1) : # �ǵ� ž���� ���������� �˻�
        for j in range (i-1,-1,-1) : # �ٷ� ������ �ϳ��� �Ųٷ� �˻�
            if heights[j] > heights[i] : 
                answer[i] = j+1
                break
        else :
            answer[i] = 0
    return answer