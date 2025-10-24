# Titanic Survival Prediction - Random Forest Model

## Competition Overview
This project tackles the classic **Titanic: Machine Learning from Disaster** Kaggle competition, which challenges participants to predict passenger survival on the Titanic using machine learning.

## Model Performance
Final Score: 0.78229** (Top 25% on Kaggle Leaderboard)

This score demonstrates that a well-tuned **classical machine learning model** can achieve competitive results against more complex approaches.

## Key Achievements
- **Score: 0.78229** - Competitive performance using traditional ML
- **Model: Random Forest Classifier** - Robust and interpretable
- **Feature Engineering: Minimal but effective** - Focused on meaningful transformations
- **Training Time: < 30 seconds** - Efficient and scalable

## Model Architecture
```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    min_samples_split=6,
    min_samples_leaf=2,
    max_features='sqrt',
    random_state=42
)
