def plotting(seek_sequence):
    plt.plot(seek_sequence, 'ro-',label= seek_sequence)
    plt.plot(seek_sequence)
    plt.title("LOOK Algorithm")
    plt.ylabel('Track Number')
    plt.xlabel('Seek Sequence Order')
    plt.legend()
    plt.show()