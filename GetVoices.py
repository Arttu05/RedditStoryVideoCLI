from gtts import gTTS
import edge_tts

def old(textToVoice, ouputPath):
    print("Creating mp3 voices")
    try:
        tts = gTTS(textToVoice)
        tts.save(ouputPath)
        return True
    except:
        return False

def GetVoice(textToVoice, savePath, voiceType):
    data = edge_tts.Communicate(textToVoice,voiceType)
    data.save_sync(savePath)

def GetVoiceAndSubtitles(textToVoice, outputPath, voiceType):

    communicate = edge_tts.Communicate(textToVoice, voiceType)
    submaker = edge_tts.SubMaker()
    with open(outputPath, "wb") as file:
        for chunk in communicate.stream_sync():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)

    subtitleList = []
    for sub in submaker.cues:
        subtitleList.append([sub.content,((sub.start.microseconds + (sub.start.seconds * 1000000)) / 1000000),((sub.end.microseconds + (sub.start.seconds * 1000000))/ 1000000)])
    return subtitleList     

def main():
    subList = GetVoiceAndSubtitles("this is a test","./outputs/tekstitys.mp3","en-US-ChristopherNeural")
    input()
if(__name__ == "__main__"):
    main()