from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import AudioFile


def getChapterRecitations(id: int) -> List[AudioFile]:
    """Get list of Chapter Recitation for specific reciter

    Parameters
    ----------
    id : int
        Id of reciter for which you want to get the recitations. You can fetch list of all reciters from :func:`~quran.api.chapters.getChapters`

    """
    point = ApiPoint(
        url="/chapter_recitations/{id}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"id": id},
    )
    return getData(point)


def getChapterRecitationsOfChapter(reciter_id: int, chapter_number: int) -> AudioFile:
    point = ApiPoint(
        url="/chapter_recitations/{reciter_id}/{chapter_number}",
        output_key="audio_file",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "chapter_number": chapter_number},
    )
    return getData(point)


def getVersesRecitaionByChapter(
    reciter_id: int, chapter_number: int, fields: str = None
) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_chapter/{chapter_number}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={
            "reciter_id": reciter_id,
            "chapter_number": chapter_number,
            "fields": fields,
        },
    )
    return getData(point)


def getVersesRecitaionByJuz(reciter_id: int, juz_number: int) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_juz/{juz_number}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "juz_number": juz_number},
    )
    return getData(point)


def getVersesRecitaionByPage(reciter_id: int, page_number: int) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_page/{page_number}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "page_number": page_number},
    )
    return getData(point)


def getVersesRecitaionByRub(reciter_id: int, rub_number: int) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_rub/{rub_number}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "rub_number": rub_number},
    )
    return getData(point)


def getVersesRecitaionByHizb(reciter_id: int, hizb_number: int) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_hizb/{hizb_number}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "hizb_number": hizb_number},
    )
    return getData(point)


def getVersesRecitaionByVerseKey(reciter_id: int, verse_key: int) -> List[AudioFile]:
    point = ApiPoint(
        url="/recitations/{reciter_id}/by_ayah/{verse_key}",
        output_key="audio_files",
        output_type=AudioFile,
        required_args={"reciter_id": reciter_id, "verse_key": verse_key},
    )
    return getData(point)
