import connexion
import six

from swagger_server import util


def upload_post(upfile=None):  # noqa: E501
    """Uploads a file.

     # noqa: E501

    :param upfile: The file to upload.
    :type upfile: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'
