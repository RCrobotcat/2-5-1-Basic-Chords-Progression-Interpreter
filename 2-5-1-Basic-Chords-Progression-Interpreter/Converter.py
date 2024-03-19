from music21 import environment, stream, harmony, chord, meter
import os


def configure_environment(musescore_path):
    env = environment.Environment()
    env['musicxmlPath'] = musescore_path


def create_chord(chord_name, duration_type='half'):
    ch = harmony.ChordSymbol(chord_name)
    notes = ch.pitches
    notes_up_an_octave = [n.transpose('P8') for n in notes]  # 将每个音高提升一个八度
    chord_notes = chord.Chord(notes_up_an_octave)  # 创建和弦
    chord_notes.duration.type = duration_type
    return chord_notes


def add_chords_to_part(part, chords, time_signature='2/4'):
    part.append(meter.TimeSignature(time_signature))
    for chord_name in chords:
        measure = stream.Measure()
        chord_notes = create_chord(chord_name)
        measure.append(chord_notes)
        part.append(measure)


def detect_the_key_251(key):
    global chord_sequence
    if key == "C major":
        chord_sequence = ['Dm7', 'G7', 'Cmaj7']
    elif key == "Db major":
        chord_sequence = ['E-m7', 'A-7', 'D-maj7']
    elif key == "D major":
        chord_sequence = ['Em7', 'A7', 'Dmaj7']
    elif key == "Eb major":
        chord_sequence = ['Fm7', 'B-7', 'E-maj7']
    elif key == "E major":
        chord_sequence = ['F#m7', 'B7', 'Emaj7']
    elif key == "F major":
        chord_sequence = ['Gm7', 'C7', 'Fmaj7']
    elif key == "F# major":
        chord_sequence = ['G#m7', 'C#7', 'F#maj7']
    elif key == "G major":
        chord_sequence = ['Am7', 'D7', 'Gmaj7']
    elif key == "Ab major":
        chord_sequence = ['B-m7', 'E-7', 'A-maj7']
    elif key == "A major":
        chord_sequence = ['Bm7', 'E7', 'Amaj7']
    elif key == "Bb major":
        chord_sequence = ['Cm7', 'F7', 'B-maj7']
    elif key == "B major":
        chord_sequence = ['C#m7', 'F#7', 'Bmaj7']
    elif key == "C minor":
        chord_sequence = ['Dm7b5', 'G7', 'Cm7']
    elif key == "Db minor":
        chord_sequence = ['E-m7b5', 'A-7', 'D-m7']
    elif key == "D minor":
        chord_sequence = ['Em7b5', 'A7', 'Dm7']
    elif key == "Eb minor":
        chord_sequence = ['Fm7b5', 'B-7', 'E-m7']
    elif key == "E minor":
        chord_sequence = ['F#m7b5', 'B7', 'Em7']
    elif key == "F minor":
        chord_sequence = ['Gm7b5', 'C7', 'Fm7']
    elif key == "F# minor":
        chord_sequence = ['G#m7b5', 'C#7', 'F#m7']
    elif key == "G minor":
        chord_sequence = ['Am7b5', 'D7', 'Gm7']
    elif key == "Ab minor":
        chord_sequence = ['B-m7b5', 'E-7', 'A-m7']
    elif key == "A minor":
        chord_sequence = ['Bm7b5', 'E7', 'Am7']
    elif key == "Bb minor":
        chord_sequence = ['Cm7b5', 'F7', 'B-m7']
    elif key == "B minor":
        chord_sequence = ['C#m7b5', 'F#7', 'Bm7']

    return chord_sequence


def xml_save(selected_directory, key):
    file_name = f"{key.replace(' ', '-')}_chords.xml"
    file_path = os.path.join(selected_directory, file_name)  # 生成完整的文件路径

    chords_sequence = detect_the_key_251(key)
    score_sequence = stream.Score()
    part_sequence = stream.Part()
    add_chords_to_part(part_sequence, chords_sequence)
    score_sequence.append(part_sequence)
    score_sequence.write('musicxml', fp=file_path)  # 使用文件路径而不是目录路径


def midi_save(selected_directory, key):
    file_name = f"{key.replace(' ', '-')}_chords.mid"
    file_path = os.path.join(selected_directory, file_name)  # 生成完整的文件路径

    chords_sequence = detect_the_key_251(key)
    score_sequence = stream.Score()
    part_sequence = stream.Part()
    add_chords_to_part(part_sequence, chords_sequence)
    score_sequence.append(part_sequence)
    score_sequence.write('midi', fp=file_path)  # 使用文件路径而不是目录路径


def GoMuseScore(selected_directory, key):
    configure_environment(f"{selected_directory}" + "/MuseScore4.exe")
    print(f"{selected_directory}" + "/MuseScore4.exe")

    chords_sequence = detect_the_key_251(key)
    score_sequence = stream.Score()
    part_sequence = stream.Part()
    add_chords_to_part(part_sequence, chords_sequence)
    score_sequence.append(part_sequence)

    score_sequence.show()


def main():
    configure_environment("C:\\Program Files\\MuseScore 4\\bin\\MuseScore4.exe")

    # 和弦序列(2-5-1)
    key = input("Please input the key of 2-5-1 sequence: ")
    chords_sequence = detect_the_key_251(key)

    score_sequence = stream.Score()
    part_sequence = stream.Part()

    add_chords_to_part(part_sequence, chords_sequence)
    score_sequence.append(part_sequence)

    score_sequence.show()


if __name__ == '__main__':
    main()
