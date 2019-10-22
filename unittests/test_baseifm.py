import unittest
import ifm_contrib as ifm
from ifm import Enum


class TestMesh(unittest.TestCase):

    def test_createFracElement(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        # doc = ifm.loadDocument("./models/example_3D_mspecies.fem")
        doc.pdoc.createFracElement(0, 1, Enum.FRAC_1D, Enum.FRAC_A, Enum.MANNING_LAW)

    def test_setFracFlowConductivity(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        fracid = doc.pdoc.createFracElement(0, 1, Enum.FRAC_1D, Enum.FRAC_A, Enum.MANNING_LAW)
        doc.setFracFlowConductivity(fracid, 1.0, Enum.ALL_FRAC_TYPES, Enum.ALL_FRAC_MODES, Enum.ALL_FRAC_LAWS)

    def test_setFracArea(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        fracid = doc.pdoc.createFracElement(0, 1, Enum.FRAC_1D, Enum.FRAC_A, Enum.MANNING_LAW)
        doc.setFracArea(fracid, 1.0, Enum.ALL_FRAC_TYPES, Enum.ALL_FRAC_MODES, Enum.ALL_FRAC_LAWS)

    def test_deleteFracElement(self):
        ifm.forceLicense("Viewer")
        doc = ifm.loadDocument("./models/example_2D.fem")
        fracid = doc.pdoc.createFracElement(0, 1, Enum.FRAC_1D, Enum.FRAC_A, Enum.MANNING_LAW)
        doc.deleteFracElement(fracid)


if __name__ == '__main__':
    unittest.main()