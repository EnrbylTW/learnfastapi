import datetime


class UsersRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_user(self, user):
        insertQuery = """INSERT INTO users
            ('first_name', 'last_name', 'email', 'phone_number', 'created_at', 'modifided_at', 'deleted_at')
            VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING *;"""

        currentDateTime = datetime.datetime.now()

        # insert the data into table
        user = self.cursor.execute(insertQuery, (user.first_name, user.last_name,
                                                 user.email, user.phone_number,
                                                 currentDateTime, currentDateTime, currentDateTime))
        self.cursor.close()
        self.connection.commit()
        print("Data Inserted Successfully !")
        print(user)

    def delete_user(self, user):
        insertQuery = """DELETE FROM users WHERE email == ?;"""

        # insert the data into table
        user = self.cursor.execute(insertQuery, (user.email,))

        self.cursor.close()
        self.connection.commit()
        print("Data Inserted Successfully !")
        print(user)

    def patch_user(self, user):
        insertQuery = """UPDATE users SET first_name == ?, last_name == ?, phone_number == ? WHERE email == ?;"""

        user = self.cursor.execute(insertQuery, (user.first_name, user.last_name,
                                                 user.phone_number, user.email))

        self.cursor.close()
        self.connection.commit()
        print("Data Inserted Successfully !")
        print(user)
