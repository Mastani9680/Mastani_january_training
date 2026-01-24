#Removing even numbers from the list
def remove_even(nums):
    result = []    #    It does not modify the list while iterating
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result


#input
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Print the corrected output
print(remove_even(nums))
