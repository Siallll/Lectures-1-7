num = input()

if num == num[::-1]:  # if the number is equal to the end (palindrome)
    print(num)  # prints the palindrome
else:
    current_num = int(num)  # creating variable with  format int of the num
    while str(current_num) != str(current_num)[::-1]:  # while loop for unidentical (palindrome)
        current_num -= 1    # minuses the current num to create the num for palindrome
    lower_palindrome = current_num  # variable of the nearest low num palindrome

    current_num = int(num)
    while str(current_num) != str(current_num)[::-1]:
        current_num += 1
    upper_palindrome = current_num  # variable of the nearest upper palindrome num
    if (upper_palindrome - int(num)) >= (int(num) - lower_palindrome):  # if loop for nearest upper or lower palindrome
        print(lower_palindrome)
    else:
        print(upper_palindrome)
