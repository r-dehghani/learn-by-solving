

from pathlib import Path


def riddle_text_files(*args, **kwargs):
    """this function just extract files within the current dir that it's suffix is .txt
    """
    # from pathlib import Path 
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
def extract_file_name_from_paths(riddle, *args,**kwargs):        
    """this function return the unique  path of text files and assign one character to that path 
        

    Args:
        riddle (list of PosixPath): this list imported from riddle_text_files function 
    """
    e_list_of_unique_paths = []
    for item in riddle:
        print(item.parent)
        
        if not item  in e_list_of_unique_paths:
            e_list_of_unique_paths.append(item.parent)
        else:
            print("path exist!!")
        print("="*20)
        print(type(item))
    
    print("_" * 20)
    print(e_list_of_unique_paths)



pathes = riddle_text_files()
# for file_path in pathes():
#     pass
if __name__ == "__main__":
    riddle_paths = riddle_text_files()
    extracted_names = extract_file_name_from_paths(riddle_paths)
    