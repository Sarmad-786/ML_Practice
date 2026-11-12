import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout,
    RandomFlip, RandomRotation, RandomZoom, RandomTranslation
)
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.preprocessing import image
import keras

# ---- 1. Load data ----
# df = pd.read_csv("fruits.csv")
#
# X = df.drop("label", axis=1).values
# y = df["label"].values
#
# X = X.reshape(-1, 32, 32, 3)
# X = X.astype("float32") / 255.0
#
# num_classes = len(np.unique(y))
# y = to_categorical(y, num_classes=num_classes)
#
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )
#
# print("Train Shape", X_train.shape)
# print("Test Shape", X_test.shape)
#
#
# # ---- 2. Model WITHOUT augmentation ----
# model_no_aug = Sequential([
#     Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
#     MaxPooling2D((2, 2)),
#     Conv2D(64, (3, 3), activation="relu"),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(64, activation="relu"),
#     Dropout(0.4),
#     Dense(num_classes, activation="softmax"),
# ])
#
# model_no_aug.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
#
# print("\n===== Training Model WITHOUT Augmentation =====")
# model_no_aug.fit(
#     X_train, y_train,
#     validation_data=(X_test, y_test),
#     epochs=40,
#     batch_size=32,
# )
#
# model_no_aug.save("fruit_cnn_no_aug.keras")
#
#
# # ---- 3. Model WITH augmentation ----
# model_with_aug = Sequential([
#     RandomFlip("horizontal"),
#     RandomRotation(0.2),
#     RandomZoom(0.2),
#     RandomTranslation(0.1, 0.1),
#     Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
#     MaxPooling2D((2, 2)),
#     Conv2D(64, (3, 3), activation="relu"),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(64, activation="relu"),
#     Dropout(0.4),
#     Dense(num_classes, activation="softmax"),
# ])
#
# model_with_aug.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
#
# print("\n===== Training Model WITH Augmentation =====")
# model_with_aug.fit(
#     X_train, y_train,
#     validation_data=(X_test, y_test),
#     epochs=40,
#     batch_size=32,
# )
#
# model_with_aug.save("fruit_cnn_with_aug.keras")
#
#
# # ---- 4. Evaluate both models ----
# print("\n===== Results WITHOUT Augmentation =====")
# loss1, acc1 = model_no_aug.evaluate(X_test, y_test)
# print(f"Test Accuracy: {acc1:.4f} | Test Loss: {loss1:.4f}")
#
# print("\n===== Results WITH Augmentation =====")
# loss2, acc2 = model_with_aug.evaluate(X_test, y_test)
# print(f"Test Accuracy: {acc2:.4f} | Test Loss: {loss2:.4f}")
#
#
# # ---- 5. Confusion matrices for both ----
# y_true = np.argmax(y_test, axis=1)
#
# y_pred_no_aug = np.argmax(model_no_aug.predict(X_test), axis=1)
# y_pred_with_aug = np.argmax(model_with_aug.predict(X_test), axis=1)
#
# cm_no_aug = confusion_matrix(y_true, y_pred_no_aug)
# cm_with_aug = confusion_matrix(y_true, y_pred_with_aug)
#
# print("\nConfusion Matrix - WITHOUT Augmentation:")
# print(cm_no_aug)
# print("\nClassification Report - WITHOUT Augmentation:")
# print(classification_report(y_true, y_pred_no_aug))
#
# print("\nConfusion Matrix - WITH Augmentation:")
# print(cm_with_aug)
# print("\nClassification Report - WITH Augmentation:")
# print(classification_report(y_true, y_pred_with_aug))
#
#
# # ---- 6. Plot both confusion matrices side by side ----
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))
#
# sns.heatmap(cm_no_aug, annot=True, fmt="d", cmap="Blues", ax=axes[0])
# axes[0].set_title(f"Without Augmentation (Acc: {acc1:.2f})")
# axes[0].set_xlabel("Predicted")
# axes[0].set_ylabel("Actual")
#
# sns.heatmap(cm_with_aug, annot=True, fmt="d", cmap="Greens", ax=axes[1])
# axes[1].set_title(f"With Augmentation (Acc: {acc2:.2f})")
# axes[1].set_xlabel("Predicted")
# axes[1].set_ylabel("Actual")
#
# plt.tight_layout()
# plt.savefig("confusion_matrix_comparison.png")
# plt.show()


img_path = r"C:\Users\HCC\Desktop\images5.jpg"

model = keras.models.load_model(r"C:\Users\HCC\PycharmProjects\ML_Learning\fruit_cnn_model.keras")

img = image.load_img(img_path, target_size=(32, 32))  # resize to match training size
img_array = image.img_to_array(img)  # convert to numpy array
img_array = img_array.astype("float32") / 255.0  # normalize (same as training)
img_array = np.expand_dims(img_array, axis=0)  # add batch dimension -> (1, 32, 32, 3)

predictions = model.predict(img_array)  # returns probabilities for each class
predicted_class = np.argmax(predictions)  # index of highest probability
confidence = np.max(predictions)  # confidence of that prediction

print("Raw probabilities:", predictions)
print(f"Predicted Label: {predicted_class}")
print(f"Confidence: {confidence:.4f}")