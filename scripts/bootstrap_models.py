import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier

# Minimal toy data for maternal model (5 features)
X_maternal = np.array([
    [25, 70, 5.2, 36.8, 80],
    [38, 95, 7.0, 37.5, 110],
    [19, 65, 4.8, 36.5, 75],
    [32, 85, 6.1, 37.2, 95],
    [42, 100, 7.5, 37.8, 120],
])
y_maternal = np.array([0, 2, 0, 1, 2])  # 0=low,1=medium,2=high risk

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_maternal)
maternal_model = LogisticRegression(max_iter=200).fit(X_scaled, y_maternal)

# Minimal toy data for fetal model (21 features)
X_fetal = np.random.rand(30, 21)
y_fetal = np.random.randint(0, 3, size=30)  # 0=normal,1=suspect,2=pathological
fetal_model = DummyClassifier(strategy="most_frequent").fit(X_fetal, y_fetal)

# Save artifacts
with open("model/scaler_maternal_model.sav", "wb") as f:
    pickle.dump(scaler, f)

with open("model/finalized_maternal_model.sav", "wb") as f:
    pickle.dump(maternal_model, f)

with open("model/fetal_health_classifier.sav", "wb") as f:
    pickle.dump(fetal_model, f)

print("Saved scaler and models to model/ directory.")
