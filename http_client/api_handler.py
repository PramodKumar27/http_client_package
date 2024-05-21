import aiohttp

from .exceptions import HTTPRequestException
from .http_class import Request


class ApiHandler:
    """
    A class for handling asynchronous HTTP requests using aiohttp.

    Attributes:
    -----------
    SESSION: aiohttp.ClientSession
        The aiohttp client session used for making HTTP requests.
    """
    SESSION = None

    @classmethod
    async def get_session(cls):
        """
        Retrieve the aiohttp client session. If the session doesn't exist, create a new one.

        Returns:
        --------
        aiohttp.ClientSession:
            The aiohttp client session.
        """
        if not cls.SESSION:
            cls.SESSION = aiohttp.ClientSession()
        return cls.SESSION

    @classmethod
    async def close_session(cls):
        """
        Close the aiohttp client session.

        This method should be called when you no longer need to make HTTP requests.

        Raises:
        -------
        aiohttp.ClientConnectorError:
            If an error occurs while closing the session.
        """
        if cls.SESSION:
            await cls.SESSION.close()
            cls.SESSION = None

    async def request(self, req: Request):
        """
        Make an asynchronous HTTP request using aiohttp.

        Args:
        -----
        req (Request): The request object containing details of the HTTP request.

        Returns:
        --------
        aiohttp.ClientResponse:
            The response object representing the response received from the HTTP request.

        Raises:
        -------
        HTTPRequestException:
            If an error occurs while making the request.
        """
        response = None
        request_info = {
            "url": req.url,
            "headers": req.headers,
            "method": req.method,
            "json": req.json,
            "data": req.data,
            "timeout": req.timeout
        }
        try:
            session = await self.get_session()
            response = await session.request(**request_info)

        except Exception:
            raise HTTPRequestException("Encountered error while making request")
        return response
