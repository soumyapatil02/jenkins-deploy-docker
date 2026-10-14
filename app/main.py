from fastapi import FastAPI

app = FastAPI(
title="Employee Management System",
description="Employee management API for a DevOps POC",
version="1.0.0",
)

@app.get("/")
def home():
    return {
        "message": "Employee Management System is running!",
        "status": "success",
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}