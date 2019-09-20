# -*- coding: utf-8 -*-

import sys
from AesEverywhere.aes256 import aes256

try:
    if sys.version_info < (2, 7):
        import unittest2
    else:
        raise ImportError()
except ImportError:
    import unittest

FAIL = "Invalid decrypt"

class TestAes256(unittest.TestCase):

    def test_decrypt1(self):
        text = aes256.decrypt("U2FsdGVkX1+Z9xSlpZGuO2zo51XUtsCGZPs8bKQ/jYg=", "pass")
        self.assertEqual(text, "test".encode('utf-8'), FAIL)

    def test_decrypt2(self):
        text = aes256.decrypt("U2FsdGVkX1+8b3WpGTbZHtd2T9PNQ+N7GqebGaOV3cI=", "Data 😄 текст")
        self.assertEqual(text, "test".encode('utf-8'), FAIL)

    def test_decrypt3(self):
        text = aes256.decrypt("U2FsdGVkX18Kp+T3M9VajicIO9WGQQuAlMscLGiTnVyHRj2jHObWshzJXQ6RpJtW", "pass")
        self.assertEqual(text, "Data 😄 текст".encode('utf-8'), FAIL)

    def test_decrypt4(self):
        text = aes256.decrypt("U2FsdGVkX1/O7iqht/fnrFdjn1RtYU7S+DD0dbQHB6N/k+CjzowfC2B21QRG24Gv", "Data 😄 текст")
        self.assertEqual(text, "Data 😄 текст".encode('utf-8'), FAIL)

    def test_encrypt_decrypt1(self):
        text = "Test! @#$%^&*"
        passw = "pass"
        enc = aes256.encrypt(text, passw)
        dec = aes256.decrypt(enc, passw)
        self.assertEqual(text.encode('utf-8'), dec, FAIL)

    def test_encrypt_decrypt2(self):
        text = "Test! @#$%^&*( 😆😵🤡👌 哈罗 こんにちわ Акїў 😺"
        passw = "pass"
        enc = aes256.encrypt(text, passw)
        dec = aes256.decrypt(enc, passw)
        self.assertEqual(text.encode('utf-8'), dec, FAIL)

    def test_encrypt_decrypt3(self):
        text = "Test! @#$%^&*( 😆😵🤡👌 哈罗 こんにちわ Акїў 😺"
        passw = "哈罗 こんにちわ Акїў 😺"
        enc = aes256.encrypt(text, passw)
        dec = aes256.decrypt(enc, passw)
        self.assertEqual(text.encode('utf-8'), dec, FAIL)


if __name__ == '__main__':
    unittest.main()

