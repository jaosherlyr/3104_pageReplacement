import matplotlib.pyplot as plt

def C_LOOK(arr, head):
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    # Sort the request array
    arr.sort()

    # Split the requests into left and right based on the head
    left = [track for track in arr if track < head]
    right = [track for track in arr if track >= head]

    # Sort left and right arrays
    left.sort()
    right.sort()

    # Service requests in the right direction
    for i in range(len(right)):
        cur_track = right[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    # Jump to the beginning of the disk and service requests in the left direction
    head = 0
    seek_count += (right[-1] - head)
    
    for i in range(len(left)):
        cur_track = left[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is", seek_sequence)

    return seek_sequence

def plotting(seek_sequence):
    plt.plot(seek_sequence, 'ro-',label= seek_sequence)
    plt.plot(seek_sequence)
    plt.title("LOOK Algorithm")
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# Driver code
arr = [176, 79, 34, 60, 92, 11, 41, 114]
head = 50

seek_sequence = C_LOOK(arr, head)
plotting(seek_sequence)
