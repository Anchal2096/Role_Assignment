import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import metrics


def model(munged_csv):
    munged_df = pd.read_csv(munged_csv)
    munged_df.drop("Other skills", axis=1, inplace=True)
    munged_df.drop("Application_ID", axis=1, inplace=True)

    Features = munged_df.iloc[:, :-1]
    Target = munged_df["Post Assigned"]

    X_train, X_test, y_train, y_test = train_test_split(Features, Target, test_size=0.8)

    clf = svm.SVC(kernel='linear')  # Linear Kernel

    # Train the model using the training sets
    clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))


# model("F:\Pycharm\Role_Assignment\Dataset\Munged_csv.csv")
