from datetime import datetime
class MoodTracker:

    allowed_emotions = ["depressed", "happy", "sad", "angry", "annoyed", "anxious", "excited", "scared"]
    range_rating = (1,5)
    def __init__(self):
        self.entries = []

def add_entry(self, emotion, rating):
    """ Validates the mood entry by checking for accetable emotion and rating

      emotion (string): emotion that the user inputs
      rating(int): rating ( on a number scale) that the user inputs 
    
      Returns:
      dict: A dictionary containing the validated mood entry 
    """
    self.emotion = emotion
    self.rating = rating 
    #This will validate emotions, checking if they're in the allowed_emotions group 
    if emotion not in self.allowed_emotions:
        raise ValueError(f"Invalid emotion input")

    #This validates rating by making sure it isn't smaller or bigger than 5 
    if not isinstance(rating,int) or not (self.range_rating[0] <= rating <= self.range_rating[1]):
        raise ValueError(f"Rating score must be between 1 and 5")
    
    #logging the timestamp

    timestamp = datetime.now().isoformat()
    #example entry
    entry = {
        "emotion": emotion,
        "rating": rating,
        "timestamp": timestamp
    }
    
    self.entries.append(entry)
    return entry 