from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

@dataclass
class Response(Generic[T]):
    success: bool
    status: int
    data: Optional[T] = None
    error: Optional[str] = None