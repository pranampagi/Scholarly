"""
Pydantic schemas for the Scholarly application.
Used for data validation, serialization, and API documentation.
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional
from .enums import ResourceStatus

class ResourceBase(BaseModel):
    """
    Base schema for a Resource, containing common fields.
    """
    title: str
    link: str
    category: str
    status: ResourceStatus = ResourceStatus.PENDING

class ResourceCreate(ResourceBase):
    """
    Schema for creating a new Resource.
    """
    pass

class ResourceUpdate(BaseModel):
    """
    Schema for updating an existing Resource. All fields are optional.
    """
    title: Optional[str] = None
    link: Optional[str] = None
    category: Optional[str] = None
    status: Optional[ResourceStatus] = None

class Resource(ResourceBase):
    """
    Full Resource schema including the database-generated ID.
    Used for reading data from the API.
    """
    id: int
    model_config = ConfigDict(from_attributes=True)
