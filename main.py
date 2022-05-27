from typing import Union
from fastapi import FastAPI
from all_classes import *

app = FastAPI()



# wiki.com/
@app.get("/")
def read_root():
    return {"Hello": "World"}

#wiki.com/user
@app.get("/user")
def read_user():
    return {"Hello" : "Dima"}

#wiki.com/user/1
@app.get("/user/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    userRepository = UserRepository()
    user = userRepository.find_one_by(by = "user_id", value = user_id)
    return {user.user_name : user.user_email}


@app.get("/create_user/{user_id}/{user_name}/{user_email}")
def read_user(user_id: int, user_name : str, user_email : str):
    userRepository = UserRepository()
    user = User(user_id, user_name, user_email)
    userRepository.add(user)
    return "User Created!!!"

