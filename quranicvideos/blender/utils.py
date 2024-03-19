import os
import bpy

from enum import Enum
from pathlib import Path
from quranicvideos.utils.quran import getChapter
from wget import download


class AreaType(Enum):
    VIEW_3D = "VIEW_3D"
    SEQUENCE_EDITOR = "SEQUENCE_EDITOR"


def run_as_context(area_type: AreaType, callback, *args, **kargs):
    areas = [
        area for area in bpy.context.window.screen.areas if area.type == area_type.value
    ]

    if len(areas) <= 0:
        raise Exception(
            f"Make sure an Area of type {area_type.value} is open or visible in your screen!"
        )

    with bpy.context.temp_override(
        window=bpy.context.window,
        area=areas[0],
        region=[region for region in areas[0].regions if region.type == "WINDOW"][0],
        screen=bpy.context.window.screen,
    ):
        callback(*args, **kargs)


def get_font_by_chapter(chapter_number) -> str:
    font_path = Path().home().joinpath("KhairulBariyyah/fonts/kingfahad2/ttf")
    return str(font_path.joinpath("p" + chapter_number + ".ttf"))


def download_audio(chapter) -> Path:
    audio_path = Path().home().joinpath("KhairulBariyyah/audios")
    audio_file_name = str(chapter.audio_file.id) + "." + chapter.audio_file.format
    audio_file_path = audio_path.joinpath(audio_file_name)
    if not os.path.isfile(audio_file_path):
        download(url=chapter.audio_file.audio_url, out=str(audio_file_path))
    return audio_file_path


def set_audio(audio_file_path: Path) -> None:
    bpy.ops.sequencer.sound_strip_add(
        filepath=str(audio_file_path),
        directory=str(audio_file_path.parent),
        files=[{"name": audio_file_path.name}],
        frame_start=0,
        channel=1,
        overlap_shuffle_override=True,
    )


def set_surah_in_sequence(chapter_number, reciter_id, translations):
    chapter = getChapter(
        chapter_number=chapter_number, reciter_id=reciter_id, translations=translations
    )

    # Download surah audio and set it in blender
    audio_file = download_audio(chapter)
    set_audio(audio_file)


def set_surah(chapter_number, reciter_id, translations) -> None:
    run_as_context(
        AreaType.SEQUENCE_EDITOR,
        set_surah_in_sequence,
        chapter_number,
        reciter_id,
        translations,
    )
