from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import Chapter, ChapterInfo


def getChapters(language: str = "en") -> List[Chapter]:
    point = ApiPoint(
        url="/chapters",
        output_key="chapters",
        output_type=Chapter,
        optional_args={"language": language},
    )
    return getData(point)


def getChapter(id: int, language: str = "en") -> Chapter:
    point = ApiPoint(
        url="/chapters/{id}",
        output_key="chapter",
        output_type=Chapter,
        required_args={"id": id},
        optional_args={"language": language},
    )
    return getData(point)


def getChapterInfo(id: int, language: str = "en") -> ChapterInfo:
    point = ApiPoint(
        url="/chapters/{id}/info",
        output_key="chapter",
        output_type=ChapterInfo,
        required_args={"id": id},
        optional_args={"language": language},
    )
    return getData(point)
