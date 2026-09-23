"""Request-scoped runtime settings for web/API calls."""

from __future__ import annotations

import os
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Iterator


_finmind_token: ContextVar[str | None] = ContextVar("finmind_token", default=None)


def get_finmind_token() -> str:
    """Return the request token when present, otherwise the server token."""
    request_token = _finmind_token.get()
    if request_token is not None:
        return request_token
    return os.environ.get("FINMIND_TOKEN", "")


@contextmanager
def use_finmind_token(token: str | None) -> Iterator[None]:
    """Temporarily use a token for one request without persisting it."""
    clean = token.strip() if token else None
    marker = _finmind_token.set(clean or None)
    try:
        yield
    finally:
        _finmind_token.reset(marker)
