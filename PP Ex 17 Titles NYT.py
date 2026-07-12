# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests


def get_request():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    print("r = requests.get(url): ", r)
    print(f"HTTP status: {r.status_code}", "\n")  # status of requests.get()
    r_html = r.text  # assigns the html text from requests.get()
    # print(r_html) # prints out the html content of 'r'
    return r_html  # returns the html text to calling code


def get_bs_view(request_content):
    soup = BeautifulSoup(request_content, "html.parser")
    # Creates a BeautifulSoup object called soup. "html.parser" → tells BeautifulSoup to use Python’s built-in HTML parser
    # soup allows you to search, navigate, and manipulate the HTML
    balanced_headlines = soup.find_all("h2")
    # finds all <h2> tags in the HTML, returns as a list
    print("balanced_headlines in HTML: \n", balanced_headlines, "\n")
    print("length of balanced_headlines =", len(balanced_headlines), "\n")
    del balanced_headlines[-2 : len(balanced_headlines)]
    # Deletes the last 2 items from balanced_headlines list

    # if-code Checks if there are any <h2> headlines left
    # Loops over each headline tag
    # .text → extracts the plain text inside the tag
    if len(balanced_headlines) > 0:
        print("<h2> Headlines:")
        for headline in balanced_headlines:
            print(headline.text)  # Prints text from each headline
    else:
        print("No headlines")


req = get_request()
get_bs_view(req)
