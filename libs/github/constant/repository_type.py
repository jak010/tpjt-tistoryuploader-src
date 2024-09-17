from enum import Enum


class RepositoryType(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    @classmethod
    def of(cls, value):
        if value == cls.PUBLIC.value:
            return RepositoryType.PUBLIC
        if value == cls.PRIVATE.value:
            return RepositoryType.PRIVATE
