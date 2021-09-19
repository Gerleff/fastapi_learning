import enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug=True)


class Operator(enum.Enum):
    PLUS = '+'
    MINUS = '-'


class ResponseSchema(BaseModel):
    """Base response model"""
    result: str = '1 + 2 = 4'


@app.get('/{first}/{operator}/{second}', response_model=ResponseSchema)
async def calculate(first: int = 1,
                    operator: Operator = Operator.PLUS.value,
                    second: int = 2):
    """Test method to calculate"""
    expression = f'{first} {operator.value} {second}'
    return {'result': f'{expression} = ' + str(eval(expression)),
            'asd': 'ГЫ'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000)
