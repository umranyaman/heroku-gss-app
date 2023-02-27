import pandas as pd
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px

gss_data = pd.read_csv("gss2016.csv")
st.title("The General Social Survey Data Analytics Web App")
st.write(f'<iframe width="500" height="315" src="https://www.youtube.com/embed/watch?v=jBb2mCmCcOk&list=PLVGPKieuvDTN4dkZP4ACXW91z3U5k0qaX" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True,)
st.write("")
# TODO check new dataset out later
#st.header("GSS 2016 Dataset")
#st.dataframe(gss_data)
gss_data_filtered = gss_data[["sex","race","age","degree","wrkstat","income","happy"]]
st.write("")
st.header("GSS Dataset")
#st.header("GSS 2016 Dataset Filtered on Sex, Race, Age, Degree, Work Status, Income and Happiness")

st.dataframe(gss_data_filtered)
columns = {"sex","race","age","degree","wrkstat","income","happy"}

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Aggregated by Counts")
pick_column = st.selectbox("Count by column: ", list(columns))

gss_data_filtered["Count"] = 0
gss_data_filtered_count = gss_data_filtered.groupby(pick_column).count()
gss_data_filtered_count = gss_data_filtered_count[["Count"]]
gss_data_filtered_count["Percentages"] = (gss_data_filtered_count.Count/gss_data_filtered_count.Count.sum()) * 100

st.dataframe(gss_data_filtered_count)

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Correlation Between Columns")

multi_select_column = st.multiselect("Multi-select columns for correlation",list(columns), default = ["sex"])
multi_select_gss_data_filtered = gss_data_filtered[multi_select_column]

st.dataframe(multi_select_gss_data_filtered)

st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Correlation Between Columns Multi-Select")

multi_select_column2 = st.multiselect("Multi-select columns grouped by:", list(columns), default = ["sex"])
multi_select_groupby = gss_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name="Count")
multi_select_groupby["Percentages"] = (multi_select_groupby.Count/multi_select_groupby.Count.sum()) * 100

st.dataframe(multi_select_groupby)
st.write("")
st.write("")
st.write("")
st.header("GSS 2016 Dataset Agrregated by Count Pie Chart")

pick_columns_visualized = st.selectbox("Visualise by Column", list(columns))

gss_data_filtered_count_visual = gss_data_filtered.groupby(pick_columns_visualized).count()

gss_data_filtered_count_visual['x-axis'] = gss_data_filtered_count_visual.index
# create a pie-chart figure
fig = go.Figure(data=[go.Pie(labels = gss_data_filtered_count_visual["x-axis"], values = gss_data_filtered_count_visual["Count"])])

st.plotly_chart(fig)

