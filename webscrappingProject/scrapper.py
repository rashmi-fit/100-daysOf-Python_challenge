import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
"""
This File will extract the top job posts which used below keywords and 
how many times its posted with a nice visualization using matplot library
"""

def main():
    print("hello world")
    url='https://news.ycombinator.com/item?id=29782099'
    print(f'scrapping: {url}')
    response= requests.get(url)

    soup= BeautifulSoup(response.content,'html.parser')
    elements = soup.find_all(class_="ind",indent=0)
    comments = [e.find_next(class_='comment') for e in elements]

    keywords={'python':0,
              'javascript':0,
              'ruby':0,
              'java':0,
              'c#':0}

    for comment in comments:
        comment_text=comment.get_text().lower()
        words= comment_text.split(" ")
        words= {w.strip(",/:;!@") for w in words}

        for k in keywords:
            if k in words:
                keywords[k]+=1

    print(keywords)

    plt.bar(keywords.keys(),keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of mentions")
    plt.show()

    # print(response)
    # print(f'Elements:{len(elements)}')
    # print(f'Comments: {len(comments)}')

if __name__== "__main__":
    main()