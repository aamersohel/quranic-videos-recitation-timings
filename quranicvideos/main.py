from pprint import pprint

from quranicvideos.utils.quran import getChapter

chapter = getChapter(chapter_number=1, reciter_id=4, translations="131")
pprint(chapter.verses[3].translations)
