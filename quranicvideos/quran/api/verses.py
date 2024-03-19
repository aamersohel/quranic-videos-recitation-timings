from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import Verse


def getByChapter(
    id: int,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
    reciter: int = None,
    word_translation_language: str = None,
) -> List[Verse]:
    point = ApiPoint(
        url="https://api.qurancdn.com/api/qdc/verses/by_chapter/{id}",
        output_key="verses",
        output_type=Verse,
        required_args={"id": id},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
            "reciter": reciter,
            "word_translation_language": word_translation_language,
        },
    )
    return getData(point)


def getByPage(
    id: int,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> List[Verse]:
    point = ApiPoint(
        url="/verses/by_page/{id}",
        output_key="verses",
        output_type=Verse,
        required_args={"id": id},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)


def getByJuz(
    id: int,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> List[Verse]:
    point = ApiPoint(
        url="/verses/by_juz/{id}",
        output_key="verses",
        output_type=Verse,
        required_args={"id": id},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)


def getByHizb(
    id: int,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> List[Verse]:
    point = ApiPoint(
        url="/verses/by_hizb/{id}",
        output_key="verses",
        output_type=Verse,
        required_args={"id": id},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)


def getByRub(
    id: int,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> List[Verse]:
    point = ApiPoint(
        url="/verses/by_rub/{id}",
        output_key="verses",
        output_type=Verse,
        required_args={"id": id},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)


def getByKey(
    key: str,
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> Verse:
    point = ApiPoint(
        url="/verses/by_key/{key}",
        output_key="verse",
        output_type=Verse,
        required_args={"key": key},
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)


def getRandom(
    language: str = "en",
    words: bool = True,
    translations: str = None,
    audio: int = None,
    tafsirs: str = None,
    word_fields: str = None,
    translation_fields: str = None,
    fields: str = None,
    page: int = 1,
    per_page: int = 10,
) -> Verse:
    point = ApiPoint(
        url="/verses/random",
        output_key="verse",
        output_type=Verse,
        optional_args={
            "language": language,
            "words": words,
            "translations": translations,
            "audio": audio,
            "tafsirs": tafsirs,
            "word_fields": word_fields,
            "translation_fields": translation_fields,
            "fields": fields,
            "page": page,
            "per_page": per_page,
        },
    )
    return getData(point)
