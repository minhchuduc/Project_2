#Coding time: 7 minutes
def reverse_string(str):
    len_str = len(str)
    output_str = ''
    for i in range(len_str):
        output_str = output_str + str[len_str-1-i]
    return output_str
    
if __name__ == '__main__':
    input_str = raw_input('Input string: ')
    output_str = reverse_string(input_str)
    print "Reverse string is:", output_str