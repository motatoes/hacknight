import unittest
from solution import num2word

class NumericTestCase(unittest.TestCase):
    def test_num2word(self):
        self.assertEqual(num2word(0), "zero")
        self.assertEqual(num2word(1), "one")
        self.assertEqual(num2word(2), "two")
        self.assertEqual(num2word(3), "three")
        self.assertEqual(num2word(4), "four")
        self.assertEqual(num2word(5), "five")
        self.assertEqual(num2word(6), "six")
        self.assertEqual(num2word(7), "seven")
        self.assertEqual(num2word(8), "eight")
        self.assertEqual(num2word(9), "nine")
        self.assertEqual(num2word(10), "ten")        
        self.assertEqual(num2word(11), "eleven")
        self.assertEqual(num2word(12), "twelve")
        self.assertEqual(num2word(13), "thirteen")
        self.assertEqual(num2word(14), "fourteen")
        self.assertEqual(num2word(15), "fifteen")
        self.assertEqual(num2word(16), "sixteen")
        self.assertEqual(num2word(17), "seventeen")
        self.assertEqual(num2word(18), "eighteen")
        self.assertEqual(num2word(19), "nineteen")
        self.assertEqual(num2word(20), "twenty")

        self.assertEqual(num2word(21), "twenty-one")
        self.assertEqual(num2word(35), "thirty-five")
        self.assertEqual(num2word(44), "fourty-four")
        self.assertEqual(num2word(59), "fifty-nine")
        self.assertEqual(num2word(77), "seventy-seven")
        self.assertEqual(num2word(89), "eighty-nine")
        self.assertEqual(num2word(90), "ninety")
        self.assertEqual(num2word(93), "ninety-three")
        self.assertEqual(num2word(99), "ninety-nine")

        self.assertEqual(num2word(100), "one hundred")
        self.assertEqual(num2word(103), "one hundred and three")
        self.assertEqual(num2word(113), "one hundred and thirteen")
        self.assertEqual(num2word(184), "one hundred and eighty-four")

        self.assertEqual(num2word(203), "two hundred and three")
        self.assertEqual(num2word(213), "two hundred and thirteen")
        self.assertEqual(num2word(308), "three hundred and eight")
        self.assertEqual(num2word(323), "three hundred and twenty-three")
        self.assertEqual(num2word(409), "four hundred and nine")
        self.assertEqual(num2word(500), "five hundred")
        self.assertEqual(num2word(604), "six hundred and four")
        self.assertEqual(num2word(640), "six hundred and fourty")
        self.assertEqual(num2word(797), "seven hundred and ninety-seven")
        self.assertEqual(num2word(833), "eight hundred and thirty-three")
        self.assertEqual(num2word(903), "nine hundred and three")
        self.assertEqual(num2word(923), "nine hundred and twenty-three")
        self.assertEqual(num2word(955), "nine hundred and fifty-five")
        self.assertEqual(num2word(1000), "one thousand")

        self.assertEqual(num2word(10_000), "ten thousand")
        self.assertEqual(num2word(10_300), "ten thousand three hundred")
        self.assertEqual(num2word(10_123), "ten thousand one hundred and twenty-three")
        self.assertEqual(num2word(10_023), "ten thousand and twenty-three")
        self.assertEqual(num2word(10_303), "ten thousand three hundred and three")
        
        self.assertEqual(num2word(100_000), "one hundred thousand")
        self.assertEqual(num2word(100_105), "one hundred thousand one hundred and five")
        self.assertEqual(num2word(100_023), "one hundred thousand and twenty-three")

        self.assertEqual(num2word(1_000_000), "one million")
        self.assertEqual(num2word(1_100_000), "one million one hundred thousand")

        self.assertEqual(num2word(10_000_000), "ten million")
        self.assertEqual(num2word(11_000_000), "eleven million")


if __name__ == "__main__":
    unittest.main()
