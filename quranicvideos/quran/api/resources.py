from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import (
    Recitation,
    RecitationInfo,
    Info,
    Resource,
    Language,
    ChapterReciter,
)


def getRecitations(language: str = "en") -> List[Recitation]:
    point = ApiPoint(
        url="/resources/recitations",
        output_key="recitations",
        output_type=Recitation,
        optional_args={"language": language},
    )
    return getData(point)


def getRecitationInfo(id: int, language: str = "en"):
    point = ApiPoint(
        url="/resources/recitations/{id}/info",
        output_key="info",
        output_type=RecitationInfo,
        required_args={"id": id},
        optional_args={"language": language},
    )
    return getData(point)


def getTranslations(language: str = "en"):
    point = ApiPoint(
        url="/resources/translations",
        output_key="translations",
        output_type=Resource,
        optional_args={"language": language},
    )
    return getData(point)


def getTranslationInfo(id: int, language: str = "en"):
    point = ApiPoint(
        url="/resources/translations/{id}/info",
        output_key="info",
        output_type=Info,
        required_args={"id": id},
        optional_args={"language": language},
    )
    return getData(point)


def getTafsirs(language: str = "en"):
    point = ApiPoint(
        url="/resources/tafsirs",
        output_key="tafsirs",
        output_type=Resource,
        optional_args={"language": language},
    )
    return getData(point)


def getTafsirInfo(id: int, language: str = "en"):
    point = ApiPoint(
        url="/resources/translations/{id}/info",
        output_key="info",
        output_type=Info,
        required_args={"id": id},
        optional_args={"language": language},
    )
    return getData(point)


def getLanguages(language: str = "en"):
    point = ApiPoint(
        url="/resources/languages",
        output_key="languages",
        output_type=Language,
        optional_args={"language": language},
    )
    return getData(point)


def getChapterReciters(language: str = "en"):
    point = ApiPoint(
        url="/resources/chapter_reciters",
        output_key="reciters",
        output_type=ChapterReciter,
        optional_args={"language": language},
    )
    return getData(point)


# def getChapterRecitationsOfChapter(reciter_id: int, chapter_number: int) -> AudioFile:
#     point = ApiPoint(
#         url="/chapter_recitations/{reciter_id}/{chapter_number}",
#         output_key="audio_file",
#         output_type=AudioFile,
#         required_args={"reciter_id": reciter_id, "chapter_number": chapter_number},
#     )
#     return getData(point)
