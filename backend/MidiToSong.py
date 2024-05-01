import mido

class MiditoSong:
    def __init__(self, temp, nam) -> None:
        self.file = None
        self.midiFile = None
        self.tempo = temp
        self.name = nam+"mid"
    
    def fileName(self, mid):
        self.file = str(mid)
        self.midiFile = mido.MidiFile(self.file)
    
    def note_number_to_name(self, note_number):
        note_names = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        octave = note_number // 12 - 1
        note = note_names[note_number % 12]
        return note + str(octave)
    
    def convertToSong(self):
        self.song = []
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
        return self.song
       

    
song = "mids/give.mid"
mysong = MiditoSong(100, "giveup")

mysong.fileName(song)
print(mysong.convertToSong())
