from peewee import PostgresqlDatabase

from settings import db
db = PostgresqlDatabase(    #класс для подключени БД
    'orm_py_25',
    user= 'aijan',
    password= '1',          # пороль субд
    host='localhost',       #куда соединиться 
    port=5432                # дефолтный цифра(код) для постгрес 

)