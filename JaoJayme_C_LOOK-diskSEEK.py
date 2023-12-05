import matplotlib.pyplot as plt

def C_LOOK(arr, head):
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    # Tracks on the left of the head will be serviced
    # once the head comes back to the beginning (left end)
    for track in arr:
        if track < head:
            left.append(track)
        if track > head:
            right.append(track)

    # Sorting left and right vectors
    left.sort()
    right.sort()

    # Service requests on the right side of the head
    for cur_track in right:
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    # Jump to the last track that needs to be serviced in the left direction
    seek_count += abs(head - left[0])
    head = left[0]

    # Service requests again on the left
    for cur_track in left:
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is", seek_sequence)

    return seek_sequence

def plotting(seek_sequence):
    plt.plot(seek_sequence, 'ro-', label="C-LOOK Seek Sequence")
    plt.title("C LOOK Algorithm")
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

seek_sequence = C_LOOK(arr, head)
plotting(seek_sequence)
