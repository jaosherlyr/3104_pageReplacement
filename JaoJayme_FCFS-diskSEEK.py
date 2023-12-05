import matplotlib.pyplot as plt

size = 8

def FCFS(arr, head):
    seek_C = 0
    distance, curr_track = 0, 0

    for i in range(size):
        curr_track = arr[i]
        distance = abs(curr_track - head)
        seek_C += distance

    print(f"Total number of seek operations = ", seek_C)
    print("Seek Sequence is")

    for i in range(size):
        print(arr[i])

def plotting(arr):
    plt.title("DISK SEEK-FCFS")
    plt.plot(arr, 'ro-', label= arr)
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()

# Driver code
if __name__ == '__main__':
    # request array
    arr = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50

    FCFS(arr, head)
    plotting(arr)