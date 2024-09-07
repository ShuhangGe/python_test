class Solution:
    def reverse(self, x: int) -> int:
        reversed_number = 0
      
        # These define the range of acceptable 32-bit signed integer values
        min_int, max_int = -2**31, 2**31 - 1
      
        while x:
            # Check if the reversed_number will overflow when multiplied by 10
            if reversed_number < min_int // 10 + 1 or reversed_number > max_int // 10:
                # Return 0 on overflow as per problem constraints
                return 0    
            print('x1: ',x)
            # Extract the least significant digit of the current number
            digit = x % 10
            print('digit: ', digit)
            # # Adjustments for negative numbers when the extracted digit is non-zero
            # if x < 0 and digit > 0:
            #     digit -= 10
          
            # Shift reversed_number digits to the left and add the new digit
            reversed_number = reversed_number * 10 + digit
            print('reversed_number: ',reversed_number)
            # Remove the least significant digit from x
            x = (x - digit) // 10
            print('x2: ', x)
      
        # Return the reversed number within the 32-bit signed integer range
        return reversed_number
solution = Solution()
result = solution.reverse(-123)
print(result)