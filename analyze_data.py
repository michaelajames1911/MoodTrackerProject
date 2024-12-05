import pandas as pd



<<<<<<< HEAD
def analyze_data(mood_data):
=======
def analyze_data(mood_data, emotions_dict):
>>>>>>> origin/main
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
    mood_data['date'] = pd.to_datetime(mood_data['date'])
    mood_data.index('date', inplace=True)
    weekly_moods = mood_data.resample('W')['mood'].apply(lambda x: x.value_counts())
    top_weekly_moods = weekly_moods.groupby(level=0).apply(lambda x: x.idxmax()[0])
    mood_shifts = top_weekly_moods != top_weekly_moods.shift()
    
    mood_counts = mood_data['mood'].value_counts()
    most_common_moods = mood_counts.head(3).index.tolist()
    
    Final_analysis = {"top_weekly_moods": top_weekly_moods,
                      "mood_shifts": mood_shifts.sum(),
                      "most_common_moods": most_common_moods,
                    }
    
    return Final_analysis

# Example Usage
#mood_data = pd.Dataframe({mood_data = pd.DataFrame({
#     "date": ["2024-11-01", "2024-11-02", "2024-11-03", "2024-11-04", ...],
#     "mood": ["happy", "sad", "anxious", "happy", ...]}