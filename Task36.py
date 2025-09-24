"""Task36"""

def delete_redendant(words):
    new_words = []
    for j in range(len(words)):
        buffer =''
        for letter in words[j]:
            if letter not in buffer:
                buffer += letter
        new_words.append(buffer)
    return new_words


def split_string(string, k):
    sub_strings = []
    for i in range(0,len(string),k):
        sub_strings.append(string[i:i+k])
    unique_substring = delete_redendant(sub_strings)
    return unique_substring


if __name__ == '__main__':
    string = input('Type any string: ')
    k = int(input('Type length of substrings:'))
    for word in split_string(string,k):
        print(word)
