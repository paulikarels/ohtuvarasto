import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(99)

        self.assertAlmostEqual(self.varasto.saldo, 10)



    def test_tilavuus_negatiivinen(self):
        varasto2 = Varasto(-10)

        self.assertAlmostEqual(varasto2.tilavuus, 0)
        
    def test_alkusaldo_negatiivinen(self):
        varasto2 = Varasto(0, -5)

        self.assertAlmostEqual(varasto2.saldo, 0)


    
    def test_lisays_ali_tilavuuden(self):
        self.varasto.lisaa_varastoon(-99)

        self.assertAlmostEqual(self.varasto.saldo, 0)

        
    def test_ota_varastosta_negatiivinen(self):
        saatu_maara = self.varasto.ota_varastosta(-50)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ota_varastosta_liikaa(self):
        saatu_maara = self.varasto.ota_varastosta(50)

        self.assertAlmostEqual(saatu_maara, self.varasto.saldo)

    def test_palauta_oikea_tuloste(self):
        self.assertAlmostEqual(str(self.varasto), f"saldo = 0, vielä tilaa 10")

