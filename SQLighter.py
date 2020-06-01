import sqlite3


class DB:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def afk(self, table_name, properties, primary):
        query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
        for key in properties:
            query += key + ' ' + properties[key]
            if primary == key:
                query += ' PRIMARY KEY'
            query += ','
        query += ')'
        print(query)

    def add_user(self, user_type, email, name, surname, age, phone):
        self.cursor.execute("INSERT INTO user (user_type, email, name, surname, age, phone) VALUES ("
                            + user_type + ", "
                            + email + ", "
                            + name + ", "
                            + surname + ", "
                            + age + ", "
                            + phone
                            + ")")
        self.connection.commit()

    def add_master(self, user_id, address, spec):
        self.cursor.execute("INSERT INTO master (user_id, address, specialisation) VALUES ("
                            + user_id + ", "
                            + address + ", "
                            + spec
                            + ")")
        self.connection.commit()

    def add_event(self, user_id, master_id, time):
        self.cursor.execute("INSERT INTO event (user_id, master_id, time) VALUES ("
                            + user_id + ", "
                            + master_id + ", "
                            + time
                            + ")")
        self.connection.commit()

    def edit_user(self, user_type, email, name, surname, age, phone):
        self.cursor.execute("UPDATE user SET user_type = "
                            + user_type + ", "
                            + "email = " + email + ", "
                            + "name = " + name + ", "
                            + "surname = " + surname + ", "
                            + "age = " + age + ", "
                            + "phone = " + phone)
        self.connection.commit()

    def edit_master(self, user_id, address, spec):
        self.cursor.execute("UPDATE master SET user_id = "
                            + user_id + ", "
                            + "address = " + address + ", "
                            + "spec = " + spec)
        self.connection.commit()

    def edit_event(self, user_id, master_id, time):
        self.cursor.execute("UPDATE event SET user_id = "
                            + user_id + ", "
                            + "master_id = " + master_id + ", "
                            + "time = " + time)
        self.connection.commit()

    def get_user(self, _id):
        self.cursor.execute("SELECT * FROM user WHERE id = " + _id)
        self.connection.commit()

    def get_master(self, _id):
        self.cursor.execute("SELECT * FROM master WHERE id = " + _id)
        self.connection.commit()

    def get_event(self, _id):
        self.cursor.execute("SELECT * FROM event WHERE id = " + _id)
        self.connection.commit()

    def del_user(self, _id):
        self.cursor.execute("DELETE FROM user WHERE id = " + _id)
        self.connection.commit()

    def del_master(self, _id):
        self.cursor.execute("DELETE FROM master WHERE id = " + _id)
        self.connection.commit()

    def del_event(self, _id):
        self.cursor.execute("DELETE FROM event WHERE id = " + _id)
        self.connection.commit()
