import gzip
from typing import Optional

from requests import Session
from requests_futures.sessions import FuturesSession


class Client:
    def __init__(self, native_endpoint: Optional[str] = None, sql_endpoint: Optional[str] = None) -> None:
        if native_endpoint is None and sql_endpoint is None:
            raise AssertionError(
                'at least one of the native and sql endpoints must be provided')

        self.session = Session()
        self.session.headers.update(
            {'Content-Type': 'application/json', 'Content-Encoding': 'gzip', 'Accept-Encoding': 'gzip'})
        self.native_endpoint = native_endpoint
        self.sql_endpoint = sql_endpoint


class AsyncClient(Client):
    def __init__(self, native_endpoint: Optional[str] = None, sql_endpoint: Optional[str] = None) -> None:
        super().__init__(native_endpoint, sql_endpoint)
        self.inner = FuturesSession(session=self.session)


class BlockingClient(Client):
    def __init__(self, native_endpoint: Optional[str] = None, sql_endpoint: Optional[str] = None) -> None:
        super().__init__(native_endpoint, sql_endpoint)
        self.inner = self.session
