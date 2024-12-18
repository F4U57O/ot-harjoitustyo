import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 500)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_metodi_palauttaa_true_jos_rahat_riittivat(self):

        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_metodi_palauttaa_false_jos_rahat_ei_riita(self):

        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroiksi_muunnetaan_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    

