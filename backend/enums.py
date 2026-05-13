"""
Common enumerations for the Scholarly application.
"""
from enum import Enum

class ResourceStatus(str, Enum):
    """
    Enum representing the possible status values for a research resource.
    """
    PENDING = "Pending"
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"
