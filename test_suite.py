"""
Comprehensive Unit Test Suite for GitHub TestBed Modules
"""
import unittest
import asyncio
from config import load_config_env, get_database_url
from auth import validate_password_length, fetch_user_session
from database import execute_user_query, find_user_by_name, pool
from api import parse_user_payload, format_api_response
from analytics import calculate_metrics, process_user_ages
from utils import calculate_discount, parse_iso_date

class TestGitHubTestBed(unittest.TestCase):

    # --- Config Tests ---
    def test_load_config_env(self):
        config = load_config_env()
        self.assertEqual(config["app_env"], "development")

    def test_get_database_url(self):
        try:
            url = get_database_url()
            self.assertIn("5432", url)
        except TypeError:
            self.fail("get_database_url raised TypeError!")

    # --- Auth Tests ---
    def test_validate_password_length(self):
        self.assertTrue(validate_password_length("12345678"))

    def test_fetch_user_session(self):
        result = asyncio.run(fetch_user_session(42))
        self.assertIsInstance(result, dict)

    # --- Database Tests ---
    def test_database_connection_leak(self):
        initial = pool.active_connections
        try:
            execute_user_query("FAIL_QUERY")
        except ValueError:
            pass
        self.assertEqual(pool.active_connections, initial)

    def test_sql_injection_parameterization(self):
        res = find_user_by_name("admin")
        self.assertEqual(res["status"], "success")

    # --- API Tests ---
    def test_parse_user_payload_missing_profile(self):
        payload = {}
        res = parse_user_payload(payload)
        self.assertIsNone(res)

    def test_format_api_response_null(self):
        res = format_api_response(None)
        self.assertEqual(res["status"], 200)

    # --- Analytics Tests ---
    def test_calculate_metrics_empty(self):
        res = calculate_metrics([])
        self.assertEqual(res["total"], 0)

    def test_process_user_ages_type(self):
        res = process_user_ages(["20", "20"])
        self.assertIsInstance(res["average"], (int, float))

    # --- Utils Tests ---
    def test_calculate_discount(self):
        res = calculate_discount(100, 20)
        self.assertEqual(res, 80.0)

    def test_parse_iso_date_date_only(self):
        res = parse_iso_date("2026-09-06")
        self.assertEqual(res["date"], "2026-09-06")

if __name__ == "__main__":
    unittest.main()