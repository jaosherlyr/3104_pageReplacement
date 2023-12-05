import matplotlib.pyplot as plt

def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head) 

def findMin(diff):
    index = -1
    minimum = float('inf')

    for i in range(len(diff)):
        if (not diff[i][1] and minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index

def shortestSeekTimeFirst(request, head):
    if (len(request) == 0):
        return []

    l = len(request)
    diff = [[0, 0] for _ in range(l)]

    seek_count = 0
    seek_sequence = [0] * (l + 1)

    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)

        diff[index][1] = True
        seek_count += diff[index][0]
        head = request[index]

    seek_sequence[len(seek_sequence) - 1] = head

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is")

    for i in range(l + 1):
        print(seek_sequence[i])

    return seek_sequence

def plotting(seek_sequence):
    plt.title("SSFT")
    plt.plot(seek_sequence, 'ro-', label=seek_sequence)
    plt.plot(seek_sequence)
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# User input for the request array
size = int(input("Enter the size of the request array: "))
proc = []
for i in range(size):
    track = int(input(f"Enter track {i + 1} of the request array: "))
    proc.append(track)

head = int(input("Enter the initial head position: "))

seek_sequence = shortestSeekTimeFirst(proc, head)
plotting(seek_sequence)
