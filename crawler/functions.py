import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
# SEARCHED_BOOK_NAME = "1984"

# make the book name suitable for searches in case there are any spaces
# BOOK_NAME = SEARCHED_BOOK_NAME.replace(" ", "%20")

# BOOK_NAME_PLUS = SEARCHED_BOOK_NAME.replace(" ", "+")


def lira(value):
    #   """Format value as TL."""
    return f"₺{value:,.2f}"


def soupify(url, HEADERS):
    # request the HTML page for the searched page
    request = requests.get(url, headers=HEADERS)
    request.raise_for_status()
    # turn the page into BS object
    text = request.text
    soup = BeautifulSoup(text, "html.parser")
    return soup


"""Kitap Yurdu için sonuçlar"""


def kitapyurdu(book):

    KYurl = (
        "https://www.kitapyurdu.com/index.php?route=product/search&filter_name=" + book
    )

    KYsoupified = soupify(KYurl, HEADERS)
    # find the book in the searched page
    box_content = KYsoupified.select(".box-content a")

    # if the book is not found on kitapyurdu
    if box_content == []:
        name = "Kitapyurdu'nda bulunamadı."
        author = "-"
        image = "-"
        price = 0
        book_url = ""
        return name, author, price, book_url, image
    else:
        # find the book's url in the searched page
        book_url = box_content[0].get("href")

        image = KYsoupified.select(".pr-img-link")[0].find_all("img")[0]["src"]
        # soupify book
        book = soupify(book_url, HEADERS)

        # get book name
        book_name = book.select(".pr_header__heading")[0].get_text().lstrip()

        # get the author name
        book_author = book.select(".pr_producers__link")[0].get_text().lstrip()

        # get the price of the book
        book_price = book.select(".price__item")[0]
        price_str = "0"

        for i in range(len(book_price.text)):
            if book_price.text[i].isnumeric() == True:
                price_str = price_str + str(book_price.text[i])
            elif book_price.text[i] == ",":
                price_str = price_str + "."

        price = float(price_str)

    return book_name, book_author, price, book_url, image


# fiyat = lira(kitapyurdu())
# print(fiyat)
"""D&R için sonuçlar"""


def dandr(book):

    DRurl = "https://www.dr.com.tr/search?q=" + book + "&cat=0%2C10001&parentId=10001"

    # soupify book search page
    booksearch = soupify(DRurl, HEADERS)

    # find the book's url in the searched page
    book_url = "https://www.dr.com.tr" + booksearch.select(".item-name")[0].get("href")

    # soupify book page
    book = soupify(book_url, HEADERS)

    # get book's cover
    image = book.select(".img-responsive")[0]["src"]

    # get book's name
    name = book.select(".product-name")[0].get_text().strip()

    # get the author name
    author = book.select(".name")[0].get_text().strip()

    # get the price of the book
    price_with_coma = (
        soupify(DRurl, HEADERS).select(".price")[0].get_text().strip()[:-2]
    )

    price = float(price_with_coma.replace(",", "."))

    return name, author, price, book_url, image


"""İdefix için sonuçlar"""


def idefix(book):
    idefixurl = (
        "https://www.idefix.com/search/?ActiveCategoryId=11693&Q="
        + book
        + "&ShowNotForSale=True"
    )

    # soupify book search page
    booksearch = soupify(idefixurl, HEADERS)

    # find the book's url in the searched page
    book_url = "https://www.idefix.com" + booksearch.select(".product-image")[0].get(
        "href"
    )

    # soupify book page
    book = soupify(book_url, HEADERS)

    # get book's cover

    image = book.find(id="main-product-img")["data-src"]
    # get book's name
    name = book.select(".mt0")[0].get_text().strip()

    # get the author name
    author = book.select(".author")[1].get_text()[7:].replace("\n", " ").strip()

    # get the price of the book
    price_with_coma = book.select(".current-price")[0].get_text().strip()[:-2]

    price = float(price_with_coma.replace(",", "."))

    return name, author, price, book_url, image


def pandora(book):
    pandoraurl = "https://www.pandora.com.tr/Arama?text=" + book + "&type=3&araButon="

    # soupify book search page
    booksearch = soupify(pandoraurl, HEADERS)
    booksearch_string = str(soupify(pandoraurl, HEADERS))

    key1 = "Üzgünüz"
    if key1 in booksearch_string:
        name = "Pandora'da  bulunamadı."
        author = "-"
        image = "-"
        price = 0
        book_url = ""
        return name, author, price, book_url, image
    else:
        books_url = "https://www.pandora.com.tr" + booksearch.select(".edebiyatIsim")[
            0
        ].find_all("a")[0].get("href")
        book_soup = soupify(books_url, HEADERS)

        book_soup = book_soup.get_text()
        key_word = "stoklarımıza"
        if key_word in book_soup:
            name = "Pandora stoklarında bulunamadı."
            author = "-"
            image = "-"
            price = 0
            book_url = ""
            return name, author, price, book_url, image
        else:
            # find the book's url in the searched page
            book_url = "https://www.pandora.com.tr" + booksearch.select(
                ".edebiyatIsim"
            )[0].find_all("a")[0].get("href")

            # get book's cover
            book_soup = soupify(books_url, HEADERS)
            image_url = book_soup.select(".kapakResim.parlama.posRel.urunPrev")[
                0
            ].find_all("img")[0]["src"]
            image = "https://www.pandora.com.tr/" + image_url

            # get book's name
            name = booksearch.select(".edebiyatIsim")[0].find_all("a")[0].get_text()

            # get the author name
            author = booksearch.select(".edebiyatYazar")[0].get_text().strip()

            # get the price of the book
            price_with_coma = (
                booksearch.select(".indirimliFiyat")[0].get_text().strip()[13:-2]
            )

            price = float(price_with_coma.replace(",", "."))

            return name, author, price, book_url, image
