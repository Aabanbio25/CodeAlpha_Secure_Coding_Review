import os
import sqlite3

# REMEDIATION 1: Retrieve API key from Environment Variables
API_SECRET_KEY = os.getenv("API_SECRET_KEY")


def get_user_data(username):
  conn = sqlite3.connect("users.db")
  cursor = conn.cursor()

  # REMEDIATION 2: Use Parameterized Query to prevent SQL Injection
  query = "SELECT * FROM users WHERE username = ?"
  cursor.execute(query, (username,))
  return cursor.fetchall()