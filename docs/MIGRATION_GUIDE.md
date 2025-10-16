# Migration Guide

## Migrating to v1.0.0

This guide helps you migrate to the new calculator feature implementation.

### New Features

#### Calculator Module

Version 1.0.0 introduces a new Calculator module with the following operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Power/Exponentiation

### Breaking Changes

**None** - This is the initial release with the calculator feature, so there are no breaking changes from previous versions.

### New Dependencies

The following dependencies have been added:

```
pytest>=7.4.0
pytest-cov>=4.1.0
pyyaml>=6.0
```

To install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration Changes

A new configuration file `config.yaml` has been added with the following structure:

```yaml
app:
  name: "testrepo"
  version: "1.0.0"

features:
  calculator:
    enabled: true
    max_precision: 10
    allow_complex_operations: false
```

You can also use environment variables via the `.env` file. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

### Usage Examples

#### Before (N/A - new feature)

This is a new feature, no migration needed.

#### After (v1.0.0)

```python
from src.features.calculator import Calculator

calc = Calculator()

result = calc.add(10, 20)
print(f"10 + 20 = {result}")

result = calc.divide(100, 4)
print(f"100 / 4 = {result}")

result = calc.power(2, 8)
print(f"2^8 = {result}")
```

### Testing

Run the test suite to ensure everything works correctly:

```bash
pytest
```

To run with coverage:
```bash
pytest --cov=src --cov-report=html
```

### Directory Structure

The new directory structure is:

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

### Rollback Instructions

If you need to rollback to the previous version:

```bash
git checkout main
```

Or to uninstall the calculator feature, simply remove the `src/` directory and associated files.

### Support

For questions or issues, please open an issue in the repository.
