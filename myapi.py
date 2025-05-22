from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Existing GET endpoint
@app.get("/hello")
def read_hello(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}

# New POST endpoint
class UserInput(BaseModel):
    name: str
    age: int

@app.post("/greet")
def greet_user(user: UserInput):
    return {"message": f"Hello {user.name}, you are {user.age} years old!"}
