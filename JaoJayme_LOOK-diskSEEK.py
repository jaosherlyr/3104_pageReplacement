import matplotlib.pyplot as plt

def LOOK(arr, head, direction):
    seek_count = 0
    distance, cur_track = 0, 0
    seek_sequence = []

    # Sort the request array based on track numbers
    arr.sort()

    if direction == "left":
        left = [track for track in arr if track <= head]
        right = [track for track in arr if track > head][::-1]
    elif direction == "right":
        right = [track for track in arr if track >= head]
        left = [track for track in arr if track < head][::-1]

    for i in range(len(left)):
        cur_track = left[i]
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    for i in range(len(right)):
        cur_track = right[i]
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
direction = "left"

seek_sequence = LOOK(arr, head, direction)
plotting(seek_sequence)
