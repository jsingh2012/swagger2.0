import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server import util
import mysql.connector


def addbook(body):  # noqa: E501
    """Add a new book to the Library

    Creates a new book in the Library # noqa: E501

    :param body: Book object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Book
    """
    status=""
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        cnx = mysql.connector.connect(user='swagger', password='Admin@123', host='127.0.0.1', database='library',
                                  auth_plugin='mysql_native_password')
        sql = """INSERT INTO library.books (ISBN, title, edition, authorid, price, category, details) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        record=(body.isbn, body.title, body.edition, body.authorid, body.price, body.category, body.details)
        cursor = cnx.cursor()
        cursor.execute(sql, record)
        cnx.commit()
        status="Success added Book"
    except mysql.connector.Error as error:
        status = "Failed to insert into MySQL table {}".format(error)
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")
    return status+' Jatinder do some magic!'
