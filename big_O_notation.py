# write function that recieve an array and sum up all given values
# run experiement to calculate the time complexity 
# plot the linear time complexity, constant and quadratic


def find_sum (array) :

    total = 0
    for i in array:
        total += i
    return total

array = [1,2,3,4,6,5,9,5,8]
anothre_array = [1,5,6]
print(find_sum(array))
print(find_sum(anothre_array))

