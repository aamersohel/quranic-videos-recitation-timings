from typing import List

from quranicvideos.quran.api.core import ApiPoint, getData
from quranicvideos.quran.models import Juz


def getJuzs() -> List[Juz]:
    point = ApiPoint(url="/juzs", output_key="juzs", output_type=Juz)
    return getData(point)
