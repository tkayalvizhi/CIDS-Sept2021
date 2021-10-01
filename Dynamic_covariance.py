# Todo: header missing.


import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


def create_data() -> pd.DataFrame:
    """
    Creates linearly related data in the shape of the specific correlation
    """
    rho = st.slider('', min_value=-1.0, max_value=1.0, value=0.0, step=0.01)
    # Create the zero-centered, normalized covariance matrix.
    mu = np.array([0.0, 0.0])
    sigma = np.array(
        [[1, rho], [rho, 1]]
    )
    # Generate the data.
    data = np.random.multivariate_normal(mu, sigma, size=500)
    print(data)
    df = pd.DataFrame(columns=['x', 'y'], data=data)
    df['(x-y)^2'] = round((df['x']-df['y'])**2, 2)
    return df


def altair_chart(df: pd.DataFrame) -> None:
    """
    Draw the chart using Altair plotting library
    :return: None
    """

    c = alt.Chart(df) \
        .mark_circle(size=60) \
        .encode(alt.X('x'), alt.Y('y'),
                alt.Color('(x-y)^2', scale=alt.Scale(scheme='goldred')),
                tooltip=[alt.Tooltip('x'), alt.Tooltip('y')]) \
        .properties(height=600)
    xline = alt.Chart(pd.DataFrame({'y': [0]})) \
        .mark_rule(size=2, opacity=0.5) \
        .encode(y='y')
    yline = alt.Chart(pd.DataFrame({'x': [0]})) \
        .mark_rule(size=2, opacity=0.5) \
        .encode(x='x')
    chart = c + xline + yline
    st.altair_chart(chart, use_container_width=True)


def matplotlib_chart(df: pd.DataFrame) -> None:
    """
        Draw the chart using default Matplotlib plotting library of python.
        :return: None
        """
    fig, ax = plt.subplots()
    ax.scatter(x=df.x, y=df.y, alpha=0.3)
    ax.spines[['left', 'bottom']].set_position('center')
    ax.spines[['right', 'top']].set_visible(False)
    st.pyplot(fig)


# ----------------------------- Main program -----------------------------------
st.title("Covariance and correlation")
st.sidebar.image(
    "https://www.supportvectors.io/gaia/pluginfile.php/1/theme_lambda/logo/1599599177/support-vectors-logo.gif")

message = r'''\text{Select a value of the correlation } \mathbf{\rho}'''
st.latex(message)

# Generate data with specific correlation.
df = create_data()
altair_chart(df)