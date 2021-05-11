import unittest
import numpy as np
from implementations_with_benchmark import next_power_of_2, pad_zeros_to


class TestFastConvolution(unittest.TestCase):
    def test_next_power_of_2(self):
        self.assertEqual(next_power_of_2(100), 128)
        self.assertEqual(next_power_of_2(200), 256)
        self.assertEqual(next_power_of_2(10), 16)
        self.assertEqual(next_power_of_2(789), 1024)

    def test_pad_zeros_to(self):
        x = np.ones((10,))
        new_x = pad_zeros_to(x, 20)

        np.testing.assert_array_equal(new_x[:10], x)
        np.testing.assert_array_equal(new_x[10:], np.zeros((10,)))


if __name__ == '__main__':
    unittest.main()
