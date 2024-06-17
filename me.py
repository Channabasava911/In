# Armstrong number
# no=int(input())
# sum=0
# rem=0
# num=no
# num=str(num)
# dig=len(num)
# num=int(num)
# while num!=0:
#     rem=num%10
#     sum=sum+rem**dig
#     num=num//10
# if sum==no:
#     print("Armstrong number")
# else:
#         print(" Not an Armstrong number")

# in a range
# Function to check if a number is an Armstrong number
# def is_armstrong(number):
#     sum = 0
#     rem = 0
#     num = number
#     num_str = str(num)
#     dig = len(num_str)
#     while num != 0:
#         rem = num % 10
#         sum = sum + rem ** dig
#         num = num // 10
#     return sum == number

# # Get the range from the user
# start_range = int(input("Enter the start of the range: "))
# end_range = int(input("Enter the end of the range: "))

# # Find and print all Armstrong numbers in the specified range
# print(f"Armstrong numbers in the range {start_range} to {end_range}:")
# for num in range(start_range, end_range + 1):
#     if is_armstrong(num):
#         print(num)



# disarium number
# no=int(input())
# sum=0
# rem=0
# num=no
# num=str(num)
# dig=len(num)
# num=int(num)
# while num!=0:
#     rem=num%10
#     sum=sum+rem**dig
#     dig=dig-1
#     num=num//10
# if sum==no:
#     print("Disarum number")
# else:
#         print(" Not a disarum number")

# Function to check if a number is a Disarium number
# def is_disarium(number):
#     sum = 0
#     num_str = str(number)
#     for i, digit in enumerate(num_str):
#         sum += int(digit) ** (i + 1)
#     return sum == number

# # Get the range from the user
# start_range = int(input("Enter the start of the range: "))
# end_range = int(input("Enter the end of the range: "))

# # Find and print all Disarium numbers in the specified range
# print(f"Disarium numbers in the range {start_range} to {end_range}:")
# for num in range(start_range, end_range + 1):
#     if is_disarium(num):
#         print(num)


# in a range
# def is_disarium(number):
#     sum = 0
#     rem = 0
#     num = number
#     num_str = str(num)
#     dig = len(num_str)
#     while num != 0:
#         rem = num % 10
#         sum = sum + rem ** dig
#         dig=dig-1
#         num = num // 10
#     return sum == number

# # Get the range from the user
# start_range = int(input("Enter the start of the range: "))
# end_range = int(input("Enter the end of the range: "))

# # Find and print all disarium numbers in the specified range
# print(f"Disarium numbers in the range {start_range} to {end_range}:")
# for num in range(start_range, end_range + 1):
#     if is_disarium(num):
#         print(num)

# chessboard
# orc="1357"
# er="2468"
# oc="aceg"
# ec="bdfh"

# s="f2"
# if s[0] in ec:
#     if s[1] in er:
#         print("black")
#     else:
#         print("white")
# else:
#     if s[0] in oc:
#         if s[1] in orc:
#             print("black")
#         else:
#             print("white")



# s = input()
# x = 0.0
# operators = ["+", "-", "*", "/", "%"]

# # Identify the operator and replace it with a space
# for op in operators:
#     if op in s:
#         operator = op
#         s = s.replace(op, " ")
#         break

# # Split the operands
# operands = list(map(float, s.split()))

# # Unpack the operands
# left_operand, right_operand = operands

# # Perform the operation based on the operator using match
# match operator:
#     case "+":
#         x = left_operand + right_operand
#     case "-":
#         x = left_operand - right_operand
#     case "*":
#         x = left_operand * right_operand
#     case "/":
#         x = left_operand / right_operand
#     case "%":
#         x = left_operand % right_operand

# print(x)  # Output: 4.0

# def move_zeros_to_end(nums):
#     non_zero_elements = [num for num in nums if num != 0]
#     zero_count = len(nums) - len(non_zero_elements)
#     return non_zero_elements + [0] * zero_count

# # Example usage:
# input_list = [4, 0, 5, 0, 1, 9, 0, 0]
# output_list = move_zeros_to_end(input_list)
# print(output_list)

# def move_zeros_to_end(nums):
#     result = []
#     zero_count = 0
    
#     # Collect non-zero elements
#     for num in nums:
#         if num != 0:
#             result.append(num)
#         else:
#             zero_count += 1
    
#     # Append zeros to the end
#     result.extend([0] * zero_count)
    
#     return result

# # Example usage:
# input_list = [4, 0, 5, 0, 1, 9, 0, 0]
# output_list = move_zeros_to_end(input_list)
# print(output_list)

# def move_zeros_to_end(nums):
#     # Initialize a pointer to keep track of the position to place the next non-zero element
#     insert_pos = 0
    
#     # Iterate through the list
#     for num in nums:
#         if num != 0:
#             # Move non-zero elements to the front of the list
#             nums[insert_pos] = num
#             insert_pos += 1
    
#     # Fill the remaining positions with zeros
#     for i in range(insert_pos, len(nums)):
#         nums[i] = 0
    
#     return nums

# # Example usage:
# input_list = [4, 0, 5, 0, 1, 9, 0, 0]
# output_list = move_zeros_to_end(input_list[:])  # Pass a copy to avoid modifying original list
# print(output_list)

# Explanation:
# Pointer insert_pos: This pointer keeps track of where to place the next non-zero element in the original list nums.

# First pass through the list:

# For each element num in nums, if num is non-zero (num != 0), it is placed at nums[insert_pos] and then insert_pos is incremented.
# Second pass to fill zeros:

# After moving all non-zero elements to the front of the list, iterate from insert_pos to the end of the list (len(nums)), setting each element to 0. This ensures all zeros are placed at the end of the list.
# Return nums: The function modifies nums in place and returns it.

# This approach is efficient with a time complexity of O(n), where n is the number of elements in the list nums, and it operates directly on the input list without creating additional lists or using extra space proportional to the input size



ls=[1,1,2,2,3,3,3]
# result=[0]*(len(ls) + 1)
# for i in ls:
#     result[i]+=1
# max_vote = max(result)

# a=[]
# count = 0
# index = 0
# for i in range(1,len(result)):
#     if result[i] == max_vote:
#         a.append(i)
#         index = i
#         count += 1
# print((index if count == 1 else -1))
    
    
# d  = {}
# for i in ls:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# max_vote = 0
# print(d)
# for i in d:
#     if max_vote < d[i]: 
#         max_vote = d[i] 
# a = []

# for i in d:
#     if max_vote == d[i]:
#         a.append(i)
# print((a[0] if len(a) == 1 else -1))
