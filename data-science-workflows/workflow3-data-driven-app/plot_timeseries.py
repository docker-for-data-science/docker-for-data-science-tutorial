# -*- coding: utf-8 -*-

'''Create live updating graph
'''

# standard library
from collections import namedtuple
import io
import os

# plot.ly modules
import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

TwoDPlot = namedtuple('TwoDPlot', ['x', 'y'])


def tail_file(filename, nlines):
    '''Return last nlines of file

    Adapted from https://gist.github.com/amitsaha/5990310
    '''
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        endf = position = qfile.tell()
        linecnt = 0
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n" and position != endf-1:
                linecnt += 1

            if linecnt == nlines:
                break
            position -= 1

        if position < 0:
            qfile.seek(0)

        return qfile.read()


def get_data(filename, nlines=20):
    '''Get data from tail of text file
    '''

    # read in file
    input_data = tail_file(filename, nlines)
    x = []
    y = []
    with io.StringIO(input_data) as f:
        for line in f:
            items = line.strip().split(', ')
            x.append(items[0])
            y.append(items[1])

    return TwoDPlot(x, y)


app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='live-graph', 
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*1000  # in milliseconds
    )
])


@app.callback(Output('live-graph', 'figure'),
              events=[Event('interval-component', 'interval')])
def update_graph():
    result = get_data('data/data.csv', nlines=200)
    return {
        'data': [
            go.Scatter(
                x=result.x,
                y=result.y
            )
        ]
    }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
