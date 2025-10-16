"""
Unit tests for the Calculator module.
"""

import pytest
from src.features.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""
    
    @pytest.fixture
    def calculator(self):
        """Create a Calculator instance for testing."""
        return Calculator()
    
    def test_add_integers(self, calculator):
        """Test adding two integers."""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
    
    def test_add_floats(self, calculator):
        """Test adding two floats."""
        assert calculator.add(2.5, 3.5) == 6.0
        assert calculator.add(1.1, 2.2) == pytest.approx(3.3)
    
    def test_subtract_integers(self, calculator):
        """Test subtracting two integers."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 5) == -5
        assert calculator.subtract(-3, -3) == 0
    
    def test_subtract_floats(self, calculator):
        """Test subtracting two floats."""
        assert calculator.subtract(5.5, 2.5) == 3.0
        assert calculator.subtract(1.1, 0.1) == pytest.approx(1.0)
    
    def test_multiply_integers(self, calculator):
        """Test multiplying two integers."""
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(0, 5) == 0
    
    def test_multiply_floats(self, calculator):
        """Test multiplying two floats."""
        assert calculator.multiply(2.5, 2) == 5.0
        assert calculator.multiply(1.5, 1.5) == pytest.approx(2.25)
    
    def test_divide_integers(self, calculator):
        """Test dividing two integers."""
        assert calculator.divide(6, 2) == 3.0
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-6, 2) == -3.0
    
    def test_divide_floats(self, calculator):
        """Test dividing two floats."""
        assert calculator.divide(7.5, 2.5) == 3.0
        assert calculator.divide(1.0, 3.0) == pytest.approx(0.333333, rel=1e-5)
    
    def test_divide_by_zero(self, calculator):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(5, 0)
    
    def test_power_integers(self, calculator):
        """Test power operation with integers."""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1
        assert calculator.power(2, -1) == 0.5
    
    def test_power_floats(self, calculator):
        """Test power operation with floats."""
        assert calculator.power(2.0, 3.0) == 8.0
        assert calculator.power(4.0, 0.5) == 2.0
    
    def test_mixed_operations(self, calculator):
        """Test combining multiple operations."""
        result = calculator.add(calculator.multiply(2, 3), 4)
        assert result == 10
        
        result = calculator.divide(calculator.subtract(10, 4), 2)
        assert result == 3.0
