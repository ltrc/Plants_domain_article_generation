import pickle
import pandas as pd

# Makes a .pkl file which can be for loading data into the template
def main():
    plantsFile = 'data/telugu.csv'
    plantsDF = pd.read_csv(plantsFile)
    pickle.dump(plantsDF, open('./123.pkl', 'wb'))

if __name__ == '__main__':
    main()