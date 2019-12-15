import unittest
from divider import encrypt_file, encrypt_mbitwise, is_multiple_of_two, convert_to_bytes

class EncrypterTest(unittest.TestCase):
    def test_encrypt_mbitwise1(self):
        bytes = b'hello world'
        key_in_bytes = b'password'
        encrypted_bytes = encrypt_mbitwise(bytes, key_in_bytes)
        print(encrypted_bytes)
        #self.assertEqual(encrypted_bytes, b'')

    def test_is_multiple_of_two1(self):
        self.assertTrue(is_multiple_of_two(0b1))

    def test_is_multiple_of_two2(self):
        self.assertTrue(is_multiple_of_two(0b1000))

    def test_is_multiple_of_two3(self):
        self.assertTrue(is_multiple_of_two(0b00010000))

    def test_is_multiple_of_two4(self):
        self.assertTrue(is_multiple_of_two(0b0))

    def test_is_multiple_of_two5(self):
        self.assertFalse(is_multiple_of_two(0b00010001))

    def test_convert_to_bytes1(self):
        integer = 3
        bytes_size = 1
        self.assertEqual(convert_to_bytes(integer, bytes_size), b'\x03')

    def test_convert_to_bytes2(self):
        integer = 256
        bytes_size = 2
        self.assertEqual(convert_to_bytes(integer, bytes_size), b'\x01\x00')

    def test_convert_to_bytes3(self):
        integer = 511
        bytes_size = 2
        self.assertEqual(convert_to_bytes(integer, bytes_size), b'\x01\xff')


'''
일단 무조건 바이트단위로 쪼개다보니 hexdump의 결과 패턴이 노출될 수 있음.
또한, 키보드상 입력 가능한 단어의 조합들이, binary의 0 무더기에 걸릴경우 암호문 자체가 노출됨.
따라서 salt를 뿌린 hash화가 필요하며, 바이트단위로 쪼개지 않고 비트단위로 접근할 필요가 있음.
'''
#    def test_encrypt_file(self):
#        filename = './hello.txt'
#        encrypt_file(fname, 'password')

if __name__=='__main__':
    unittest.main()
