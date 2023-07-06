from pydub import AudioSegment
import os

def hide_file_in_wav(wav_file_path, file_to_hide):
    # Load the WAV file
    audio = AudioSegment.from_file(wav_file_path, format="wav")

    # Load the file to hide
    with open(file_to_hide, "rb") as file:
        file_content = file.read()

    # Append the file content to the audio
    audio_with_hidden_data = audio + file_content

    # Create an output file path
    output_file_path = os.path.splitext(wav_file_path)[0] + "_hidden.wav"

    # Export the modified audio as a WAV file
    audio_with_hidden_data.export(output_file_path, format="wav")

    print("File hidden successfully in the WAV file:", output_file_path)

def retrieve_hidden_file(wav_file_path, output_file_path):
    # Load the WAV file with hidden data
    audio_with_hidden_data = AudioSegment.from_file(wav_file_path, format="wav")

    # Retrieve the hidden data from the audio
    hidden_data = audio_with_hidden_data[-len(audio_with_hidden_data):-1]

    # Write the hidden data to the output file
    with open(output_file_path, "wb") as file:
        file.write(hidden_data)

    print("Hidden file retrieved successfully:", output_file_path)

# Paths to the WAV file and the file to hide/retrieve
wav_file_path = "soft.wav"
file_to_hide = "new.txt"
output_file_path = "retrieved_file.txt"

# Call the function to hide the file within the WAV file
hide_file_in_wav(wav_file_path, file_to_hide)

# Call the function to retrieve the hidden file from the
