#  ======================================================================
#  By:  Sherly R. Jao
#       Joel T. Jayme
#  Detail:  Page replacement using LRU [Least Recently Used] algorithm
#  ======================================================================
import copy


#  Accept input for page items and frame list
def get_input():
    page_list = []

    page_num = int(input("\nEnter the number of PAGES: "))

    # accept the page items
    for i in range(page_num):
        user_input = input(f"Item {i + 1}: ")
        page_list.append(user_input)

    # accept number of frames
    frame_num = int(input("\nEnter number of frames: "))

    return page_list, frame_num


#  Display
def display(page_list, frame_list, status_list, frame_num):
    print("\nFIRST IN FIRST OUT Algorithm")

    print("|===========|", end="")
    print("=======|" * len(page_list))

    print("Page:\t\t", end="")
    for item in page_list:
        print(f"\t{item}\t", end="")

    print("\n\t\t\t", end="")
    for i in range(1, len(page_list) + 1):
        print(f"\t{i}\t", end="")

    print("\n-------------", end="")
    print("--------" * len(page_list), end="")

    #  loop for each frame
    for i in range(frame_num):
        print(f"\nFrame {i + 1}:\t", end="")
        print("\t-\t" * i, end="")
        #  loop for each item
        for n in range(i, len(frame_list)):
            print(f"\t{frame_list[n][i]}\t", end="")

        print("")

    print("|===========|", end="")
    print("=======|" * len(page_list))


#  Accept Page list and Frame number
def lru_logic(page_list, frame_num):
    list_item = []
    frame_list = []
    status_list = []
    arrival_order = []

    #  loop through the items
    for i in range(len(page_list)):
        status = "fault"

        #  check if i is not the first iteration, so we can copy the previous
        if i != 0:
            list_item = copy.deepcopy(frame_list[i - 1])

        # check if i is less than frame_num, so we can append
        if i < frame_num:
            list_item.append(page_list[i])
        else:
            for n in range(len(list_item)):
                if page_list[i] == list_item[n]:
                    status = "hit"


            if status != "hit":
                order = arrival_order.pop(0)

                for m in range(len(list_item)):
                    if first == list_item[m]:
                        list_item[m] = page_list[i]

        if status != "hit":
            arrival_order.append(page_list[i])

        frame_list.append(list_item)
        status_list.append(status)

    return frame_list, status_list


def main():
    #  page_list, frame_num = get_input()
    page_list = [7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_num = 3

    frame_list, status_list = lru_logic(page_list, frame_num)
    display(page_list, frame_list, status_list, frame_num)


if __name__ == "__main__":
    main()