def check(x: str, file: str):
    words = x.split()
    words_lower = [word.lower() for word in words]
    words_count = {}
    # for word in words_lower:
    #     if word in words_count:
    #         words_count[word] += 1
    #     else:
    #         words_count[word] = 1

    for word in words_lower:
        words_count[word] = words_count.get(word, 0) + 1

    words_sorted = sorted(words_count)
    #print(words_sorted)
    with open(file,'w') as f:
        for word in words_sorted:
        #print(str(word) + ' ' + str(words_count[word]))
            f.write(str(word) + ' ' + str(words_count[word]) + '\n')

