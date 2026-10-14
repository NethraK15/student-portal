"""User lookup service."""
def get_user_by_username(conn, username):
    cursor = conn.cursor()
    # Flaw: f-string query formatting vulnerable to SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchone()
