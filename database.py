# Database connection module
import sqlite3
import hashlib

# TODO: Move to environment variables
DB_PASSWORD = "admin123"
SECRET_KEY = "my-secret-key-12345"

def connect_to_database():
    # Security issue: hardcoded database credentials
    connection = sqlite3.connect("users.db")
    return connection

def authenticate_user(username, password):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    # Security vulnerability: SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    
    # Performance issue: inefficient loop
    users = []
    for i in range(len(result)):
        users.append(result[i])
    
    return len(users) > 0

def hash_password(password):
    # Security issue: weak hashing without salt
    return hashlib.md5(password.encode()).hexdigest()

def create_user(username, password, email):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    hashed_password = hash_password(password)
    
    # Security vulnerability: SQL injection in INSERT
    query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{hashed_password}', '{email}')"
    
    # Quality issue: no error handling
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    # Debug print left in production
    print(f"Created user: {username} with password hash: {hashed_password}")

def get_user_data(user_id):
    conn = connect_to_database()
    cursor = conn.cursor()
    
    # Another SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id={user_id}"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    
    # Quality issue: bare except
    try:
        return process_user_data(result)
    except:
        return None

def process_user_data(data):
    # Performance issue: unnecessary computation
    processed = []
    for item in data:
        for i in range(1000):  # Wasteful loop
            temp = item * i
        processed.append(item)
    
    return processed