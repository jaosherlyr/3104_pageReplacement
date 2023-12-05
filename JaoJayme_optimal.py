# ======================================================================
#  By:  Sherly R. Jao
#       Joel T. Jayme
#  Detail:  Page replacement using OPT [Optimal] algorithm
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
# Page replacement Log
def display(page_list, frame_list, status_list, frame_num, log, text_log):
    print("===== Memory Management Simulator [Optimal Page Replacement Algorithm] =====\n")

    
    print("\n> Page Replacement Log")
    print(f"Legend: [Item]: [State| [[Pages] < [Most Optimal]] [Status] [Log]")
    for i in range(len(page_list)):
        print(f"{i + 1}:\t\t\t", end="")

        for j, frame_content in enumerate(frame_list[i]):
            if j == 0:
                next_to_replace = frame_list[i + 1][0] if i + 1 < len(frame_list) else None
                print(f"[ {frame_content} ", end="") if frame_content != next_to_replace else print(f"[ {frame_content} ", end="")
            elif j == frame_num - 1:
                print(f"{frame_content} ] ", end="")
            else:
                print(f"{frame_content} ", end="")

        # Display the optimal replacement indication
        if i < len(page_list) - 1:
            optimal_replacement = frame_list[i + 1][0]
            print(f"< [ {optimal_replacement} ] ", end="")

        if status_list[i] == 'hit':
            print("\t📌 HIT\t", end="")
        else:
            print("\t🙅‍ FAULT", end="")

        if text_log[i]['text'] != 'replaced':
            print(f"\tPage{text_log[i]['page']} {text_log[i]['text']} in Frame {text_log[i]['frame'] + 1}")
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
    fr = ["-"] * frame_num  # Use "-" to represent an empty frame
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
            if fr[j] == "-":  # Check for an empty frame represented by "-"
                fr[j] = page_list[i]
                emptyFrame = True
                break

        if emptyFrame:
            status_list.append('fault')
            frame_list.append(fr.copy())
            text_log.append({'text': 'added', 'page': page_list[i], 'replaced': '', 'frame': j})
            continue

        farthest = -1
        replaceIndex = 0
        for j in range(frame_num):
            k = i + 1
            while k < len(page_list):
                if fr[j] == page_list[k]:
                    if k > farthest:
                        farthest = k
                        replaceIndex = j
                    break
                k += 1
            if k == len(page_list):
                replaceIndex = j
                break

        if fr[replaceIndex] != page_list[i]:
            
            fr[replaceIndex] = page_list[i]
        status_list.append('fault')
        frame_list.append(fr.copy())
        text_log.append({'text': 'replaced', 'page': page_list[i], 'replaced': fr[replaceIndex], 'frame': replaceIndex})

    return frame_list, status_list, log, text_log




def main():
# Example usage
    page_list, frame_num = get_input()
    # page_list = [7, 7, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7]
    # page_list = [3, 2, 1, 3, 3, 7, 4, 10, 7, 9, 7, 3, 1, 7, 6, 6, 4]
    # page_list = [7,0,1,2,0,3,4,2,3,0,3,2,1,2,0,1,7]
    # frame_num = 3
    page_list = [5, 6, 7, 5, 4, 3, 5, 2, 1, 9, 8, 7, 9, 6, 5, 4, 5, 6, 3, 3, 5, 6, 7, 8]
    frame_num = 5

    frame_list, status_list, log, text_log = optimal_algorithm(page_list, frame_num)
    display(page_list, frame_list, status_list, frame_num, log, text_log)

if __name__ == "__main__":
        main()