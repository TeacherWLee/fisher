from app.libs.helper import get_isbn
from app.models import db
from app.models.book import Book


class MySQL:
    @classmethod
    def has_existed(cls, isbn):
        book = Book.query.filter_by(isbn=isbn).first()
        if book:
            return book
        else:
            return None

    @classmethod
    def persistence_yushu(cls, book):
        book_model = Book()
        book_model.set_attrs(book)

        # book_model.isbn = book['isbn13'] or book['isbn10']
        book_model.isbn = get_isbn(book)
        book_model.image = book['images']['large']
        # book_model.origin_url = book['url']
        # book_model.score = book['rating']['average']
        # book_model.tags = book['tags']
        db.session.add(book_model)
        db.session.commit()
        return book_model

