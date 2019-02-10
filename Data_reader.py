import pandas as pd
#import numpy
#import gmaps
import matplotlib.pyplot as plt

def main():
    dim = pd.read_csv("C:\\Users\\Shubham2\\Desktop\\SageAI\\SAGE\Datasets\\311_Service_Requests_2017_to_Present.csv")
    fixColumns(dim)
    commonComplaints(dim)
    complaintsPerBorough(dim)

def fixColumns(df):
    df['Created Date' and 'Closed Date'] = pd.to_datetime(df['Created Date' and 'Closed Date'])
  #  df['Closed Date'] = pd.to_datetime(df['Closed Date'])

def commonComplaints(df):
    uniqueBoroughs = pd.unique(df['Borough'])
    print(df['Borough'].value_counts(),'\n',uniqueBoroughs)
  #  print(uniqueBoroughs)

def complaintsPerBorough(df):
    complaints = df['Complaint Type'].value_counts()
    print(complaints)
    fig = plt.figure(1)
    complaints.plot(kind='bar')
    fig = plt.figure(2)
    complaints.plot(kind='pie')
    plt.show()
main()