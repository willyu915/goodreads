import requests
from bs4 import BeautifulSoup


def get_link_id(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    book_links_ids = soup.select(".coverWrapper")
    link_id_list = []
    if (len(book_links_ids) >= 100):
        for link_id in book_links_ids:
            book_list = []
            # import pdb;pdb.set_trace()
            book_link = link_id.select_one("a")
            if book_link != None:
                book_link = book_link.get("href")
            else:
                book_link = "Not Found"
            book_id = link_id.get("id").split("_")[-1]
            book_link = "https://www.goodreads.com" + book_link
            book_list.append(book_link)
            book_list.append(book_id)
            link_id_list.append(book_list)
        return link_id_list


if __name__ == "__main__":
    print(get_link_id("https://www.goodreads.com/genres/most_read/historical-fiction"))
