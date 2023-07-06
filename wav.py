import subprocess

def convert_mp3_to_wav(mp3_file_path, output_wav_file_path):
    # FFmpeg command to convert MP3 to WAV
    command = ['ffmpeg', '-i', mp3_file_path, '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', output_wav_file_path]

    # Run the FFmpeg command
    subprocess.run(command, check=True)

    print("MP3 converted to WAV successfully:", output_wav_file_path)

# Paths to the MP3 file and the output WAV file
mp3_file_path = "soft.mp3"
output_wav_file_path = "soft.wav"

# Call the function to convert the MP3 file to WAV
convert_mp3_to_wav(mp3_file_path, output_wav_file_path)
