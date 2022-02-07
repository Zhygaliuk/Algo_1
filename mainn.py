from knuth_morris_pratt import kmp

if __name__ == '__main__':
    with open('knuth_morris_pratt.in', 'r') as input_file:
        data = input_file.readlines()
    sub_str = data[1]
    text_str = data[0]

    print('Result =>', kmp(sub_str, text_str))