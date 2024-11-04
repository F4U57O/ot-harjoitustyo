import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_riittavalla_rahalla_edullisten_lounaiden_osalta(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)

        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_ei_toimi_liian_vahalla_rahalla_edullisten_lounaiden_osalta(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu)

        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_riittavalla_rahalla_maukkaiden_lounaiden_osalta(self):
        maksu = 500
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)

        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_ei_toimi_liian_vahalla_rahalla_maukkaiden_lounaiden_osalta(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu)

        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisiin_jos_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.maksukortti.ota_rahaa(240), True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_ei_toimi_edullisiin_jos_ei_riittavasti_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(kortti.ota_rahaa(240), False)
        self.assertEqual(self.kassapaate.edulliset, 0)  

    def test_korttiosto_toimii_maukkaisiin_jos_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.maksukortti.ota_rahaa(400), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_ei_toimi_maukkaisiin_jos_ei_riittavasti_rahaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(kortti.ota_rahaa(400), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 

    def test_kortille_rahaa_ladatessa_kortin_ja_kassan_saldo_kasvaa_ladatun_maaran(self):
        summa = 1000
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, summa) 
        self.assertEqual(self.maksukortti.saldo, 2000)    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000) 

    def test_negatiivisen_summan_lataaminen_kortille_ei_onnistu(self):
        summa = -1000
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, summa)
        self.assertEqual(self.maksukortti.saldo, 1000)    
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 

    def test_kassan_rahat_muutetaan_euroiksi_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

        

    


    