# Eigen oplossing O(N * M)
steps=0
def sum_swap(array1, array2):
    global steps
    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            sum_of_array1 = sum(array1) - array1[i] + array2[j]
            sum_of_array2 = sum(array2) - array2[j] + array1[i]
            steps+=2

            if sum_of_array1 == sum_of_array2:
                return [i, j]
            steps+=1
    
    return None

# Oplossing met O(N + M): één keer over elke array itereren
# De 'target' som van beide arrays ligt in het midden tussen de twee sommen.
# Oftewel het gemiddelde tussen de twee.
# loop over de eerste array
# ...
# Concept (niet af)
def sum_swap2(array1, array2):
    sum_of_array1 = sum(array1)
    sum_of_array2 = sum(array2)

    if sum_of_array1 > sum_of_array2:
        higher_array = array1
        lower_array = array2
        sum_of_higher_array = sum_of_array1
        sum_of_lower_array = sum_of_array2

    elif sum_of_array2 > sum_of_array1:
        higher_array = array2
        lower_array = array1
        sum_of_higher_array = sum_of_array2
        sum_of_lower_array = sum_of_array1

    else:
        return "Sums of both arrays are already equal!"

    target_sum = (sum_of_array1 + sum_of_array2) // 2
    indices = []

    for i in range(0, len(higher_array)):
        if sum_of_lower_array + higher_array[i] == target_sum:
            indices.append(i)
            break

    for i in range(0, len(lower_array)):
        if sum_of_higher_array - lower_array[i] == target_sum:
            indices.append(i)
            break

    return indices

# Oplossing boek O(N + M)
def sum_swap3(array_1, array_2):
    hash_table = {}
    sum_1 = 0
    sum_2 = 0

    for i in range(0, len(array_1)):
        sum_1 += array_1[i]
        hash_table[array_1[i]] = i

    for i in range(0, len(array_2)):
        sum_2 += array_2[i]
    
    shift_amount = (sum_1 - sum_2) // 2

    for i in range(0, len(array_2)):
        if hash_table[array_2[i] + shift_amount]:
            return [hash_table[array_2[i] + shift_amount], i]
        
    return None

myArray1 = [5,3,2,9,1]
myArray2 = [1,12,5]
print(sum_swap3(myArray1, myArray2))
print(steps)

