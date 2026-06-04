# Add a simple test for numpy
import numpy as np
"""
    This test checks if numpy is working correctly by performing a simple array addition and verifying the result.
    The same function but not in the last git branch, so we can test if the new branch is working correctly.
"""
def test_numpy():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    assert np.array_equal(c, np.array([5, 7, 9]))

if __name__ == "__main__":
    test_numpy()
    print("Numpy test passed successfully!")