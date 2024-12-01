steps = 0

def longest_consecutive_sequence(array):
    global steps

    hash_table = {}
    current_longest_consecutive_sequence = 0
    for number in array:
        hash_table[number] = True
        steps+=1
    
    for number in hash_table:
        current_sequence_count = 1
        current_number = number

        while current_number + 1 in hash_table:
            current_sequence_count += 1
            current_number += 1
            steps+=1
            
        if current_sequence_count > current_longest_consecutive_sequence:
            current_longest_consecutive_sequence = current_sequence_count

        steps+=1

    return current_longest_consecutive_sequence

#myArray = [10, 5, 12, 3, 55, 30, 4, 11, 2]
myArray = [19, 13, 15, 12, 18, 14, 17, 11, 45, 7766, 7565, 33, 34, 67, 12, 45, 64]
print(f"{longest_consecutive_sequence(myArray)} \nThe size of the input was {len(myArray)} and the number of steps was {steps}.")
 