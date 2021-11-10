import gzip
from typing import Optional

from requests import Session
from requests_futures.sessions import FuturesSession

class Client:
    def __init__(self, native_endpoint: Optional[str] = None, sql_endpoint: Optional[str] = None) -> None:
        if native_endpoint is None and sql_endpoint is None:
            raise AssertionError('at least one of the native and sql endpoints must be provided')
        
        session = Session()
        session.headers.update({'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Accept-Encoding': 'gzip'})
        self.inner = FuturesSession(session=session)
        self.native_endpoint = native_endpoint
        self.sql_endpoint = sql_endpoint
