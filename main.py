import os
import subprocess
import ffmpeg

# Function to check if a file is a video by its extension
def is_video_file(file):
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.mpeg', '.mpg', '.m4v']
    ext = os.path.splitext(file)[1].lower()
    return ext in video_extensions

# Function to get bitrate of a video file using ffprobe
def get_bitrate(filepath):
    try:
        # Manually specify the path to ffprobe if not in PATH (update path as needed)
        ffprobe_path = r'C:\ffmpeg-2024-10-13-git-e347b4ff31-full_build\bin\ffprobe.exe'
        probe = ffmpeg.probe(filepath, cmd=ffprobe_path)
        
        # If ffmpeg is in PATH, no need for ffprobe_path
        #probe = ffmpeg.probe(filepath)
        bitrate = int(probe['format']['bit_rate'])
        return bitrate
    except Exception as e:
        print(f"Error getting bitrate for {filepath}: {e}")
        return None


# Function to scan folder for video files and list them by bitrate
def scan_folder_for_videos(folder_path):
    video_files = []
    
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if is_video_file(file):
                filepath = os.path.join(root, file)
                bitrate = get_bitrate(filepath)
                if bitrate:
                    video_files.append((file, bitrate, filepath))

    # Sort by bitrate (ascending)
    video_files.sort(key=lambda x: x[1], reverse=True)

    # Print the video files with their bitrates
    if video_files:
        print(f"\n{'Video File':<40} {'Bitrate (bps)':<15} {'Path'}")
        print("=" * 80)
        for file, bitrate, path in video_files:
            print(f"{str(file)[:10]} {str(bitrate/1000)[:10]} {path[:10]}")
    else:
        print("No video files found.")

# Specify the folder path you want to scan
folder_path = r'G:\Media'

# Scan the folder
scan_folder_for_videos(folder_path)
