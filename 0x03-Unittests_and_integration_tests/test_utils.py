#!/usr/bin/env python3
'''
Test module for utils.access_nested_map
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    Class to test get json method
    '''
    @parameterized.expand([
      ("http://example.com"), {"payload": True},
      ("http://holberton.io"), {"payload": False}
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_req_get):
        '''
        Function to test that utils.get_json
        returns expected result
        '''
        mock_res = Mock()
        # json return value of mock object is test_payload
        mock_res.json.return_value = test_payload

        # return value or mock reguest is a mock object
        mock_req_get.return_value = mock_res

        result = get_json(test_url)

        mock_req_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
