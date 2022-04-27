from typing import Optional
from pydantic import BaseModel


class Dataset(BaseModel):
    name: str
    private: bool
    owner_org: str
    title: Optional[str]
    author: Optional[str]
    author_email: Optional[str]
    maintainer: Optional[str]
    maintainer_email: Optional[str]
    license_id: Optional[str]
    notes: Optional[str]
