# testrepo

A Python repository featuring a calculator module with comprehensive testing and documentation.

## Overview

This repository demonstrates best practices for Python development including:
- Modular code architecture
- Comprehensive unit and integration testing
- API documentation
- Configuration management
- Type hints and error handling

## Features

### Calculator Module

A feature-rich calculator providing:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Power/exponentiation operations
- Error handling (e.g., division by zero protection)
- Type safety with Union types

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cdballer51-rgb/testrepo.git
cd testrepo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment (optional):
```bash
cp .env.example .env
```

## Usage

### Basic Example

```python
from src.features.calculator import Calculator

calc = Calculator()

result = calc.add(10, 5)
print(f"10 + 5 = {result}")

result = calc.multiply(3, 4)
print(f"3 * 4 = {result}")

result = calc.divide(20, 4)
print(f"20 / 4 = {result}")

result = calc.power(2, 3)
print(f"2^3 = {result}")
```

### Advanced Usage

```python
from src.features.calculator import Calculator

calc = Calculator()

total = calc.add(100, 50)
total = calc.multiply(total, 2)
total = calc.subtract(total, 100)
final = calc.divide(total, 4)

print(f"Result: {final}")
```

### Error Handling

```python
from src.features.calculator import Calculator

calc = Calculator()

try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

## Testing

Run all tests:
```bash
pytest
```

Run with coverage report:
```bash
pytest --cov=src --cov-report=html
```

Run only unit tests:
```bash
pytest tests/unit/
```

Run only integration tests:
```bash
pytest tests/integration/
```

## Test Coverage

The project maintains >80% code coverage as configured in `pytest.ini`.

## Documentation

- [API Documentation](docs/API.md) - Detailed API reference for all modules
- [Migration Guide](docs/MIGRATION_GUIDE.md) - Guide for migrating to new versions

## Configuration

The calculator can be configured via `config.yaml`:

```yaml
features:
  calculator:
    enabled: true
    max_precision: 10
    allow_complex_operations: false
```

See `.env.example` for environment variable configuration options.

## Project Structure

```
testrepo/
├── src/
│   ├── __init__.py
│   └── features/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_calculator.py
│   └── integration/
│       ├── __init__.py
│       └── test_calculator_integration.py
├── docs/
│   ├── API.md
│   └── MIGRATION_GUIDE.md
├── config.yaml
├── .env.example
├── requirements.txt
├── pytest.ini
└── README.md
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Ensure tests pass and coverage is maintained
4. Submit a pull request

## License

This project is for testing purposes.

## Version

Current version: 1.0.0
