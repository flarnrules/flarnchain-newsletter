import sqlite3
import argparse

def connect_to_database():
    conn = sqlite3.connect('../database/flarnchain_newsletter.db')
    return conn

def fetch_emails(conn, table_name):
    cursor = conn.cursor()
    query = f'SELECT email FROM {table_name}'
    cursor.execute(query)
    emails = [row[0] for row in cursor.fetchall()]
    return emails

def close_connection(conn):
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Send emails from the specified table.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--mailing_list', action='store_true', help='Send emails from mailing_list')
    group.add_argument('--test_list', action='store_true', help='Send emails from test_list')

    args = parser.parse_args() # Parse the arguments first

    if args.mailing_list:
        table_name = 'mailing_list'
    elif args.test_list:
        table_name = 'test_list'
    else:
        print('List not selected, please type --mailing_list OR --test_list at the end of your command to send email')
        sys.exit(1)

    conn = connect_to_database()
    emails = fetch_emails(conn, table_name)
    close_connection(conn)

    return emails

if __name__ == '__main__':
    main()



