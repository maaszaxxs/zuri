# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        contents = f.read() 
        
    return contents


def count_words():
    text = read_file_content("./story.txt")
    text_list = text.split()
    dict_final = {}
    for word in text_list:
        count = text_list.count(word)
        dict_final.update({word: count})

    return dict_final

result = count_words()
print(result)
