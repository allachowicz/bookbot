def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        text = f.read()
        w = wordcount(text)
        cc = characters(text)
        key_list = list(cc.keys())
        key_values = list(cc.values())
        listd = []
    
        for i in range(0, len(key_list)):
            keydict = {}
            keydict["char"] = key_list[i]
            keydict["count"] = key_values[i]
            listd.append(keydict)
        listd.sort(reverse = True, key=sort_on)        
        report(filepath, w, listd)
        
def sort_on(dict):
    return dict["count"]


def wordcount(text):
    words = text.split()
    return len(words)

def characters(text):
    char_list = list(text.lower())
    alpha_list =[]
    for i in range(len(char_list)):
        if char_list[i].isalpha() == True:
            alpha_list.append(char_list[i])

    char_dict = {}
    for char in alpha_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
             char_dict[char] = 1
    return char_dict

def report(filepath, w, listd):
    print(f"--- Begin report of {filepath} ---")
    print(f"{w} words found in the document")
    print("")
    for i in range(len(listd)):
        char = listd[i]["char"]
        count = listd[i]["count"]
        print(f" The '{char}' character was found {count} times")
    print(f"---End report---")
        
main()