"""
Calculator module providing basic arithmetic operations.

This module demonstrates a simple feature implementation with
proper error handling and validation.
"""

from typing import Union


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            Difference of a and b
        """
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent
