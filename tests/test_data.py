import unittest
from oceanography_tutor import data

class TestData(unittest.TestCase):
    def test_tide_init(self):
        tide = data.Tide('2022-01-01', 1.0)
        self.assertEqual(tide.date, '2022-01-01')
        self.assertEqual(tide.height, 1.0)

    def test_current_init(self):
        current = data.Current('2022-01-01', 1.0, 45.0)
        self.assertEqual(current.date, '2022-01-01')
        self.assertEqual(current.speed, 1.0)
        self.assertEqual(current.direction, 45.0)

    def test_salinity_init(self):
        salinity = data.Salinity('2022-01-01', 10.0)
        self.assertEqual(salinity.date, '2022-01-01')
        self.assertEqual(salinity.value, 10.0)

    def test_datastore_add_tide(self):
        store = data.DataStore()
        tide = data.Tide('2022-01-01', 1.0)
        store.add_tide(tide)
        self.assertIn(tide, store.get_tides())

    def test_datastore_get_tides(self):
        store = data.DataStore()
        tide = data.Tide('2022-01-01', 1.0)
        store.add_tide(tide)
        tides = store.get_tides()
        self.assertEqual(len(tides), 1)

if __name__ == '__main__':
    unittest.main()
