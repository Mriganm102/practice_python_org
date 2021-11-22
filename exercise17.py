from bs4 import BeautifulSoup
import requests
class decode(object):
    def title_finder(self):
        url = "https://www.nytimes.com/"
        r = requests.get(url)
        rr = r.text
        soup = BeautifulSoup(rr, features="html.parser")
        c = soup.find_all("h3")
        for d in c:
            print(d.text)
    def __init__(self):
        self.title_finder()

def main():
    exercise17 = decode()
if __name__ == '__main__':
    main()
