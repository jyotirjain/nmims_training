# #lex_auth_0127382164803993601239

# #This verification is based on string match.

# def sum_of_numbers(list_of_num,filter_func=None):
#     if filter_func == None:
#         return sum(list_of_num)
#     else:
#         return sum(filter_func(list_of_num))

# def even(data):
#     return list(filter(lambda x: (x % 2 == 0), data))

# def odd(data):
#     return list(filter(lambda x: (x % 2 == 1), data))

# sample_data = range(1,11)

# print(sum_of_numbers(sample_data,None))

# #lex_auth_01269441810970214471

# def check_double(number):
#     if len(str(number)) == len(str(number * 2)):
#         num1 = set(str(number))
#         num2 = set(str(number * 2))
#         if num1 == num2:
#             return True
#     return False


# #Provide different values for number and test your program
# print(check_double(125874))

# lex_auth_012693816779112448160

# def calculate(distance,no_of_passengers):
#     cost = distance * 7
#     if (80 * no_of_passengers - cost) > 0:
#         return 80 * no_of_passengers - cost 
#     return -1

# #Provide different values for distance, no_of_passenger and test your program
# distance=20
# no_of_passengers=50
# print(calculate(distance,no_of_passengers))

# #lex_auth_01269438947391897654

# #Global variable
# list_of_marks=(12,18,25,24,2,5,18,20,20,21)

# def find_more_than_average():
#     avg = sum(list_of_marks)/len(list_of_marks)
#     return len(list(filter(lambda x: (x > avg), list_of_marks)))/len(list_of_marks) * 100

# def sort_marks():
#     return sorted(list_of_marks)

# def generate_frequency():
#     lst = [0] * 26
#     for i in list_of_marks:
#         lst[i]+=1
#     return lst
    
    

# print(find_more_than_average())
# print(generate_frequency())
# print(sort_marks())