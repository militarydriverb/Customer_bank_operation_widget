import unittest
from unittest.mock import mock_open, patch

from src.utils import dic_list


class TestInputTransaction(unittest.TestCase):

    def test_valid_data(self):
        """Тестирование успешного выполнения функции"""
        mock_data = '[{"id": 1, "amount": 100}]'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = dic_list("path/to/mockfile.json")
            self.assertEqual(result, [{"id": 1, "amount": 100}])

    def test_not_valid_data(self):
        """Тестирование выполнения функции при отсутствии данных о транзакциях"""
        with patch('builtins.open', mock_open(read_data=None)):
            result = dic_list("path/to/mockfile.json")
            self.assertEqual(result, [])

    def test_empty_file(self):
        """Тестирование выполнения функции при пустом файле"""
        with patch('builtins.open', mock_open(read_data='')):
            result = dic_list("path/to/mockfile.json")
            self.assertEqual(result, [])

    def test_file_data_not_list(self):
        """Тестирование выполнения функции если файл содержит не список транзакций"""
        with patch('builtins.open', side_effect=TypeError):
            result = dic_list("path/to/mockfile.json")
            self.assertEqual(result, [])

    def test_file_not_found(self):
        """Тестирование выполнения функции если файл не найден"""
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = dic_list("path/to/mockfile.json")
            self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
