import pickle
import pandas as pd


# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    
    df = pd.Dataframe([user_input])

    output = model.predict(df)[0]

    #get probabilties for all classes
    probabilty = model.predict_proba(df)[0]
    confidence = max(probabilty)

    class_probs = dict(zip(class_labels,map(lambda p: round(p,4),probabilty)))

    return output{
        "predicted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilties": class_probs
    }