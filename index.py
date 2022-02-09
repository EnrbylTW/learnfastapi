from fastapi import FastAPI
from schemas import CreateUser, DeleteUser, UpdateUser
import sqlite3

from users_repository import UsersRepository

# make the database connection with detect_types
connection = sqlite3.connect('users.db')
userRepository = UsersRepository(connection)

app = FastAPI()


@app.get('/')
async def read_users():
    return


@app.post('/')
async def create_user(created_user: CreateUser):
    user = userRepository.add_user(created_user)
    return user


@app.patch('/')
async def edit_user(updated_user: UpdateUser):
    user = userRepository.patch_user(updated_user)
    return user


@app.delete('/')
async def delete_user(deleted_user: DeleteUser):
    user = userRepository.delete_user(deleted_user)
    return user
