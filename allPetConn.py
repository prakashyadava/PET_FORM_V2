import psycopg2
from configuration.config import Config
from Operations.crud import Operations
from log import *
class DBConnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(cls):
        cls.conn  = psycopg2.connect(Config.getCredentials())
        cls.cur = cls.conn.cursor()
        Log.log_connection(True)
    @classmethod
    def create_table(cls):
        cls.cur.execute(Operations.create())
        Log.log_create(True)
    
    @classmethod
    def display_records(cls):
        try:
            cls.cur.execute(Operations.display())
            data  = cls.cur.fetchall()
            Log.log_read(data)
            return data
        except Exception as e:
            print(e)
    @classmethod
    def insert_data(cls,pet_name,pet_owner,pet_breed):
        cls.cur.execute(Operations.insert(pet_name,pet_owner,pet_breed))
        cls.conn.commit()
        Log.log_insert(pet_name,pet_owner,pet_breed)
    @classmethod
    def update_data(cls,pet_id,pet_name,pet_owner,pet_breed):
        cls.cur.execute(Operations.update(pet_id,pet_name,pet_owner,pet_breed))
        cls.conn.commit()
        Log.log_update(pet_id,pet_name,pet_owner,pet_breed)
    @classmethod
    def delete_row(cls,pet_id):  
        cls.cur.execute(Operations.delete(pet_id))
        cls.conn.commit()
        Log.log_delete(pet_id)

    @classmethod
    def close_db(cls):
        cls.conn.close()
        Log.log_close(True)
