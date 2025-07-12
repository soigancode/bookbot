def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_char_list(chars_dict):
    char_list = [{"char": char, "num": count} for char, count in chars_dict.items()]
    return sorted(char_list, key=lambda x: x["num"], reverse=True)
