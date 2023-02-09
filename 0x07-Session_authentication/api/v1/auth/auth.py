#!/usr/bin/env python3
"This is a line of text"
from flask import request
from typing import List, TypeVar
import os


class Auth():
    "This is a line of text"
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        "This is a line of text"
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        "This is a line of text"
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        "This is a line of text"
        return None

    def session_cookie(self, request=None):
        "This is a line of text"
        if request:
            return request.cookies.get(os.getenv('SESSION_NAME'))
