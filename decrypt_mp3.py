from pydub import AudioSegment
import os

def decrypt_file_from_mp3(mp3_file_path, output_file_path):
    # Load the MP3 file
    audio = AudioSegment.from_file(mp3_file_path, format="mp3")

    # Extract the hidden data (last part of the audio)
    hidden_data = audio[-len(audio) // 10:]

    # Export the hidden data as a separate file
    hidden_data.export(output_file_path, format="raw")

    print("File decrypted successfully:", output_file_path)

# Path to the MP3 file and output file path for the decrypted file
mp3_file_path = "soft_hidden.mp3"
output_file_path = "decrypted_file.txt"

# Call the function to decrypt the hidden file from the MP3 file
decrypt_file_from_mp3(mp3_file_path, output_file_path)
