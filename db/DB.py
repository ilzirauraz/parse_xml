import sqlite3
from pydantic import BaseModel
import db.migrations as migrations


class DB():

    def create_conn(self):
        return sqlite3.connect('db/sqlite.db')

    def save(self, table_name: str, obj: BaseModel):
        conn = self.create_conn()
        cursor = conn.cursor()
        query = 'INSERT INTO %s %s VALUES %s' % (table_name, tuple(obj.dict().keys()), tuple(obj.dict().values()))
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def run_migrations(self):
        conn = self.create_conn()
        migrations.run(conn)
