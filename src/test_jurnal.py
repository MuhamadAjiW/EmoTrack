import pytest
from JurnalController import *
from Jurnal import *

class TestJurnal:
    def test_jurnal_ctor(self):
        jurnal = Jurnal(None, 'Menyelesaikan tubes', 'Hari ini aku menyelesaikan tubes')
        assert jurnal.id is None
        assert jurnal.waktuEdit is not None
        assert jurnal.isi == 'Hari ini aku menyelesaikan tubes'
        assert jurnal.judul == 'Menyelesaikan tubes'

    def test_curnal_ctor_from_table(self):
        jurnal = createFromTable([3, 'Beli barang', 'Aku beli barang di toko'])
        assert jurnal.id == 3
        assert jurnal.waktuEdit is not None
        assert jurnal.isi == 'Aku beli barang di toko'
        assert jurnal.judul == 'Beli barang'

    def test_check_today_works(self):
        controller = JurnalController()
        with pytest.raises(Exception):
            controller.addJurnal('Ini judul', 'Ini isi')
            controller.checkToday()

    def test_check_foreach(self):
        self.panjang = 0
        def addPanjang(_):
            self.panjang += 1
        controller = JurnalController()
        controller.foreach(addPanjang)

        assert self.panjang == len(controller.daftarJurnal)

    def test_check_frequency_array_return_list_with_length_12(self):
        controller = JurnalController()
        freq = controller.getFrequencyArray(2023)
        assert len(freq) == 12
        for i in range(12):
            assert freq[i] >= 0
    



    