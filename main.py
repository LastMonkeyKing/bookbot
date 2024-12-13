
def main(): 
    path_to_file = "./books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
    
    word_count = count_words(file_contents)
    character_counter = count_characters(file_contents)
    sorted_dict = dict(sorted(character_counter.items(), key=lambda item: item[1], reverse=True))
  

    print("-- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for key in sorted_dict:
        print(f"The {key} character was found {sorted_dict[key]} times.")
    
    print("--- End Report ---")

def count_words(file_to_count):
    total_word_count = 0
    content_split = file_to_count.split()
    for x in content_split:
        total_word_count += 1
    return total_word_count

def count_characters(file_to_count):
    character_dict ={"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, 
                    "k":0, "l":0, "m":0, "n":0,"o":0, "p":0, "q": 0, "r":0, "s":0,
                    "t":0, "u":0, "v":0, "w": 0, "x": 0, "y":0, "z":0}
    joined_file = "".join(file_to_count)

    for x in joined_file:
        if x in character_dict:
            character_dict[x] += 1
    return character_dict 

main()