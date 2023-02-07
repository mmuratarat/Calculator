from fastapi import FastAPI
from pydantic import BaseModel
from typing import *
from calculator import calculate
from fastapi.responses import JSONResponse

class UserInput(BaseModel):
    x: Union[int, float]
    y: Union[int, float]
    operation: str

app = FastAPI()

@app.post("/calculate", response_class=JSONResponse)
def operation_endpoin(input: UserInput):
    return calculate(x = input.x, y = input.y, operation=input.operation)