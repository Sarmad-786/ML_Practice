import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout,
    RandomFlip, RandomRotation, RandomZoom, RandomTranslation,
    Layer ,GlobalAveragePooling2D
)
import gc
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import keras
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns

class LRN(Layer):
    def __init__(self, depth_radius=5, bias=2.0, alpha=1e-4, beta=0.75, **kwargs):
        super().__init__(**kwargs)
        self.depth_radius = depth_radius
        self.bias = bias
        self.alpha = alpha
        self.beta = beta

    def call(self, x):
        return tf.nn.local_response_normalization(
            x,
            depth_radius=self.depth_radius,
            bias=self.bias,
            alpha=self.alpha,
            beta=self.beta
        )

    def get_config(self):
        config = super().get_config()
        config.update({
            "depth_radius": self.depth_radius,
            "bias": self.bias,
            "alpha": self.alpha,
            "beta": self.beta,
        })
        return config
chunks = pd.read_csv("/content/drive/MyDrive/fruits227.csv", dtype="float32", chunksize=500)
df_list = []
for chunk in chunks:
    df_list.append(chunk)
df = pd.concat(df_list, ignore_index=True)
del df_list
gc.collect()

X = df.drop("label", axis=1).values
y = df["label"].values.astype("int32")
del df
gc.collect()

X = X.reshape(-1, 227, 227, 3)
X = X / 255.0

num_classes = len(np.unique(y))
y = to_categorical(y, num_classes=num_classes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Train Shape", X_train.shape)
print("Test Shape", X_test.shape)

model_alexnet = Sequential([
    RandomFlip("horizontal"),
    RandomRotation(0.2),
    RandomZoom(0.2),
    RandomTranslation(0.1, 0.1),

    Conv2D(32, (11, 11), activation="relu", padding="same", input_shape=(227, 227, 3)),
    LRN(),
    MaxPooling2D((2, 2)),

    Conv2D(64, (5, 5), activation="relu", padding="same"),
    LRN(),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation="relu", padding="same"),
    LRN(),
    Conv2D(128, (3, 3), activation="relu", padding="same"),
    LRN(),
    Conv2D(64, (3, 3), activation="relu", padding="same"),
    LRN(),
    MaxPooling2D((2, 2)),

    GlobalAveragePooling2D(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(num_classes, activation="softmax"),
])

model_alexnet.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

print("Training AlexNet-style CNN")
model_alexnet.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=30,
    batch_size=16,
)
model_alexnet.save("fruit_cnn_alexnet.keras")

y_true = np.argmax(y_test, axis=1)
y_pred_alexnet = np.argmax(model_alexnet.predict(X_test), axis=1)

cm_alexnet = confusion_matrix(y_true, y_pred_alexnet)
loss3, acc_alexnet = model_alexnet.evaluate(X_test, y_test)

print("\nConfusion Matrix - AlexNet-style:")
print(cm_alexnet)
print("\nClassification Report - AlexNet-style:")
print(classification_report(y_true, y_pred_alexnet))

plt.figure(figsize=(6, 5))
sns.heatmap(cm_alexnet, annot=True, fmt="d", cmap="Purples")
plt.title(f"AlexNet-style (Acc: {acc_alexnet:.2f})")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("confusion_matrix_alexnet.png")
plt.show()


# img_path = r"C:\Users\HCC\Desktop\images5.jpg"
#
# model = keras.models.load_model(r"E:\PycharmProjects\ML_Learning\fruit_cnn_alexnet.keras", custom_objects={"LRN": LRN})
#
# img = image.load_img(img_path, target_size=(227, 227))
# img_array = image.img_to_array(img)
# img_array = img_array.astype("float32") / 255.0
# img_array = np.expand_dims(img_array, axis=0)
#
# predictions = model.predict(img_array)
# predicted_class = np.argmax(predictions)
# confidence = np.max(predictions)
#
# print("Raw probabilities:", predictions)
# print(f"Predicted Label: {predicted_class}")
# print(f"Confidence: {confidence:.4f}")