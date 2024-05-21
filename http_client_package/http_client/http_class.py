from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

from .exceptions import ValidationError


@dataclass
class Request:
    """
    Represents a request object used to pass parameters to the request function.

    Attributes:
    -----------
        url : str
            The URL to be sent to the request function.
        method : str
            The HTTP method to be used in the API request (e.g., GET, POST, DELETE, UPDATE).
        headers : Dict[str, str]
            The headers to be included in the API request, including the content-type and authorization.
        data : Dict, optional
            The payload to be sent with the request.
        params : Dict, optional
            Query parameters for the request.
        timeout : Optional[int], default=86400
            The timeout (in seconds) for the session.

    Raises:
    -------
        ValidationError:
            If any validation checks fail for the parameters.
    """
    url: str
    method: str
    headers: Dict[str, str]
    json: Dict = None
    data: Dict = None
    params: Dict = None
    timeout: Optional[int] = field(default=86400)

    def __post_init__(self):
        self.validate_url()
        self.validate_timeout()
        self.validate_header()

    def validate_url(self):
        if self.url is None:
            raise ValidationError("URL cannot be None")
        if not self.url.startswith("http"):
            raise ValidationError("Invalid URL format")

    def validate_timeout(self):
        if self.timeout <= 0:
            raise ValidationError("Timeout must be a positive integer")

    def validate_header(self):
        if self.headers is None:
            raise ValidationError("Headers cannot be empty")
        if not isinstance(self.headers, dict):
            raise ValidationError("Headers must be a dictionary.")
        for key, value in self.headers.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise ValidationError("Header keys and values must be strings.")

@dataclass
class Response:
    """
    Represents a response object used to store response from any http call.

    Attributes
    ----------
        status_code: int
            Represents the status code of http response
        data: Optional[Dict]
            The data message in case of succesfull http response
        error: Optional[Dict]
            The error message in case of unsuccesfull http response
        meta: Optional[Dict]
            Raw response
        event_id: Optional[str]
            Request id
    """
    status_code: int
    data: Optional[Dict] = None
    error: Optional[Dict] = None
    meta: Optional[Dict] = None
    event_id: Optional[str] = None

    def __post_init__(self):
        """Raises validation error if both data and error are null"""
        if not self.data and not self.error:
            raise ValidationError("data and error both cannot be null")


class HTTPStatusCodes(Enum):
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 500
    TIMEOUT_ERROR = 408
