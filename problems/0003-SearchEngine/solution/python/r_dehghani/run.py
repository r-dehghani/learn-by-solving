from msilib.schema import File
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


def recieving_words(*args, **kwargs):

    i_word = input(
        "please input any word you want to search through the files --> \n").split(" ")
    if "END" in i_word:
        print("you just intruppt the program!!!")
    else:
        proccess_on_given_words(i_word)
        recieving_words()


def proccess_on_given_words(words: list, *args, **kwargs):
    list_of_paths = riddle_text_files()
    x = []
    my_dic = {}
    first_letter = words[0][0]
    # with open("test.text", "r", encoding="utf-8") as f:
    with open(f"{first_letter.lower()}.text", "r") as f:
        sentence_list = f.readlines()
        for item in sentence_list:
            sentc_to_one_str = item.replace(" ", "")
            splited_sentc = sentc_to_one_str.split("|")
            if splited_sentc[0] in words:
                for _ in splited_sentc[-1]:
                    if _.isnumeric():
                        with open(list_of_paths[int(_)], "r", encoding="utf-8") as ff:
                            content_sentence = ff.readlines()
                            my_dic[int(_)] = content_sentence
                            for key, val in my_dic.items():
                                for each_sentc_in_file in val:
                                    if all(xxx in each_sentc_in_file for xxx in words):
                                        print(
                                            f"<---- {each_sentc_in_file} ---->")
                                        print(
                                            f"the file path number is: {key}")
                                        print("==" * 10)


if __name__ == "__main__":
    recieving_words()
