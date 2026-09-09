"""
API Endpoint Payload Processing and Response Formatting
"""

def parse_user_payload(data):
    """
    Extracts user profile settings from incoming JSON payload.
    Uses default settings if profile or settings are missing.
    """
    if data is None:
        data = {}
    profile = data.get("profile") or {}
    settings = profile.get("settings") or {}
    
    theme = settings.get("theme", "light")
    notifications = settings.get("notifications", True)
    
    return {
        "theme": theme,
        "notifications": notifications
    }

def format_api_response(response_data):
    """
    Formats string response data into lowercase standardized JSON output.
    """
    formatted_msg = response_data.lower()
    return {"status": 200, "message": formatted_msg}