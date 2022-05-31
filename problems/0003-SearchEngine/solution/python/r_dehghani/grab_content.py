from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen("http://www.wikipedia.com")
html = response.read()
with open("data.txt", "wb") as f:
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
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
with open("exported_text", "w") as f:
    f.write(text)
print(text)
