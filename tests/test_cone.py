import pytest
import math
from geometry.cone import volume_cone

def test_volume_cone_valid_inputs():
	"""
	Testing valid dimensions on cone
	"""
	base_radius, height = 3.0, 5.0
	expected = 47.12388980384689
	assert volume_cone(base_radius,height) == expected

def test_volume_cone_negative_dimension():
	"""
	document current behaviour when negative dimension
	"""
	base_radius, height = 3.0 , -5.0 #has to be height since base_r will be always positive
	expected = -47.12388980384689
	assert volume_cone(base_radius, height) == expected

def test_volume_cone_float_tolerance():
	"""
	Test volume computation using approx comparison
	"""
	base_radius, height = 2.0, 6.5
	expected =  (1/3) * math.pi * base_radius**2 * height
	assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)
