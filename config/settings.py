import psycopg2

SECRET_KEY = 'Ti_LbW2UihelqoouQfa7zAYcVQlf61c_lQ0Li4SHe1Q='

def connection_db():
    """Connection driver postgresql"""
    conn = psycopg2.connect(
        host="db",
        port=5432,
        dbname="dbcreditcard",
        user="postgres",
        password="postgres",
        sslmode="disable",
        connect_timeout=5
    )
    conn.autocommit = True
    return conn.cursor()
