import pytest
from src.utils.helpers import safe_eval, format_result

def test_safe_eval():
    assert safe_eval("2+3") == 5
    assert safe_eval("2*3") == 6
    assert safe_eval("6/3") == 2.0
    assert safe_eval("5-3") == 2
    assert safe_eval("invalid_expr") == "Error"

def test_format_result():
    assert format_result(5.0) == "5"
    assert format_result("5.0") == "5"
    assert format_result(5.123) == "5.123"
    assert format_result("Error") == "Error"
