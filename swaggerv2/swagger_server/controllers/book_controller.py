import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util


def addbook(body):  # noqa: E501
    """Add a new book to the Library

    Creates a new book in the Library # noqa: E501

    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Book
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
