import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.loader import NewsDataLoader
from src.config import cfg

# Set page configuration
st.set_page_config(
    page_title="Global News Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto",
)

# Custom CSS to style the header
st.markdown(
    """
    <style>
    .body{
    margin: 0,
    padding: 0;
    }
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        background-color: #f0f0f0;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Data Loader
data_loader = NewsDataLoader(cfg.path)
data_df = data_loader.get_news_data()
traffic_data = data_loader.get_traffic_data()
domains_df = data_loader.get_domain_location_data()


page = st.selectbox(" ", ["Home", "Exploratory Data Analysis", "Keyword Extraction", "Topic Modeling"])

# Custom Header (Navigation)
st.markdown(
    """
    <div class="header">
        <span style='color: #ff6666;'>Global News Analytics</span> Dashboard
    </div>
    """,
    unsafe_allow_html=True,
)

# Page Content

if page == "Home":
    st.title("Global News Analytics Dashboard")

    st.markdown("""

This interactive dashboard provides a comprehensive view of the key insights gleaned from our exploration of the Global News
                 Dataset. Dive deeper into topic modeling to  to find trending topics over time.
                 Utilize the keyword extraction feature to identify the most frequently used terms within specific topics or events. By interacting with
                 these visualizations, you can gain a richer understanding of the current news landscape and uncover hidden patterns within the data.
 """)

elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")

    image_path = "./Images/photo_2024-04-13 17.37.29.jpeg"
    st.image(image_path, caption='Top 10 and bottom ten countries with many article written about them')

    image_path = "./Images/photo_2024-04-13 17.37.37.jpeg"
    st.image(image_path, caption='Top 10 and bottom ten countries with highest number of news media organization')

    image_path = "./Images/photo_2024-04-13 17.37.38.jpeg"
    st.image(image_path, caption='Top 10 and bottom ten countries with highest traffic')

    image_path = "./Images/photo_2024-04-13 17.37.40.jpeg"
    st.image(image_path, caption='Top 10 websites with largest count of news articles')

 
    
    
    image_path = "./Images/distribution of title lenght.png"
    st.image(image_path, caption='distribution of title length')

    image_path = "./Images/10 websites with negative senitment.png"
    st.image(image_path, caption='Top 10 websites with negative senitment')

    image_path = "./Images/positive sentiment.png"
    st.image(image_path, caption='Top 10 websites with positive senitment')
    

    image_path = "./Images/neuteral sentiment.png"
    st.image(image_path, caption='Top 10 websites with neuttral senitment')
    
 
elif page == "Keyword Extraction":
    st.title("Keyword Extraction")

    image_path = "./Images/overlap of title and content.png"
    st.image(image_path, caption='Overlap between title and content keywords')

    image_path = "./Images/top 30 keywords.png"
    st.image(image_path, caption='Top 10 websites with positive senitment')

    
    




elif page == "Topic Modeling":
    st.title("Topic Modeling")
    image_path = "./Images/trend of all topics over time.png"  # Update with your image path
    st.image(image_path, caption='Trend of topic modeling over time')
