def solution(n):
    answer = ""
    while n > 0:
        remains = int(n % 3)
        if remains == 0:
            answer += '4'
        elif remains == 1:
            answer += '1'
        elif remains == 2:
            answer += '2'
        n = int((n-1)/3)

    return answer[::-1]

for i in range(1,21):
    print(i, " : ", solution(i))
