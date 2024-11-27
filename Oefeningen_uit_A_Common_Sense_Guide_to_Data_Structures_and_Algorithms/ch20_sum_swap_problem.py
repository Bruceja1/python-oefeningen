# Eigen oplossing O(N * M)
def sum_swap(array1, array2):
    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            sum_of_array1 = sum(array1) - array1[i] + array2[j]
            sum_of_array2 = sum(array2) - array2[j] + array1[i]

            if sum_of_array1 == sum_of_array2:
                return [i, j]
    
    return None

# Oplossing met O(N + M) 
# Som van de een ligt hoger dan de som van de ander
# De 'target' som van beide arrays ligt in het midden tussen de twee sommen.
# Oftewel het gemiddelde tussen de twee.
# loop over de eerste array
# 
def sum_swap2(array1, array2):
    sum_of_array1 = sum(array1)
    sum_of_array2 = sum(array2)

    target_sum = (sum_of_array1 + sum_of_array2) / 2

    target = target_sum % 2
    if target_sum // 2 != 0:
        return None

    return target_sum

myArray1 = [5,3,2,9,1]
myArray2 = [1,12,5]
print(sum_swap2(myArray1, myArray2))


