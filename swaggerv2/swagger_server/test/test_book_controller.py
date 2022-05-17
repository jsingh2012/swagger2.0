# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_addbook(self):
        """Test case for addbook

        Add a new book to the Library
        """
        body = Book()
        response = self.client.open(
            '/book/add',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
