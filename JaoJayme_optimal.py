#  ======================================================================
#  By:  Sherly R. Jao
#       Joel T. Jayme
#  Detail:  Page replacement using optimal algorithm
#  ======================================================================

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

def display(page_list, frame_list, status_list, frame_num, log, text_log):
    print("===== Memory Management Simulator [Optimal Page Replacement Algorithm] =====\n")

    # Page replacement Log
    print("\n> Page Replacement Log")
    print("page length",len(page_list) * "=====")
    print(f"Legend: \t [page reference] \t \t [Status] \t \t [Log]")
    for i in range(len(page_list)):
        print(f"{i + 1}:\t\t\t", end="")

        print(page_list[i],end="")

        if status_list[i] == 'hit':
            print("\t\t \t 📌 HIT", end="")
        else:
            print("\t\t \t 🙅‍ FAULT", end="")

        if text_log[i]['text'] != 'replaced':
            print(f"\t \tPage{text_log[i]['page']} {text_log[i]['text']} in Frame {text_log[i]['frame'] + 1}scsc")
        else:
            print(f"\tPage{text_log[i]['page']} {text_log[i]['text']} Page {text_log[i]['replaced']} in Frame {text_log[i]['frame'] + 1}")

    # Memory State Visualization
    print("\n> Memory State Visualization")
    print("|===========|", end="" )
    print( "=======|" * len(page_list) )

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

    # Performance Metrics
    print("\n> Performance Metrics")
    hit_count = status_list.count("hit")
    fault_count = status_list.count("fault")
    print(f"Number of HITS:\t[\t{hit_count}\t]\t\t\tNumber of FAULTS:\t[\t{fault_count}\t]")
    print(f"HIT ratio:\t\t[\t{hit_count / len(page_list) * 100 :.2f}%\t]", end="")
    print(f"\t\tFAULT ratio:\t\t[\t{fault_count / len(page_list) * 100 :.2f}%\t]")


def optimal_algorithm(page_list, frame_num):
    fr = [1] * frame_num
    frame_list = []
    status_list = []
    log = []
    text_log = []

    hit = 0
    for i in range(len(page_list)):
        found = False
        for j in range(frame_num):
            if fr[j] == page_list[i]:
                hit += 1
                found = True
                break

        if found:
            status_list.append('hit')
            frame_list.append(fr.copy())
            text_log.append({'text': 'found', 'page': page_list[i], 'replaced': '', 'frame': j})
            continue

        emptyFrame = False
        for j in range(frame_num):
            if fr[j] == -1:
                fr[j] = page_list[i]
                emptyFrame = True
                break

        if emptyFrame:
            status_list.append('fault')
            frame_list.append(fr.copy())
            text_log.append({'text': 'added', 'page': page_list[i], 'replaced': '', 'frame': j})
            continue

        farthest = -1
        replaceIndex = -1
        for j in range(frame_num):
            k = i + 1
            while(k < len(page_list)):
                if fr[j] == page_list[k]:
                    if k > farthest:
                        farthest = k
                        replaceIndex = j
                    break
                k += 1
            if k == len(page_list):
                replaceIndex = j
                break

        fr[replaceIndex] = page_list[i]
        status_list.append('fault')
        frame_list.append(fr.copy())
        text_log.append({'text': 'replaced', 'page': page_list[i], 'replaced': fr[replaceIndex], 'frame': replaceIndex})

    return frame_list, status_list, log, text_log


def main():
# Example usage
    # page_list, frame_num = get_input()
    page_list = [7, 7, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    frame_num = 3

    frame_list, status_list, log, text_log = optimal_algorithm(page_list, frame_num)
    display(page_list, frame_list, status_list, frame_num, log, text_log)

if __name__ == "__main__":
        main()