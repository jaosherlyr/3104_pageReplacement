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
def display(page_list, frame_list, status_list, frame_num, order_log, text_list, frequency_list):
    print("\n===== Memory Management Simulator [LFU - Least Frequently Used] =====\n")

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
    print(f"Legend: [Item]: [State| [[Page : Frequency] ...] [Status] [Log]")
    for i in range(len(page_list)):
        print(f"{i + 1}:\t\t[ ", end="")
        for n in range(frame_num):
            if n < len(order_log[i]):
                print(f" [{order_log[i][n]} : {frequency_list[i][n]}] ", end="")
            else:
                print(" [- : -] ", end="")

        print(" ]\t", end="")

        if status_list[i] == 'hit':
            print("📌 HIT\t", end="")
        else:
            print("🙅‍ FAULT", end="")

        if text_list[i]['text'] != 'replaced':
            print(f"\tPage {text_list[i]['page']} {text_list[i]['text']} in Frame {text_list[i]['frame'] + 1}")
        else:
            print(
                f"\tPage {text_list[i]['page']} {text_list[i]['text']} Page {text_list[i]['replaced']} in Frame {text_list[i]['frame'] + 1}")

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


def lfu_logic(page_list, frame_num):
    frame_list = []
    frequency_list = []
    text_list = []
    status_list = []
    order_log = []
    optimal_list = []

    frame_item = []
    frequency_item = []

    order = []
    replaced = 0

    for i in range(len(page_list)):
        status = "fault"
        if_replace = False
        is_hit = False

        if i != 0:
            frame_item = copy.deepcopy(frame_list[i - 1])
            frequency_item = copy.deepcopy(frequency_list[i -1])
            order = copy.deepcopy(order_log[i - 1])

        if page_list[i] in frame_item:
            status = "hit"
            frame = frame_item.index(page_list[i])
            text = "found"
            # index = order.index(page_list[i])
            is_hit = True
            frequency_item[frame] += 1
        elif i < frame_num or len(frame_item) < frame_num:
            text = "placed"
            frame = 0 if i == 0 else len(frame_item)
            frequency_item.append(1)
            frame_item.append(page_list[i])
        else:
            freq_dict = {}

            for item, freq in zip(frame_item, frequency_item):
                freq_dict[item] = freq

            min_freq = min(freq_dict.values())
            min_freq_items = [item for item, freq in freq_dict.items() if freq == min_freq]
            replaced_page = min(min_freq_items, key=lambda x: order.index(x))

            text = "replaced"
            frame = frame_item.index(replaced_page)
            replaced = replaced_page
            if_replace = True

            frame_item[frame] = page_list[i]
            frequency_item[frame] = 1

            index = order.index(replaced_page)
            order.pop(index)

        if not if_replace:
            text_item = {
                "page": page_list[i],
                "text": text,
                "frame": frame
            }
        else:
            text_item = {
                "page": page_list[i],
                "text": text,
                "frame": frame,
                "replaced": replaced
            }

        text_list.append(text_item)
        if not is_hit:
            order.append(page_list[i])
        order_log.append(order)
        frame_list.append(frame_item)
        status_list.append(status)
        frequency_list.append(frequency_item)

    return frame_list, status_list, order_log, text_list, frequency_list


def main():
    # page_list, frame_num = get_input()
    page_list = [7, 7, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_num = 3

    frame_list, status_list, order_log, text_list, frequency_list = lfu_logic(page_list, frame_num)
    display(page_list, frame_list, status_list, frame_num, order_log, text_list, frequency_list)


if __name__ == "__main__":
    main()