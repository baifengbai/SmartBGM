#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#==========================
#  Name:        Remixer
#  Author:      zr
#  Time:        2017/04/18
#  Desciption:  Remix video with audio to generate final output

# Configurations
REMIXER_TMP_SOUNDTRACK= r"./tmp/soundtrack/"
REMIXER_TMP_OUTFILE= r'./out/'
# put your module level global var here

# Imports
import time
import os, re, threading, unicodedata
from multiprocessing import Process
from moviepy.editor import *
from pydub import AudioSegment
# put your imports here

# Classes
class Remixer:
    def __init__(self, path_to_video, path_to_audio):
        self.timespan_video = []
        self.timespan_audio = []

        self.audioName = path_to_audio
        self.videoName = path_to_video
        self.audio=AudioFileClip(path_to_audio)
        self.video=VideoFileClip(path_to_video)

        self.soundTrackName = time.strftime("%H%M%S", time.localtime())
        self.soundTrackName=self.soundTrackName+'.mp3'
        self.outfileName=time.strftime("%H%M%S", time.localtime())+'.mp4'

        self.writeDownSoundTrack(self.soundTrackName)
        self.soundTrack = AudioSegment.from_file(self.soundTrackName)

    # 得到视频的音轨，并且将这个音轨写下来，文件名自己指定
    # 放在TMP_SOUNDTRACK下，返回的是完整路径
    # 最好用多线程的方式去执行这个函数
    def writeDownSoundTrack(self,fileName):
        fileName= REMIXER_TMP_SOUNDTRACK + fileName
        temp=self.video.audio
        temp.write_audiofile(fileName)
        self.soundTrackName=fileName

    # 作为常用的接口
    # 规则：
    # 音频时间设为T0到end,end-T0=t1,视频时间总时间设为0到t2,视频两个点之间的时间设为T1到T2，T2-T1=t3.
    # 1.if t1>t3，对音频进行操作，从T0到t3+T0的音频,和长度为t3的视频合成，然后t3+T0到end的音频丢弃
    # 2.if t1=t3,直接合成
    # 3.if t1<t3,不妨设t3=n*t1+m(n,m均为整数)，则将歌曲循环n遍，只循环T0到end部分，剩余的m时间，重复步骤1
    # def video_merge(self, cutinTime, cutoutTime, audioTime, audiooutTime=0, mode='overlay'):
    def remix(self):
        audio = AudioSegment.from_file(self.audioName)
        soundtrack = self.soundTrack
        cutinTime=self.timespan_video[0]
        cutoutTime=self.timespan_video[1]
        audioTime=self.timespan_audio[0]
        audiooutTime=self.timespan_audio[1]

        t3 = cutoutTime - cutinTime
        soundtrack_len = soundtrack.__len__() / 1000.0
        t1 = audiooutTime - audioTime

        # 这里是代码部分
        part1 = soundtrack[0:cutinTime * 1000]
        part2 = soundtrack[cutinTime * 1000:cutoutTime * 1000]
        part3 = soundtrack[cutoutTime * 1000:soundtrack_len * 1000]
        # part1.export(out_f='part1.mp3')
        # part2.export(out_f='part2.mp3')
        # part3.export(out_f='part3.mp3')
        final_part2 = None

        # part1=AudioSegment.from_file('part1.mp3')
        # part2=AudioSegment.from_file('part2.mp3')
        # part3=AudioSegment.from_file('part3.mp3')

        # 这里是代码部分
        audio_cut = audio[audioTime * 1000:audiooutTime * 1000]
        # audio_cut.export('audio_cut.mp3')
        # audio_cut=AudioSegment.from_file('audio_cut.mp3')

        # 音频长度小于视频的情况
        if (t1 < t3):
            qutient = t3 / t1
            reminder = t3 % t1

            # debug1 关于for range
            # for i in range(2,3):
            #     print "this is test:{}\n".format(i)
            # 他这个range非常蛋疼。。。默认是小于号，这里只会输出一次

            # debug2
            # 总是会忘记*1000...迷之蛋疼
            # audio_cut[0:reminder].export('audio_cut_reminder.mp3')

            # 这里是代码部分
            # audio_adapter,表示audio的part2对应长度部分的合集
            # audio_cut,表示audio截取出来的长度的合集
            audio_adapter = audio_cut
            for i in range(1, qutient):
                audio_adapter = audio_adapter.append(audio_cut)
            audio_adapter = audio_adapter.append(audio_cut[0:reminder * 1000])

            # debug3
            # audio_adapter.export('audio_adapter.mp3')
            # audio_adapter=AudioSegment.from_file('audio_adapter.mp3')

            final_part2 = part2.overlay(audio_adapter)
            # final_part2.export('final_part2.mp3')

        # 音频长度大于视频的情况
        else:
            print 'else'
            end_point = audioTime + t3
            audio_adapter = audio_cut[audioTime * 1000:end_point * 1000]
            # audio_adapter.export('audio_adapter.mp3')
            final_part2 = part2.overlay(audio_adapter)
            # final_part2.export('final_part2.mp3')

        soundtrack = part1 + final_part2 + part3
        soundtrack.export(self.soundTrackName)
        print 'over_remix_part1'
        self.merge()
        return REMIXER_TMP_OUTFILE + self.outfileName
 
    def merge(self):
        self.video=self.video.without_audio()
        result_audio=AudioFileClip(self.soundTrackName)
        self.video =self.video.set_audio(result_audio)
        self.video.write_videofile(REMIXER_TMP_OUTFILE + self.outfileName)
        print 'over_remix_part2'

# Main Entrance
def main():
    # 1.Construct
    # remixer = Remixer('path_to_video', 'path_to_audio')
    remixer = Remixer('test/cononL.mp4', 'music/Over The Edge.mp3')

    # 2.Configure
    # use whatever data struct suitable to indicate START POINT and LENGTH of the clip to insert to
    # remixer.timespan_video = [100, 300]
    # remixer.timespan_audio = [500, 900]
    remixer.timespan_video = [3, 400]
    remixer.timespan_audio = [5, 150]

    # 3.Call methods
    # path_to_outile_dir = remixer.remix()
    path_to_outfile = remixer.remix()
    print 'outfile tmppath=' + path_to_outfile

if __name__ == '__main__':
    # Run a Module as Main will run the example test routine
    main()
