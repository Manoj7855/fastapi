from fastapi import FastAPI


emp=[
    {'id':101,'name':'manoj','place':'chennai'},
    {'id':102,'name':'sam','place':'trichy'}
]


app= FastAPI()

@app.get("/display/{id}")
def viewforpath(id:int):
    for e in emp:
        if e['id']==id:
            return e
        

@app.get("/display")
def viewforquery(id:int):
    for e in emp:
        if e['id']== id:
            return e