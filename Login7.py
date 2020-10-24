import pandas 
col_list= {"Status"}
df = pandas.read_csv('Test.csv', usecols=col_list)            
df.to_csv('Result1.csv')