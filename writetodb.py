# Сначала нужно импортировать переменные conn и cur из файла database.py. Через эти переменные будет идти общение с бд.
from database import conn, cur

# создадим техническое уведомление, которое будем выводить в терминал, когда отработает функция
dataexecuted = 'Данные успешно записаны в базу'

# далее попробуем добавить одного юзера
cur.execute("""INSERT INTO users(userid, fname, lname, gender, usertype)
    VALUES('00001', 'Yuri', 'Borisov', 'male', 'admin');""")
conn.commit()
print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль

# также мы можем сначала создать кортеж с информацией о юзере, а потом загрузить его в бд
# создаем кортеж
newusertodb = ('00002', 'Max', 'Kolygin', 'male', 'admin')
# а теперь добавим юзера в таблицу users
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", newusertodb)
conn.commit()
# В данном случае все значения заменены на '?' и добавлен параметр, содержащий значения, которые нужно добавить.
print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль

# Также мы можем создать переменную с набором кортежей, содержащщих информацию о юзере.
# В таком случае мы сможем добавить в бд сразу несколько юзеров за раз
several_users_to_db = [('00003', 'Имя1', 'Фамилия1', 'male', 'manager'),
                       ('00004', 'Имя2', 'Фамилия2', 'female', 'manager'),
                       ('00005', 'Имя3', 'Фамилия3', 'female', 'manager')]
# А теперь пишем кортеж с данными в БД (используем не execute, а executemany)
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?);", several_users_to_db)
conn.commit()
print(dataexecuted) # когда юзер добавлен, выводим уведомление в консоль
# Также стоит помнить, что способ с ? помогает логически противостоять разным SQL-инъекциям