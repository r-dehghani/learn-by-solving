# Problem 0002 - Index Search

This problem dependens on the output of the [Problem 0001 - File System](https://github.com/mafshin/learn-by-solving/tree/main/problems/0001-FileSystem).

Write a solution to provide the end-user with the ability to quickly find any given user input inside the indexed documents.

The input contains an unlimited number of lines containting either a single word or a phrase of multiple words.
The end of user input is recognized when END is entered.

For each line of input, your solution should find the list of all sentenses in all already indexed documents which
contains the provided input ignoring casing. For a multi-words input, the words may appear anywhere in a single sentense.

A sentense boundary is recognized by either of these characters: [. ! ?] (We also have abbreviations like Mr. Dr. Phd. .... :-) )

## Sample Input / Output

### Documents

```
Doc01:
Because Wikipedia content is distributed under an open license, anyone can reuse or re-distribute it at no charge. The content of Wikipedia has been published in many forms, both online and offline, outside the Wikipedia website.

Doc02:
An English version, 2006 Wikipedia CD Selection, contained about 2,000 articles.[285][286] The Polish-language version contains nearly 240,000 articles.[287] There are German- and Spanish-language versions as well.
```

#### Input:
```
wikipedia
articles
wikipedia articles
wikipedia website
distributed license
online forms
END
```

#### Output:

```
<-- Search results for 'wikipedia' -->

File: 'Doc01', Sentenses: 2

Because Wikipedia content is distributed under an open license, anyone can reuse or re-distribute it at no charge. 

The content of Wikipedia has been published in many forms, both online and offline, outside the Wikipedia website.

File: 'Doc02', Sentenses: 1

An English version, 2006 Wikipedia CD Selection, contained about 2,000 articles.


<-- Search results for 'articles' -->

File: 'Doc02', Sentenses: 2
An English version, 2006 Wikipedia CD Selection, contained about 2,000 articles.
[285][286] The Polish-language version contains nearly 240,000 articles.

<-- Search results for 'wikipedia articles' -->

File: 'Doc01', Sentenses: 1

In English version, 2006 Wikipedia CD Selection, contained about 2,000 articles.


<-- Search results for 'wikipedia website' -->

File: 'Doc01', Sentenses: 1
The content of Wikipedia has been published in many forms, both online and offline, outside the Wikipedia website.

<-- Search results for 'distributed license' -->

File: 'Doc01', Sentenses: 1
Because Wikipedia content is distributed under an open license, anyone can reuse or re-distribute it at no charge.


<-- Search results for 'online forms' -->

File: 'Doc01', Sentenses: 1
The content of Wikipedia has been published in many forms, both online and offline, outside the Wikipedia website.
```




