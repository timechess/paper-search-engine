from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Paper(_message.Message):
    __slots__ = ("title", "abstract", "authors")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ABSTRACT_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    title: str
    abstract: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        title: _Optional[str] = ...,
        abstract: _Optional[str] = ...,
        authors: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class SearchPaperRequest(_message.Message):
    __slots__ = ("query", "num_results")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    NUM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    query: str
    num_results: int
    def __init__(
        self, query: _Optional[str] = ..., num_results: _Optional[int] = ...
    ) -> None: ...

class SearchPaperResponse(_message.Message):
    __slots__ = ("papers",)
    PAPERS_FIELD_NUMBER: _ClassVar[int]
    papers: _containers.RepeatedCompositeFieldContainer[Paper]
    def __init__(
        self, papers: _Optional[_Iterable[_Union[Paper, _Mapping]]] = ...
    ) -> None: ...

class QueryAugmentationRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class QueryAugmentationResponse(_message.Message):
    __slots__ = ("res",)
    RES_FIELD_NUMBER: _ClassVar[int]
    res: str
    def __init__(self, res: _Optional[str] = ...) -> None: ...
