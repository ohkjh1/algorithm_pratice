# 우선 순위 표
# 스택 밖에 있을때 우선 순위
icp = {"+": 1, "/": 2, "(": 3}
# 스택 안에 있을때 우선 순위
isp = {"+": 1, "/": 2, "(": 0}
# # 우선 순위 표
# # 스택 밖에 있을때 우선 순위
# icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
# # 스택 안에 있을때 우선 순위
# isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}



# 중위표기식을 후위표기식으로 바꾸자
# infix ==> postfix

# infix : 후위표기식으로 바꿀 중위표기식
# n : 식의 길이
def get_postfix(infix, n):
    postfix = ""  # 결과로 출력할 후위 표기식

    stack = []

    # 문자열(중위표기식)에서 한글자씩 떼어오기
    for i in range(n):
        # i번째 글자가 피연산자인가?
        if infix[i] !=  "+":
            # i번째 글자가 피연산자이면 결과에 출력
            postfix += infix[i]
        # i번째 글자가 연산자인가?
        else:
            # i번째 글자가 닫는 괄호인경우
            if infix[i] == ")":
                # 여는 괄호가 나올 때까지 pop 해서 결과 출력
                while stack:
                    # 스택에서 연산자 하나 꺼내오기
                    c = stack.pop()
                    # 꺼낸 연산자가 여는 괄호면 연산자 꺼내기 중단
                    if c == "(":
                        break
                    # 여는 괄호가 아니면 괄호 안에 있는 연산자라는 의미
                    # 먼저 계산되어야한다. => 결과에 출력
                    postfix += c
            # i번째 글자가 닫는 괄호를 제외한 연산자인 경우
            else:
                # 현재 연산자의 우선순위보다
                # 스택의 탑에 있는 연산자의 우선순위가 같거나 높으면
                # 계속 pop 해서 출력한다.
                #isp의 s가 stack
                #infix(전위)는 처리해야할 subject
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    # 스택의 꼭대기에 있는 연산자가
                    # 현재 연산자보다 우선순위가 같거나 높으면 먼저 계산해야
                    # 하기 때문에 꺼내서 출력한다.
                    postfix += stack.pop()

                # 스택의 탑에 있는 연산자의 우선순위가 나보다 작으면
                # push
                stack.append(infix[i])

    # 스택에 남은 연산자 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix

# 후위표기식을 계산해서 결과를 내보내는 함수
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자 하나씩 떼어오기
    for c in postfix:

        # 글자 c가 피연산자이면 스택에 넣기
        if c != "+":
            stack.append(int(c))  # 타입 조심
            

        # 글자 c가 연산자인 경우 연산에 필요한 만큼 스택에서 피연산자를 꺼내서 계산
        # 계산한 결과를 다시 다음 연산에 사용해야하기 때문에 stack에 push
        else:
            # 오른쪽이 먼저 나온다.
            right = stack.pop()
            # 왼쪽이 나중에
            left = stack.pop()

            result = 0

            # 연산자의 종류에 따라서 계산
            if c == "+":
                result = left + right
            # elif c == "-":
            #     result = left - right
            # elif c == "*":
            #     result = left * right
            # elif c == "/":
            #     result = left / right


            # 계산한 결과를 다음 연산자의 피연산자로 사용해야한다.
            # 스택에 push
            stack.append(result)

    # 계산이 잘 됬다면 스택 안에는 하나만 남아 있을것이다.
    # 마지막에 스택에 남은 하나의 결과를 꺼내서 출력
    return stack.pop()



T=10
for tc in range(1,T+1):

    # infix = "(6+5*(2-8)/2)"
    N=int(input())
    infix = list(input())

    postfix = get_postfix(infix, len(infix))

    print(postfix)

    result = get_result(postfix)

    print(result)

