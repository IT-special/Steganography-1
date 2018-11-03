import unittest
import os

import sys
sys.path.append("..")

from stego import stego

_cwd = os.getcwd()
ENCRYPT_IMAGE = os.path.join(_cwd, 'test.png')
DECRYPT_IMAGE = os.path.join(_cwd, 'new_test.png')
TEST_FILE = os.path.join(_cwd, 'file_test.txt')
PRIVATE_KEY = os.path.join(_cwd, 'keys/pri')
PUBLIC_KEY = os.path.join(_cwd, 'keys/pub')

class StegoTests(unittest.TestCase):
    def test_magic(self):
        print("Test magic password.")
        stego.encrypt(ENCRYPT_IMAGE, TEST_FILE, "password", "magic", None)
        with open(TEST_FILE, 'r') as f:
            text = f.read()
        self.assertEqual(text, stego.decrypt(DECRYPT_IMAGE, "password", "magic", None))

    def test_rsa(self):
        print("\nTest RSA.")
        stego.encrypt(ENCRYPT_IMAGE, TEST_FILE, None, None, PUBLIC_KEY)
        with open(TEST_FILE, 'r') as f:
            text = f.read()
        self.assertEqual(text, stego.decrypt(DECRYPT_IMAGE, None, None, PRIVATE_KEY))

if __name__ == "__main__":
    unittest.main()
