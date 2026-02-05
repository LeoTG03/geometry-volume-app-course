import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid_input():
    """
    Testing valid dimension on sphere
    """
    radius = 2.0
    expected = 33.510321638291124
    assert volume_sphere(radius) == expected

def test_volume_sphere_negative_dimension():
    """
    Current behaviour when negative dimensions
    """
    radius = -3.0
    with pytest.raises(ValueError):
	    volume_sphere(radius)

def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approx comparison
    """
    radius = 2.0
    expected = (4 / 3) * math.pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
