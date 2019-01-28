from .book import BookViewModel


class MyWishes:
    def __init__(self, wishes, gifts_count):
        self.my_wishes = []
        self.__parse(wishes, gifts_count)

    def __parse(self, wishes, gifts_count):
        my_wishes = []
        for wish in wishes:
            count = 0
            for wish_count in gifts_count:
                if wish.isbn == wish_count[1]:
                    count = wish_count[0]
            else:
                r = {
                    'wishes_count': count,
                    'book': BookViewModel(wish.book.first),
                    'id': wish.id
                }
                my_wishes.append(r)
        self.my_wishes = my_wishes


