from typing import List, Optional, Dict, Tuple
from pydantic import BaseModel


class Pagination(BaseModel):
    per_page: Optional[int] = None
    current_page: Optional[int] = None
    next_page: Optional[int] = None
    total_pages: Optional[int] = None
    total_records: Optional[int] = None


class TranslatedName(BaseModel):
    language_name: Optional[str] = None
    name: Optional[str] = None


class Chapter(BaseModel):
    id: int
    revelation_place: Optional[str] = None
    revelation_order: Optional[int] = None
    bismillah_pre: Optional[bool]
    name_complex: Optional[str] = None
    name_arabic: Optional[str] = None
    verses_count: Optional[int] = None
    pages: List[int] = []
    translated_name: Optional[TranslatedName] = None


class ChapterInfo(BaseModel):
    chapter_id: Optional[int] = None
    text: Optional[str] = None
    short_text: Optional[str] = None
    language_name: Optional[str] = None
    source: Optional[str] = None


class ChapterRecitation(BaseModel):
    id: Optional[int] = None
    chapter_id: Optional[int] = None
    file_size: Optional[int] = None
    format: Optional[str] = None
    total_files: Optional[int] = None
    audio_url: Optional[str] = None


class ChapterReciter(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    arabic_name: Optional[str] = None
    relative_path: Optional[str] = None
    format: Optional[str] = None
    files_size: Optional[int] = None


class Translation(BaseModel):
    resource_id: Optional[int] = None
    resource_name: Optional[str] = None
    id: Optional[int] = None
    text: Optional[str] = None
    verse_id: Optional[int] = None
    language_id: Optional[int] = None
    language_name: Optional[str] = None
    verse_key: Optional[str] = None
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    juz_number: Optional[int] = None
    hizb_number: Optional[int] = None
    rub_number: Optional[int] = None
    page_number: Optional[int] = None


class Info(BaseModel):
    id: Optional[int] = None
    info: Optional[str] = None


class Transliteration(BaseModel):
    text: Optional[str] = None
    language_name: Optional[str] = None


class Word(BaseModel):
    id: Optional[int] = None
    position: Optional[int] = None
    text_uthmani: Optional[str] = None
    text_indopak: Optional[str] = None
    text_imlaei: Optional[str] = None
    verse_key: Optional[str] = None
    page_number: Optional[int] = None
    line_number: Optional[int] = None
    audio_url: Optional[str] = None
    location: Optional[str] = None
    char_type_name: Optional[str] = None
    code_v1: Optional[str] = None
    code_v2: Optional[str] = None
    translation: Optional[Translation] = None
    transliteration: Optional[Transliteration] = None


class Verse(BaseModel):
    id: Optional[int] = None
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    verse_key: Optional[str] = None
    verse_index: Optional[int] = None
    text_uthmani: Optional[str] = None
    text_uthmani_simple: Optional[str] = None
    text_imlaei: Optional[str] = None
    text_imlaei_simple: Optional[str] = None
    text_indopak: Optional[str] = None
    text_uthmani_tajweed: Optional[str] = None
    juz_number: Optional[int] = None
    hizb_number: Optional[int] = None
    rub_number: Optional[int] = None
    sajdah_type: Optional[str] = None
    sajdah_number: Optional[int] = None
    page_number: Optional[int] = None
    v2_page: Optional[int] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    words: Optional[List[Word]] = None
    translations: Optional[List[Translation]] = None


class Tafsir(BaseModel):
    verse_id: Optional[int] = None
    language_id: Optional[int] = None
    text: Optional[str] = None
    language_name: Optional[str] = None
    resource_name: Optional[str] = None
    verse_key: Optional[str] = None
    chapter_id: Optional[int] = None
    verse_number: Optional[int] = None
    juz_number: Optional[int] = None
    hizb_number: Optional[int] = None
    rub_number: Optional[int] = None
    page_number: Optional[int] = None


class AudioFile(BaseModel):
    url: Optional[str] = None
    duration: Optional[int] = None
    format: Optional[str] = None
    segments: Optional[List[Tuple[int, int, int]]] = None


class VerseTiming(BaseModel):
    verse_key: Optional[str] = None
    timestamp_from: Optional[int] = None
    timestamp_to: Optional[int] = None
    duration: Optional[int] = None
    segments: Optional[List[Tuple[int, int, int]]] = None


class QdcAudioFile(BaseModel):
    id: Optional[int] = None
    chapter_id: Optional[int] = None
    file_size: Optional[float] = None
    format: Optional[str] = None
    audio_url: Optional[str] = None
    duration: Optional[int] = None
    verse_timings: Optional[List[VerseTiming]]


class Recitation(BaseModel):
    id: Optional[int] = None
    reciter_name: Optional[str] = None
    style: Optional[str] = None
    translated_name: Optional[TranslatedName]


class RecitationInfo(BaseModel):
    id: Optional[int] = None
    info: Optional[str] = None


class Language(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    native_name: Optional[str] = None
    iso_code: Optional[str] = None
    direction: Optional[str] = None
    translated_names: Optional[List[TranslatedName]]


class MediaContent(BaseModel):
    url: Optional[str] = None
    embed_text: Optional[str] = None
    provider: Optional[str] = None
    author_name: Optional[str] = None


class Juz(BaseModel):
    juz_number: Optional[int] = None
    first_verse_id: Optional[int] = None
    last_verse_id: Optional[int] = None
    verses_count: Optional[int] = None
    verse_mapping: Optional[Dict]


class TranslatedName(BaseModel):
    name: Optional[str] = None
    language_name: Optional[str] = None


class Resource(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    author_name: Optional[str] = None
    slug: Optional[str] = None
    language_name: Optional[str] = None
    translated_name: TranslatedName
