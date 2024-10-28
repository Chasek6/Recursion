#Chase Stratton 
# Recursion
# October 25th 2024' 
# 10 Pts



  
#Import math for accessing built-in mathematical functions.
import math
# We use "import math" to access mathematical functions and constants.which helps simplify and optimize our calculations.
# This approach makes the code clearer, more concise, and easier to refactor if needed in larger scale project.
def binomial_coefficient_factorial(n, k):


# The line will calculate the biomial coefficient "n choose k" using the factorial formula, it returns the integer result of the dividing n! by dividing (k! * (n-k)!)
# which will represent the number of ways to choose k item from n without needing regard to order 
# As well, the double (//) performs integer division so the result will is always a whole number.

# Calculates n! / (k! * (n-k)!) using integer division to ensure  a whole number as the result.,
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))



# Test cases " to make sure each code functions as intended correctly " --> printing the expected outcome once the code is ran.

print("B(14, 10) =", binomial_coefficient_factorial(14, 10))   # Expected: 1001

print("B(10, 6) =", binomial_coefficient_factorial(10, 6))   # Expected: 210

print("B(13, 8) =", binomial_coefficient_factorial(13, 8))   # Expected: 1287

# Using math.factorial ensures accurate computation of large values.