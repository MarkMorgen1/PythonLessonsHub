# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests


def get_request():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    print(f"HTTP status: {r.status_code}")
    return r.text


def get_bs_view(request_content):
    soup = BeautifulSoup(request_content, "html.parser")
    balanced_headlines = soup.find_all("h2")

    # Optional: remove last 2 elements if needed
    if len(balanced_headlines) > 2:
        balanced_headlines = balanced_headlines[:-2]

    # Write to file
    with open("Headlines NYT.txt", "w", encoding="utf-8") as write_file:
        if balanced_headlines:
            write_file.write("NYT <h2> Headlines:\n\n")
            print("NYT <h2> Headlines:\n")
            for headline in balanced_headlines:
                text = headline.get_text(separator="\n", strip=True)
                print(text)
                write_file.write(text + "\n")  # ✅ write each headline on a new line

        else:
            print("No headlines found")
            write_file.write("No Headlines Today\n")


# -------------------------
req = get_request()
get_bs_view(req)
