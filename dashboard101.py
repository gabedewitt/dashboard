from pkg_resources import run_script
import streamlit as st
import plotly.graph_objects as go


st.title("Welcome to Streamlit!")

fig = go.Figure(
    data=[go.Pie(
        labels=['A', 'B', 'C'],
        values=[30, 20, 50]
    )]
)
fig = fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=15
)

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)
value = st.slider('val')  # this is a widget
st.write(value, 'squared is', value * value)
