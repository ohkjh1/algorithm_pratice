# T=int(input())
# for tc in range(1,T+1):
#     arr=list(input().split())
#     num=0
#     for i in arr:
#         for j in arr:
#             if i<j or j>i:
#                 if arr[j:j+1]=="()" and (arr[i]=="(" or ")"):
#                     num+=len(arr[j:j+1])+1
#     print(f"#{tc} {num}")            


# T=int(input())
# for tc in range(1,T+1):
#     arr=list(input())
#     sliced_sticks=0
#     new_sticks=0
#     final_sticks=0
#     lazer=0

#     for i in range(len(arr)):
#         if arr[i]=="(" and arr[i+1]==")":
#             arr[i]="lazer_s"
#             arr[i+1]="lazer_f"

    

#     for i in range(len(arr)):
#         if arr[i]=="(":
#             new_sticks+=1
#             final_sticks+=1
#     #for i in range(len(arr)):
#         elif arr[i]=="lazer_s":
#             lazer+=1

#     #for i in range(len(arr)):
#         elif arr[i]==")":
#             final_sticks-=1


#     sliced_sticks=lazer+new_sticks

#     print(f"#{tc} {sliced_sticks}")


T=int(input())
for tc in range(1,T+1):
    stack=[]
    sliced_sticks=0
    arr=list(input())

    for i in range(len(arr)):
        if arr[i]=="(": 
            stack.append("(")
        elif arr[i]==")":
            if arr[i-1] =="(":#규칙: 레이저로 쏜 나무가지 (레이저한 개수) + 해당 나무가지  수 
                stack.pop()#레이저가 쏜 나무가지 수가 현재까지 나무가지 수 이고 
                sliced_sticks+=len(stack) #현재까지 나뭇가지 수 
            else:
                stack.pop()#마지막으로 나뭇가지 만들기 끝내면서 이 나뭇가지를 하나 추가 
                sliced_sticks+=1 #마지막 괄호로 나뭇가지 만들기 끝내면서 그 나뭇가지 수 하나 추가 

            
    print(f"#{tc} {sliced_sticks}")
