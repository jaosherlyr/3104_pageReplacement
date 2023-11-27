# ======================================================================
#  By:  Sherly R. Jao
#       Joel T. Jayme
#  Detail:  Page replacement using FIFO [First In First Out] algorithm
#  ======================================================================
import copy


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
def display(page_list, frame_list, status_list, frame_num, log, text_log):
    print("===== Memory Management Simulator [FIFO - First in First Out] =====\n")

    #  print details
    print("> Details")
    print("Pages: [ ", end="")
    for i in range(len(page_list)):
        print(f"{page_list[i]}", end="")
        if i < len(page_list) - 1:
            print(", ", end="")
    print(" ]")
    print(f"Frames: [ {frame_num} ]\n")

    #  Page replacement Log
    print("> Page Replacement Log")
    print(f"Legend: [Item]: [State| Oldest in Memory <-- Newest in Memory] [Status] [Log]")
    for i in range(len(page_list)):
        print(f"{i + 1}:\t\t[ ", end="")
        for n in range(frame_num):
            if n < len(log[i]):
                print(f" {log[i][n]} ", end="")
            else:
                print(" - ", end="")

        print(" ]\t", end="")

        if status_list[i] == 'hit':
            print("📌 HIT\t", end="")
        else:
            print("🙅‍ FAULT", end="")

        if text_log[i]['text'] != 'replaced':
            print(f"\tPage {text_log[i]['page']} {text_log[i]['text']} in Frame {text_log[i]['frame'] + 1}")
        else:
            print(
                f"\tPage {text_log[i]['page']} {text_log[i]['text']} Page {text_log[i]['replaced']} in Frame {text_log[i]['frame'] + 1}")

    #  memory stata Visualization
    print("\n> Memory State Visualization")
    print("|===========|", end="")
    print("=======|" * len(page_list))

    print("Page:\t\t|", end="")
    for item in page_list:
        print(f"\t{item}\t|", end="")

    print("\n\t\t\t+", end="")
    print("-------+" * len(page_list))

    print("\t\t\t|", end="")
    for i in range(1, len(page_list) + 1):
        print(f"\t{i}\t|", end="")

    print("\n\t\t\t+", end="")
    print("-------+" * len(page_list))
    #  loop for each frame
    for i in range(frame_num):
        print(f"Frame {i + 1}:\t|", end="")
        print("\t-\t|" * i, end="")
        #  loop for each item
        for n in range(i, len(frame_list)):
            if i < len(frame_list[n]):
                print(f"\t{frame_list[n][i]}\t|", end="")
            else:
                print("\t-\t|", end="")

        print("")

    print("\t\t\t+", end="")
    print("-------+" * len(page_list))

    print("Status:\t\t|", end="")
    for status in status_list:
        print(f"\t{'H' if status == 'hit' else 'F'}\t|", end="")

    print("")
    print("|===========|", end="")
    print("=======|" * len(page_list))

    #  Performance Metrics
    print("\n> Performance Metrics")
    hit_count = status_list.count("hit")
    fault_count = status_list.count("fault")
    print(f"Number of HITS:\t[\t{hit_count}\t]\t\t\tNumber of FAULTS:\t[\t{fault_count}\t]")
    print(f"HIT ratio:\t\t[\t{hit_count / len(page_list) * 100 :.2f}%\t]", end="")
    print(f"\t\tFAULT ratio:\t\t[\t{fault_count / len(page_list) * 100 :.2f}%\t]")

    # Summary Statistics


def fifo_logic(page_list, frame_num):
    list_item = []
    frame_list = []
    status_list = []
    arrival_order = []
    log = []
    text_log = []
    frame = 0

    #  loop through the items
    for i in range(len(page_list)):
        status = "fault"

        #  check if i is not the first iteration, so we can copy the previous
        if i != 0:
            list_item = copy.deepcopy(frame_list[i - 1])

        # check if i is less than frame_num, so we can append
        if i < frame_num or len(list_item) < frame_num:
            if page_list[i] in list_item:
                status = "hit"
                frame = list_item.index(page_list[i])
                temp = {
                    "page": page_list[i],
                    "frame": frame,
                    "text": 'found'
                }
                text_log.append(temp)
            else:
                list_item.append(page_list[i])
                temp = {
                    "page": page_list[i],
                    "frame": i,
                    "text": 'placed'
                }
                text_log.append(temp)

        else:
            for n in range(len(list_item)):
                if page_list[i] == list_item[n]:
                    status = "hit"
                    temp = {
                        "page": page_list[i],
                        "frame": n,
                        "text": 'found'
                    }
                    text_log.append(temp)

            if status != "hit":
                first = arrival_order.pop(0)

                for n in range(len(list_item)):
                    if first == list_item[n]:
                        list_item[n] = page_list[i]
                        frame = n

                temp = {
                    "page": page_list[i],
                    "frame": frame,
                    "text": 'replaced',
                    "replaced": first
                }
                text_log.append(temp)

        if status != "hit":
            arrival_order.append(page_list[i])

        log_item = copy.deepcopy(arrival_order)
        log.append(log_item)
        frame_list.append(list_item)
        status_list.append(status)

    return frame_list, status_list, log, text_log


def main():
    #  page_list, frame_num = get_input()
    page_list = [7, 7, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_num = 3

    frame_list, status_list, log, text_log = fifo_logic(page_list, frame_num)
    display(page_list, frame_list, status_list, frame_num, log, text_log)


if __name__ == "__main__":
    main()
