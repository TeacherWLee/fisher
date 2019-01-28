from .book import BookViewModel
from collections import namedtuple

GiftWishCount = namedtuple('GiftWishCount', ['wish_count', 'book', 'id'])


class MyGifts:
    def __init__(self, gifts, wishes_count):
        self.my_gifts = []
        self.__parse(gifts, wishes_count)

    def package(self):
        return self.my_gifts

    def __parse(self, gifts, wishes_count):
        my_gifts = []
        for gift in gifts:
            count = 0
            for wish_count in wishes_count:
                if gift.isbn == wish_count[1]:
                    count = wish_count[0]
            else:
                r = {
                    'wishes_count': count,
                    'book': BookViewModel(gift.book.first),
                    'id': gift.id
                }
                my_gifts.append(r)
        self.my_gifts = my_gifts


