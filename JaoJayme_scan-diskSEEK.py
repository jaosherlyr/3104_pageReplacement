import matplotlib.pyplot as plt

def SCAN(request, initial_head, direction):
    size = len(request)
    disk_size = 200

    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    # Appending end values
    # which have to be visited
    # before reversing the direction
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(disk_size - 1)

    for i in range(size):
        if request[i] < initial_head:
            left.append(request[i])
        if request[i] > initial_head:
            right.append(request[i])

    # Sorting left and right vectors
    left.sort()
    right.sort()

    # Run the while loop two times.
    # one by one scanning right
    # and left of the head
    run = 2
    while run != 0:
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - initial_head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                initial_head = cur_track

            direction = "right"

        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]

                # Appending current track to seek
                # sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - initial_head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now new head
                initial_head = cur_track

            direction = "left"

        run -= 1

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is", seek_sequence)

    return seek_sequence

def plotting(seek_sequence, algorithm_name):
    plt.title(algorithm_name)
    plt.plot(seek_sequence, 'ro-', label=seek_sequence)
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# User input for request array
request_array = list(map(int, input("Enter the request array (comma-separated): ").split(',')))

# User input for initial head position
initial_head_position = int(input("Enter the initial head position: "))

# User input for initial direction
initial_direction = input("Enter the initial direction (left/right): ")

# Run SCAN algorithm
seek_sequence_scan = SCAN(request_array, initial_head_position, initial_direction)

# Plot the seek sequence
plotting(seek_sequence_scan, "SCAN")
