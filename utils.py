from quranicvideos.quran.models import Verse, QdcAudioFile
from quranicvideos.utils.quran import ChapterVerse, Chapter, AudioFile


def get_static_chapter(chapter_dict, audio_file_dict):
    verses = []
    verses_dict_list = chapter_dict.get("verses")
    file = QdcAudioFile(**(audio_file_dict.get("audio_files")[0]))

    result_file = AudioFile(
        id=file.id,
        chapter_id=file.chapter_id,
        file_size=file.file_size,
        format=file.format,
        audio_url=file.audio_url,
        duration=file.duration,
    )

    for i, verse_dict in enumerate(verses_dict_list):
        verse = ChapterVerse(
            **(Verse(**verse_dict)).model_dump(), timing=file.verse_timings[i]
        )
        verses.append(verse)

    return Chapter(audio_file=result_file, verses=verses)
