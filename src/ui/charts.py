import plotly.express as px


def bar_chart(df, x, y, title):

    fig = px.bar(
        df,
        x=x,
        y=y,
        text=y,
        title=title,
        color=y,
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="plotly_dark",
        title_font_size=20,
        title_x=0.5,
        height=420,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=False,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font=dict(color="white")
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig