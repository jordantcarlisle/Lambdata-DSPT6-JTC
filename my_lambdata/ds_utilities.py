import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint
from IPython.display import display


def enlarge(n):
    '''
    This function will multiple the input by 100
    '''
    return n * 1000



def download(url):
    filename = url.split('/')[-1]
    #print(f'Downloading {url}')
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    #print(f'Downloaded {filename}')


def to_dataframe_column(list):
    x = pd.series(list)
    df = DataFrame(x)
    print(df)

class My_Data_Splitter():
    '''
    This class implements a 3-way data split and outputs summary metrics.
    '''

    def __init__(self, df, features, target):
        self.df = df
        self.features = features
        self.target = target
        self.X = df[features]
        self.y = df[target]

    def train_validation_test_split(self,
                                    train_size=0.7, val_size=0.1,
                                    test_size=0.2, random_state=None,
                                    shuffle=True):
        '''
        This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or
        matrices into train, validation, and test subsets.
        Args:
            X (Numpy array or DataFrame): This is a dataframe with features.
            y (Numpy array or DataFrame): This is a pandas Series with target.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, and validation dataframes for features (X) and target (y).
        '''
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, shuffle=shuffle)

        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)

        return X_train, X_val, X_test, y_train, y_val, y_test

    def print_split_summary(self, X_train, X_val, X_test):
        '''
        This function prints summary statistics for X_train, X_val, and X_test.
        '''
        print('######################## TRAINING DATA ########################')
        print(f'X_train Shape: {X_train.shape}')
        display(X_train.describe(include='all').transpose())
        print('')

        print('######################## VALIDATION DATA ######################')
        print(f'X_val Shape: {X_val.shape}')
        display(X_val.describe(include='all').transpose())
        print('')

        print('######################## TEST DATA ############################')
        print(f'X_test Shape: {X_test.shape}')
        display(X_test.describe(include='all').transpose())
        print('')


if __name__ == '__main__':
    # Test the enlarge function
    # y = int(input("Choose a number: "))
    # print(y, enlarge(y))

    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    # Test the My_Data_Splitter Class
    splitter = My_Data_Splitter(df=df, features=['ash', 'hue'], target='target')
    X_train, X_val, X_test, y_train, y_val, y_test = splitter.train_validation_test_split()
    splitter.print_split_summary(X_train, X_val, X_test)
