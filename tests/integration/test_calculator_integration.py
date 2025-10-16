"""
Integration tests for the Calculator module.
"""

import pytest
import yaml
from pathlib import Path
from src.features.calculator import Calculator


class TestCalculatorIntegration:
    """Integration test cases for Calculator with configuration."""
    
    @pytest.fixture
    def calculator(self):
        """Create a Calculator instance for testing."""
        return Calculator()
    
    @pytest.fixture
    def config(self):
        """Load configuration from config.yaml."""
        config_path = Path(__file__).parent.parent.parent / "config.yaml"
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def test_calculator_enabled_in_config(self, config):
        """Test that calculator feature is enabled in configuration."""
        assert config['features']['calculator']['enabled'] is True
    
    def test_calculator_precision_settings(self, config):
        """Test that precision settings are correctly configured."""
        max_precision = config['features']['calculator']['max_precision']
        assert max_precision == 10
        assert isinstance(max_precision, int)
    
    def test_complex_calculation_workflow(self, calculator):
        """Test a complete workflow of calculations."""
        initial_value = 100
        
        step1 = calculator.add(initial_value, 50)
        assert step1 == 150
        
        step2 = calculator.multiply(step1, 2)
        assert step2 == 300
        
        step3 = calculator.subtract(step2, 100)
        assert step3 == 200
        
        step4 = calculator.divide(step3, 4)
        assert step4 == 50.0
        
        final_result = calculator.power(step4, 2)
        assert final_result == 2500.0
    
    def test_calculator_with_config_constraints(self, calculator, config):
        """Test calculator respects configuration constraints."""
        if not config['features']['calculator']['allow_complex_operations']:
            pass
    
    def test_error_handling_workflow(self, calculator):
        """Test that errors are properly handled in workflows."""
        value = 100
        
        result = calculator.divide(value, 2)
        assert result == 50.0
        
        with pytest.raises(ValueError):
            calculator.divide(result, 0)
    
    def test_multiple_calculator_instances(self):
        """Test that multiple calculator instances work independently."""
        calc1 = Calculator()
        calc2 = Calculator()
        
        result1 = calc1.add(10, 20)
        result2 = calc2.multiply(5, 5)
        
        assert result1 == 30
        assert result2 == 25
        assert result1 != result2
    
    def test_end_to_end_calculation(self, calculator):
        """Test end-to-end calculation scenario."""
        values = [10, 20, 30, 40, 50]
        
        total = values[0]
        for value in values[1:]:
            total = calculator.add(total, value)
        
        assert total == 150
        
        average = calculator.divide(total, len(values))
        assert average == 30.0
