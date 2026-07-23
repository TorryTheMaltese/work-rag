from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    filename: str


class DocumentRead(BaseModel):
    id: int
    filename: str

    model_config = ConfigDict(from_attributes=True)