#Coding time: 45min
if __name__ == '__main__':
    file_name = raw_input('File name to process: ')
    input_file = open(file_name, 'r')
    words_dict = {}
    line_num = 0
    while True:
        line = input_file.readline()
        line_num += 1
        if not line: break
        list_words = line.strip("\n").split(" ")
        for word in list_words:
            words_dict.setdefault(word, []).append(line_num)
            """ You can figure the line above by: run Python interpreter, a = {}, help(a)
                It will show you all dict-methods """

    freq = {}
    for word in words_dict.keys():
        freq[word] = len(words_dict[word])
        words_dict[word] = list(set(words_dict[word]))  #Convert list --> set --> list: muc dich la` de de-duplicate
        tmp_list = ["%s" % element for element in words_dict[word]] #Convert list like [1,2,3,4] to ['1','2',3','4']
        print freq[word], word, " ".join(tmp_list)  #Convert list like ['1','2',3','4'] to a string '1 2 3 4'