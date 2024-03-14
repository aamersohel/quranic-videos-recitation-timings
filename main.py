from datetime import timedelta
import os
import whisper

def transcribe_audio(path):
    model = whisper.load_model("large") # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path, word_timestamps=True, language='ar')
    segments = transcribe['segments']
    file_content = ""

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        # srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        # with open(srtFilename, 'a', encoding='utf-8') as srtFile:
        #     srtFile.write(segment)
        file_content += segment

    return transcribe['text']


srt = transcribe_audio("/Users/aamersohel/KhairulBariyyah/audios/457.mp3")

print(srt)