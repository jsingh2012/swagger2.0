import connexion
import six

from swagger_server.models.cat import Cat  # noqa: E501
from swagger_server.models.cats_response import CatsResponse  # noqa: E501
from swagger_server import util


def add_cat(body):  # noqa: E501
    """Add a new cat to the store

    Creates a new cat in the store # noqa: E501

    :param body: Cat object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        body = Cat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_cat(cat_id):  # noqa: E501
    """Delete a cat

    Delete a cat # noqa: E501

    :param cat_id: Id of the cat desired to be deleted
    :type cat_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_cat(cat_id):  # noqa: E501
    """Retrieve a single cat

    Retrieve a single cat # noqa: E501

    :param cat_id: Id of the cat desired to be retrieved
    :type cat_id: str

    :rtype: Cat
    """
    return 'do some magic!'


def list_cats():  # noqa: E501
    """Retrieves the list of all cats

    Retrieves the list of all cats # noqa: E501


    :rtype: CatsResponse
    """
    return 'do some magic!'


def multi_pages_request(multipages_input, pdf=None, image0=None, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None, image7=None, image8=None, image9=None, X_Client_Trace_Id=None):  # noqa: E501
    """Takes a list of images and run pipeline including stitch

    Runs pipeline for the provided images and stitches images that are needed to be stitched. Then, runs the whole pipeline on the stitched image, too. Note: Image is optional if imageN is provided in multi-part formData. See [/multipages/doc](#/OCR/multipages_doc) Note: We officially only support png and jpeg data and the image size is limited to 7000x7000 pixels  # noqa: E501

    :param multipages_input: Important: Due to openapi v2.0 issues, see /multipages_request for input model of multipages_input.  See [/multipages/doc](#/OCR/multipages_doc) 
    :type multipages_input: str
    :param pdf: PDF file content. We will consider imageN parameters only if pdf parameter is missing from request.
    :type pdf: werkzeug.datastructures.FileStorage
    :param image0: 
    :type image0: werkzeug.datastructures.FileStorage
    :param image1: 
    :type image1: werkzeug.datastructures.FileStorage
    :param image2: 
    :type image2: werkzeug.datastructures.FileStorage
    :param image3: 
    :type image3: werkzeug.datastructures.FileStorage
    :param image4: 
    :type image4: werkzeug.datastructures.FileStorage
    :param image5: 
    :type image5: werkzeug.datastructures.FileStorage
    :param image6: 
    :type image6: werkzeug.datastructures.FileStorage
    :param image7: 
    :type image7: werkzeug.datastructures.FileStorage
    :param image8: 
    :type image8: werkzeug.datastructures.FileStorage
    :param image9: 
    :type image9: werkzeug.datastructures.FileStorage
    :param X_Client_Trace_Id: Optional, unique ID provided by the caller of the API to track this single http request.  Returned in responses to aid in debugging and tracking.  Each request should have a unique id. Recommend a random, opaque UUID with no semantic, private, or secure information included.  IMPORTANT:  This documentation refers to the wrong header name.  Please use \&quot;X-Client-Trace-Id\&quot; 
    :type X_Client_Trace_Id: str

    :rtype: Cat
    """
    return 'do some magic!'


def update_cat(cat_id, body):  # noqa: E501
    """Update an existing cat

     # noqa: E501

    :param cat_id: Id of the cat desired to be updated
    :type cat_id: str
    :param body: Cat object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Cat
    """
    if connexion.request.is_json:
        body = Cat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
