import numpy as np
import random as rd
import time as ti

scales = [
            ['C','D','E','F','G','A','B'],
            ['F','G','A','Bb','C','D','E'],
            ['Bb','C','D','Eb','F','G','A'],
            ['Eb','F','G','Ab','Bb','C','D'],
            ['Ab','Bb','C','Db','Eb','F','G'],
            ['Db','Eb','F','Gb','Ab','Bb','C'],
            ['Gb','Ab','Bb','Cb','Db','Eb','F'],
            ['B','C#','D#','E','F#','G#','A#'],
            ['E','F#','G#','A','B','C#','D#'],
            ['A','B','C#','D','E','F#','G#'],
            ['D','E','F#','G','A','B','C#'],
            ['G','A','B','C','D','E','F#']
          ]


set_of_notes = ['C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G']
interval_names = ['nineth','third','fourth','fifth','sixth','seventh']
intervals = [1,2,3,4,5,6]

random_note_index = rd.randrange(len(set_of_notes))
random_interval_index = rd.randrange(len(intervals))

question_number = 1
score = 0
total_elapsed_time = 0.0

while question_number <= 20:
    random_note_index = rd.randrange(len(set_of_notes))
    random_interval_index = rd.randrange(len(interval_names))
    correct_note = scales[random_note_index][intervals[random_interval_index]]
    
    print ('question ', question_number, ', score ', score)
    print (interval_names[random_interval_index], ' of ',\
          set_of_notes[random_note_index])
    start_time = ti.time()
    answer = input('your answer: ')
    end_time = ti.time()
    elapsed_time = end_time-start_time
    total_elapsed_time += elapsed_time
    if answer == correct_note:
        print ('correct, timing: ', round(elapsed_time, 2))
        score += 1
    else:
        print ('incorrect, correct note is ', correct_note, '; ')
    print ('-------------------------------------------------------------------')
    question_number +=1

print ('your total score is: ', score, '/20')
print ('total elapsed time is:', round(total_elapsed_time, 2) )
    
