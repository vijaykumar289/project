import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load the Dataset
dataset = pd.read_csv('Training_Dataset.csv')

# Step 2: Data Preprocessing
label_encoder = LabelEncoder()

# Convert non-numeric columns to numeric or encode categorical variables
for column in dataset.columns:
    if dataset[column].dtype == 'object':  # Check if the column is categorical
        dataset[column] = label_encoder.fit_transform(dataset[column])

# Assuming the target variable is the last column
X = dataset.iloc[:, :-1]  # Features (all columns except the last one)
y = label_encoder.fit_transform(dataset.iloc[:, -1])  # Target (the last column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 3: Train the Gradient Boosting Classifier
gb_clf = GradientBoostingClassifier(random_state=42)
gb_clf.fit(X_train, y_train)

# Step 4: Make Predictions and Evaluate the Model
y_pred = gb_clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(classification_report(y_test, y_pred))

# Step 5: Save the Model
joblib.dump(gb_clf, 'gradient_boosting_model.pkl')
print("Model saved as 'gradient_boosting_model.pkl'")
