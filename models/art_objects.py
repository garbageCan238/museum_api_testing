from pydantic import BaseModel, Field


class ArtObjects(BaseModel):
    total: int
    object_ids: list[int] | None = Field(alias='objectIDs')


class ArtObject(BaseModel):
    object_id: int = Field(alias='objectID')
    title: str
    artist_display_name: str = Field(alias='artistDisplayName')
    object_date: str = Field(alias='objectDate')
    object_begin_date: int = Field(alias='objectBeginDate')
    object_end_date: int = Field(alias='objectEndDate')


class SearchResult(ArtObjects):
    pass
