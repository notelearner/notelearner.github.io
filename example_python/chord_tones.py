import random as rd
import sys

major_chords = ['Cmaj7','Fmaj7','Bbmaj7','Ebmaj7','Abmaj7','Dbmaj7','Gbmaj7','Bmaj7','Emaj7','Amaj7','Dmaj7','Gmaj7']
minor_chords = ['Amin7','Dmin7','Gmin7','Cmin7','Fmin7','Bbmin7','Ebmin7','G#min7','C#min7','F#min7','Bmin7','Emin7']
seventh_chords = ['G7','C7','F7','Bb7','Eb7','Ab7','Db7','F#7','B7','E7','A7','D7']
half_dim_chords = ['B-7b5','E-7b5','A-7b5','D-7b5','G-7b5','C-7b5','F-7b5','A#-7b5','D#-7b5','G#-7b5','C#-7b5','F#-7b5']

major_chord_tones = [
                        ['C','E','G','B'],
                        ['F','A','C','E'],
                        ['Bb','D','F','A'],
                        ['Eb','G','Bb','D'],
                        ['Ab','C','Eb','G'],
                        ['Db','F','Ab','C'],
                        ['Gb','Bb','Db','F'],
                        ['B','D#','F#','A#'],
                        ['E','G#','B','D#'],
                        ['A','C#','E','G#'],
                        ['D','F#','A','C#'],
                        ['G','B','D','F#'],
                     ]

minor_chord_tones = [
                        ['A','C','E','G'],
                        ['D','F','A','C'],
                        ['G','Bb','D','F'],
                        ['C','Eb','G','Bb'],
                        ['F','Ab','C','Eb'],
                        ['Bb','Db','F','Ab'],
                        ['Eb','Gb','Bb','Db'],
                        ['G#','B','D#','F#'],
                        ['C#','E','G#','B'],
                        ['F#','A','C#','E'],
                        ['B','D','F#','A'],
                        ['E','G','B','D'],
                     ]

seventh_chord_tones = [
                        ['G','B','D','F'],
                        ['C','E','G','Bb'],
                        ['F','A','C','Eb'],
                        ['Bb','D','F','Ab'],
                        ['Eb','G','Bb','D'],
                        ['Ab','C','Eb','Gb'],
                        ['Db','F','Ab','C'],
                        ['F#','A#','C#','E'],
                        ['B','D#','F#','A'],
                        ['E','G#','B','D'],
                        ['A','C#','E','G'],
                        ['D','F#','A','C'],
                       ]

half_dim_chord_tones = [
                            ['B','D','F','A'],
                            ['E','G','Bb','D'],
                            ['A','C','Eb','G'],
                            ['D','F','Ab','C'],
                            ['G','Bb','Db','F'],
                            ['C','Eb','Gb','Bb'],
                            ['F','Ab','Cb','Eb'],
                            ['A#','C#','E','G#'],
                            ['D#','F#','A','C#'],
                            ['G#','B','D','F#'],
                            ['C#','E','G','B'],
                            ['F#','A','C','E'],
                        ]

chords = major_chords + minor_chords + seventh_chords + half_dim_chords
chord_tones = major_chord_tones + minor_chord_tones + seventh_chord_tones + half_dim_chord_tones

question_number = 1
score = 0
total_elapsed_time = 0.0

wrong_indices = []

while question_number <= 10:
    random_index = rd.randrange(len(chords))
    wrongness = 0
    print('What is ',chords[random_index],'?', sep="")

    tone0 = input('1: ')
    while tone0 != chord_tones[random_index][0]:
        wrongness = 1
        tone0 = input('Wrong, try again: ')

    tone1 = input('3: ')
    while tone1 != chord_tones[random_index][1]:
        wrongness = 1
        tone1 = input('Wrong, try again: ')

    tone2 = input('5: ')
    while tone2 != chord_tones[random_index][2]:
        wrongness = 1
        tone2 = input('Wrong, try again: ')

    tone3 = input('7: ')
    while tone3 != chord_tones[random_index][3]:
        wrongness = 1
        tone3 = input('Wrong, try again: ')

    if wrongness == 1:
        wrong_indices += [random_index]
    question_number += 1
    print('')

print('Wrong chords: ')
for index in wrong_indices:
    print(chords[index])