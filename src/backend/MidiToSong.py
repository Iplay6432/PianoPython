import mido
import json
from pathlib import Path
from .enums import Note
import io

class MidiToSong:
    def __init__(self, tempo: int, name: str) -> None:
        self.file = None
        self.midiFile = None
        self.tempo = tempo
        self.name = f"{name}"
        self.song = None
    
    def filename(self, mid: str):
        self.file = str("mids/"+mid)
        self.midiFile = mido.MidiFile(self.file)
    
    def note_number_to_name(self, note_number: int) -> str:
        note_names = [note.value for note in Note]
        octave = note_number // 12 - 1
        note = note_names[note_number % 12]
        return f"{note}{octave}"
    
    def convertToSong(self) -> list[tuple[str, int]]:
        self.song: list[tuple[str, int]] = []
        note_start_times = {}
        absolute_time = 0
        for msg in self.midiFile.tracks[0]:
            absolute_time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                note_start_times[msg.note] = absolute_time
            elif (msg.type == 'note_off') or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in note_start_times:
                    note_duration = mido.tick2second(absolute_time - note_start_times[msg.note], 
                                                        self.midiFile.ticks_per_beat, 
                                                        mido.bpm2tempo(self.tempo))  # assuming a tempo of 120 BPM
                    note_name = self.note_number_to_name(msg.note)
                    self.song.append((note_name, note_duration*1000))
                    del note_start_times[msg.note]
        
        with (Path(__file__).parent.parent / f"jsons/{self.name}.json").open("w") as f:
            json.dump(self.song, f, indent=4)  

