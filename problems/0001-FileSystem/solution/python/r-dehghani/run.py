from pathlib import Path


def riddle_text_files(*args, **kwargs):
    """this function just extract files within the current dir that it's suffix is .txt
    """
    paths_dict = {}
    path = Path.cwd()
    list_of_file_pathes = [p for p in path.rglob('*') if p.is_file()]
    list_of_text_files_pathes = []

    for path in list_of_file_pathes:
        if path.suffix == ".txt":       # here you can change the file suffix
            list_of_text_files_pathes.append(path)

    enum_paths = enumerate(list_of_text_files_pathes)

    for count, val in enum_paths:
        print(f"the related number to the path is ---> {count}")
        print(f"the {count} file path is ---> {val}")
        paths_dict[count] = val

    return paths_dict


def search_through_files(paths: dict, *args, **kwargs):
    word_dict = {}
    _ = []
    ALPHABETE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    for key, exported_path in paths.items():
        with open(exported_path, "r", encoding="utf-8") as my_file:
            line_text = my_file.readlines()
            # print(line_text)
        for sentence in line_text:
            line_words = sentence.split()
            for word in line_words:
                if word[0] in ALPHABETE or word[0].lower() in ALPHABETE:
                    if word in word_dict.keys():
                        if not key in word_dict[word]:
                            word_dict[word].append(key)
                    else:
                        word_dict[word] = [key]
    return word_dict


def sort_data_into_seprate_files(all_vocabs: dict, all_paths: dict, * args, **kwargs):
    ALPHABETE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    for word, location in all_vocabs.items():
        for _ in ALPHABETE:
            if (word[0] == _) or (word[0].lower() == _):
                with open(f"{word[0].lower()}.txt", "a", encoding="utf-8") as f:
                    f.write(str(word) + " | " + str(location) + "\n")


if __name__ == "__main__":
    riddle_paths = riddle_text_files()
    all_word = search_through_files(riddle_paths)
    sort_data_into_seprate_files(all_word, riddle_paths)
