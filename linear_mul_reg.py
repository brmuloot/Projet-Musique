import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import ShuffleSplit, cross_val_score


# Importation et nettoyage de la base de donnée
df = pd.read_csv(r"D:/ressources/top100000.csv")
df = df[['artiste_popularity','popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']]
df = df.drop_duplicates()

# Affichage de la répartition des popularités
sns.set(rc = {'figure.figsize':(11.7,8.27)})

sns.distplot(df['popularity'], bins = 30)
plt.show()

# Affichage de la matrice de corrélation
matrice_corr = df.corr().round(2)
sns.heatmap(data = matrice_corr, annot = True)
plt.show()

# Création d'un set avec les colonnes séléctionné au début mais sans popularity
X = pd.DataFrame(np.c_[df[['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness']]], 
                 columns = ['artiste_popularity','song_danceability','artistes_followers','explicit','genre_energy','genre_popularity','genre_speechiness','genre_instrumentalness','genre_danceability','song_acousticness','song_speechiness','song_loudness'])

#Sélection de la variable rechercher
Y = df['popularity']

# ShuffleSplit est utilisée pour la validation croisée
cv = ShuffleSplit(3, test_size = 0.2)
results = cross_val_score(LinearRegression(), X, Y, cv = cv)

print('Accuracy :', results.mean() * 100.0, '%')
print('\nCross-Val Details :', results)

from sklearn.model_selection import train_test_split

#création des variables d'entreinement et de test 
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

# Application du modèle linéaire
linear_model = LinearRegression()

linear_model.fit(X_train, Y_train)


# évaluation du modèle pour l'ensemble d'entraînement
y_train_predict = linear_model.predict(X_train)
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)

print("La performance du Modèle pour le set de Training")
print("------------------------------------------------")
print("l'erreur RMSE esst {}".format(rmse))
print('le score R2 est {}'.format(r2))
print("\n")

# évaluation du modèle pour le set de test
y_test_predict = linear_model.predict(X_test)

# racine carrée de l'erreur quadratique moyenne du modèle
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))

# score R carré du modèle
r2 = r2_score(Y_test, y_test_predict)
print("La performance du Modèle pour le set de Test")
print("--------------------------------------------")
print("l'erreur RMSE est {}".format(rmse))
print('le score R2 score est {}'.format(r2))

# Graphique affichant les valeurs test comparer au valeur prédite
sns.scatterplot(x=Y_test, y=y_test_predict)
plt.show()
