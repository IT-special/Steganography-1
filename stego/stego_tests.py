import unittest
import stego
import os

_cwd = os.getcwd()
ENCRYPT_IMAGE = os.path.join(_cwd, 'tests/test.png')
DECRYPT_IMAGE = os.path.join(_cwd, 'tests/new_test.png')
ENCRYPT_AUDIO = os.path.join(_cwd, 'tests/test.mov')
DECRYPT_AUDIO = os.path.join(_cwd, 'tests/new_test.mov')
TEST_FILE = os.path.join(_cwd, 'tests/hello')
DECRYPT_FILE = os.path.join(_cwd, 'tests/world')
PRIVATE_KEY = os.path.join(_cwd, 'tests/private_key.pem')
PUBLIC_KEY = os.path.join(_cwd, 'tests/public_key.pem')

class StegoTests(unittest.TestCase):
    def test_magic(self):
        print("Test magic password.")
        stego.encrypt(ENCRYPT_IMAGE, DECRYPT_IMAGE, TEST_FILE, "password", "magic", None)
        print("")
        stego.decrypt(DECRYPT_IMAGE, DECRYPT_FILE, "password", "magic", None)

    # def test_rsa(self):
    #     print("\nTest RSA.")
    #     stego.encrypt(ENCRYPT_IMAGE, DECRYPT_IMAGE, TEST_FILE, None, None, PUBLIC_KEY)
    #     print("")
    #     stego.decrypt(DECRYPT_IMAGE, DECRYPT_FILE, None, None, PRIVATE_KEY)

    # def test_audio(self):
    #     print("\nTest audio.")
    #     stego.encrypt(ENCRYPT_AUDIO, TEST_FILE, None, None, PUBLIC_KEY)
    #     print("")
    #     stego.decrypt(DECRYPT_AUDIO, None, None, PRIVATE_KEY)

if __name__ == "__main__":
    unittest.main()
