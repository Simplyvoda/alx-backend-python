#!/usr/bin/env python3
'''
Test module for utils.access_nested_map
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    '''
    Class to test access nested map method
    '''
    @parameterized.expand([
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2)
    ])  # provide different inputs to test the access_nested_map function
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected_result: Union[Dict, int]
          ) -> None:
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
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        expected_exception
          ) -> None:
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
      ("http://example.com", {"payload": True}),
      ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict
          ) -> None:
        '''
        Function to test that utils.get_json
        returns expected result
        '''
        with patch("requests.get") as mock_get:
            mock_res = Mock()  # setting response to be mock object
            # setting return value of mock res to be test_payload
            mock_res.json = Mock(return_value=test_payload)
            # setting return value of mock_get
            # mock_get replaces "request.get"
            mock_get.return_value = mock_res

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''
    class to test memoize decorator
    '''
    def test_memoize(self):
        '''
        This function declares a class
        and then tests the utils.memoize decorator
        '''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


        # patch.object should be used when patching methods
        # within a class
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
          test_obj = TestClass()

          mock_method.assert_called_once()

          self.assertEqual(test_obj.a_property(), 42)
          self.assertEqual(test_obj.a_property(), 42)

if __name__ == "__main__":
    unittest.main()
