import sqlite3


class DB:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.connection.commit()

    def add_user(self, email, name, surname, age, phone, user_type='client'):
        self.cursor.execute("INSERT INTO user (user_type, email, name, surname, age, phone) VALUES ("
                            + str(user_type) + ", "
                            + str(email) + ", "
                            + str(name) + ", "
                            + str(surname) + ", "
                            + str(age) + ", "
                            + str(phone)
                            + ")")
        self.connection.commit()
        return self.cursor.lastrowid

    def add_master(self, email, name, surname, age, phone, address, spec):
        user_id = self.add_user(email, name, surname, age, phone, user_type='master');
        self.cursor.execute("INSERT INTO master (user_id, address, specialisation) VALUES ("
                            + str(user_id) + ", "
                            + str(address) + ", "
                            + str(spec)
                            + ")")
        self.connection.commit()
        return self.cursor.lastrowid

    def add_event(self, user_id, master_id, time):
        self.cursor.execute("INSERT INTO event (user_id, master_id, time) VALUES ("
                            + str(user_id) + ", "
                            + str(master_id) + ", "
                            + str(time)
                            + ")")
        self.connection.commit()
        return self.cursor.lastrowid

    def edit_user(self, user_id, email, name, surname, age, phone):
        self.cursor.execute("UPDATE user SET "
                            + "email = " + str(email) + ", "
                            + "name = " + str(name) + ", "
                            + "surname = " + str(surname) + ", "
                            + "age = " + str(age) + ", "
                            + "phone = " + str(phone)
                            + "WHERE id = " + str(user_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def edit_master(self, master_id, email, name, surname, age, phone, address, spec):
        self.cursor.execute("SELECT user_id FROM master WHERE id = " + str(master_id))
        user_id = self.cursor.fetchall()
        self.edit_user(user_id, email, name, surname, age, phone)
        self.cursor.execute("UPDATE master SET "
                            + "address = " + str(address) + ", "
                            + "spec = " + str(spec)
                            + "WHERE id = " + str(master_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def edit_event(self, event_id, user_id, master_id, time):
        self.cursor.execute("UPDATE event SET "
                            + "master_id = " + str(master_id) + ", "
                            + "user_id = " + str(user_id) + ", "
                            + "time = " + str(time)
                            + "WHERE id = " + str(event_id))
        self.connection.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM user")
        return self.cursor.fetchall()

    def get_masters(self):
        self.cursor.execute("SELECT * FROM master")
        return self.cursor.fetchall()

    def get_events(self):
        self.cursor.execute("SELECT * FROM event")
        return self.cursor.fetchall()

    def get_user(self, _id):
        self.cursor.execute("SELECT * FROM user WHERE id = " + str(_id))
        return self.cursor.fetchall()[0]

    def get_master(self, _id):
        self.cursor.execute("SELECT * FROM master WHERE id = " + str(_id))
        master = self.cursor.fetchall()[0]
        user = self.get_user(master[0])
        return tuple([master[1], master[2], master[3]]) + user

    def get_event(self, _id):
        self.cursor.execute("SELECT * FROM event WHERE id = " + str(_id))
        return self.cursor.fetchall()[0]

    def del_user(self, _id):
        self.cursor.execute("DELETE FROM user WHERE id = " + str(_id))
        self.connection.commit()

    def del_master(self, _id):
        self.cursor.execute("DELETE FROM master WHERE id = " + str(_id))
        self.connection.commit()

    def del_event(self, _id):
        self.cursor.execute("DELETE FROM event WHERE id = " + str(_id))
        self.connection.commit()
