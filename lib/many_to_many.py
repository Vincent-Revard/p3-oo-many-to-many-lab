class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        contracts_list = []

        for contract in Contract.all:
            if contract.book is self:
                contracts_list.append(contract)

        return contracts_list

    def authors(self):
        # authors = set()
        # for contract in self.contracts:
        #     authors.add(contract.author)
        # return list(authors)
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    @staticmethod
    def validate_input(author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a str")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an int")


    def __init__(self, author, book, date, royalties):
        self.validate_input(author, book, date, royalties)
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    @classmethod
    def contracts_by_date(cls, date):

        # return [contract for contract in cls.all if contract.date == date]
        # contract_list = []

        # for contract in cls.all:
        #     if contract.date == date:
        #         contract_list.append(contract)

        # return contract_list
        get_contract_list = lambda cls, date: [contract for contract in cls.all if contract.date is date]
        return get_contract_list(cls, date)
