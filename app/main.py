from fastapi import FastAPI
from .database import engine, Base
from .routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="1.0.0")
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API version 2.0", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "New healthy version"}
