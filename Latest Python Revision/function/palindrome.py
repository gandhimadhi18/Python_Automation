def palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print("Given number is palindrome:")
    else:
        print("Given number is not palindrome:")
palindrome(205)
palindrome(1221)
palindrome(7)
palindrome(1234)

# 1. Extract last digit
#
# digit = num % 10
#
# 2. Build reverse
#
# reverse = reverse * 10 + digit
#
# 3. Remove last digit
#
# num = num // 10
# \(205 \ne 502\) → Not a palindrome

#   Loop numbefore	Digit extracted	Reverse calculation	Newreverse	numafter
#     1     121          1               0 * 10 +1               1        12
#     2     12           2               1 *10 + 2              12         1
#     3     1            1               12 * 10 + 1            121        0