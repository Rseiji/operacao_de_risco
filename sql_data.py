import psycopg2
import pandas as pd


class Postgre:
    def __init__(self):
        self.labsoft, self.labprog = self.get_tables()


    def connect(self):
        connection = psycopg2.connect(user="postgres",
                                      password="friend91",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        return connection, cursor

    def close(self, cursor, conn):
        cursor.close()
        conn.close()

    def get_tables(self):
        conn, cursor = self.connect()
        sql_select1 = 'select * from med_labsoft;'
        cursor.execute(sql_select1)
        table_labsoft1 = pd.DataFrame(cursor.fetchall(),columns=['tempo', 'total', 'iluminacao', 'Sistema Navegacao', 'Sistema Comunicacao', 'ar', 'Mostradores'])
        table_labsoft = table_labsoft1.set_index('tempo')
        sql_select2 = 'select * from med_labprog;'
        cursor.execute(sql_select2)
        table_labprog1 = pd.DataFrame(cursor.fetchall(), columns=['tempo', 'total', 'iluminacao', 'Sistema Comunicacao', 'ar', 'Tela dos bancos'])
        table_labprog =table_labprog1.set_index('tempo')
        self.close(cursor, conn)
        return table_labsoft, table_labprog


if __name__ == '__main__':
    sql = Postgre()

    print(sql.labsoft)
    print(sql.labprog)
