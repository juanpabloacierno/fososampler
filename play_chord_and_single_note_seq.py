from synthesizer import Player, Synthesizer, Waveform


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

# Play C major
chord = ["C4", "E4", "G4"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

# You can also specify frequencies to play just intonation
chord = [440.0, 550.0, 660.0]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

# play random chord sequence
chord_sequence = ["C4", "E4", "G4", "C5", "E5", "G5", "C6", "E6", "G6"]
for chord in chord_sequence:
    player.play_wave(synthesizer.generate_chord([chord], 1.5))
