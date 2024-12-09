import unittest
from blackjack import calculate_score

class TestBlackjack(unittest.TestCase):
    
    def test_blackjack_natural(self):
        """Testa se a mão [10, 11] é reconhecida como Blackjack."""
        hand = [10, 11]
        self.assertEqual(calculate_score(hand), 0, f"Erro ao calcular Blackjack para {hand}")
    
    def test_score_below_21(self):
        """Testa uma mão válida abaixo de 21."""
        hand = [5, 5, 5]
        self.assertEqual(calculate_score(hand), 15, f"Erro ao calcular pontuação para {hand}")

    def test_score_exactly_21(self):
        """Testa uma mão que soma exatamente 21."""
        hand = [7, 7, 7]
        self.assertEqual(calculate_score(hand), 21, f"Erro ao calcular pontuação para {hand}")

    def test_bust_hand(self):
        """Testa uma mão que ultrapassa 21."""
        hand = [10, 6, 6]
        self.assertEqual(calculate_score(hand), 22, f"Erro ao calcular pontuação para {hand}")

    def test_ace_adjustment(self):
        """Testa se o valor do Ás é ajustado corretamente quando necessário."""
        hand = [11, 10, 2]
        self.assertEqual(calculate_score(hand), 13, f"Erro ao ajustar o valor do Ás para {hand}")

    def test_multiple_aces(self):
        """Testa se múltiplos Ás são ajustados corretamente."""
        hand = [11, 11, 9]
        self.assertEqual(calculate_score(hand), 21, f"Erro ao ajustar múltiplos Ás para {hand}")

    def test_blackjack_with_face_cards(self):
        """Testa uma mão que contém cartas de figuras e forma Blackjack."""
        hand = [10, 10, 11]
        self.assertEqual(calculate_score(hand), 21, f"Erro ao calcular Blackjack com figuras para {hand}")
    
    def test_empty_hand(self):
        """Testa o cálculo de pontuação para uma mão vazia."""
        hand = []
        self.assertEqual(calculate_score(hand), 0, f"Erro ao calcular pontuação para {hand}")

    def test_single_card(self):
        """Testa o cálculo de pontuação para uma única carta."""
        hand = [7]
        self.assertEqual(calculate_score(hand), 7, f"Erro ao calcular pontuação para {hand}")

if __name__ == '__main__':
    unittest.main()