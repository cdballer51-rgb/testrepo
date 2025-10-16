# API Documentation

## Calculator Module

The Calculator module provides basic arithmetic operations with proper error handling and type safety.

### Class: Calculator

A simple calculator class that performs basic arithmetic operations.

#### Methods

##### add(a, b)

Adds two numbers together.

**Parameters:**
- `a` (int | float): First number
- `b` (int | float): Second number

**Returns:**
- (int | float): Sum of a and b

**Example:**
```python
from src.features.calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)  # Returns 8
```

##### subtract(a, b)

Subtracts b from a.

**Parameters:**
- `a` (int | float): Number to subtract from
- `b` (int | float): Number to subtract

**Returns:**
- (int | float): Difference of a and b

**Example:**
```python
calc = Calculator()
result = calc.subtract(10, 4)  # Returns 6
```

##### multiply(a, b)

Multiplies two numbers.

**Parameters:**
- `a` (int | float): First number
- `b` (float): Second number

**Returns:**
- (int | float): Product of a and b

**Example:**
```python
calc = Calculator()
result = calc.multiply(3, 4)  # Returns 12
```

##### divide(a, b)

Divides a by b.

**Parameters:**
- `a` (int | float): Numerator
- `b` (int | float): Denominator

**Returns:**
- (float): Quotient of a and b

**Raises:**
- `ValueError`: If b is zero

**Example:**
```python
calc = Calculator()
result = calc.divide(10, 2)  # Returns 5.0

try:
    result = calc.divide(10, 0)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

##### power(base, exponent)

Raises base to the power of exponent.

**Parameters:**
- `base` (int | float): The base number
- `exponent` (int | float): The exponent

**Returns:**
- (int | float): base raised to the power of exponent

**Example:**
```python
calc = Calculator()
result = calc.power(2, 3)  # Returns 8
result = calc.power(4, 0.5)  # Returns 2.0 (square root)
```

## Configuration

The calculator module can be configured via `config.yaml`:

```yaml
features:
  calculator:
    enabled: true
    max_precision: 10
    allow_complex_operations: false
```

### Configuration Options

- `enabled` (bool): Enable or disable the calculator feature
- `max_precision` (int): Maximum decimal precision for calculations
- `allow_complex_operations` (bool): Enable complex number operations (future feature)
