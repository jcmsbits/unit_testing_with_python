
import unittest 
SERVER = "server_a"
RUNNING_API = False

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("No_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2,5,7,10])
        self.assertNotIn(4, [1,3,5])

    def test_assert_dicts(self):
        user = {"first_name" : "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name" : "Luis", "last_name": "Martinez"},
            user
        )
    
    def test_assert_sets(self):
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    # Se pueden saltar pruebas con el decorador unittest
    # y se pueden agregar mensajes
    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual(100, 100)

    # Saltar si la condición es verdadera
    @unittest.skipIf(SERVER == "server_a", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100,101)

    # Error esperado
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual("Hola", "alo")

    # Saltar al menos que se cumpla una condición
    @unittest.skipUnless(RUNNING_API, "La api no está disponible")
    def test_skip_unless(self):
        self.assertGreaterEqual(12,10)
