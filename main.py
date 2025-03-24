from fastapi import FastAPI
from app.routers import documents, qa
from app.database import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(qa.router, prefix="/qa", tags=["Q&A"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management and Q&A API!"}
