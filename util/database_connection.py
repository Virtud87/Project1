from psycopg2 import connect, OperationalError
import os


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)

# environment variables: PYTHONUNBUFFERED=1;HOST=database-1.ckokj6ajfvpg.us-west-1.rds.amazonaws.com;DB=postgres;
# PASSWORD=Udonlamei31;PORT=5432;USER=Virtud87
