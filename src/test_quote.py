import pytest
from QuoteController import *
from Quote import *

class TestQuote:
    def test_quotes_ctor(self):
        quote = Quote(None, "Aku suka ikan cupang")
        assert quote.id is None
        assert quote.waktuEdit is not None
        assert quote.quote == "Aku suka ikan cupang"
        assert quote.builtin == False

    def test_quotes_ctor_from_table(self):
        quote = createFromTable([0, 'Cupang warna biru', '2021-04-01 12:00:00', False])
        assert quote.id == 0
        assert quote.waktuEdit == "2021-04-01 12:00:00"
        assert quote.quote == 'Cupang warna biru'
        assert quote.builtin == False

    def test_check_foreach(self):
        self.panjang = 0
        def addPanjang(_):
            self.panjang += 1
        controller = QuoteController()
        controller.foreach(addPanjang)

        assert self.panjang == len(controller.daftarQuotes)

    def test_random(self):
        controller = QuoteController()
        output = controller.fetchRandom()
        
        assert output is not None
    



    