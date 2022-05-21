
from pathlib import Path


def riddle_text_files(*args, **kwargs):
    """this function just extract files within the current dir that it's suffix is .txt
    """
    from pathlib import Path 
    path = Path.cwd()
    list_of_file_pathes = [p for p in path.rglob('*') if p.is_file()]
    list_of_text_files_pathes = []
    for path in list_of_file_pathes:
        if path.suffix == ".txt":       # here you can change the file suffix 
            list_of_text_files_pathes.append(path)
        # return list_of_text_files_pathes
    print(f"this is the list of text file pathes")
    print(list_of_text_files_pathes)
    return list_of_text_files_pathes

pathes = riddle_text_files()
# for file_path in pathes():
#     pass
if __name__ == "__main__":
    riddle_text_files()
    