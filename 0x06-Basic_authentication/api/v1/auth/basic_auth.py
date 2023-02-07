#!/usr/bin/env python3
"This is a line of text"
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    "This is a line of text"
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        "This is a line of text"
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')
        if header[0] == "Basic":
            return header[1]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        "This is a line of text"
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            thebase = base64_authorization_header.encode("utf-8")
            message = base64.b64decode(thebase)
            return message.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        "This is a line of text"
        if not decoded_base64_authorization_header:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        lst = decoded_base64_authorization_header.split(':', 1)
        if lst:
            return (lst[0], lst[1])
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar("User"):
        "This is a line of text"
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        if user and user[0].is_valid_password(user_pwd):
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        "This is a line of text"
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        decode_header = self.decode_base64_authorization_header(base64_header)
        u = self.extract_user_credentials(decode_header)
        return self.user_object_from_credentials(u[0], u[1])
