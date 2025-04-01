from moviepy.editor import VideoFileClip


def get_video_length(video_path):
    
    video_clip = VideoFileClip(video_path)
    
   
    duration = video_clip.duration
    
    return duration


video_path = "path_to_your_video.mp4"  


video_length = get_video_length(video_path)
print(f"The video length is: {video_length} seconds")
