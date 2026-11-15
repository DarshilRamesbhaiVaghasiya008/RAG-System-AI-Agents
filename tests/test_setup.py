import unittest


class PackageSetupTests(unittest.TestCase):
    def test_medrag_package_is_importable(self):
        import medrag

        self.assertIsNotNone(medrag.__file__)
