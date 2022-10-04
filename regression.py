import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Projet\Projetmusic/top2500.csv")
cor = df.corr().round(2)
sns.heatmap(data=cor,annot=True)
plt.show()

# Checking na values
df.isna().sum()
# Dropping/Removing unnecessary columns
# Storing required values
Xi = df['popularity']
yi = df['artiste_popularity']
m = Xi.count()
# Normalization
X = (Xi - min(Xi))/(max(Xi)-min(Xi))
y = (yi - min(yi))/(max(yi)-min(yi))
# Standardization
X = (X - np.mean(X)) / np.std(X)
y = (y - np.mean(y)) / np.std(y)


plt.scatter(X,y, alpha = 0.4)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

X = X.to_numpy()
y = y.to_numpy()



X = X.reshape((m,1))

def hypothesis(X,w):
    return (w[1]*np.array(X[:,0])+w[0])

def cost(w,X,y):
    return (.5/m) * np.sum(np.square(hypothesis(X,w)-np.array(y)))


def grad(w,X,y):
    g = [0]*2
    g[0] = (1/m) * np.sum(hypothesis(X,w)-np.array(y))
    g[1] = (1/m) * np.sum((hypothesis(X,w)-np.array(y))*np.array(X[:,0]))
    return g

def descent(w_new, w_prev, lr):
    print(w_prev)
    print(cost(w_prev,X,y))
    i=0
    while True:
        w_prev = w_new
        w0 = w_prev[0] - lr*grad(w_prev,X,y)[0]
        w1 = w_prev[1] - lr*grad(w_prev,X,y)[1]
        w_new = [w0, w1]
        print(w_new)
        print(cost(w_new,X,y))
        if (w_new[0]-w_prev[0])**2 + (w_new[1]-w_prev[1])**2 <= pow(10,-6):
            return w_new
        if i>700: 
            return w_new
        i+=1

w = [0,0] # w = weights or theta
w = descent(w,w,.1)


def graph(formula, x_range):  
    x = np.array(x_range)  
    y = my_formula(x)  
    plt.plot(x, y)  
    
def my_formula(x):
    return w[0]+w[1]*x
plt.scatter(X,y,color = 'red', alpha = 0.2)
graph(my_formula, range(-4,5))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

def r2_test(y,y_calc):
    SSE = np.sum((y-y_calc)**2)
    SST = np.sum((y-y.mean())**2)
    return (1-(SSE/SST))*100
print(r2_test(y,hypothesis(X,w)))

# imports
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# generate random data-set
#np.random.seed(0)
#x = np.random.rand(100, 1)
#y = X + y * X + np.random.rand(100, 1)
# sckit-learn implementation
# Model initialization
regression_model = LinearRegression()
# Fit the data(train the model)
regression_model.fit(X, y)
# Predict
y_predicted = regression_model.predict(X)
# model evaluation
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)
# printing values
print('Slope:' ,regression_model.coef_)
print('Intercept:', regression_model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)
# plotting values
# data points
plt.scatter(X, y, s=10)
plt.xlabel('x')
plt.ylabel('y')
# predicted values
plt.plot(X, y_predicted, color='r')
plt.show()

