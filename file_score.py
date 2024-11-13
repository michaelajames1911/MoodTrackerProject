import re
from emotions_dictionary import emotions_dicts

def score_emotion(emotion, emotions_dict, score=0):
    emotion = emotion.lower()

    final = score

    for category, emotions in emotions_dict.items():
        matchedemotions = [e for e in emotions if e == emotion]
        if 'HighEnergy' in category:
            final += 4
        elif 'LowEnergy' in category:
            final += 2
        
        if 'plesant' in category:
            final += 5

        elif 'unplesant' in category:
            final += 2

        return final
