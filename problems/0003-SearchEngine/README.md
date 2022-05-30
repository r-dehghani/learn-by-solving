# Problem 0003 - Search Engine

It was 1998 that Larry Page and Sergey Brin officially launched Google.
24 years later and their business worthes $1.4 Trillion. 
Now we ask you to re-create what they have built, a search engine.

Inspired by two previous problems [Problem 0001 - File System](https://github.com/mafshin/learn-by-solving/tree/main/problems/0001-FileSystem).
and [Problem 0002 - Index Search](https://github.com/mafshin/learn-by-solving/tree/main/problems/0002-IndexSearch), write a solution to provide the end-user with the ability to search through a specific set of web pages.


First line of input contains a number, representing the mode your application is running with:

- **Mode 1**: In this mode your application should crawl webpages based on the provided inputs. In this mode, 4 lines of input are provided.
The first next input is a Url, the next line is a number representing the depth of crawling and the next line specifies the maximum number of unique Urls that may be crawled. The last line contains either 'true' or 'false'. If true is provided it means only the nested Urls under same domain as starting Url should be crawled.
- **Mode 2**: In this mode your application should show the url and title of the matched web pages for each user query. Unlimited number of lines are provided by end user as input queries, end of input is marked with END.

*Note that your application must be restarted for switching to different mode.*

Your solution should start crawling the starting url and any links inside any crawled page, up until those two thresholds are valid, maximum number of link deptch and maximum number of crawled pages in total. Maximum number of crawled pages has higher priority so as soon as you reached that threshold, you should stop crawling any other page.

The index that you create in Mode 1 should have enough information for finding the search results, such that in Mode 2, no web page loading is performed at all.

For each line of user input, you should print the matched url in two lines, first line the Title of the web page (Header Title tag) and second line the Url of the page.

## Sample Input:
```
1
https://en.wikipedia.org/wiki/Google
5
100
true
```

*Application is restarted*

```
2
jumping likelihood
exchange university
commemorate
unincorporated
```

## Sample Output:
```
--------------------------------------
Found 1 result(s) for 'jumping likelihood' 
--------------------------------------
PageRank - Wikipedia
https://en.wikipedia.org/wiki/PageRank

--------------------------------------
Found 2 result(s) for 'exchange university'
--------------------------------------
PageRank - Wikipedia
https://en.wikipedia.org/wiki/PageRank

Stanford University - Wikipedia
https://en.wikipedia.org/wiki/Stanford_University

--------------------------------------
Found 1 results(s) fro 'commemorate'
--------------------------------------
White Memorial Fountain - Wikipedia
https://en.wikipedia.org/wiki/White_Memorial_Fountain

--------------------------------------
Found 2 result(s) for 'unincorporated'
--------------------------------------
Stanford University - Wikipedia
https://en.wikipedia.org/wiki/Stanford_University

Unincorporated area - Wikipedia
https://en.wikipedia.org/wiki/Unincorporated_area
```
