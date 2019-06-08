import os
import io
import logging
import unittest

import responses

from src.rewardp.mailgun import Mailgun


class TestMailgun(unittest.TestCase):

    def setUp(self):
        self.mailgun = Mailgun('test-api-key-123')

    @responses.activate
    def test_send_simple_message(self):
        url = 'https://api.eu.mailgun.net/v3/www.rewardp.com/messages'
        responses.add(responses.POST, url)
        response = self.mailgun.send_simple_message(
            'Welcome', 
            'Confirm your email', 
            ['jkrclaro@gmail.com']
        )

        assert 'from=Rewardp+%3Cmailgun%40www.rewardp.com%3E&to=jkrclaro%40gmail.com&subject=Welcome&text=Confirm+your+email' == response.request.body


if __name__ == '__main__':
    unittest.main()
