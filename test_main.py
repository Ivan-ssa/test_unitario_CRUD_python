# test_main.py
import unittest
from main import adicionar_reserva, listar_reservas, cancelar_reserva

class TestMain(unittest.TestCase):

    def setUp(self):
        self.reservas = [
            {"sala": "Sala 1", "data": "2024-10-15", "hora": "10:00"},
            {"sala": "Sala 2", "data": "2024-10-16", "hora": "11:00"},
        ]

    def test_adicionar_reserva(self):
        reserva = adicionar_reserva("Sala 3", "2024-10-17", "12:00")
        self.assertEqual(reserva, {"sala": "Sala 3", "data": "2024-10-17", "hora": "12:00"})

    def test_adicionar_reserva_campos_vazios(self):
        with self.assertRaises(ValueError):
            adicionar_reserva("", "2024-10-17", "12:00")

    def test_listar_reservas(self):
        reservas = listar_reservas(self.reservas)
        self.assertEqual(reservas, self.reservas)

    def test_cancelar_reserva(self):
        resultado = cancelar_reserva(self.reservas, "Sala 1")
        self.assertTrue(resultado)
        self.assertNotIn({"sala": "Sala 1", "data": "2024-10-15", "hora": "10:00"}, self.reservas)

    def test_cancelar_reserva_inexistente(self):
        resultado = cancelar_reserva(self.reservas, "Sala 3")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
