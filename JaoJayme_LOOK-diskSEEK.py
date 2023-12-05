import matplotlib.pyplot as plt

def LOOK(arr, head, direction): 
    seek_count = 0
    distance = 0
    cur_track = 0

    left = [] 
    right = [] 

    seek_sequence = [] 

    # Appending values which are 
    # currently at left and right 
    # direction from the head. 
    for i in range(size): 
        if (arr[i] < head): 
            left.append(arr[i]) 
        if (arr[i] > head): 
            right.append(arr[i]) 

    # Sorting left and right vectors 
    # for servicing tracks in the 
    # correct sequence. 
    left.sort() 
    right.sort() 

    # Run the while loop two times. 
    # one by one scanning right 
    # and left side of the head 
    run = 2
    while (run): 
        if (direction == "left"): 
            for i in range(len(left) - 1, -1, -1): 
                cur_track = left[i] 

                # Appending current track to 
                # seek sequence 
                seek_sequence.append(cur_track) 

                # Calculate absolute distance 
                distance = abs(cur_track - head) 

                # Increase the total count 
                seek_count += distance 

                # Accessed track is now the new head 
                head = cur_track 

            # Reversing the direction 
            direction = "right"
              
        elif (direction == "right"): 
            for i in range(len(right)): 
                cur_track = right[i] 

                # Appending current track to  
                # seek sequence 
                seek_sequence.append(cur_track) 

                # Calculate absolute distance 
                distance = abs(cur_track - head) 
                  
                # Increase the total count 
                seek_count += distance 

                # Accessed track is now new head 
                head = cur_track 

            # Reversing the direction 
            direction = "left"
              
        run -= 1

    print("Total number of seek operations =", seek_count) 
    print("Seek Sequence is") 

    for i in range(len(seek_sequence)): 
        print(seek_sequence[i]) 
        
    return seek_sequence

def plotting(seek_sequence):
    plt.plot(seek_sequence, 'ro-', label="LOOK Seek Sequence")
    plt.plot(seek_sequence)
    plt.title("LOOK Algorithm")
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# User input for size and disk size
size = int(input("Enter the size of the request array: "))
disk_size = int(input("Enter the disk size: "))

# User input for the request array
arr = []
for i in range(size):
    track = int(input(f"Enter track {i + 1} of the request array: "))
    arr.append(track)

head = int(input("Enter the initial head position: "))
direction = input("Enter the direction (left or right): ")

seek_sequence = LOOK(arr, head, direction)
plotting(seek_sequence)
