from unittest import TestCase

class AllAssertsTests(TestCase):

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