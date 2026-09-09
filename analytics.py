"""
Analytics and Reporting Metrics
"""

def calculate_metrics(data_list):
    """
    Calculates total sum and integer average of a dataset.
    """
    total = sum(data_list)
    average = total // len(data_list)
    
    return {
        "total": total,
        "average": average
    }

def process_user_ages(age_strings):
    """
    Parses string ages and computes average age metric.
    """
    parsed_ages = [int(a) for a in age_strings]
    avg_age = sum(parsed_ages) / len(parsed_ages) if parsed_ages else 0.0
    
    return {
        "count": len(parsed_ages),
        "average": str(avg_age)
    }