import numpy as np
import matplotlib.pyplot as plt

##############
# HOMEWORK 2 #
##############

# Part 1

# write a function that takes as input a 1-dimensional numpy array and
# calculates the number of elements that are bigger than 0 but smaller than
# 10.

print("# HOMEWORK 2\n\n## Part 1\n")


def n_greater_zero_less_ten(arr):

    arr_tmp = []
    for i in arr:
        if i > 0 and i < 10:
            arr_tmp.append(i)
    return len(arr_tmp)


arr = np.array([1, 2, 3, -5, 222, 12, 8, 5, 7, 6, 5, 4, -9, 8])

print(
    n_greater_zero_less_ten(arr),
    "numbers in the following array are greater than 0 or smaller than 10:\n",
    arr,
)


# Part 2

print("\n## Part 2\n")

# 2.1. make a 1-dimensional array of 50 normally distributed random values, with
# mean=10 and SD=4

# 2.2. make a figures with two subplots, on subplot 1 should be a histogram of
# the result on subplot 2 should be a scatter plot containing the values in
# order on the X axis, and the actual values on the Y  (plt.subplot)

# 2.3. calculate the proporiton of these numbers that are smaller than 7

# 2.4. calculate the proportion of that is smaller 5 or bigger than 14

# 2.5. make a new scatter plot that has different color for these extreme values
# (red), that you found in 4. (you can use a for cycle to make a scatter for
# each dot individually)

np.random.seed(0)

# 2.1
arr_norm = np.random.normal(10, 4, 50)
print(
    "### Task 2.1: 1-dimensional Array with 50 normally distributed random values (M=10, SD=4):\n\n",
    arr_norm,
)


# 2.2
print("\n### Task 2.2: See plot")
plt.figure(figsize=(16, 6))
plt.subplot(121)
plt.hist(arr_norm, bins=10)
plt.title("Histogram")
plt.suptitle("Task 2.2: A figure with 2 subplots")
plt.subplot(122)
plt.scatter(range(len(arr_norm)), arr_norm)
plt.title("Scatter plot")
plt.show()

# 2.3
proportion_smaller_7 = len(arr_norm[arr_norm > 7]) / len(arr_norm)
print(
    "\n### Task 2.3: In the same array the proportion of numbers that are smaller than 7 is",
    proportion_smaller_7,
)
# alternative solution
# le = np.shape(arr_norm)
# pr1 = np.sum(arr_norm > 7) / le
# print(pr1[0])


# 2.4
proportion_sm5_gr14 = np.sum((arr_norm < 5) | (arr_norm > 14)) / len(arr_norm)
print(
    "\n### Task 2.4: While the proportion of numbers that are smaller than 5 or greater than 14 is",
    proportion_sm5_gr14,
)

# 2.5
print("\n### Task 2.5: See plot")

plt.figure(figsize=(8, 6))
plt.title("Task 2.5: Scatter plot showing the extreme values in red")
for i, val in enumerate(arr_norm):
    if val < 5 or val > 14:
        plt.scatter(i, val, c="r")
    else:
        plt.scatter(i, val, c="b")
plt.show()


# Part 3

print("\n## Part 3\n")

# write a function (My10Up) that takes as an input 2d numpy array (matrix) of
# numbers, calculates the number of elements that are bigger than 10 for each
# row. this function should return an array (Num10Up) that is the length of
# the number of rows in the input.

# 3.1. first write a solution with a for cycle, where you initialize Num10Up
# with an array of zeros (equaling the number of rows).

# 3.2. In fact the task can be solved without for cycle with a single line
# of code, try to find this solution as well.


# 3.1


def My10Up(arr):

    zerolen = np.zeros(len(arr))

    for i in range(np.shape(arr)[0]):
        for l in range(np.shape(arr)[1]):
            if arr[i, l] > 10:
                zerolen[i] = zerolen[i] + 1
    return zerolen


arr = np.array([[1, 20, 6], [40, 5, 70], [55, 23, 12], [78, 11, 22]])

res = My10Up(arr)

print("### Task 3.1: In this array\n\n", arr)
print("\nthe number of values over 10 are\n")
for i in range(len(res)):
    print(int(res[i]), "in row", i + 1)


# 3.2a: nested list comprehension


def my_10_up_nlc(arr):
    res = [len([i for i in row if i > 10]) for row in arr]
    return res


print("\n### Task 3.2: Use a one-liner for the same procedure:")
print("\nThe nested list comprehension gives us: ", my_10_up_nlc(arr))


# 3.2b: list comprehension with conditional sum


def my_10_up_lcsum(arr):
    res = [sum(row > 10) for row in arr]
    return res


print("\nThe list comprehension with conditional sum gives us: ", my_10_up_lcsum(arr))
