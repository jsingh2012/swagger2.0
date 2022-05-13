# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cat import Cat  # noqa: E501
from swagger_server.models.cats_response import CatsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCatController(BaseTestCase):
    """CatController integration test stubs"""

    def test_add_cat(self):
        """Test case for add_cat

        Add a new cat to the store
        """
        body = Cat()
        response = self.client.open(
            '/cats',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_cat(self):
        """Test case for delete_cat

        Delete a cat
        """
        response = self.client.open(
            '/cats/{cat_id}'.format(cat_id='cat_id_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cat(self):
        """Test case for get_cat

        Retrieve a single cat
        """
        response = self.client.open(
            '/cats/{cat_id}'.format(cat_id='cat_id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_cats(self):
        """Test case for list_cats

        Retrieves the list of all cats
        """
        response = self.client.open(
            '/cats',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_cat(self):
        """Test case for update_cat

        Update an existing cat
        """
        body = Cat()
        response = self.client.open(
            '/cats/{cat_id}'.format(cat_id='cat_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
