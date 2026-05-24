import time

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = time.time() - start

        response.headers["X-Process-Time"] = str(duration)

        return response