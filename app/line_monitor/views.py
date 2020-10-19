from django.shortcuts import render
import plotly.graph_objects as go
import pandas as pd


def index(request):
    # Load data
    df = pd.read_csv("/usr/src/app/reports/line-monitor.csv")

    # Create figure
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=list(df.datetime), y=list(df.rtt_millis)))

    # Set title
    fig.update_layout(
        title_text="Ping RTT (-1 is timeout)"
    )

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    graph_div = fig.to_html()
    context = {'graph_div': graph_div}

    return render(request, "index.html", context=context)
