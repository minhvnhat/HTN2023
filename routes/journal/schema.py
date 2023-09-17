
from dataclasses import dataclass
from datetime import datetime

@dataclass
class JournalResponse():
    uid: int
    date: datetime
    prompt: str
    message: str