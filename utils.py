
from moviepy import VideoFileClip, CompositeVideoClip, AudioClip, AudioFileClip
import os
import random
import string




def cut_main_video(video_path):
    dir_for_cuts = "origin_video_cut/"

    if not os.path.exists(dir_for_cuts):
        os.makedirs(dir_for_cuts)

        
    video_duaration_seconds = 0
    start_value = 0
    count = 0

    origin_video = VideoFileClip(video_path)
    video_duaration_seconds = origin_video.duration

    while start_value < video_duaration_seconds:
        end_video = min(start_value + 60, video_duaration_seconds)
        sub_video = origin_video.subclipped(start_value, end_video)
        random_letters = ''.join(random.sample(string.ascii_lowercase, 3))
        sub_video.write_videofile(f"origin_video_cut/part_{start_value}_{random_letters}.mp4")
        start_value += 60
        count += 1

    return f"{count} videos were compiled"


# print(cut_main_video("videos/Timeline 1.MP4"))


def cut_short_vieo(short_video_path):
    dir_for_shorts_timelines = "short_video_templates/outputs"
    if not os.path.exists(dir_for_shorts_timelines):
        os.makedirs(dir_for_shorts_timelines)

    video_duaration_seconds = 0
    start_value = 0
    count = 0

    origin_video = VideoFileClip(short_video_path).without_audio()
    video_duaration_seconds = origin_video.duration

    while start_value + 60 <= video_duaration_seconds:
        end_video = start_value + 60
        sub_video = origin_video.subclipped(start_value, end_video)
        random_letters = ''.join(random.sample(string.ascii_lowercase, 3))
        sub_video.write_videofile(f"short_video_templates/outputs/short_v_{random_letters}.mp4")

        start_value += 60
        count += 1
        

    return f"{count} videos were compiled"


# print(cut_short_vieo("short_video_templates/ssstik.io_@liberavideo__1746634052742.mp4"))





def create_tik_tok():
    main_timelines_folder = "origin_video_cut"
    short_videos_folder = "short_video_templates/outputs"

    main_timelines_files = os.listdir(main_timelines_folder)
    short_vides_files = os.listdir(short_videos_folder)

    ready_tik_tok_dir = "ready_tik_tok"
    if not os.path.exists(ready_tik_tok_dir):
        os.makedirs(ready_tik_tok_dir)

    try:
        if main_timelines_files and short_vides_files:

            for main_timeline_item in main_timelines_files:
                random_short_vides_file = random.choice(short_vides_files)

                main_timeline_file_path = os.path.join(main_timelines_folder, main_timeline_item)
                short_video_path = os.path.join(short_videos_folder, random_short_vides_file)

                clip_top = VideoFileClip(main_timeline_file_path)
                clip_top_resized = clip_top.resized(height=960)

                clip_bottom = VideoFileClip(short_video_path)
                clip_bottom_resized = clip_bottom.resized(height=960)

                final_clip = CompositeVideoClip([
                    clip_top_resized.with_position(("center", "top")),
                    clip_bottom_resized.with_position(("center", "bottom"))
                ], size=(1080, 1920))

                random_letters = ''.join(random.sample(string.ascii_lowercase, 3))
                final_clip.write_videofile(f"ready_tik_tok/final_video_{random_letters}.mp4", codec="libx264", audio_codec="aac")

                os.remove(main_timeline_file_path)
        else:
            print("main video timelines or short video timelines doesn't exist")

    except Exception as ex:
        print(ex)

    finally:
        print("Create all possible videos")


create_tik_tok()


















