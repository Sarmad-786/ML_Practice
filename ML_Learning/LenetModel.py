import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout,
    RandomFlip, RandomRotation, RandomZoom, RandomTranslation,AveragePooling2D
)
from tensorflow.keras.preprocessing import image

import keras
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.python.keras.metrics import acc
#
# df = pd.read_csv("fruits.csv")
#
# X = df.drop("label" ,axis=1).values
# y = df["label"].values
#
# X = X.reshape(-1,32,32,3)
# X = X.astype("float32")/255.0
#
# num_classes = len(np.unique(y))
# y = to_categorical(y, num_classes=num_classes)
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
# print("Train Shape",X_train.shape)
# print("Test Shape",X_test.shape)
#
# model_lenet = Sequential([
#     RandomFlip("horizontal"),
#     RandomRotation(0.2),
#     RandomZoom(0.2),
#     RandomTranslation(0.1, 0.1),
#     Conv2D(6, (5, 5), activation="tanh", padding="same", input_shape=(32, 32, 3)),
#     AveragePooling2D((2, 2)),
#     Conv2D(16, (5, 5), activation="tanh"),
#     AveragePooling2D((2, 2)),
#     Flatten(),
#     Dense(120, activation="tanh"),
#     Dense(84, activation="tanh"),
#     Dense(num_classes, activation="softmax"),
# ])
# model_lenet.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
#
# print("Training LeeNet 5")
# model_lenet.fit(
#     X_train,y_train,
#     validation_data=(X_test,y_test),
#     epochs=40,
#     batch_size=16,
#
# )
# model_lenet.save("fruit_cnn_lenet.keras")
# y_true = np.argmax(y_test, axis=1)
# y_pred_lenet = np.argmax(model_lenet.predict(X_test), axis=1)
#
# cm_lenet = confusion_matrix(y_true, y_pred_lenet)
# loss2, acc_lenet = model_lenet.evaluate(X_test, y_test)
#
# print("\nConfusion Matrix - LeNet-5:")
# print(cm_lenet)
# print("\nClassification Report - LeNet-5:")
# print(classification_report(y_true, y_pred_lenet))
#
# plt.figure(figsize=(6, 5))
# sns.heatmap(cm_lenet, annot=True, fmt="d", cmap="Purples")
# plt.title(f"LeNet-5 (Acc: {acc_lenet:.2f})")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.tight_layout()
# plt.savefig("confusion_matrix_lenet.png")
# plt.show()


img_path = r"C:\Users\HCC\Desktop\images.jfif"

model = keras.models.load_model(r"E:\PycharmProjects\ML_Learning\fruit_cnn_lenet.keras")

img = image.load_img(img_path, target_size=(32, 32))
img_array = image.img_to_array(img)
img_array = img_array.astype("float32") / 255.0
img_array = np.expand_dims(img_array, axis=0)

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions)
confidence = np.max(predictions)

print("Raw probabilities:", predictions)
print(f"Predicted Label: {predicted_class}")
print(f"Confidence: {confidence:.4f}")
