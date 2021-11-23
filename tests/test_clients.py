import asyncio

from druid_query.client import Client, AsyncClient

def test_client_close():
    with Client(sql_endpoint='some') as client:
        pass
    assert client.inner.is_closed

def test_async_client_close():
    async def _test():
        async with AsyncClient(sql_endpoint='some') as client:
            pass
        assert client.inner.is_closed
    asyncio.run(_test())
