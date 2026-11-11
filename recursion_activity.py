# Activity 6: Recursive Array Toolkit
# Name: Angel Mai C. Tomenio
# Section: BSIT-2B

# MANUAL TRACING

# 1. SUM THE ARRAY
# Example: sum_array([2, 4, 6])
# = 2 + sum_array([4, 6])
# = 2 + 4 + sum_array([6])
# = 2 + 4 + 6 + sum_array([])
# = 2 + 4 + 6 + 0
# = 12


# 2. FIND THE LARGEST NUMBER
# Example: find_largest([3, 9, 5])
# = max(3, find_largest([9, 5]))
# = max(3, max(9, find_largest([5])))
# = max(3, max(9, 5))
# = 9


# 3. COUNT A CHOSEN NUMBER
# Example: count_number([2, 5, 2], 2)
# = 1 + count_number([5, 2], 2)
# = 1 + 0 + count_number([2], 2)
# = 1 + 0 + 1 + count_number([], 2)
# = 2


# 1. SUM THE ARRAY

def sum_array(numbers):

    # Base Case: An empty array has a sum of 0.
    if len(numbers) == 0:
        return 0

    # Recursive Case: Add the first number to the sum of the remaining numbers.
    return numbers[0] + sum_array(numbers[1:])


# 2. FIND THE LARGEST NUMBER

def find_largest(numbers):

    # Input Rule: The array must contain at least one number.
    if len(numbers) == 0:
        raise ValueError("The array must not be empty.")

    # Base Case: If only one number remains, it is the largest.
    if len(numbers) == 1:
        return numbers[0]

    # Recursive Case: Find the largest number in the remaining array.
    largest_in_rest = find_largest(numbers[1:])

    if numbers[0] > largest_in_rest:
        return numbers[0]
    else:
        return largest_in_rest


# 3. COUNT A CHOSEN NUMBER

def count_number(numbers, target):

    # Base Case: An empty array has no numbers to count.
    if len(numbers) == 0:
        return 0

    # Check if the first number matches the target.
    if numbers[0] == target:
        current_count = 1
    else:
        current_count = 0

    # Recursive Case: Count the target in the remaining array.
    return current_count + count_number(numbers[1:], target)


# TEST CASES

print("===== ACTIVITY 6: RECURSIVE ARRAY TOOLKIT =====")

# 1. SUM THE ARRAY

print("\n1. SUM THE ARRAY")

print("Empty array:", sum_array([]))
print("One number:", sum_array([7]))
print("Positive and negative numbers:", sum_array([5, -2, 8, -1]))

# Expected Results: 0, 7, 10


# 2. FIND THE LARGEST NUMBER

print("\n2. FIND THE LARGEST NUMBER")

print("One number:", find_largest([6]))
print("Largest at the beginning:", find_largest([20, 4, 9, 2]))
print("Largest at the end:", find_largest([3, 8, 5, 15]))
print("Negative numbers:", find_largest([-8, -3, -12, -5]))

# Expected Results: 6, 20, 15, -3


# 3. COUNT A CHOSEN NUMBER

print("\n3. COUNT A CHOSEN NUMBER")

print("Empty array:", count_number([], 4))
print("Target appears several times:", count_number([2, 5, 2, 8, 2], 2))
print("Target does not appear:", count_number([1, 3, 5, 7], 2))

# Expected Results: 0, 3, 0