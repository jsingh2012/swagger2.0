# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Book(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, isbn: str=None, title: str=None, edition: int=None, price: int=None, category: str=None, authorid: str=None, details: str=None):  # noqa: E501
        """Book - a model defined in Swagger

        :param isbn: The isbn of this Book.  # noqa: E501
        :type isbn: str
        :param title: The title of this Book.  # noqa: E501
        :type title: str
        :param edition: The edition of this Book.  # noqa: E501
        :type edition: int
        :param price: The price of this Book.  # noqa: E501
        :type price: int
        :param category: The category of this Book.  # noqa: E501
        :type category: str
        :param authorid: The authorid of this Book.  # noqa: E501
        :type authorid: str
        :param details: The details of this Book.  # noqa: E501
        :type details: str
        """
        self.swagger_types = {
            'isbn': str,
            'title': str,
            'edition': int,
            'price': int,
            'category': str,
            'authorid': str,
            'details': str
        }

        self.attribute_map = {
            'isbn': 'ISBN',
            'title': 'title',
            'edition': 'edition',
            'price': 'price',
            'category': 'category',
            'authorid': 'authorid',
            'details': 'details'
        }

        self._isbn = isbn
        self._title = title
        self._edition = edition
        self._price = price
        self._category = category
        self._authorid = authorid
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def isbn(self) -> str:
        """Gets the isbn of this Book.

        ISBN number of the book  # noqa: E501

        :return: The isbn of this Book.
        :rtype: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str):
        """Sets the isbn of this Book.

        ISBN number of the book  # noqa: E501

        :param isbn: The isbn of this Book.
        :type isbn: str
        """
        if isbn is None:
            raise ValueError("Invalid value for `isbn`, must not be `None`")  # noqa: E501

        self._isbn = isbn

    @property
    def title(self) -> str:
        """Gets the title of this Book.

        Name of the book  # noqa: E501

        :return: The title of this Book.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Book.

        Name of the book  # noqa: E501

        :param title: The title of this Book.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def edition(self) -> int:
        """Gets the edition of this Book.


        :return: The edition of this Book.
        :rtype: int
        """
        return self._edition

    @edition.setter
    def edition(self, edition: int):
        """Sets the edition of this Book.


        :param edition: The edition of this Book.
        :type edition: int
        """
        if edition is None:
            raise ValueError("Invalid value for `edition`, must not be `None`")  # noqa: E501

        self._edition = edition

    @property
    def price(self) -> int:
        """Gets the price of this Book.


        :return: The price of this Book.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price: int):
        """Sets the price of this Book.


        :param price: The price of this Book.
        :type price: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def category(self) -> str:
        """Gets the category of this Book.

        Category of the book  # noqa: E501

        :return: The category of this Book.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this Book.

        Category of the book  # noqa: E501

        :param category: The category of this Book.
        :type category: str
        """
        allowed_values = ["noval", "general", "story"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def authorid(self) -> str:
        """Gets the authorid of this Book.


        :return: The authorid of this Book.
        :rtype: str
        """
        return self._authorid

    @authorid.setter
    def authorid(self, authorid: str):
        """Sets the authorid of this Book.


        :param authorid: The authorid of this Book.
        :type authorid: str
        """
        if authorid is None:
            raise ValueError("Invalid value for `authorid`, must not be `None`")  # noqa: E501

        self._authorid = authorid

    @property
    def details(self) -> str:
        """Gets the details of this Book.


        :return: The details of this Book.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details: str):
        """Sets the details of this Book.


        :param details: The details of this Book.
        :type details: str
        """

        self._details = details
