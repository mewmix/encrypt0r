from pydub import AudioSegment
import os

def retrieve_hidden_file(mp3_file_path, output_file_path):
    # Load the MP3 file
    audio = AudioSegment.from_file(mp3_file_path, format="mp3")

    # Extract the hidden raw audio data
    hidden_raw_audio_data = audio[-len(audio) // 10:]

    # Export the hidden raw audio data as a separate file
    with open(output_file_path, "wb") as file:
        hidden_raw_audio_data.export(file, format="raw")

    print("Hidden file retrieved successfully:", output_file_path)

# Path to the MP3 file and output file path for the retrieved hidden file
mp3_file_path = "soft_hidden.mp3"
output_file_path = "retrieved_file.txt"

# Call the function to retrieve the hidden file from the MP3 file
retrieve_hidden_file(mp3_file_path, output_file_path)
