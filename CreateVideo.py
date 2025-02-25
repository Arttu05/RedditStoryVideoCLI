from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy import ImageClip
from moviepy import vfx
from moviepy.video.fx import FadeOut

from GetVoices import GetVoice, GetVoiceAndSubtitles
#from CreateBanner import GetBannerWithText
from PictureTextCreator import GetPictureWithText
from PIL import Image
import random
import math

generalSpeed = 1.1
bannerPixelLevel = 190

def CreateFinalVideo(videoName, titleText, commentText, gameplayPath):

    print(videoName)

    titlePath = "./temp/title.mp3"
    commentPath = "./temp/comment.mp3"

    GetVoice(titleText,titlePath, "en-US-ChristopherNeural")
    subtitleList = GetVoiceAndSubtitles(commentText,commentPath, "en-US-ChristopherNeural")

    titleAudio = AudioFileClip(titlePath).with_speed_scaled(generalSpeed).with_start(0.1)
    commentAudio = AudioFileClip(commentPath).with_speed_scaled(generalSpeed).with_start(titleAudio.duration + 1)

    compinedAudio = CompositeAudioClip([titleAudio,commentAudio]).with_volume_scaled(1.75)

    gameplayClip = VideoFileClip(gameplayPath)

    gameplayStartSecond = random.randrange(5,math.floor(gameplayClip.duration - (titleAudio.duration + commentAudio.duration + 10)))
    gameplayEndSecond = (gameplayStartSecond + titleAudio.duration + commentAudio.duration + 1)

    gameplayClip = gameplayClip.subclipped(gameplayStartSecond,gameplayEndSecond)
    gameplayClip = gameplayClip.with_audio(compinedAudio)
        
    #Create reddit banner
    GetPictureWithText("./assets/Template.png", bannerPixelLevel, titleText, "./fonts/Arial-BD.ttf", "./temp/redditBanner.png", textWrapValue=34)
    redditBanner = ImageClip("./temp/redditBanner.png").with_duration(titleAudio.duration + 0,5).with_position("center","center").with_start(0)

    #Create "tiktok" subtitles
    print("getting subtitle video")
    subtitleVideo = GetSubtitleVideo(subtitleList,titleAudio.duration + 1).with_position("center","center")

    # Overlay the text clip on the first video clip
    final_video = CompositeVideoClip([gameplayClip,redditBanner,subtitleVideo])
    final_video.write_videofile(videoName)


def GetSubtitleVideo(subtitleList, startTime):
    textClipList = []
    index = 0
    for subtitle in subtitleList:

        subDuration = subtitle[2] - subtitle[1]
        if((index + 1) != len(subtitleList)):
            subDuration = (subtitleList[index + 1][1] - subtitle[1])
        elif(subtitle[1] > subtitle[2]): #for a bug where last subtitles length is negative subtitle[2] - subtitle[1] 
            subDuration = 0.2

        fontSize = 200
        strokeSize = 8

        if len(subtitle[0]) > 6:
            fontSize = 100
            strokeSize = 5

        textClipObj = TextClip(text=subtitle[0],font_size=fontSize, color="white", font="./fonts/Arial-BD.ttf" ,stroke_color="black", stroke_width=strokeSize, size=(1080,600)).with_start(startTime + subtitle[1]+ 0.25).with_duration(subDuration).with_position("center","center")
        textClipObj = textClipObj.with_effects([vfx.Resize(lambda t: MakeTextBiggerOverTime(t)) ])
        textClipList.append(textClipObj)
        index += 1
    
    return CompositeVideoClip(textClipList).with_speed_scaled(generalSpeed)

def MakeTextBiggerOverTime(t):
    return 1 + (t * 0.25)

def main():
    CreateFinalVideo("./outputs/testiNopeus.mp4","this is done with 2.x","this is done with 2.x","./gameplay/x.mp4")

if(__name__ == "__main__"):
    main()