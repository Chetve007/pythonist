from collections import defaultdict

import requests
from bs4 import BeautifulSoup, Tag


# TODO Task
# Путем веб-краулинга исследуйте веб-страницу и выведите слово,
# которое встречается на ней чаще всего, а также
# количество вхождений этого слова.

# Страница для краулинга:
# https://en.wikipedia.org/wiki/Apple_Inc.

# Учитывайте только слова из раздела «History».


def find_most_common():
    page = requests.get("https://en.wikipedia.org/wiki/Apple_Inc.")
    soup = BeautifulSoup(page.text, "html.parser")
    history = soup.find(id="History").parent.next_siblings

    max_count = 0
    max_word = ""
    dd = defaultdict(int)

    for elem in history:
        if isinstance(elem, Tag):
            if elem.name == "h2":
                print(f"'{max_word}', is the most common, appearing '{max_count}' times")
                return max_count

            words = elem.get_text().split()
            for word in words:
                dd[word] += 1
                if dd[word] > max_count:
                    max_count = dd[word]
                    max_word = word
    return "Error"


if __name__ == '__main__':
    find_most_common()
