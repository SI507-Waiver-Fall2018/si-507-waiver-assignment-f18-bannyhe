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
f = open("noun_data.csv", "r")
f_read = f.readlines()
f.close()

for n in range(len(f_read)):
	if n > 0:
		line = f_read[n].split(",")
		word.append(str(line[0]))
		freq.append(int(line[1].strip()))

data = [go.Bar(
            x = word,
            y = freq,
            name = 'Most Frequent Nouns',
    )]

layout = go.Layout(title="Most Used Nouns")
nouns_figure = go.Figure(data=data, layout=layout)

py.plot(data, filename='part4_viz_image')
py.image.save_as(nouns_figure, filename='part4_viz_image.png')
