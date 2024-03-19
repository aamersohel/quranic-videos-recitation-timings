from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import Verse, AudioFile, Tafsir, QdcAudioFile


def getScript(name, **kargs) -> List[Verse]:
    point = ApiPoint(
        url="/quran/verses/{}".format(name),
        output_key="verses",
        output_type=Verse,
        optional_args=kargs,
    )
    return getData(point)


def getIndoPakScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "indopak",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


def getUthmaniScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "uthmani",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


def getUthmaniSimpleScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "uthmani_simple",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


def getUthmaniTajweedScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "uthmani_tajweed",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


def getImlaeiScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "imlaei",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


# Need to verify this api
def getImlaeiSimpleScript(
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    return getScript(
        "imlaei_simple",
        {
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )


# Need to confirm
def getAudioFilesByRecitation(
    id: int,
    fields: str = None,
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[AudioFile]:
    point = ApiPoint(
        url="/quran/recitations/{id}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"id": id},
        optional_args={
            "fields": fields,
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )
    return getData(point)


def getTafsir(
    id: int,
    fields: str = None,
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Tafsir]:
    point = ApiPoint(
        url="/quran/tafsirs/{id}",
        output_key="tafsirs",
        output_type=Tafsir,
        required_args={"id": id},
        optional_args={
            "fields": fields,
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )
    return getData(point)


def getV1Codes(
    fields: str = None,
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    point = ApiPoint(
        url="/quran/verses/code_v1",
        output_key="verses",
        output_type=Verse,
        optional_args={
            "fields": fields,
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )
    return getData(point)


def getV2Codes(
    fields: str = None,
    chapter_number: int = None,
    juz_number: int = None,
    page_number: int = None,
    hizb_number: int = None,
    rub_number: int = None,
    verse_key: int = None,
) -> List[Verse]:
    point = ApiPoint(
        url="/quran/verses/code_v2",
        output_key="verses",
        output_type=Verse,
        optional_args={
            "fields": fields,
            "chapter_number": chapter_number,
            "juz_number": juz_number,
            "page_number": page_number,
            "hizb_number": hizb_number,
            "rub_number": rub_number,
            "verse_key": verse_key,
        },
    )
    return getData(point)


def getRecitationByChapter(reciter_id: int, chapter_number: int) -> QdcAudioFile:
    point = ApiPoint(
        url="https://api.qurancdn.com/api/qdc/audio/reciters/{reciter_id}/audio_files",
        required_args={"reciter_id": reciter_id},
        optional_args={
            "chapter": chapter_number,
            "segments": "true",
        },
        output_key="audio_files",
        output_type=QdcAudioFile,
    )
    return getData(point)[0]
