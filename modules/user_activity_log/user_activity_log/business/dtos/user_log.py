from typing import Dict, Optional

from odmantic import Model

from datetime import datetime


class UserLog(Model):
    data: Optional[Dict[str, str]] = None
    created_by: str
    created_at: Optional[datetime] = datetime.now()
    update_at: Optional[datetime] = datetime.now()
