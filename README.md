# En Ucuz Kitap(TR) - The Cheapest Book(EN)

"En Ucuz Kitap" in Turkish or "The Cheapest Book" in English is a Flask-based web crawler application. This application was developed as a Final Project for Harvard University's CS50x 2021.

Libraries used:

Flask

BeautifulSoup

Request


## Description

The purpose of this application is to find the cheapest option for a book that you're planning to buy online through four major online bookstores in Turkey. The bookstores parsed by this application are [D&R Online Store](https://www.dr.com.tr/), [İdefix](https://www.idefix.com/), [Kitapyurdu](https://www.kitapyurdu.com/) and [Pandora](https://www.pandora.com.tr/), which are major online bookstores in Turkey.

The application uses BeautifulSoup and Request libraries to parse the websites listed above and it uses a very simple page design. As there was no login/register function I wanted the page to have a navigation bar at the top and the homepage link with the project's name in the middle. After the user searches any book, the application renders a table that shows the book's cover, name, author, price, and a link to the bookstore's page.

In order to bring the information from each website, separate functions were used and each function returns a link to the cover image, name of the book, book's author, the current price at that book store, and a link to the bookstore's page. The link to the bookstore's page is displayed as a button and after clicking it, the user is redirected to that book's page on the respective bookstore's website, where the user can make a purchase from the vendor.

## How it works

The idea and the application are quite simple. You are greeted with a search bar at the homepage, you type the name of a book you're planning to purchase, and hit search. The application then parses through the four bookstores listed above and presents you the book's cover, name, author, price, and a link to the bookstore's page, which you can click and proceed to purchase from that bookstore.

For a detailed demonstration, check out the link for the Youtube vide below.


## Video Demo

You can watch this [video](https://youtu.be/eOEf5FrtDRc) demonstration to see how this application works.


## Usage

You must install Flask before starting to use this application. Afterward, you can just go to the directory of the file in your Command-Line and execute below:

```python
python application.py
```
Originally you should be able to search the book by its title but searching with the author's name also works very well. For best results, especially for less popular books, it is best to search with the book's title and the name of the author.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Roadmap

At the moment, the application is not hosted and you need to download and use it on your own computer. I'm planning to further work on it to increase the speed, after which I would feel comfortable hosting it on Heroku.

## License
[MIT](https://choosealicense.com/licenses/mit/)