from pathlib import Path

from pyparsing import alphanums


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
        print(f"thie counter is : {count}")
        print(f"the value is : {val}")
        paths_dict[count] = val

    return paths_dict


def search_through_files(paths: dict, *args, **kwargs):
    word_dict = {}
    _ = []
    ALPHABETE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    for key, exported_path in paths.items():
        with open(exported_path, "r") as my_file:
            line_text = my_file.readlines()
            print(line_text)
        for sentence in line_text:
            line_words = sentence.split(" ")
            for word in line_words:
                if word[0] in ALPHABETE or word[0].lower() in ALPHABETE:
                    if word in word_dict.keys():
                        word_dict[word].append(key)

                    else:
                        word_dict[word] = [key]
    print(word_dict)
    return word_dict


if __name__ == "__main__":
    riddle_paths = riddle_text_files()
    search_through_files(riddle_paths)
