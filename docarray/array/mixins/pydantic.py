from typing import TYPE_CHECKING, Type, List

if TYPE_CHECKING:
    from docarray.document.pydantic_model import PydanticDocumentArray

    from docarray.typing import T
    from pydantic import BaseModel


class PydanticMixin:
    @classmethod
    def get_json_schema(cls, indent: int = 2) -> str:
        """Return a JSON Schema of DocumentArray class."""
        from pydantic import schema_json_of
        from docarray.document.pydantic_model import PydanticDocumentArray

        return schema_json_of(
            PydanticDocumentArray, title='DocumentArray Schema', indent=indent
        )

    def to_pydantic_model(self) -> 'PydanticDocumentArray':
        """Convert a DocumentArray object into a Pydantic model."""
        return [d.to_pydantic_model() for d in self]

    @classmethod
    def from_pydantic_model(cls: Type['T'], model: List['BaseModel']) -> 'T':
        """Convert a list of PydanticDocument into DocumentArray

        :param model: the list of pydantic data model objects that represents a DocumentArray
        :return: a DocumentArray
        """
        from docarray import Document

        return cls(Document.from_pydantic_model(m) for m in model)
