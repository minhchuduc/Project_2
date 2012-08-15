#Coding time: 1 minutes
def reverse_string(string):
    return string[::-1]
    
if __name__ == '__main__':
    input_str = raw_input('Input string: ')
    output_str = reverse_string(input_str)
    print "Reverse string is:", output_str
