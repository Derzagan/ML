def square():
    res = []
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        res.append(nums[i] ** 2)
    evenNums = [num for num in res if num % 2 == 0]
    return evenNums


    

    
Answer = square()
print(Answer)

# def square():
#     res = []
#     EveNums = []
#     nums = list(map(int, input().split()))
#     for i in range(len(nums)):
#         res.append(nums[i] ** 2)
#     for j in range(len(res)):
#         if res[j] % 2 == 0:
#             EveNums.append(res[j])
#     return EveNums
    


    

    
# Answer = square()
# print(Answer)
