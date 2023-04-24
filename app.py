import moviepy.editor as mp

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    try:
        # Load the MP4 video clip
        video_clip = mp.VideoFileClip(mp4_file_path)
        
        # Extract audio from the video clip
        audio_clip = video_clip.audio
        
        # Save the audio clip as MP3
        audio_clip.write_audiofile(mp3_file_path)
        
        print("MP4 to MP3 conversion completed successfully!")
    except Exception as e:
        print("An error occurred while converting MP4 to MP3:", e)

# Usage example
mp4_file_path = "input.mp4"  # Specify the input MP4 file path
mp3_file_path = "output.mp3"  # Specify the output MP3 file path

convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
