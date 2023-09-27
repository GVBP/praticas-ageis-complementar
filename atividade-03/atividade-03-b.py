import unittest

def contarCaracteres(frase):
    return len(frase)

class TestContarCaracteres(unittest.TestCase):
    def test_contagem_de_caracteres(self):
        resultado = contarCaracteres("Esta é uma frase de teste")
        self.assertEqual(resultado, 27)

    def test_frase_vazia(self):
        resultado = contarCaracteres("")
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
