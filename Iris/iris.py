import pandas as pd
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# Dataset available on https://archive.ics.uci.edu/ml/datasets/iris

def unpack():
    '''
        Unpack iris data from sklearn dataset repo and return into DataFrame.
    '''
    iris = datasets.load_iris()
    digits = datasets.load_digits()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df['Type Index'] = iris.target
    df['Type'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    return df


def df_info(df):
    '''
        Exploratory analysis into loaded DataFrame. It shows:
            1. Shape of DataFrame(number of rows and columns)
            2. Columns to be analyzed (and its respective types of data)
            3. Head and tail of the DataFrame (5 occurences) and data distribution per type
            4. Checking for NaNs and blank values
            5. Statistical resume from analyzed columns
    '''
    print('This dataset contains', df.shape[0], 'rows and', df.shape[1], 'columns.\n')
    print(df.dtypes, end = '\n\n')
    print(df.head(5), end = '\n')
    print(df.tail(5), end = '\n')
    print(df['Type'].value_counts(), end = '\n')
    print(df.isnull().sum(), end = '\n')
    print(df.describe(), end = '\n\n')


def df_explore(df):
    '''
        Explore categories and generate visualizations, such as:
            1. Histogram for distribution of each variable
            2. Scatter plot comparing different variable
            3. First two views consolidated (macro relationships)
            4. Consolidated histograms by attribute
    '''
    # Uncomment to see isolated graphics
    # for column in df.columns.tolist()[:-2]:
    #     plt.hist(df[column])
    #     plt.xlabel(column)
    #     plt.ylabel('Quantity')
    #     plt.title('Distribution per ' + column)
    #     plt.show()

    # s = list()
    # for i in range(4):
    #     x = df.iloc[:, i]
    #     for j in df.columns.tolist()[:-2]:
    #         y = df[j]
    #         s.append([x.name, y.name])
    #         if x.name != y.name:
    #             plt.scatter(x,y, c = df['Type Index'])
    #             plt.xlabel(x.name)
    #             plt.ylabel(y.name)
    #             plt.title('Scatter plot between features, coloured by plant type')
    #             plt.show()

    pd.plotting.scatter_matrix(df[df.columns.tolist()[:4]], c = df['Type Index'],  figsize=(16,12))
    df.iloc[:, [0,1,2,3]].hist(figsize=(12,12))
    plt.show()
    plt.clf()
    return True


def lin_reg(df):
    '''
        1. Trains a Linear regression model to predict petal width;
        2. Scatter plots accuracy and returns its MSE and Score 
    '''
    model = LinearRegression()
    X = df.iloc[:, :4]
    Y = df['petal width (cm)']
    model.fit(X, Y)

    print(model.predict(X))

    plt.scatter(Y, model.predict(X))
    plt.xlabel("Model Accuracy")
    plt.ylabel("Petal width (cm)")
    plt.title("Accuracy from Linear Regression model")
    plt.show()

    # MSE (Mean Squared Error)
    mse = np.mean((Y - model.predict(X)) ** 2)
    print("MSE: ", mse)
    print("Score: ", model.score(X, Y))

def main():
    df = unpack()
    df_info(df)
    df_explore(df)
    lin_reg(df)

main()