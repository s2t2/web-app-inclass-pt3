from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def classifier_model():
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X, y)
    print("CLASSIFIER", clf)
    return clf

if __name__ == "__main__":

    X, y = load_iris(return_X_y=True)

    clf = classifier_model()

    results = clf.predict(X[:2, :])
    print(X[:2, :])
    print("RESULTS", results)
