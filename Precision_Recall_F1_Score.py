import numpy as np
from sklearn.metrics import recall_score , precision_score
import matplotlib.pyplot as plt


# The higher the precision, the more confident the model is when it classifies a sample as Positive.
# The higher the recall, the more positive samples the model correctly classified as Positive.
# When a model has high recall but low precision, then the model classifies most of the positive samples correctly but it has many false positives (i.e. classifies many Negative samples as Positive).
# When a model has high precision but low recall, then the model is accurate when it classifies a sample as Positive but it may classify only some of the positive samples.

y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative", "positive", "positive", "positive", "positive", "negative", "negative", "negative"]
pred_scores = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3, 0.7, 0.5, 0.8, 0.2, 0.3, 0.35]

threshold = np.arange(0.2,0.7,0.05)

recall_values = []
precision_values = []
for i in np.arange(len(threshold)):
    recall_values.append(recall_score(y_true, ['positive' if value >= threshold[i] else 'negative' for value in pred_scores],pos_label='positive'))
    precision_values.append(precision_score(y_true, ['positive' if value >= threshold[i] else 'negative' for value in pred_scores],pos_label='positive'))

plt.plot(recall_values ,precision_values)
plt.xlabel('Recall values')
plt.ylabel('Precision Values')
plt.title("Precision Recall Curve")
plt.show()

# Get F1 Score
f1_score = (2*(np.array(precision_values) * np.array(recall_values))) / ((np.array(precision_values) + np.array(recall_values)))
print(f1_score) # [0.72 ,0.69565217 ,0.69565217 ,0.7,0.73684211, 0.82352941,0.82352941, 0.8,0.71428571 ,0.61538462]

plt.plot(f1_score)
plt.title('F1_Score')
plt.show()

# Here F1 is maximum at 6th position so take precision and recall value at 6th position
plt.plot(recall_values ,precision_values)
plt.scatter(recall_values[5], precision_values[5], color = 'red')
plt.xlabel('Recall values at different threshold')
plt.ylabel('Precision Values at different threshold')
plt.title("Precision Recall Curve with F1 point")
plt.show()