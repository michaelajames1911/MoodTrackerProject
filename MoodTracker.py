# main project
from datetime import datetime
import pandas as pd
import matplotlib as plt
import seaborn as sns
from emotions_dictionary import emotions_dict
from argparse import ArgumentParser

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

class MoodAnalysis:
    def analyze_data(mood_data):
        """
        Analyzes mood trends over time, identifys the mood shifts and computs the mean mood values
        over a specified time interval.
        Attributes:
            mood_data(pd.Dataframe): DataFrame with columns ['date', 'mood'], where 'date' is the timestamp
                                    and 'mood' is the mood label.
            emotions_dict (dict): A Ditionary of moods and their related descriptions
        Returns:
            Final analysis (dict): Dictionary with top weekly moods, mood shifts and most common moods. 
        """
        mood_data = pd.read_csv(file_path, header=None, names = ["date", "mood", "entry"])
        mood_data['date'] = pd.to_datetime(mood_data['date'], format='%m/%d/%y')
        mood_data.sort_values(by = "date", inplace=True)
        mood_data['category'] = mood_data['mood'].apply(MoodAnalysis.get_mood_category)
        mood_data['definition'] = mood_data['mood'].apply(MoodAnalysis.get_mood_definition)
        mood_counts = mood_data.groupby('mood').size().reset_index(name='count')
        mood_data.set_index('date', inplace=True)
        weekly_moods = mood_data.resample('W')['mood'].agg(lambda x: x.mode()[0]).reset_index(name='top_mood')
        merged_data= pd.merge(weekly_moods, mood_counts, left_on='top_mood', right_on ='mood', how = 'left')
        mood_data.reset_index(inplace=True)
        
        total_shifts = (mood_data['mood'] != mood_data['mood'].shift()).sum()
        
        Final_analysis = {"Your total mood shifts": total_shifts,
                          "Your weekly moods": weekly_moods,
                          "Your most common moods": mood_counts.sort_values(by='count', ascending=False).head(3).to_dict(orient="records"),                  
                        }
        
        return Final_analysis
    def get_mood_category(mood):
        for category, moods in emotions_dict.items():
            if mood in moods:
                return category
        else:
            return "Unknown mood"
    def get_mood_definition(mood):
        for moods in emotions_dict.values():
            if mood in moods:
                return moods
        else:
            return "Definition not found for this mood."
        
    def data_visualize(mood_data, merged_data):
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.countplot(x='top_mood', data=merged_data, palette='Set2')
        plt.title("Top Weekly Moods")
        plt.xticks(rotation=45)
        plt.show()

        # Plotting the mood distribution
        plt.figure(figsize=(10, 6))
        sns.barplot(x='mood', y='count', data=mood_data, palette='coolwarm')
        plt.title("Mood Distribution")
        plt.xticks(rotation=45)
        plt.show()

def ArgumentParser():
    parser = ArgumentParser()
    parser.add_argument('date', type=str, help = 'The date of the entry (fromat: MM/DD/YY)')
    parser.add_argument('mood', type=str, help = 'The mood(e.g., happy, sad, excited, etc.)')
    parser.add_argument('entry', type=str, help='A journal entry related to the mood')
    
    args  = parser.parse_args()
    
    return args.date, args.mood, args.entry

if __name__=="__main__":
    date, mood, entry = ArgumentParser()
    print(f"Date: {date}, Mood: {mood}, Entry: {entry}")
    