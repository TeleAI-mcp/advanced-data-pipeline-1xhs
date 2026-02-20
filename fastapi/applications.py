"""
FastAPI applications.
"""
from __future__ import annotations

from typing import Any

from fastapi.routing import APIRouter


class FastAPI:
    """
    The main FastAPI class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: list[Any] | None = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: str | None = "/openapi.json",
        openapi_tags: list[dict[str, Any]] | None = None,
        docs_url: str | None = "/docs",
        redoc_url: str | None = "/redoc",
        swagger_ui_oauth2_redirect_url: str | None = None,
        swagger_ui_init_oauth: dict[str, Any] | None = None,
        middleware: list[Any] | None = None,
        exception_handlers: dict[Any, Any] | None = None,
        on_startup: list[Any] | None = None,
        on_shutdown: list[Any] | None = None,
        **extra: Any,
    ) -> None:
        """
        Initialize the FastAPI application.
        """
        self.debug = debug
        self.routes = routes or []
        self.title = title
        self.description = description
        self.version = version
        self.openapi_url = openapi_url
        self.openapi_tags = openapi_tags
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.swagger_ui_oauth2_redirect_url = swagger_ui_oauth2_redirect_url
        self.swagger_ui_init_oauth = swagger_ui_init_oauth
        self.middleware = middleware or []
        self.exception_handlers = exception_handlers or {}
        self.on_startup = on_startup or []
        self.on_shutdown = on_shutdown or []
        self.extra = extra

    def include_router(self, router: APIRouter, *, prefix: str = "", tags: list[str] | None = None) -> None:
        """
        Include an APIRouter in the application.
        """
        self.routes.extend(router.routes)
