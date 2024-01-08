#!/usr/bin/env python3
'''
Test module for client
'''
import unittest
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    '''
    This class contains test cases for
    the GithubOrgClient class
    '''
    # using parameterized to pass different inputs
    @parameterized.expand([
      ("google", {"payload": True}),
      ("abc", {"payload": False})
    ])
    @patch("requests.get")
    def test_org(
         self,
         mock_get: Mock,
         test_org: str,
         test_payload: Dict) -> None:
        '''
        This method tests that GithubOrgClient.org
        returns the correct value
        '''
        # Creating a mock response object to mimic the response
        mock_res = Mock()
        # Mocking the json method of the mock response
        # to return the test_payload
        mock_res.json = Mock(return_value=test_payload)
        # Setting the return value of mock request
        mock_get.return_value = mock_res
        # creating test instance
        test_obj = GithubOrgClient(test_org)
        result = test_obj.org()

        mock_get.assert_called_once_with(
          f"https://api.github.com/orgs/{test_org}"
        )
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
