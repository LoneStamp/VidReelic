import ffmpeg

def extract_frame(input_video, output_image, time="00:00:10"):
    try:
        ffmpeg.input(input_video, ss=time).output(output_image, vframes=1).run()
        print(f"Frame extracted successfully from {input_video} at {time} to {output_image}")
    except ffmpeg.Error as e:
        print(f"Error during frame extraction: {e}")
        

extract_frame('input_video.mp4', 'frame.png', time="00:01:00") 
