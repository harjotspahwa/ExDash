from sklearn.ensemble import RandomForestClassifier

from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_embarked, feature_descriptions
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print('In App')
#     X_train, y_train, X_test, y_test = titanic_embarked()
#     model = RandomForestClassifier(n_estimators=50, max_depth=10).fit(X_train, y_train)

#     explainer = ClassifierExplainer(model, X_test, y_test, 
#                                     cats=['Sex', 'Deck'], 
#                                     descriptions=feature_descriptions,
#                                     labels=['Queenstown', 'Southampton', 'Cherbourg'])

#     db = ExplainerDashboard(explainer)
    print('About to run')
#     db.run(mode="external")
    print('Ran??')
    return "There?"
