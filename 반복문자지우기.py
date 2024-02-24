import sys
sys.stdin = open("sample_input (1).txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    s = list(input().strip())  # 입력 문자열을 리스트로 변환하고 양쪽 공백을 제거합니다.
    stack = []

    for char in s:
        if stack and stack[-1] == char:  # 스택이 비어있지 않고, 스택의 가장 위에 있는 문자와 현재 문자가 같다면
            stack.pop()  # 스택의 가장 위에 있는 문자를 제거합니다.
        else:
            stack.append(char)  # 그렇지 않으면 현재 문자를 스택에 추가합니다.

    print(f"#{test_case} {len(stack)}")  # 스택에 남아 있는 문자의 개수를 출력합니다.

# T = int(input())
# for T in range(1, T + 1):
#     s=list(input())
#     stack=[]

#     for i in range(len(s)-1):
#         if len(s)!=0 and s[i] != s[i+1]:
#             stack.append(s[i])
#         else:
#             stack.append(s[i])
#             print(stack)
#             stack.pop()
#             print(stack)
            
            
            
        


#     print(f"#{T} {len(stack)}")