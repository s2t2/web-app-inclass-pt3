
#import pickle

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_FILEPATH = "my_model.pkl"

#def train_and_save_model():
#    classifier =
#    with open(MODEL_FILEPATH, "wb") as model_file:
#        pickle.dump(classifier, file)
#
#def trained_model():
#    MODEL_FILEPATH = "my_model.pkl"
#    with open(MODEL_FILEPATH, "rb") as model_file:
#        model = pickle.load(model_file)


if __name__ == "__main__":
    X, y = load_iris(return_X_y=True)
    print("TRAINING DATA")
    #print(type(X), X.shape) #> <class 'numpy.ndarray'> (150, 4)
    #print(type(y), y.shape) #> <class 'numpy.ndarray'> (150,)

    clf = LogisticRegression().fit(X, y)
    print("CLASSIFIER:", clf)

    inputs = X[:2, :]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)
