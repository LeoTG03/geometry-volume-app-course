import pytest
import math
from geometry.cylinder import volume_cylinder

def test_volume_cylinder_valid_inputs():
    """
    Testing valid dimensions for cone
    """
    radius, height = 3, 5
    expected = 141.3716694115407
    assert volume_cylinder(radius,height) == expected

def test_volume_cylinder_negative_dimensions():
    """
    document current behaviour when negative dimensions
    """
    radius, height = 3, -5
    excepted = -141.3716694115407
    assert volume_cylinder(radius, height) == excepted

def test_volume_cylinder_float_tolerance():
    """
    Test volume computation using approx comparison    
    """
    radius, height = 2.0, 3.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius,height) == pytest.approx(expected, rel=1e-6)
