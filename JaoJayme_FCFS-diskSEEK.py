import matplotlib.pyplot as plt

def FCFS(request, initial_head):
    size = len(request)
    seek_count = 0
    distance, curr_track = 0, 0
    seek_sequence = []

    for i in range(size):
        curr_track = request[i]
        distance = abs(curr_track - initial_head)
        seek_count += distance
        seek_sequence.append(curr_track)

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is", seek_sequence)

    return seek_sequence

def plotting(seek_sequence, algorithm_name):
    plt.title(algorithm_name)
    plt.plot(seek_sequence, 'ro-', label= seek_sequence)
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# User input for request array
request_array_fcfs = list(map(int, input("Enter the request array (comma-separated): ").split(',')))

# User input for initial head position
initial_head_position_fcfs = int(input("Enter the initial head position: "))

# Run FCFS algorithm
seek_sequence_fcfs = FCFS(request_array_fcfs, initial_head_position_fcfs)

# Plot the seek sequence
plotting(seek_sequence_fcfs, "FCFS")
