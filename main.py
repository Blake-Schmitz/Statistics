from fastapi import FastAPI
from pydantic import BaseModel
import outliers
import uvicorn


URL = '127.0.0.1'
PORT = 5000

app = FastAPI()

class OutliersRequest(BaseModel):
    data: list


@app.post('/max/')
def maximum(request: OutliersRequest):
    result = outliers.maximum(request.data)
    return {'result': result['result'], 'index': result['index']}

@app.post('/min/')
def minimum(request: OutliersRequest):
    result = outliers.minimum(request.data)
    return {'result': result['result'], 'index': result['index']}

@app.post('/long/')
def long(request: OutliersRequest):
    result = outliers.long(request.data)
    return {'result': result['result'], 'index': result['index']}

@app.post('/short/')
def short(request: OutliersRequest):
    result = outliers.short(request.data)
    return {'result': result['result'], 'index': result['index']}

@app.post('/threshold/')
def threshold(request: OutliersRequest, threshold: float=0):
    result = outliers.threshold(request.data, threshold)
    return {'result': result['result'], 'percent': result['percent']}


if __name__ == '__main__':
    uvicorn.run(app, host = URL, port = PORT)