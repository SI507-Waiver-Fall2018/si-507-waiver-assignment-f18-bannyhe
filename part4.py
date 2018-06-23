# Name: Mu He
# Uniq: bannyhe
# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import csv

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

# Create new lists for words and their frequencies
word = []
freq = []

# Open CSV file
with open("noun_data.csv") as f:
    first = True
    for line in f:
        if first:
            first = False
        else:
            data = line.split(",")
            word.append(data[0])
            freq.append(int(data[1].strip('\n')))

data = [go.Bar(x=word, y=freq)]
offline.plot(data, filename='part4_viz_image.html', image='png', image_filename='part4_viz_image')
