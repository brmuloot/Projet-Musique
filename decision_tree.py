#### Importation des librairie utilisé ----
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#### Importation de la base de donnée ----
data = pd.read_csv(r"D:/ressources/top100000.csv")

data.info()

#### Détermination de la valeure à déterminer (y) par les valeures que l'on connaît (x)
y = data["popularity"]
x = data[['song_duration_ms','explicit','song_danceability','song_energy','song_key','song_loudness','song_mode','song_speechiness','song_acousticness','song_instrumentalness','song_liveness','song_valence','song_tempo','song_time_signature','artistes_followers','artiste_popularity','genre_mode','genre_acousticness','genre_danceability','genre_duration_ms','genre_energy','genre_instrumentalness','genre_liveness','genre_loudness','genre_speechiness','genre_tempo','genre_valence','genre_popularity','genre_key']]

#### Création des valeurs qui entraîne le modèle et des valeurs qui vont nous servir à le tester
x_train, x_test, y_train, y_test  = train_test_split(x, 
                                                     y, 
                                                     test_size=0.25, 
                                                     random_state=42)

#### Définition du modèle de foret de regression aléatoire ----
modele_rf = RandomForestRegressor(
    n_estimators=100,
    criterion='squared_error',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.0,
    max_features='auto',
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    bootstrap=True,
    oob_score=False,
    n_jobs=None,
    random_state=None,
    verbose=0,
    warm_start=False,
    ccp_alpha=0.0,
    max_samples=None,)

    
#### Entreinement du modèle avec les variables précédemment défini
modele_rf.fit(x_train, y_train)

#### Calcul des prédiction à partir de la variable test à partir de valeure connue
prediction = modele_rf.predict(x_test)


#### Affichage du pourcentage du coefficient de détermination et du graphique (popularité_connue / popularité_prédite)
print(f"Le pourcentage du coefficeint de détermination R² est de : {r2_score(y_test,prediction)*100} %")
sns.scatterplot(x=y_test, y=prediction)
plt.show()

#### Triage des préiction par ordre décroissant et selection de la plus petite popularité prédite du top 50
test = sorted(prediction, reverse=True)
print(test[0:50])
mini = min(test[0:50])

#### Importation de la nouvelle data pour tester le nombre de chanson sélectionner pour être dans le top 50
data_test = pd.read_csv(r"D:/ressources/top100000.csv")
data_test = data_test[['song_duration_ms','explicit','song_danceability','song_energy','song_key','song_loudness','song_mode','song_speechiness','song_acousticness','song_instrumentalness','song_liveness','song_valence','song_tempo','song_time_signature','artistes_followers','artiste_popularity','genre_mode','genre_acousticness','genre_danceability','genre_duration_ms','genre_energy','genre_instrumentalness','genre_liveness','genre_loudness','genre_speechiness','genre_tempo','genre_valence','genre_popularity','genre_key']]

xp = modele_rf.predict(data_test)
compteur = 0

#### Boucle qui compare la valeure de la nouvelle popularité prédite par rapport à la précedente
for exp in xp:
    if(exp >= mini):
        compteur+=1
        print(exp)
print(compteur)

#### On obtient environ 375 chanson sélectionner

# testing = pd.DataFrame()
# test = modele_rf.predict()