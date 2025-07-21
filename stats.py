def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        file_words = file_contents.split()
    return len(file_words)

def get_num_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
        num_chars = {}
        for char in file_contents:
            if char not in num_chars:
                num_chars[char] = 1
            else:
                num_chars[char] += 1
    return num_chars

def sort_on(items):
    return items["count"]

def sort_char_count(chars_dict):
    unsorted_list = []
    for i in chars_dict:
        temp_dict ={"char": i, "count": chars_dict[i]}
        unsorted_list.append(temp_dict)
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list



