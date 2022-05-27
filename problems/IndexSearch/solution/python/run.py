from pathlib import Path
from FileSystem.solution.python.run import riddle_text_files

# def riddle_text_files(*args, **kwargs):
#     """this function just extract files within the current dir that it's suffix is .txt
#     """
#     paths_dict = {}
#     path = Path.cwd()
#     list_of_file_pathes = [p for p in path.rglob('*') if p.is_file()]
#     list_of_text_files_pathes = []

#     for path in list_of_file_pathes:
#         if path.suffix == ".txt":       # here you can change the file suffix
#             list_of_text_files_pathes.append(path)

#     enum_paths = enumerate(list_of_text_files_pathes)

#     for count, val in enum_paths:
#         print(f"the related number to the path is ---> {count}")
#         print(f"the {count} file path is ---> {val}")
#         paths_dict[count] = val

#     return paths_dict  # {1: c:../.../file.txt, }


def recieving_words(*args, **kwargs):
    i = 0
    input_words = []
    _ = ""
    while _ != "END":
        i_word = input(
            "please input any word you want to search through the files --> \n")
        _ = i_word
        input_words.append(i_word)
        i += 1
        # print(input_words[:-1])
    return(input_words)


def proccess_on_given_words(words: list, *args, **kwargs):
    list_of_paths = riddle_text_files()
    x = []
    my_dic = {}
    i = 0
    for word in words[:-1]:
        first_letter = word[0]
        with open("test.text", "r", encoding="utf-8") as f:
            # with open(f"./../../../0001-FileSystem/{first_letter}.txt", "r") as f:
            sentence_list = f.readline()
            print(f.name)
            sentc_to_one_str = "".join(sentence_list).replace(" ", "")
            splited_sentc = sentc_to_one_str.split("|")
            if splited_sentc[0] in word:
                for _ in splited_sentc[-1]:
                    if _.isnumeric():
                        x.append(_)
                        with open(list_of_paths[int(_)], "r", encoding="utf-8") as ff:
                            content_sentence = ff.readlines()
                            my_dic[int(_)] = content_sentence
                            # print(my_dic)
                            for key, val in my_dic.items():
                                for w in val:

                                    if word in w.split():
                                        print(f"<---- {w} ---->")
                                        print(
                                            f"the file path number is: {key}")
                                        print("==" * 10)

            else:
                pass


if __name__ == "__main__":
    l_o_path = riddle_text_files
    l_o_words = recieving_words()
    proccess_on_given_words(l_o_words)
