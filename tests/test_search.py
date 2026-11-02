import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

        result = search_by_category(items, "animation")
        titles = [dvd.title for dvd in result]

        self.assertEqual(titles, ["The Lion King", "Aladdin"])


class TestSearchByTitle(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

    def test_search_title_lowercase_keyword(self):
        result = search_by_title(self.items, "lion")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_title_uppercase_keyword(self):
        result = search_by_title(self.items, "LION")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_title_no_match(self):
        result = search_by_title(self.items, "harry potter")
        self.assertEqual(result, [])

    def test_search_title_empty_keyword(self):
        result = search_by_title(self.items, "   ")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
