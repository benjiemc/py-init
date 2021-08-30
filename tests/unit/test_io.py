import os
from tempfile import TemporaryDirectory
from unittest import TestCase

from pyinit.io import add_file


class TestAddFile(TestCase):
    def test_setup_py(self):
        with TemporaryDirectory() as dir:
            add_file("setup.py", {"package_name": "Test Package",
                                  "package_description": "This is a test.",
                                  "author_name": "Test Name",
                                  "author_email": "test@email.com"}, dir)
            with open(os.path.join(dir, "setup.py"), 'r') as fh:
                content = fh.readlines()

        self.assertEqual(content[0], "from setuptools import setup\n")

    def test_setup_cfg(self):
        with TemporaryDirectory() as dir:
            add_file("setup.cfg", {"package_name": "Test Package",
                                   "package_description": "This is a test.",
                                   "author_name": "Test Name",
                                   "author_email": "test@email.com"}, dir)
            with open(os.path.join(dir, "setup.cfg"), 'r') as fh:
                content = fh.readlines()

        self.assertEqual(content[0], "[metadata]\n")
        self.assertEqual(content[1], "name = Test Package\n")
