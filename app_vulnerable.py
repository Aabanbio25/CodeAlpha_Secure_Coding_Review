import sqlite3

# VULNERABILITY 1: Hardcoded API Secret Key
API_SECRET_KEY = "SUPER_SECRET_ADMIN_KEY_12345"


def get_user_data(username):
  conn = sqlite3.connect("users.db")
  cursor = conn.cursor()

  # VULNERABILITY 2: SQL Injection via String Concatenation
  query = f"SELECT * FROM users WHERE username = '{username}'"
  cursor.execute(query)
  return cursor.fetchall()