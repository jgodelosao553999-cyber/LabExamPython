def toBinaryIfNumber(valNumber):
    if valNumber == 0:
        return "0"
    elif valNumber == 1:
        return "1"
    else:
        return toBinaryIfNumber(valNumber // 2) + str(valNumber % 2)

def isPalindrome(valString):
    if len(valString) <= 1:
        return True
    else:
        if valString[0] != valString[-1]:
            return False
        else:
            return isPalindrome(valString[1:-1])

print("Enter a value: ")
val = input()

if val.isdigit():  
    is_input_palindrome = isPalindrome(val)
    print(f"Input is a palindrome: {is_input_palindrome}")

    
    binary_val = toBinaryIfNumber(int(val))
    print(f"Binary equivalent: {binary_val}")
    is_binary_palindrome = isPalindrome(binary_val)
    print(f"Binary is a palindrome: {is_binary_palindrome}")
else:
   
    is_input_palindrome = isPalindrome(val)
    print(f"Input is a palindrome: {is_input_palindrome}")
    print("(No binary conversion since input is text)")