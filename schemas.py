from pydantic import BaseModel

class DocumentBase(BaseModel):
    name: str
    content: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int

    class Config:
        from_attributes = True
