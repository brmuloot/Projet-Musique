import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

df = pd.read_csv(r"D:/ressources/top100000.csv")
df = df[['artiste_popularity','popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']]
df = df.drop_duplicates()


sns.set(rc = {'figure.figsize':(11.7,8.27)})

sns.distplot(df['popularity'], bins = 30)
plt.show()

matrice_corr = df.corr().round(2)
sns.heatmap(data = matrice_corr, annot = True)
plt.show()

# Variation des variables explicatives
# plt.figure(figsize=(20, 5))

# features = ['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']
# target = df['popularity']

# for i, col in enumerate(features):
#     plt.subplot(1, len(features) , i+1)

#     x = df[col]
#     y = target

#     plt.scatter(x, y, marker='o')
#     plt.title(col)

# plt.ylabel('Popularité')
# plt.show()

# Création d'un set avec les colonnes LSTAT, RM
X = pd.DataFrame(np.c_[df[['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']]], 
                 columns = ['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness'])

Y = df['popularity']

# ShuffleSplit est utilisée pour la validation croisée
cv = ShuffleSplit(3, test_size = 0.2)
results = cross_val_score(LinearRegression(), X, Y, cv = cv)

print('Accuracy :', results.mean() * 100.0, '%')
print('\nCross-Val Details :', results)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3, random_state=101)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()

linear_model.fit(X_train, Y_train)

from sklearn.metrics import mean_squared_error, r2_score
# évaluation du modèle pour l'ensemble d'entraînement
y_train_predict = linear_model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)
print("La performance du Modèle pour le set de Training")
print("------------------------------------------------")
print("l'erreur RMSE esst {}".format(rmse))
print('le score R2 est {}'.format(r2))
print("\n")
# évaluation du modèle pour le set de tesst
y_test_predict = linear_model.predict(X_test)
# racine carrée de l'erreur quadratique moyenne du modèle
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
# score R carré du modèle
r2 = r2_score(Y_test, y_test_predict)
print("La performance du Modèle pour le set de Test")
print("--------------------------------------------")
print("l'erreur RMSE est {}".format(rmse))
print('le score R2 score est {}'.format(r2))

sns.scatterplot(x=Y_test, y=y_test_predict)
plt.show()