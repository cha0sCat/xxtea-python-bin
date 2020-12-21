# encoding: utf-8
import sys
import xxtea_bin
import unittest

class TestXXTEA(unittest.TestCase):
    def test_xxtea_bin1(self):
        if sys.version_info < (3, 0):
            text = "Hello World! 你好，中国！"
            key = "1234567890"
        else:
            text = "Hello World! 你好，中国！".encode("utf-8")
            key = "1234567890".encode("utf-8")
        encrypt_data = xxtea_bin.encrypt(text, key)
        decrypt_data = xxtea_bin.decrypt(encrypt_data, key)
        self.assertEqual(text, decrypt_data)
    def test_xxtea_bin2(self):
        if sys.version_info < (3, 0):
            text = "Hello World! 你好，中国！".decode("utf-8")
            key = "1234567890".decode("utf-8")
        else:
            text = "Hello World! 你好，中国！"
            key = "1234567890"
        encrypt_data = xxtea_bin.encrypt(text, key)
        decrypt_data = xxtea_bin.decrypt_utf8(encrypt_data, key)
        self.assertEqual(text, decrypt_data)

if __name__ == '__main__':
    unittest.main()
