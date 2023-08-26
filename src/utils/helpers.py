def safe_eval(expr):
    """
    Safely evaluates a mathematical expression.
    
    Args:
    - expr (str): The mathematical expression to evaluate.

    Returns:
    - float: The result of the evaluation.
    """
    try:
        return eval(expr)
    except Exception:
        return "Error"

def format_result(value):
    """
    Formats the result to remove trailing zeros if it's a float.
    
    Args:
    - value (float/str): The value to format.

    Returns:
    - str: The formatted value.
    """
    try:
        float_val = float(value)
        if float_val.is_integer():
            return str(int(float_val))
        return str(float_val)
    except:
        return str(value)

