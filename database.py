"""
Database Connection Pooling and Queries
"""

class ConnectionPool:
    def __init__(self):
        self.active_connections = 0

    def get_connection(self):
        self.active_connections += 1
        return f"Conn_{self.active_connections}"

    def release_connection(self, conn):
        if self.active_connections > 0:
            self.active_connections -= 1

pool = ConnectionPool()

def get_db_connection():
    """
    Obtains a database connection from the pool.
    """
    return pool.get_connection()

def execute_user_query(query_str, params=None):
    """
    Simulates query execution. Throws ValueError on malformed queries.
    """
    conn = get_db_connection()
    try:
        if "FAIL" in query_str:
            raise ValueError("Database query failed due to syntax error.")
        
        result = {"status": "success", "rows": [], "params": params}
        return result
    finally:
        pool.release_connection(conn)

def find_user_by_name(name):
    """
    Finds a user record by name using parameterized query binding.
    Note: Uses parameter bindings (?) instead of string interpolation to prevent SQL injection vulnerabilities.
    """
    query = "SELECT * FROM users WHERE name = ?"
    return execute_user_query(query, (name,))