# Problem 0001 - File System

Write a program that given the path of a directory in local file system, creates an index of words stored in the files and stores them in a target folder
with the following structure:

```
Target Folder:
              - A.dic
              - B.dic
              - C.dic
              - D.dic
              - ...


Sample A.dic:
Apple | References TO DOCS THAT CONTAINS 'Apple'
Are   | Referecnes to docs that contains 'Are'

Sample B.dic:
Book | References to docs that contains 'Books'
Baby | References to docs that contains 'Baby'
```

              
Each letter .dic file should contain the list of words starting with that letter and a reference to the original document which contains that word.

The input consists of two lines. First line is a valid directory path in local file system. The directory may contain several sub-directories and files 
with different extensions. The second line is a valid direcotyr path for storing the index you create.

Tips: You can use an [inverted index](https://www.geeksforgeeks.org/inverted-index)

Warning: The input directory may contain many files so keep that in mind while designing your solution.
