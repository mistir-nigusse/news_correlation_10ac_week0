import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.loader import NewsDataLoader

class TestLoader(unittest.TestCase):
    
    def setUp(self):
        self.loader = NewsDataLoader(path='data')

    def test_get_news(self):
        expected_path = os.path.join('data', 'rating.csv')
        self.assertEqual(self.loader.get_news_path(), expected_path)

    def test_get_traffic(self):
        expected_path = os.path.join('data', 'traffic.csv')
        self.assertEqual(self.loader.get_traffic_path(), expected_path)

    def test_get_domain_location(self):
        expected_path = os.path.join('data', 'domains_location.csv')
        self.assertEqual(self.loader.get_domain_location_path(), expected_path)

if __name__ == '__main__':
    unittest.main()