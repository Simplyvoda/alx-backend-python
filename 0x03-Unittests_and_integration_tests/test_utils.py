#!/usr/bin/env python3
'''
Test module for utils.access_nested_map
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Class to test access nested map method
    '''
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2)
    ])  # provide different inputs to test the access_nested_map function
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''
        This functions tests that the actual result
        and expected result are same
        '''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
      ({}, ("a",), KeyError),
      ({"a": 1}, ("a", "b"), KeyError)
    ])  # provide different inputs to test the access_nested_map function
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        '''
        This function tests that KeyError is raised
        '''
        access_nested_map(nested_map, path)
        with self.assertRaises(expected_exception, msg="Key not found"):
            return expected_exception


if __name__ == "__main__":
    unittest.main()
