# import run as runiing
import validators
from bs4 import BeautifulSoup
import urllib.request
import os
from more_itertools import difference
import requests
os.system("cls")


def mode_choose():
    mode_num = input("please input the mode number --> ")
    if mode_num == "1":
        print(f"you choose the mode number {mode_num}")
        return mode_num
    elif mode_num == "2":
        print(f"you choose the mode number {mode_num}")
        return mode_num
    else:
        print("insert right number between 1 and 2!!!")
        mode_choose()


def getting_input_from_mode_1():

    URL = input("input the url -->")
    if URL == "END":
        return "Ending the program"

    depth_of_crawl = input("input the depth of crawl -->")
    max_num_of_unique_url = input("how many unique url waana grab ? --> ")
    start_with_same_URL = input(
        "crawl under the same URL (True = yes , False = NO) -->")

    class Mode1Inputs:
        def __init__(self, url=URL, depth=depth_of_crawl, max_url=max_num_of_unique_url, start_same_url=start_with_same_URL):
            self.url = url
            self.depth = depth
            self.max_url = max_url
            self.start_same_url = start_same_url

    return Mode1Inputs()


def grab_data_from_website(URL: str):
    if validators.url(URL):
        response = urllib.request.urlopen(URL)
        html = response.read()
        with open(f"{URL.split(r'//')[-1].replace(r'/','')}.txt", "wb") as f:
            f.write(html)

        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        with open(f"{URL.split(r'//')[-1].replace(r'/', '')}.text", "w", encoding="utf-8") as f:
            f.write(text)
        print(text)
        return {URL: text}


def crawl_nested_pages(url, num_of_link_to_crawl, num_of_nest):
    num_of_nest = 0
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        _ = link.get('href')
        if validators.url(_):
            if not _ in urls:
                urls.append(_)
    with open("urls.csv", "a") as f:
        f.write(str(urls))

    if int(num_of_link_to_crawl) < len(urls):

        for _ in range(int(num_of_link_to_crawl)):
            grab_data_from_website(urls[_])
    elif int(num_of_link_to_crawl) > len(urls):
        diferrence = int(num_of_link_to_crawl) - len(urls)
        x += 1

        if x < num_of_nest:

            for _ in range(int(num_of_link_to_crawl)):
                grab_data_from_website(urls[_])
            for _ in range(diferrence):
                crawl_nested_pages(urls[_])
        else:
            print("number of nested pages exceed")


if __name__ == "__main__":
    mode_num = mode_choose()
    if mode_num == "1":
        # return a class of input data mode-1
        inputs_mode_1 = getting_input_from_mode_1()
        text_data = {}
        # یک دیکشنری است کلید لینک و مقدار محتوای همون لینک
        text_data[inputs_mode_1.url] = grab_data_from_website(
            inputs_mode_1.url)
        print("====" * 10)
        crawl_nested_pages(inputs_mode_1.url,
                           inputs_mode_1.max_url, inputs_mode_1.depth)

    elif mode_num == "2":
        pass
