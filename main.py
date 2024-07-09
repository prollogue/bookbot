def main():
    file_path = "books/frankenstein.txt"
    file_contents = read(file_path)
    count = word_count(file_contents)
    characters = char_count(file_contents)
    char_list = dict_to_list(characters)
    char_list.sort(reverse=True, key=sort)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words were found in the document\n")
    for char in char_list:
            print(f"The '{char['Key']}' character was found {char['Value']} times")
    print("--- End report ---")
    

def read(path):
    with open(path, "r") as file:
        return file.read()


def word_count(text):
    words = text.split()
    return len(words)

def char_count(string):
    char_dict = {}
    lowered_strng = string.lower()
    for char in lowered_strng:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return(char_dict)

def dict_to_list(dict):
    dict_list = []
    for key, values in dict.items():
        new_dict = {"Key": key, "Value": values}
        if key.isalpha():
            dict_list.append(new_dict)
    return dict_list

def sort(dict):
    return dict["Value"]

main()