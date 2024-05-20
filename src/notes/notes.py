import os
import mido
from tqdm import tqdm

# Define the notes and their corresponding MIDI numbers
notes = {
    'C': 0,
    'Db': 1,
    'D': 2,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'Gb': 6,
    'G': 7,
    'Ab': 8,
    'A': 9,
    'Bb': 10,
    'B': 11
}
# Create a MIDI file for each note
for note_name, midi_number in tqdm(notes.items()):
    for octave in range(0, 10):  # MIDI octaves range from 0 to 9
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Add a note. addNote expects the following information:
        pitch = midi_number + (octave) * 12
        if pitch > 127:  # Skip pitches that exceed the MIDI limit
            continue
        duration = 2  # In beats
        track.append(mido.Message('note_on', note=pitch, velocity=64, time=0))
        track.append(mido.Message('note_off', note=pitch, velocity=127, time=int(duration * 480)))  # 480 ticks per beat

        # Write it to disk
        midi_file_name = note_name + str(octave -1) + '.mid'
        mid.save(midi_file_name)