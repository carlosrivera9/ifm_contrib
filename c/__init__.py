import ifm
#from . import enum
#from . import diff
from . import obj
from . import files

def closeAllDocuments():
    """
    Close all open documents

    :return:
    """
    while ifm.getNumberOfDocuments() > 0:
        ifm.getDocument(0).closeDocument()
