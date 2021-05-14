import unittest
import numpy as np
from implementations_with_benchmark import next_power_of_2, pad_zeros_to, naive_convolution, overlap_add_convolution, overlap_save_convolution


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

    def test_naive_convolution(self):
        x = np.array([1.0, -1.0, 3.0])
        h = np.array([2.0, -1.0, 1.0, -0.5, 0.3])

        x_h_convolution_numpy = np.convolve(x, h, 'full')
        x_h_convolution = naive_convolution(x, h)

        np.testing.assert_array_equal(x_h_convolution, x_h_convolution_numpy)

    def test_ola_convolution(self):
        x = np.array([1.0, -1.0, 3.0])
        h = np.array([2.0, -1.0, 1.0, -0.5, 0.3])

        x_h_convolution_numpy = np.convolve(x, h, 'full')
        x_h_convolution = overlap_add_convolution(x, h, B=3)

        np.testing.assert_array_almost_equal(x_h_convolution, x_h_convolution_numpy, decimal=10)

    def test_ols_convolution(self):
        x = np.array([1.0, -1.0, 3.0])
        h = np.array([2.0, -1.0, 1.0, -0.5, 0.3])

        x_h_convolution_numpy = np.convolve(x, h, 'full')
        x_h_convolution = overlap_save_convolution(x, h, B=3)

        np.testing.assert_array_almost_equal(x_h_convolution, x_h_convolution_numpy, decimal=10)



if __name__ == '__main__':
    unittest.main()
