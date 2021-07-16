from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Christian'}} 

@app.get('/about')
def about():
    return {'data': {'about': 'Page About'}} 