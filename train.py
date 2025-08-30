

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense


#Load the dataset

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)


#Preprocess data

maxlen = 200 
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)


#Build the model

model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=64, input_length=maxlen))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()


#Train the model

model.fit(
    x_train, y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.2
)


#Save the model
model.save("sentiment_model.h5")
print("Model saved as sentiment_model.h5")
