def sep_words(input_str):
    words = []
    start = 0
    terminators = [".", "?", "!"]
    split_string = input_str.split(' ')
    #print(len(split_string))
    #print("Split :", split_string)
    for i in range(len(split_string)):
        #print("i = ", split_string[i])
        for j in terminators:
            if j in split_string[i]:
                #print("Found = ", split_string[i])
                end = i
                #print("end", end)
                #print(split_string[start:end+1])
                words.append(split_string[start:(end+1)])
                start = end + 1
    if end < (len(split_string)-1):
        words.append(split_string[end+1:])
    return words

print("Output = ", sep_words("Hello, world! How are you? Your oceans are pretty. Incomplete sentence"))