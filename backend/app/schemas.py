from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    filename: str


class DocumentRead(BaseModel):
    id: int
    filename: str

    model_config = ConfigDict(from_attributes=True)


class DocumentChunkCreate(BaseModel):
    document_id: int
    chunk_index: int
    chunk_text: str


class DocumentChunkRead(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    chunk_text: str

    model_config = ConfigDict(from_attributes=True)


class ChunkSearchRequest(BaseModel):
    query: str
    limit: int = 3


class ChunkSearchResult(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    chunk_text: str
    distance: float