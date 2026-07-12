# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture

from bs4 import BeautifulSoup
import requests
import os

# Folder where you want to save the file
output_folder = r"C:\Users\markm\OneDrive\Desktop\Python files"
os.makedirs(output_folder, exist_ok=True)  # create folder if it doesn't exist

# Path to the output file
output_file = os.path.join(output_folder, "Page_Scrape.txt")

# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
url = "https://www.vanityfair.com/story/danceteria-oral-history#intcid=_vanity-fair-article-bottom-recirc-bkt-a_a18f688a-37f8-4847-9a87-cbbaeb3b6713_closr_fallback_roberta-similarity1"
# url = "https://www.codecademy.com/learn"
r = requests.get(url)
print("r = requests.get(url): ", r)
print(f"HTTP status: {r.status_code}", "\n")  # status of requests.get()
# r_html = r.text  # assigns the html text from requests.get()
# print(r_html)  # prints out the html content of 'r'

soup = BeautifulSoup(r.text, features="html.parser")
# Creates a BeautifulSoup object called soup. "html.parser" → tells BeautifulSoup to use Python’s built-in HTML parser
# BSoup allows you to search, navigate, and manipulate the HTML
# text_body = soup.select("div.parbase.cn_text>div.body>p")
# print("text body =", text_body)
# for element in text_body:
#     print(element.text)

elements = soup.find_all(class_="body__inner-container")

for element in elements:
    # split text into paragraphs, strip extra spaces
    paragraphs = [p.strip() for p in element.text.split("\n") if p.strip()]
    for p in paragraphs:
        print(p)
        print()  # blank line between paragraphs

# Open the file and write paragraphs
with open(output_file, "w", encoding="utf-8") as f:
    for element in elements:
        paragraphs = element.find_all("p")
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                f.write(text + "\n\n")  # add blank line between paragraphs

print(f"Article saved to {output_file}")
