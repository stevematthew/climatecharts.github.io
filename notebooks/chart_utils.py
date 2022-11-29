from datetime import datetime

def bracket_annotation(fig, y0, y1, x, style='dot', width=100):
    # bracket_annotation(fig, 310, 420, '1930.1', style='dashdot', width=2000)

    x_to_dt = lambda d: datetime.strptime(d, '%Y.%m')

    fig.add_shape(type='line',
        xref='x', yref='y',
        x0=x_to_dt(x),
        x1=x_to_dt(x),
        y0=y0, 
        y1=y1,
        line=dict(
            color='black',
            dash=style,
            width=1,
        )
    )


    fig.add_shape(type='line',
        xref='x', yref='y',
        x0=x_to_dt(x),
        x1=x_to_dt(x) + timedelta(days=width),
        y0=y0, 
        y1=y0,
        line=dict(
            color='black',
            dash=style,
            width=1,
        )
    )

    # right
    fig.add_shape(type='line',
        xref='x', yref='y',
        x0=x_to_dt(x),
        x1=x_to_dt(x) + timedelta(days=width),
        y0=y1, 
        y1=y1,
        line=dict(
            color='black',
            dash=style,
            width=1,
        )
    )
