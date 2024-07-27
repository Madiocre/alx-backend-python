#!/usr/bin/env python3
""" Test unit for utils functions
"""
import unittest
from parameterized import parameterized, parameterized_class
from typing import Dict, Tuple, Union

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
if __name__ == '__main__':
    unittest.main()