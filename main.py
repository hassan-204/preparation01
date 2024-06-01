import streamlit as st
import time 

st.write("# Hello World1")

progressbar = st.progress(0,"Show loading")

for i in range(100):
    progressbar.progress(i+1,"Show loading")
    time.sleep(0.001)



import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df) 

st.markdown("""
<div style='background-color:lightblue; padding:10px; border-radius:10px;'>
    <h2 style='color:navy;'>This is a custom HTML block</h2>
    <p>You can add any HTML code here!</p>
    <button onclick="displayAlert()">Click me!</button>
</div>
<script>
function displayAlert() {
    alert("Button clicked!");
}
</script>
            """, unsafe_allow_html=True)