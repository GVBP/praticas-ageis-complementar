import unittest

def contarCaracteres(frase):
    return len(frase)

class TestContarCaracteres(unittest.TestCase):
    def test_contagem_de_caracteres(self):
        resultado = contarCaracteres("Esta é uma frase de teste")
        self.assertEqual(resultado, 27)

if __name__ == '__main__':
    unittest.main()
