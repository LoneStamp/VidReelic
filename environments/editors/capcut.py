from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

def trim_video(input_file, start_time, end_time):
    video = VideoFileClip(input_file).subclip(start_time, end_time)
    return video

def add_text(video, text, position=("center", "bottom")):
    txt_clip = TextClip(text, fontsize=70, color='white')
    txt_clip = txt_clip.set_position(position).set_duration(video.duration)
    
    video_with_text = CompositeVideoClip([video, txt_clip])
    return video_with_text

def merge_videos(video_files):
    clips = [VideoFileClip(file) for file in video_files]
    final_video = concatenate_videoclips(clips)
    return final_video

def main():
 
    trimmed_video = trim_video("input_video.mp4", 5, 15)

 
    video_with_text = add_text(trimmed_video, "Hello, World!")

   
    video_with_text.write_videofile("output_video.mp4", fps=24)

    
    video_files = ["video1.mp4", "video2.mp4"]
    merged_video = merge_videos(video_files)
    merged_video.write_videofile("merged_video.mp4", fps=24)

if __name__ == "__main__":
    main()
