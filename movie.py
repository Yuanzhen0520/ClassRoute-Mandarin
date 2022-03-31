import moviepy.editor as mp
my_clip = mp.VideoFileClip(r"/Users/zhangyuanzhen/Desktop/classRoute/Force.mp4")
my_clip.audio.write_audiofile(r"my_result.wav")
