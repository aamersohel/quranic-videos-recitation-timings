from typing import List, Optional

from quranicvideos.quran.models import Verse, VerseTiming
from quranicvideos.quran.api import verses, quran
from pydantic import BaseModel

import json


chapter_data = """
{
    "1": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Fatihah",
        "versesCount": 7,
        "translatedName": "The Opener",
        "slug": "al-fatihah"
    },
    "2": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Baqarah",
        "versesCount": 286,
        "translatedName": "The Cow",
        "slug": "al-baqarah"
    },
    "3": {
        "revelationPlace": "madinah",
        "transliteratedName": "Ali 'Imran",
        "versesCount": 200,
        "translatedName": "Family of Imran",
        "slug": "ali-imran"
    },
    "4": {
        "revelationPlace": "madinah",
        "transliteratedName": "An-Nisa",
        "versesCount": 176,
        "translatedName": "The Women",
        "slug": "an-nisa"
    },
    "5": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Ma'idah",
        "versesCount": 120,
        "translatedName": "The Table Spread",
        "slug": "al-maidah"
    },
    "6": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-An'am",
        "versesCount": 165,
        "translatedName": "The Cattle",
        "slug": "al-anam"
    },
    "7": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-A'raf",
        "versesCount": 206,
        "translatedName": "The Heights",
        "slug": "al-araf"
    },
    "8": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Anfal",
        "versesCount": 75,
        "translatedName": "The Spoils of War",
        "slug": "al-anfal"
    },
    "9": {
        "revelationPlace": "madinah",
        "transliteratedName": "At-Tawbah",
        "versesCount": 129,
        "translatedName": "The Repentance",
        "slug": "at-tawbah"
    },
    "10": {
        "revelationPlace": "makkah",
        "transliteratedName": "Yunus",
        "versesCount": 109,
        "translatedName": "Jonah",
        "slug": "yunus"
    },
    "11": {
        "revelationPlace": "makkah",
        "transliteratedName": "Hud",
        "versesCount": 123,
        "translatedName": "Hud",
        "slug": "hud"
    },
    "12": {
        "revelationPlace": "makkah",
        "transliteratedName": "Yusuf",
        "versesCount": 111,
        "translatedName": "Joseph",
        "slug": "yusuf"
    },
    "13": {
        "revelationPlace": "madinah",
        "transliteratedName": "Ar-Ra'd",
        "versesCount": 43,
        "translatedName": "The Thunder",
        "slug": "ar-rad"
    },
    "14": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ibrahim",
        "versesCount": 52,
        "translatedName": "Abraham",
        "slug": "ibrahim"
    },
    "15": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Hijr",
        "versesCount": 99,
        "translatedName": "The Rocky Tract",
        "slug": "al-hijr"
    },
    "16": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Nahl",
        "versesCount": 128,
        "translatedName": "The Bee",
        "slug": "an-nahl"
    },
    "17": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Isra",
        "versesCount": 111,
        "translatedName": "The Night Journey",
        "slug": "al-isra"
    },
    "18": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Kahf",
        "versesCount": 110,
        "translatedName": "The Cave",
        "slug": "al-kahf"
    },
    "19": {
        "revelationPlace": "makkah",
        "transliteratedName": "Maryam",
        "versesCount": 98,
        "translatedName": "Mary",
        "slug": "maryam"
    },
    "20": {
        "revelationPlace": "makkah",
        "transliteratedName": "Taha",
        "versesCount": 135,
        "translatedName": "Ta-Ha",
        "slug": "taha"
    },
    "21": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Anbya",
        "versesCount": 112,
        "translatedName": "The Prophets",
        "slug": "al-anbya"
    },
    "22": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Hajj",
        "versesCount": 78,
        "translatedName": "The Pilgrimage",
        "slug": "al-hajj"
    },
    "23": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Mu'minun",
        "versesCount": 118,
        "translatedName": "The Believers",
        "slug": "al-muminun"
    },
    "24": {
        "revelationPlace": "madinah",
        "transliteratedName": "An-Nur",
        "versesCount": 64,
        "translatedName": "The Light",
        "slug": "an-nur"
    },
    "25": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Furqan",
        "versesCount": 77,
        "translatedName": "The Criterion",
        "slug": "al-furqan"
    },
    "26": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ash-Shu'ara",
        "versesCount": 227,
        "translatedName": "The Poets",
        "slug": "ash-shuara"
    },
    "27": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Naml",
        "versesCount": 93,
        "translatedName": "The Ant",
        "slug": "an-naml"
    },
    "28": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qasas",
        "versesCount": 88,
        "translatedName": "The Stories",
        "slug": "al-qasas"
    },
    "29": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-'Ankabut",
        "versesCount": 69,
        "translatedName": "The Spider",
        "slug": "al-ankabut"
    },
    "30": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ar-Rum",
        "versesCount": 60,
        "translatedName": "The Romans",
        "slug": "ar-rum"
    },
    "31": {
        "revelationPlace": "makkah",
        "transliteratedName": "Luqman",
        "versesCount": 34,
        "translatedName": "Luqman",
        "slug": "luqman"
    },
    "32": {
        "revelationPlace": "makkah",
        "transliteratedName": "As-Sajdah",
        "versesCount": 30,
        "translatedName": "The Prostration",
        "slug": "as-sajdah"
    },
    "33": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Ahzab",
        "versesCount": 73,
        "translatedName": "The Combined Forces",
        "slug": "al-ahzab"
    },
    "34": {
        "revelationPlace": "makkah",
        "transliteratedName": "Saba",
        "versesCount": 54,
        "translatedName": "Sheba",
        "slug": "saba"
    },
    "35": {
        "revelationPlace": "makkah",
        "transliteratedName": "Fatir",
        "versesCount": 45,
        "translatedName": "Originator",
        "slug": "fatir"
    },
    "36": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ya-Sin",
        "versesCount": 83,
        "translatedName": "Ya Sin",
        "slug": "ya-sin"
    },
    "37": {
        "revelationPlace": "makkah",
        "transliteratedName": "As-Saffat",
        "versesCount": 182,
        "translatedName": "Those who set the Ranks",
        "slug": "as-saffat"
    },
    "38": {
        "revelationPlace": "makkah",
        "transliteratedName": "Sad",
        "versesCount": 88,
        "translatedName": "The Letter 'Saad'",
        "slug": "sad"
    },
    "39": {
        "revelationPlace": "makkah",
        "transliteratedName": "Az-Zumar",
        "versesCount": 75,
        "translatedName": "The Troops",
        "slug": "az-zumar"
    },
    "40": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ghafir",
        "versesCount": 85,
        "translatedName": "The Forgiver",
        "slug": "ghafir"
    },
    "41": {
        "revelationPlace": "makkah",
        "transliteratedName": "Fussilat",
        "versesCount": 54,
        "translatedName": "Explained in Detail",
        "slug": "fussilat"
    },
    "42": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ash-Shuraa",
        "versesCount": 53,
        "translatedName": "The Consultation",
        "slug": "ash-shuraa"
    },
    "43": {
        "revelationPlace": "makkah",
        "transliteratedName": "Az-Zukhruf",
        "versesCount": 89,
        "translatedName": "The Ornaments of Gold",
        "slug": "az-zukhruf"
    },
    "44": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ad-Dukhan",
        "versesCount": 59,
        "translatedName": "The Smoke",
        "slug": "ad-dukhan"
    },
    "45": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Jathiyah",
        "versesCount": 37,
        "translatedName": "The Crouching",
        "slug": "al-jathiyah"
    },
    "46": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Ahqaf",
        "versesCount": 35,
        "translatedName": "The Wind-Curved Sandhills",
        "slug": "al-ahqaf"
    },
    "47": {
        "revelationPlace": "madinah",
        "transliteratedName": "Muhammad",
        "versesCount": 38,
        "translatedName": "Muhammad",
        "slug": "muhammad"
    },
    "48": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Fath",
        "versesCount": 29,
        "translatedName": "The Victory",
        "slug": "al-fath"
    },
    "49": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Hujurat",
        "versesCount": 18,
        "translatedName": "The Rooms",
        "slug": "al-hujurat"
    },
    "50": {
        "revelationPlace": "makkah",
        "transliteratedName": "Qaf",
        "versesCount": 45,
        "translatedName": "The Letter 'Qaf'",
        "slug": "qaf"
    },
    "51": {
        "revelationPlace": "makkah",
        "transliteratedName": "Adh-Dhariyat",
        "versesCount": 60,
        "translatedName": "The Winnowing Winds",
        "slug": "adh-dhariyat"
    },
    "52": {
        "revelationPlace": "makkah",
        "transliteratedName": "At-Tur",
        "versesCount": 49,
        "translatedName": "The Mount",
        "slug": "at-tur"
    },
    "53": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Najm",
        "versesCount": 62,
        "translatedName": "The Star",
        "slug": "an-najm"
    },
    "54": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qamar",
        "versesCount": 55,
        "translatedName": "The Moon",
        "slug": "al-qamar"
    },
    "55": {
        "revelationPlace": "madinah",
        "transliteratedName": "Ar-Rahman",
        "versesCount": 78,
        "translatedName": "The Beneficent",
        "slug": "ar-rahman"
    },
    "56": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Waqi'ah",
        "versesCount": 96,
        "translatedName": "The Inevitable",
        "slug": "al-waqiah"
    },
    "57": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Hadid",
        "versesCount": 29,
        "translatedName": "The Iron",
        "slug": "al-hadid"
    },
    "58": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Mujadila",
        "versesCount": 22,
        "translatedName": "The Pleading Woman",
        "slug": "al-mujadila"
    },
    "59": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Hashr",
        "versesCount": 24,
        "translatedName": "The Exile",
        "slug": "al-hashr"
    },
    "60": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Mumtahanah",
        "versesCount": 13,
        "translatedName": "She that is to be examined",
        "slug": "al-mumtahanah"
    },
    "61": {
        "revelationPlace": "madinah",
        "transliteratedName": "As-Saf",
        "versesCount": 14,
        "translatedName": "The Ranks",
        "slug": "as-saf"
    },
    "62": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Jumu'ah",
        "versesCount": 11,
        "translatedName": "The Congregation, Friday",
        "slug": "al-jumuah"
    },
    "63": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Munafiqun",
        "versesCount": 11,
        "translatedName": "The Hypocrites",
        "slug": "al-munafiqun"
    },
    "64": {
        "revelationPlace": "madinah",
        "transliteratedName": "At-Taghabun",
        "versesCount": 18,
        "translatedName": "The Mutual Disillusion",
        "slug": "at-taghabun"
    },
    "65": {
        "revelationPlace": "madinah",
        "transliteratedName": "At-Talaq",
        "versesCount": 12,
        "translatedName": "The Divorce",
        "slug": "at-talaq"
    },
    "66": {
        "revelationPlace": "madinah",
        "transliteratedName": "At-Tahrim",
        "versesCount": 12,
        "translatedName": "The Prohibition",
        "slug": "at-tahrim"
    },
    "67": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Mulk",
        "versesCount": 30,
        "translatedName": "The Sovereignty",
        "slug": "al-mulk"
    },
    "68": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qalam",
        "versesCount": 52,
        "translatedName": "The Pen",
        "slug": "al-qalam"
    },
    "69": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Haqqah",
        "versesCount": 52,
        "translatedName": "The Reality",
        "slug": "al-haqqah"
    },
    "70": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Ma'arij",
        "versesCount": 44,
        "translatedName": "The Ascending Stairways",
        "slug": "al-maarij"
    },
    "71": {
        "revelationPlace": "makkah",
        "transliteratedName": "Nuh",
        "versesCount": 28,
        "translatedName": "Noah",
        "slug": "nuh"
    },
    "72": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Jinn",
        "versesCount": 28,
        "translatedName": "The Jinn",
        "slug": "al-jinn"
    },
    "73": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Muzzammil",
        "versesCount": 20,
        "translatedName": "The Enshrouded One",
        "slug": "al-muzzammil"
    },
    "74": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Muddaththir",
        "versesCount": 56,
        "translatedName": "The Cloaked One",
        "slug": "al-muddaththir"
    },
    "75": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qiyamah",
        "versesCount": 40,
        "translatedName": "The Resurrection",
        "slug": "al-qiyamah"
    },
    "76": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Insan",
        "versesCount": 31,
        "translatedName": "The Man",
        "slug": "al-insan"
    },
    "77": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Mursalat",
        "versesCount": 50,
        "translatedName": "The Emissaries",
        "slug": "al-mursalat"
    },
    "78": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Naba",
        "versesCount": 40,
        "translatedName": "The Tidings",
        "slug": "an-naba"
    },
    "79": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Nazi'at",
        "versesCount": 46,
        "translatedName": "Those who drag forth",
        "slug": "an-naziat"
    },
    "80": {
        "revelationPlace": "makkah",
        "transliteratedName": "'Abasa",
        "versesCount": 42,
        "translatedName": "He Frowned",
        "slug": "abasa"
    },
    "81": {
        "revelationPlace": "makkah",
        "transliteratedName": "At-Takwir",
        "versesCount": 29,
        "translatedName": "The Overthrowing",
        "slug": "at-takwir"
    },
    "82": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Infitar",
        "versesCount": 19,
        "translatedName": "The Cleaving",
        "slug": "al-infitar"
    },
    "83": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Mutaffifin",
        "versesCount": 36,
        "translatedName": "The Defrauding",
        "slug": "al-mutaffifin"
    },
    "84": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Inshiqaq",
        "versesCount": 25,
        "translatedName": "The Sundering",
        "slug": "al-inshiqaq"
    },
    "85": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Buruj",
        "versesCount": 22,
        "translatedName": "The Mansions of the Stars",
        "slug": "al-buruj"
    },
    "86": {
        "revelationPlace": "makkah",
        "transliteratedName": "At-Tariq",
        "versesCount": 17,
        "translatedName": "The Nightcommer",
        "slug": "at-tariq"
    },
    "87": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-A'la",
        "versesCount": 19,
        "translatedName": "The Most High",
        "slug": "al-ala"
    },
    "88": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Ghashiyah",
        "versesCount": 26,
        "translatedName": "The Overwhelming",
        "slug": "al-ghashiyah"
    },
    "89": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Fajr",
        "versesCount": 30,
        "translatedName": "The Dawn",
        "slug": "al-fajr"
    },
    "90": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Balad",
        "versesCount": 20,
        "translatedName": "The City",
        "slug": "al-balad"
    },
    "91": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ash-Shams",
        "versesCount": 15,
        "translatedName": "The Sun",
        "slug": "ash-shams"
    },
    "92": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Layl",
        "versesCount": 21,
        "translatedName": "The Night",
        "slug": "al-layl"
    },
    "93": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ad-Duhaa",
        "versesCount": 11,
        "translatedName": "The Morning Hours",
        "slug": "ad-duhaa"
    },
    "94": {
        "revelationPlace": "makkah",
        "transliteratedName": "Ash-Sharh",
        "versesCount": 8,
        "translatedName": "The Relief",
        "slug": "ash-sharh"
    },
    "95": {
        "revelationPlace": "makkah",
        "transliteratedName": "At-Tin",
        "versesCount": 8,
        "translatedName": "The Fig",
        "slug": "at-tin"
    },
    "96": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-'Alaq",
        "versesCount": 19,
        "translatedName": "The Clot",
        "slug": "al-alaq"
    },
    "97": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qadr",
        "versesCount": 5,
        "translatedName": "The Power",
        "slug": "al-qadr"
    },
    "98": {
        "revelationPlace": "madinah",
        "transliteratedName": "Al-Bayyinah",
        "versesCount": 8,
        "translatedName": "The Clear Proof",
        "slug": "al-bayyinah"
    },
    "99": {
        "revelationPlace": "madinah",
        "transliteratedName": "Az-Zalzalah",
        "versesCount": 8,
        "translatedName": "The Earthquake",
        "slug": "az-zalzalah"
    },
    "100": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-'Adiyat",
        "versesCount": 11,
        "translatedName": "The Courser",
        "slug": "al-adiyat"
    },
    "101": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Qari'ah",
        "versesCount": 11,
        "translatedName": "The Calamity",
        "slug": "al-qariah"
    },
    "102": {
        "revelationPlace": "makkah",
        "transliteratedName": "At-Takathur",
        "versesCount": 8,
        "translatedName": "The Rivalry in world increase",
        "slug": "at-takathur"
    },
    "103": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-'Asr",
        "versesCount": 3,
        "translatedName": "The Declining Day",
        "slug": "al-asr"
    },
    "104": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Humazah",
        "versesCount": 9,
        "translatedName": "The Traducer",
        "slug": "al-humazah"
    },
    "105": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Fil",
        "versesCount": 5,
        "translatedName": "The Elephant",
        "slug": "al-fil"
    },
    "106": {
        "revelationPlace": "makkah",
        "transliteratedName": "Quraysh",
        "versesCount": 4,
        "translatedName": "Quraysh",
        "slug": "quraysh"
    },
    "107": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Ma'un",
        "versesCount": 7,
        "translatedName": "The Small kindnesses",
        "slug": "al-maun"
    },
    "108": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Kawthar",
        "versesCount": 3,
        "translatedName": "The Abundance",
        "slug": "al-kawthar"
    },
    "109": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Kafirun",
        "versesCount": 6,
        "translatedName": "The Disbelievers",
        "slug": "al-kafirun"
    },
    "110": {
        "revelationPlace": "madinah",
        "transliteratedName": "An-Nasr",
        "versesCount": 3,
        "translatedName": "The Divine Support",
        "slug": "an-nasr"
    },
    "111": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Masad",
        "versesCount": 5,
        "translatedName": "The Palm Fiber",
        "slug": "al-masad"
    },
    "112": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Ikhlas",
        "versesCount": 4,
        "translatedName": "The Sincerity",
        "slug": "al-ikhlas"
    },
    "113": {
        "revelationPlace": "makkah",
        "transliteratedName": "Al-Falaq",
        "versesCount": 5,
        "translatedName": "The Daybreak",
        "slug": "al-falaq"
    },
    "114": {
        "revelationPlace": "makkah",
        "transliteratedName": "An-Nas",
        "versesCount": 6,
        "translatedName": "Mankind",
        "slug": "an-nas"
    }
}
"""


def get_total_aayaat(surah_number):
    return json.loads(chapter_data).get(str(surah_number)).get("versesCount")


class AudioFile(BaseModel):
    id: Optional[int] = None
    chapter_id: Optional[int] = None
    file_size: Optional[float] = None
    format: Optional[str] = None
    audio_url: Optional[str] = None
    duration: Optional[int] = None


class ChapterVerse(Verse):
    timing: Optional[VerseTiming] = None


class Chapter(BaseModel):
    audio_file: AudioFile
    verses: List[ChapterVerse]


def getChapter(
    chapter_number: int, reciter_id: int, translations: str = None
) -> Chapter:
    all_verses = verses.getByChapter(
        chapter_number,
        words=True,
        translation_fields="resource_name,language_id",
        fields="text_uthmani,chapter_id,hizb_number,text_imlaei_simple,translations",
        translations=translations,
        reciter=reciter_id,
        word_translation_language="en",
        word_fields="verse_key,verse_id,page_number,location,text_uthmani,code_v2,qpc_uthmani_hafs",
    )

    file = quran.getRecitationByChapter(reciter_id, chapter_number)

    result_file = AudioFile(
        id=file.id,
        chapter_id=file.chapter_id,
        file_size=file.file_size,
        format=file.format,
        audio_url=file.audio_url,
        duration=file.duration,
    )

    result_verses: List[ChapterVerse] = []
    for i, verse in enumerate(all_verses):
        result_verses.append(
            ChapterVerse(**verse.model_dump(), timing=file.verse_timings[i])
        )

    return Chapter(audio_file=result_file, verses=result_verses)


def getAayaat(
    chapter_number: int,
    reciter_id: int,
    translations: str = None,
    from_aayah: int = -1,
    to_aayah: int = -1,
) -> Chapter:
    per_page = 10

    if from_aayah == -1:
        from_aayah = 1

    if to_aayah == -1:
        to_aayah = get_total_aayaat(chapter_number)

    from_page = int(from_aayah / per_page)
    to_page = int(to_aayah / per_page)

    all_verses: List[Verse] = []
    for page in range(from_page + 1, to_page + 2):
        page_verses: List[Verse] = verses.getByChapter(
            chapter_number,
            words=True,
            translation_fields="resource_name,language_id",
            fields="text_uthmani,chapter_id,hizb_number,text_imlaei_simple,translations",
            translations=translations,
            reciter=reciter_id,
            page=page,
            per_page=per_page,
            word_translation_language="en",
            word_fields="verse_key,verse_id,page_number,v2_page,location,text_uthmani,code_v2,qpc_uthmani_hafs",
        )

        for verse in page_verses:
            if verse.verse_number >= from_aayah and verse.verse_number <= to_aayah:
                all_verses.append(verse)

    file = quran.getRecitationByChapter(reciter_id, chapter_number)

    result_file = AudioFile(
        id=file.id,
        chapter_id=file.chapter_id,
        file_size=file.file_size,
        format=file.format,
        audio_url=file.audio_url,
        duration=file.duration,
    )

    result_verses: List[ChapterVerse] = []

    for i, verse in enumerate(all_verses):
        result_verses.append(
            ChapterVerse(
                **verse.model_dump(), timing=file.verse_timings[i + from_aayah - 1]
            )
        )

    return Chapter(audio_file=result_file, verses=result_verses)
