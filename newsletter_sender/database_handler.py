import sqlite3

def connect_to_database():
    conn = sqlite3.connect('../database/flarnchain_newsletter.db')
    return conn

def fetch_emails(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM mailing_list')
    emails = [row[0] for row in cursor.fetchall()]
    return emails

def close_connection(conn):
    conn.close()
