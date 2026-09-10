"""
Utility Functions for Math and Formatting
"""

def calculate_discount(price, percent):
    """
    Calculates final discounted price.
    """
    discounted_price = price - (price * (percent / 100))
    return discounted_price

def parse_iso_date(timestamp):
    """
    Splits ISO timestamp string into date and time components.
    """
    parts = timestamp.split("T")
    date_part = parts[0]
    time_part = parts[1]
    
    return {
        "date": date_part,
        "time": time_part
    }