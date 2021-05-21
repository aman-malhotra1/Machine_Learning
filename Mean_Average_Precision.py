# The average precision (AP) is a way to summarize the precision-recall curve into a single value representing the average of all precisions.
# The AP is calculated according to the next equation. Using a loop that goes through all precisions/recalls, the difference between the current and next recalls
# is calculated and then multiplied by the current precision. In other words, the AP is the weighted sum of precisions at each threshold where the weight is the
# increase in recall.

import numpy as np
from sklearn.metrics import recall_score , precision_score

y_true = ["positive", "negative", "negative", "positive", "positive", "positive", "negative", "positive", "negative", "positive", "positive", "positive", "positive", "negative", "negative", "negative"]
y_predicted = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.4, 0.2, 0.4, 0.3, 0.7, 0.5, 0.8, 0.2, 0.3, 0.35]
threshold =  np.arange(0.2,0.7,0.05)

recall_scores = []
precision_scores = []
for i in np.arange(len(threshold)):
    recall_scores.append(recall_score(y_true,['positive' if (value >= threshold[i]) else 'negative' for value in y_predicted], pos_label='positive'))
    precision_scores.append(precision_score(y_true,['positive' if (value >= threshold[i]) else 'negative' for value in y_predicted], pos_label='positive'))

precision_scores.append(1)
recall_scores.append(0)

precision_scores = np.array(precision_scores)
recall_scores = np.array(recall_scores)

print(precision_scores)
print(recall_scores)
AP = np.sum((recall_scores[:-1] - recall_scores[1:]) * precision_scores[:-1])
print(AP)