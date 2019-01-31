from app.spider.douban_book import DouBanBook


class BookSpider():
    @classmethod
    def is_book_exited(cls, isbn):
        pass

    @classmethod
    def douban_isbn(self, isbn):
        DouBanBook.search_by_isbn(isbn)
