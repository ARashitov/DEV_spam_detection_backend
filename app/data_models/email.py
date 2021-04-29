from pydantic import BaseModel
from typing import Optional


class Email(BaseModel):
    content: str
    is_spam: Optional[bool] = None
    spam_probability: Optional[float] = None
