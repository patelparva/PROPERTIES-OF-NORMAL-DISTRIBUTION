import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

index_input=input('Enter the index name of the column which you want to get statistics. ')

df=pd.read_csv('StudentsPerformance.csv')
data=[]

# print(len(df))

for i in range(0,len(df)):
    try:
        data.append(int(df[index_input][i]))
    except:
        print('Invalid Index Value')
        break

if(data!=[]):
    mean = statistics.mean(data)
    print('Mean of this data is {}'.format(mean))

    median=statistics.median(data)
    print('Median of this data is {}'.format(median))

    mode=statistics.mode(data)
    print('Mode of this data is {}'.format(mode))

    stdev=statistics.stdev(data)
    print('Standard Deviation of this data is {}'.format(stdev))

    first_stdev_start,first_stdev_end=mean-stdev,mean+stdev
    second_stdev_start,second_stdev_end=mean-(stdev*2),mean+(stdev*2)
    third_stdev_start,third_stdev_end=mean-(stdev*3),mean+(stdev*3)

    first_stdev_data=[result for result in data if result>first_stdev_start and result<first_stdev_end]
    second_stdev_data=[result for result in data if result>second_stdev_start and result<second_stdev_end]
    third_stdev_data=[result for result in data if result>third_stdev_start and result<third_stdev_end]

    first_data_percent=len(first_stdev_data)/len(data)*100
    print('{}% of the data lies within first standard deviations.'.format(first_data_percent))

    second_data_percent=len(second_stdev_data)/len(data)*100
    print('{}% of the data lies within second standard deviations.'.format(second_data_percent))

    third_data_percent=len(third_stdev_data)/len(data)*100
    print('{}% of the data lies within third standard deviations.'.format(third_data_percent))

    fig = ff.create_distplot([data], [index_input], show_hist=False, show_rug=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.03],mode='lines',name='Mean'))

    fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.03],mode='lines',name='Start of First Standard Deviation'))
    fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.03],mode='lines',name='End of First Standard Deviation'))

    fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.03],mode='lines',name='Start of Second Standard Deviation'))
    fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.03],mode='lines',name='End of Second Standard Deviation'))

    fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.03],mode='lines',name='Start of Third Standard Deviation'))
    fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.03],mode='lines',name='End of Third Standard Deviation'))

    fig.show()
