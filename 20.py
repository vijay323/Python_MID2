"""Q20. Using Scikit-learn, load a sample dataset (e.g., Iris), split it into training and testing sets, 
train a simple Logistic Regression model, and report accuracy."""
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score 
 
def run(): 
    iris = load_iris() 
    X, y = iris.data, iris.target 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, 
stratify=y) 
    clf = LogisticRegression(max_iter=200) 
    clf.fit(X_train, y_train) 
    preds = clf.predict(X_test) 
    acc = accuracy_score(y_test, preds) 
    print(f"Test accuracy: {acc:.4f}") 
 
if __name__ == "__main__": 
    run()
