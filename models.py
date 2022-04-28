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


class Resource(BaseModel):
    package_id: str
    url: Optional[str]
    description: Optional[str]
    _format: Optional[str]
    _hash: Optional[str]
    name: Optional[str]
    resource_type: Optional[str]
    mimetype: Optional[str]
    mimetype_inner: Optional[str]
    cache_url: Optional[str]
    size: Optional[str]
    created: Optional[str]
    last_modified: Optional[str]
    cache_last_updated: Optional[str]
    upload: Optional[str]
