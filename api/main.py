from fastapi import FastAPI,Form
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware 


app=FastAPI()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="luzdomundo1",
    database="mydb",   
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return{"message":"Hello World"}

@app.get("/get_tasks")
def get_tasks():
    cursor=conn.cursor(dictionary=True)
    cursor.execute("select * from todo")
    records=cursor.fetchall()
    return records

@app.post("/add_task")
def add_task(task:str=Form(...)):
    cursor=conn.cursor()
    cursor.execute("insert into todo (task) values (%s)",(task,))
    conn.commit()
    return "Added Sucessfully"


@app.post("/delete_task")
def delete_task(id:str=Form(...)):
    cursor=conn.cursor()
    cursor.execute("delete from todo where id=%s",(id,))
    conn.commit()
    return "Delete Sucessfully"
