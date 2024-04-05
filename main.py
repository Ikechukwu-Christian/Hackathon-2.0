from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    operation:str
    operand1:float
    operand2:float

    # def __init__(self, operation:str, operand1:float, operandi:float):
    #     self.operation = operation
    #     self.operand1 = operand1
    #     self.operandi = operandi

@app.post("/calculate")
def calculate(operation: Operation):
    if operation.operation == "add":
        result = operation.operand1 + operation.operand2
    elif operation.operation == "subtract":
        result = operation.operand1 - operation.operand2
    elif operation.operation == "multiply":
        result = operation.operand1 * operation.operand2
    elif operation.operation == "divide":
        if operation.operand2 == 0:
            return {"error": "Division by zero is not allowed"}
        result = operation.operand1 / operation.operand2
    else:
        return {"error": "Invalid operation"}

    return {"result": result}


class InterestRequest(BaseModel):
    principal: float = Query(..., gt=0, description="Principal amount")
    rate: float = Query(..., gt=0, description="Rate of interest per year")
    time: int = Query(..., gt=0, description="Time period in years")


class InterestResponse(BaseModel):
    interest: float


@app.get("/interest", response_model=InterestResponse, status_code=200)
def calculate_interest(request: InterestRequest):
    interest = (request.principal * request.rate * request.time) / 100
    return InterestResponse(interest=interest)


# Example request data for the /interest endpoint
example_request_data = {
    "principal": 1000,
    "rate": 5,
    "time": 2
}


class PalindromeRequest(BaseModel):
    text: str = Query(..., description="Text to check for palindrome")


class PalindromeResponse(BaseModel):
    is_palindrome: bool


@app.get("/palindrome", response_model=PalindromeResponse, status_code=200)
def check_palindrome(request: PalindromeRequest):
    clean_text = request.text.lower().replace(" ", "")
    is_palindrome = clean_text == clean_text[::-1]
    return PalindromeResponse(is_palindrome=is_palindrome)


# Example request data for the /palindrome endpoint
example_request_data = {
    "text": "A man, a plan, a canal, Panama"
}






