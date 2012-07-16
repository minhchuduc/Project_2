if __name__ == '__main__':
    filename = raw_input("File name to process: ")
    input_file = open(filename, 'r')
    words_dict = {}
    for i, line in enumerate(input_file.readlines()):
        #print i, line.strip('\n')
        for word in line.strip('\n').lower().split():
            if word not in words_dict.keys():
                words_dict[word] = [1, set([i+1])]    # words_dict format:  {word: [freq, set(line_numbers)]}, use "set" to auto-deduplicate
            else:   # existed in words_dict
                words_dict[word][0] += 1
                words_dict[word][1].add(i+1)    # add to set(line_numbers)
    
    words_list = [(-freq, word, line_numbers) for (word, (freq, line_numbers)) in words_dict.items()] 
    words_list.sort()
    #print words_list

    for freq, word, line_numbers in words_list:
        print -freq, word, " ".join([str(i) for i in line_numbers])
