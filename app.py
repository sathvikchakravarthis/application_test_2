import streamlit as st
from data_analysis import load_data, analyze_data

# Title of the app
st.title("Data Analysis Web App")

# Sidebar for navigation between screens
st.sidebar.title("Navigation")
screen = st.sidebar.radio("Select a screen", ["Upload Data", "Data Overview", "Analysis Results"])

# Screen 1: Upload Data
if screen == "Upload Data":
    st.header("Step 1: Upload your Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        # Save the uploaded file to a session state for later use
        st.session_state.df = load_data(uploaded_file)

# Screen 2: Data Overview
elif screen == "Data Overview":
    if "df" in st.session_state:
        df = st.session_state.df
        st.header("Step 2: Data Overview")
        st.subheader("Data Shape:")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")
        
        st.subheader("Data Head:")
        st.write(df.head())
        
        st.subheader("Basic Statistics:")
        st.write(df.describe())
    else:
        st.warning("Please upload data in the 'Upload Data' screen first.")

# Screen 3: Analysis Results
elif screen == "Analysis Results":
    if "df" in st.session_state:
        df = st.session_state.df
        st.header("Step 3: Analysis Results")
        
        # Get analysis summary and heatmap image
        summary, heatmap_image = analyze_data(df)
        
        st.subheader("Data Summary:")
        st.write(summary['describe'])
        
        st.subheader("Correlation Heatmap:")
        st.image(heatmap_image)  # Display the heatmap image
    else:
        st.warning("Please upload data in the 'Upload Data' screen first.")

