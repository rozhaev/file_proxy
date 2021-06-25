from pydantic.main import BaseModel


class AudioInformationSerializer(BaseModel):
    uri: str
    name: str
    content_type: str
    content_length: int
