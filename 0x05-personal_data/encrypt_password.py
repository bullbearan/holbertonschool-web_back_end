#!/usr/bin/env python3
"This is a line of text"
import bcrypt


def hash_password(password: str) -> bytes:
    "This is a line of text"
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    "This is a line of text"
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
