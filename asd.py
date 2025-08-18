#print A
# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str = result_str + "*"  
#         else:
#             result_str = result_str + " " 
#     result_str = result_str + "\n"  
# print(result_str) 

result = ""
for i in range(0,7):
    for j in range(0,7):
        print(j * "*")
        if(( j== 1 or j == 5 ) and i != 0) or ((i == 0 or i == 3) and (j > 1 and j <5 )):
            result = result + "*"
        else:
            result = result + " "
    result = result + "\n"
print(result)
        
