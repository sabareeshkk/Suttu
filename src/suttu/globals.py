from contextvars import ContextVar
from werkzeug.local import LocalProxy


_no_req_msg = """\
This typically means that you attempted to use functionality that needed
an active HTTP request.\
"""

_request_var = ContextVar("suttu.request")
request = LocalProxy(  # type: ignore[assignment]
    _request_var, unbound_message=_no_req_msg
)
