def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words



def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_numb(char_dict: dict):
    formatted_list = []
    for k, v in char_dict.items():
        formatted_list.append({"char": k, "num": v})
    formatted_list.sort(key=lambda x: x["num"], reverse=True)
    return formatted_list