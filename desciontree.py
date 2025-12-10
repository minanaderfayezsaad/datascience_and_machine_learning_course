import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import numpy as np
# Load the dataset
df = pd.read_csv("D:/dr wael data science/digital_marketing_campaign_dataset.csv")

# Drop 'CustomerID' since it's just an ID and not useful for prediction
df = df.drop(columns=["CustomerID"])

# Apply one-hot encoding to the categorical columns
categorical_columns = ["Gender", "CampaignChannel", "CampaignType", "AdvertisingPlatform", "AdvertisingTool"]
df_encoded = pd.get_dummies(df, columns=categorical_columns)

# Separate features and label
X = df_encoded.drop(columns=["Conversion"])
y = df_encoded["Conversion"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree classifier
clif = DecisionTreeClassifier(max_depth=5)
clif.fit(X_train, y_train)
# Predict and evaluate
y_pred = clif.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

"""# Optional: Visualize the tree
plt.figure(figsize=(20,10))
plot_tree(clif, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.show()"""


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
clif = DecisionTreeClassifier(max_depth=5)
clif.fit(X, y)
y_pred = clif.predict(X)

# Now confusion matrix on all 8000 rows
cm = confusion_matrix(y, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Conversion", "Conversion"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix (Full Dataset)")
plt.show()
