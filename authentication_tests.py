#   Unit tests for the Project1.authentication module
from unittest import TestCase
from mock import patch
import authentication as auth

class StandAloneTests(TestCase):
    #   Test the stand-alone module functions
    @patch('builtins.open')
    def test_login(self, mock_open):
        #   correct arguments
        mock_open.return_value.read.read_value = \
            'netease|password\n'
        self.assertTrue(auth.login('netease', 'password'))
        #self.assertFalse(auth.login('netease', 'password'))
    @patch('builtins.open')
    def test_login_bad_creds(self, mock_open):
        #   wrong arguments
        mock_open.return_value.read.return_value = \
            'netease|password'
        self.assertFalse(auth.login('netease', 'badpassword'))

    @patch('builtins.open')
    def test_login_error(self, mock_open):
        #   exceptions
        mock_open.side_effect = IOError()
        self.assertFalse(auth.login('netease', 'badpassword'))
