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
