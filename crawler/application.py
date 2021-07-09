from flask import Flask, render_template, request
from functions import kitapyurdu, dandr, idefix, pandora, lira

app = Flask(__name__)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
# SEARCHED_BOOK_NAME = "1984"

# make the book name suitable for searches in case there are any spaces
# BOOK_NAME = SEARCHED_BOOK_NAME.replace(" ", "%20")

# BOOK_NAME_PLUS = SEARCHED_BOOK_NAME.replace(" ", "+")


@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        searched_book = str(request.form.get("kitap"))
        book = str(searched_book).replace(" ", "%20")
        KY_info = kitapyurdu(book)
        KY_name = KY_info[0]
        KY_author = KY_info[1]
        KY_price = lira(KY_info[2])
        KY_url = KY_info[3]
        KY_image = KY_info[4]

        DR_info = dandr(book)
        DR_name = DR_info[0]
        DR_author = DR_info[1]
        DR_price = lira(DR_info[2])
        DR_url = DR_info[3]
        DR_image = DR_info[4]

        idefix_info = idefix(book)
        idefix_name = idefix_info[0]
        idefix_author = idefix_info[1]
        price_idefix = lira(idefix_info[2])
        idefix_url = idefix_info[3]
        idefix_image = idefix_info[4]

        book_plus = str(searched_book).replace(" ", "+")
        pandora_info = pandora(book_plus)
        pandora_name = pandora_info[0]
        pandora_author = pandora_info[1]
        pandora_price = lira(pandora_info[2])
        pandora_url = pandora_info[3]
        pandora_image = pandora_info[4]

        return render_template(
            "searched.html",
            book_imageKY=KY_image,
            book_nameKY=KY_name,
            book_authorKY=KY_author,
            priceKY=KY_price,
            book_urlKY=KY_url,
            book_imageDR=DR_image,
            book_nameDR=DR_name,
            book_authorDR=DR_author,
            priceDR=DR_price,
            book_image_idefix=idefix_image,
            book_urlDR=DR_url,
            book_nameidefix=idefix_name,
            book_authoridefix=idefix_author,
            priceidefix=price_idefix,
            book_urlidefix=idefix_url,
            book_image_pandora=pandora_image,
            book_namepandora=pandora_name,
            book_authorpandora=pandora_author,
            pricepandora=pandora_price,
            book_urlpandora=pandora_url,
        )
    else:
        return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
