from pydub import AudioSegment
import os

def hide_file_in_mp3(mp3_file_path, file_to_hide):
    # Load the MP3 file
    audio = AudioSegment.from_file(mp3_file_path, format="mp3")

    # Load the file to hide
    with open(file_to_hide, "rb") as file:
        file_content = file.read()

    # Convert the file content into raw audio data
    raw_audio_data = AudioSegment.from_file(file_to_hide, format="raw", frame_rate=44100, channels=2, sample_width=2)

    # Append the raw audio data to the audio segment
    audio_with_hidden_data = audio + raw_audio_data

    # Create an output file path
    output_file_path = os.path.splitext(mp3_file_path)[0] + "_hidden.mp3"

    # Export the modified audio as an MP3 file
    audio_with_hidden_data.export(output_file_path, format="mp3")

    print("File hidden successfully in the MP3 file:", output_file_path)

# Paths to the MP3 file and the file to hide
mp3_file_path = "soft.mp3"
file_to_hide = "test.txt"

# Call the function to hide the file within the MP3 file
hide_file_in_mp3(mp3_file_path, file_to_hide)
