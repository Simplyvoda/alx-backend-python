#!/usr/bin/env python3
'''
Test module for client
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

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
    def test_org(
        self,
        test_org,
        test_payload):
        '''
        This method tests that GithubOrgClient.org
        returns the correct value
        '''
        # patching the get_json call
        with patch.object(
          GithubOrgClient, 
          "requests.get"
        ) as mock_req:
            mock_res = Mock()
            mock_res.json = Mock(return_value=test_payload)
            test_obj = GithubOrgClient(test_org)
            result = test_obj.org()

            mock_req.assert_called_once_with(test_org)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
  unittest.main()
