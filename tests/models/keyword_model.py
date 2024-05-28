from typing import List, Optional
from pydantic import BaseModel


class KeywordModel(BaseModel):
    total: int
    objectIDs: Optional[List[int]]
