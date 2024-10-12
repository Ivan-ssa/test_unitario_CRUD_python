import unittest
from unittest import mock
from reservas import criar_reserva, listar_reservas, atualizar_reserva, cancelar_reserva, validar_data, reservas

class TestReservas(unittest.TestCase):
    def test_criar_reserva(self):
        with mock.patch('builtins.input', side_effect=["Reserva Teste", "01012024"]):
            criar_reserva()  # Chame a função que você quer testar
            self.assertEqual(len(reservas), 1)  # Verifique se a reserva foi adicionada

    def test_listar_reservas(self):
        with mock.patch('builtins.print') as mock_print:
            listar_reservas()  # Chame a função que você quer testar
            mock_print.assert_called()  # Verifique se a função print foi chamada

    def test_atualizar_reserva(self):
        # Aqui você pode adicionar uma reserva para atualizar
        reservas.append({"id": 1, "nome": "Reserva Teste", "data": "01012024"})
        with mock.patch('builtins.input', side_effect=["1", "Reserva Atualizada", "02022024"]):
            atualizar_reserva()  # Chame a função que você quer testar
            self.assertEqual(reservas[0]['nome'], "Reserva Atualizada")  # Verifique se o nome foi atualizado

    def test_cancelar_reserva(self):
        # Aqui você pode adicionar uma reserva para cancelar
        reservas.append({"id": 1, "nome": "Reserva Teste", "data": "01012024"})
        with mock.patch('builtins.input', side_effect=["1"]):
            cancelar_reserva()  # Chame a função que você quer testar
            self.assertEqual(len(reservas), 0)  # Verifique se a reserva foi removida

if __name__ == "__main__":
    unittest.main()
