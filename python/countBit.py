input_string = '010101010101'

big_obj = {}
stop = False
for t in range(0, len(input_string)): 
    char_num = len(input_string) - t
    for j in range(0, len(input_string) - char_num):
        char_obj = {}
        i = j
        while i < len(input_string):
            char = input_string[i: i+char_num]
            if len(char) == char_num:
                char_obj[char] = char_obj.get(char, 0) + 1
            if char_obj.get(char, 0) > 1:
                big_obj[char] = char_obj.get(char, 0);
                stop = True
                break
            i += char_num
        if stop == True:
            break
    if stop == True:
        break

        print(char_obj)

print (big_obj)
