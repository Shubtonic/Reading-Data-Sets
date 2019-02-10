import pandas as pd
import matplotlib.pyplot as plt
#import dash
#import dash_core_components as dcc
#import dash_html_components as html

#app = dash.Dash()
#app.layout = html.Div(children=[]html.Div(id='output-graph'))
def main():
    dim = pd.read_csv("C:\\Users\\Shubham2\\Desktop\\SageAI\\SAGE\Datasets\\311_Service_Requests_2017_to_Present.csv")
    plot_data(dim, 'Complaint Type', 'bar')
    plot_data(dim, 'Borough', 'pie')
    plot_data(dim, 'City', 'bar')


def plot_data(df, column, chart_type):
    print("Plotting", column, "as a", chart_type, "chart.")
    complaints = df[column].value_counts()
    plt.figure(1)
    complaints.plot(kind=chart_type)
    plt.show()


#@app.callback(Output(plt.show()),
 #             events=[Event('graph-update', 'interval')])

#app.layout = html.Div(children=content)

    
#app.run_server()

main()