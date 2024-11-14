import streamlit as st 
import nltk
import os
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import base64
import requests
from io import BytesIO
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import joblib
#nltk.download("averaged_perceptron_tagger")
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')
nltk.download('omw-1.4')
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")





df_detailed_places=pd.read_csv('cleaned_ddetailed_kids_friendly_places_paris_with_reviews.csv')
df_detailed_places=df_detailed_places.drop(columns='Unnamed: 0')
trends_5years=pd.read_csv('ttrends_kids_friendly_paris_5years.csv')
trends_5years=trends_5years.drop(columns='Unnamed: 0')
df=pd.read_csv("population_france.csv")
df_parks_with_playground = pd.read_excel('espaces_verts.xlsx')
df_parks_with_playground=df_parks_with_playground.drop(columns='Unnamed: 0')
df_faire= pd.read_csv('qque-faire-a-paris-.csv')
df_faire=df_faire.drop(columns='Unnamed: 0')
df_paris_data=pd.read_csv('population_paris_2021.csv')
df_paris_data=df_paris_data.drop(columns=['Unnamed: 0','Name Arrondissement'])
trends_comparison=pd.read_csv('trends_comparison.csv')
trends_comparison=trends_comparison.drop(columns=['Unnamed: 0','Unnamed: 0.1'])
data = pd.read_csv("Gral_df_Scores.csv", dtype={'zip_code': str})
df_kf_places_paris=pd.read_csv('extra_kfplaces_paris.csv')



st.sidebar.title("Contents")

pages = ["Overview of the projet", "Data Exploration", "Data Analysis","Recommendations", "Machine Learning","API"]

page = st.sidebar.radio("Go to the page :", pages)

if page == pages[0] : 

    
    def image_to_base64(image):
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()

    # Load and resize the image
    image = Image.open("bateaux.jpg")
    image_base64 = image_to_base64(image)  

    # Display the centered image with rounded edges and shadow effect
    st.markdown(
        f"""
        <style>
        .rounded-image {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 900px; /* Adjust width here */
            height: 150px; /* Adjust height here */
            border-radius: 70px; /* Rounded corners, increase for more rounded edges */
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        }}
        </style>
        <img class="rounded-image" src="data:image/jpeg;base64,{image_base64}" alt="rounded image">
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)

    #st.title("Welcome to the Kid-Friendly Places in Paris App!")
    st.markdown('<p class="centered-text">Welcome to the Kid-Friendly Places in Paris App!</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
   
    st.write("This application is designed to help parents and caregivers discover and explore kid-friendly spots across Paris, whether you're searching for restaurants, parks, events, or other family-friendly places. The app is structured to offer a complete analysis of various locations and activities that are welcoming to children. Here’s a brief overview of what each section provides:")
    
    st.markdown("***1.	Overview of the projet:***")
    st.write("This page gives an introduction of the application and its purpose.")
    st.markdown("***2.	Data Exploration:***")
    st.write("In this section, you'll find details about the datasets used for the project, including their sources, allowing transparency in data provenance.")
    st.markdown("***3.	Data Analysis:***")
    st.write("Here, you can explore detailed analyses on Paris' population by arrondissement, monthly trends in Google searches for kid-friendly places, and evaluations of events and kid-friendly locations by year or arrondissement.")
    st.markdown("***4.	Recommendations:***")
    st.write("This page offers tailored recommendations for places officially categorized as kid-friendly in Paris, helping you plan outings and activities for your family.")
    st.markdown("***5.	Predictive Model for Non-Categorized Restaurants:***")
    st.write("Using a machine learning NLP model trained on customer reviews, this section predicts whether a restaurant that isn’t officially marked as kid-friendly is likely to offer a welcoming environment for children, giving parents additional dining options.")
    st.markdown("***6. Data Download Center:***")
    st.write("This section provides downloadable datasets used in the project, allowing you to explore and analyze key data on kid-friendly locations and trends in Paris.")  
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("This app is my final project, created after several weeks of intensive bootcamp in data analysis. I chose this topic because, as a new mother, I know how much parents want to continue enjoying outings while seamlessly incorporating their children. Many parents, especially when visiting a new city, face the challenge of finding places where they and their children will feel welcome.")
    st.write("With this app, I hope to make it a little easier for parents to find child-friendly places in Paris, so you can focus on spending quality time with your family.")
    st.write("Thank you for using the app, and I hope it brings value to your Paris experience!")
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="text-align: right;">
            By Xinly ROY
        </div>
        """,
        unsafe_allow_html=True
    )    



    # Load and resize the image
    image2 = Image.open("imageintro.jpg")
    image2_base64 = image_to_base64(image2) 
        # Display the centered image with rounded edges and shadow effect
    st.markdown(
        f"""
        <style>
        .rounded-image2 {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 800px; /* Adjust width here */
            height: 600px; /* Adjust height here */
            border-radius: 60px; /* Rounded corners, increase for more rounded edges */
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
        }}
        </style>
        <img class="rounded-image2" src="data:image2/jpeg;base64,{image2_base64}" alt="rounded image">
        """,
        unsafe_allow_html=True
    )


    
elif page == pages[1]:

    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: black;  /* Adjust the color if needed */
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="centered-title">Data Exploration</h1>
        """,
        unsafe_allow_html=True
    ) 


    st.write("To conduct the analysis for this project, we used datasets sourced through web scraping, APIs, and downloads from various database provider sites. ")
    st.write("Below, you will find some of them: ")
    
    st.markdown("***1.-Dataset coming from the Pytrends Google API, showing user searches on Google for kid-friendly places in Paris over the last 5 years :***")
    st.dataframe(trends_5years.head())
    st.write("DataFrame Dimensions :")
    st.write(trends_5years.shape)
    if st.checkbox("Show Missing Values", key="missing_values_trends") : 
        st.dataframe(trends_5years.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_trends") : 
        st.write(trends_5years.duplicated().sum())

    st.markdown("***2.-Dataset downloaded via web scraping from the Liternaute website, showing the population ranking in France for the year 2021 :***")
    st.dataframe(df.head())
    st.write("DataFrame Dimensions :")
    st.write(df.shape)
    if st.checkbox("Show Missing Values", key="missing_values_population") : 
        st.dataframe(df.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_population") : 
        st.write(df.duplicated().sum())

    st.markdown("***3.-Dataset downloaded via web scrapping from Wikipedia, showing the population of Paris by arrondissement for the year 2021 :***")
    st.dataframe(df_paris_data.head())
    st.write("DataFrame Dimensions :")
    st.write(df_paris_data.shape)
    if st.checkbox("Show Missing Values", key="missing_values_population_paris") : 
        st.dataframe(df_paris_data.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_population_paris") : 
        st.write(df_paris_data.duplicated().sum())

    st.markdown("***4.-Dataset downloaded from the Paris.fr website with information on all squares and parks in Paris. :***")
    st.dataframe(df_parks_with_playground.head())
    st.write("DataFrame Dimensions :")
    st.write(df_parks_with_playground.shape)
    if st.checkbox("Show Missing Values", key="missing_values_parks") : 
        st.dataframe(df_parks_with_playground.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_parks") : 
        st.write(df_parks_with_playground.duplicated().sum())
    
    st.markdown("***5.-Dataset coming from the Google API, showing places classified as kid-friendly on Google :***")
    st.dataframe(df_detailed_places.head())
    st.write("DataFrame Dimensions :")
    st.write(df_detailed_places.shape)
    if st.checkbox("Show Missing Values",key="missing_values_places") : 
        st.dataframe(df_detailed_places.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_places") : 
        st.write(df_detailed_places.duplicated().sum())

    st.markdown("***6.-Dataset from Kaggle, showing events for kids in Paris in 2024 and beyond :***")
    st.dataframe(df_faire.head())
    st.write("DataFrame Dimensions :")
    st.write(df_faire.shape)
    if st.checkbox("Show Missing Values",key="missing_values_faire") : 
        st.dataframe(df_faire.isna().sum())
    
    if st.checkbox("Show Duplicates", key="duplicates_faire") : 
        st.write(df_faire.duplicated().sum())
        
elif page == pages[2]:

    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: black;  /* Adjust the color if needed */
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="centered-title">Data Analysis</h1>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown("<br><br>", unsafe_allow_html=True)
   
    st.write("We start by examining Google search trends for kid-friendly places in Paris over the past months and years. How interested are people in Paris in these topics? We found the following:")
    
    # Convert 'date' to datetime format and handle errors
    trends_comparison["Date"] = pd.to_datetime(trends_comparison["Date"], errors='coerce')

    # Melt DataFrame to long format for easier plotting with Plotly, excluding unnecessary columns
    trends_comparison_melted = trends_comparison.melt(
        id_vars=["Date"], 
        value_vars=["Restaurant kid_friendly", "Kid's activities", "Parks"],  # Only actual activity columns
        var_name="Activity", 
        value_name="Search Interest"
    )

    # Drop rows with missing values in 'Search Interest' to ensure clean plotting
    trends_comparison_melted = trends_comparison_melted.dropna(subset=["Search Interest"])

    # Plotting with Plotly
    fig = px.line(
        trends_comparison_melted, 
        x="Date", 
        y="Search Interest", 
        color="Activity", 
        title="Trends of Searches by Month and Activity",
        labels={"Date": "Date", "Search Interest": "Interest Level", "Activity": "Activity Type"}
    )

    # Customize x-axis to show each month
    fig.update_xaxes(
        dtick="M1",  # Ticks at each month
        tickformat="%B",  # Full month name
        ticklabelmode="period"  # Display each month fully
    )

    # Show the figure in Streamlit
    st.plotly_chart(fig)
    st.write("The graph shows that Restaurant kid-friendly has the most seasonal variability in search interest, likely influenced by periods when families dine out more frequently. Kid's activities have a stable level of interest, while Parks remain consistently low in search frequency, possibly due to ease of access or less need for planning.")    
    st.markdown("<br><br>", unsafe_allow_html=True)
    


    st.markdown("**Trends in monthly searches and activities over the past 3 years**<br><br>", unsafe_allow_html=True)
    st.write("The following charts indicate seasonal patterns in search behaviors related to kid-friendly activities in Paris over the past 3 years.")
    
    trends_5years['Date'] = pd.to_datetime(trends_5years['Date'])
    trends_5years['Year'] = trends_5years['Date'].dt.year
    trends_5years['Month'] = trends_5years['Date'].dt.month_name()

    # Filter the data for the last three years (2022, 2023, 2024)
    recent_trends = trends_5years[trends_5years['Year'].isin([2022, 2023, 2024])]

    # Define month order to ensure consistent ordering in plots
    month_order = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]

    # Define activities for separate plotting
    activity_columns = ["Kid's-friendly restaurant", 'Kid’s activity Paris', 'Children’s park Paris']

    # Initialize three columns for plots in Streamlit
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    # Generate line plots for each activity
    for i, activity in enumerate(activity_columns):
        # Create a pivot table for each activity with months ordered consistently
        pivot_data = recent_trends.pivot_table(
            index='Month', columns='Year', values=activity, aggfunc='mean'
        ).reindex(month_order)

        # Check if there is data to plot
        if pivot_data.notna().values.any():
            # Plot each activity trend for the last three years
            fig, ax = plt.subplots(figsize=(6, 4))
            pivot_data.plot(ax=ax, marker='o', linewidth=2)

            ax.set_title(activity, fontsize=14, fontweight='bold')
            ax.set_xlabel("Month", fontsize=10)
            ax.set_ylabel("Search Popularity", fontsize=10)
            ax.set_xticks(range(12))
            ax.set_xticklabels(month_order, rotation=45, ha="right")

            # Display the plot in Streamlit column
            with columns[i]:
                st.pyplot(fig)
        else:
            # Display a message if no data is available for the activity
            with columns[i]:
                st.write(f"No data available for '{activity}' for the last three years.")
    
    st.write("Across all activities, there are observable seasonal patterns. Interest in kid-friendly restaurants and activities is spread throughout the year with particular peaks, while interest in parks is mostly concentrated in the warmer months.")
    st.write("Although there are variations, the general pattern for each activity appears similar across the years, indicating consistent seasonal behavior among searchers. The trends reflect how parental interest in planning kid-friendly outings aligns with school holidays, warmer weather, and seasonal family time.")
    st.markdown("<br><br>", unsafe_allow_html=True)
    

    st.markdown("**Number of Kid's Friendly Restaurants by Zip Code**<br><br>", unsafe_allow_html=True)
    st.write("This bar chart shows the distribution of kid-friendly restaurants across various postal codes in Paris.")
    df_detailed_places['zipcode'] = df_detailed_places['zipcode'].astype(str)

    # Count the number of restaurants per zip code
    zipcode_counts = df_detailed_places['zipcode'].value_counts().sort_index()

    # Convert the result to a DataFrame for Plotly compatibility
    zipcode_counts_df = zipcode_counts.reset_index()
    zipcode_counts_df.columns = ['Zip Code', 'Number of Restaurants']

    # Create the bar plot with categorical ordering
    fig1 = px.bar(
        zipcode_counts_df, 
        x='Zip Code', 
        y='Number of Restaurants', 
        title="Number of Kid's Friendly Restaurants by Zip Code",
        text='Number of Restaurants',
        category_orders={'Zip Code': sorted(zipcode_counts_df['Zip Code'])}
    )

    # Update layout for better readability
    fig1.update_layout(xaxis_type='category', xaxis_tickangle=45, margin=dict(t=50))
    fig1.update_traces(texttemplate='%{text}', textposition='inside')

    # Display the plot in Streamlit
    st.plotly_chart(fig1)
    st.write("The zip codes 75004, 75005, 75009, and 75018 have a relatively high count of kid-friendly restaurants. Some areas like 75003 and 75020 have a moderate presence, while others have only a few kid-friendly restaurants. This distribution could reflect both the density of family-friendly areas and the popularity of specific neighborhoods for family dining in Paris.")
    st.markdown("<br><br>", unsafe_allow_html=True)
    


    st.markdown("**Distribution of Parks by Zip Code and Type**<br><br>", unsafe_allow_html=True)
    st.write("This stacked bar chart shows the number of parks by postal code and category (like 'Jardin' and 'Square.")
    df_parks_with_playground['Code postal'] = df_parks_with_playground['Code postal'].astype(str)

    # Filter out unwanted postal codes if necessary
    filtered_parks = df_parks_with_playground[df_parks_with_playground["Code postal"] != "94300"]

    # Group the data by 'Code postal' and 'Catégorie', and count occurrences
    park_counts = filtered_parks.groupby(['Code postal', 'Catégorie']).size().unstack(fill_value=0)

    # Convert the result to a DataFrame for Plotly compatibility
    park_counts_df = park_counts.reset_index().melt(id_vars='Code postal', var_name='Category', value_name='Count')

    # Create the stacked bar plot with categorical x-axis
    fig2 = px.bar(
        park_counts_df, 
        x='Code postal', 
        y='Count', 
        color='Category', 
        title="Number of Parks by Zip Code and Category",
        text='Count',
        category_orders={'Code postal': sorted(park_counts_df['Code postal'].unique())}
    )

    # Update layout for better readability
    fig2.update_layout(xaxis_type='category', xaxis_tickangle=45, margin=dict(t=50))
    fig2.update_traces(texttemplate='%{text}', textposition='inside')

    # Display the plot in Streamlit
    st.plotly_chart(fig2)
    st.write("75015 and 75020 have the highest concentration of parks, especially squares, indicating that these neighborhoods may have more family-friendly outdoor spaces. Categories like 'Jardin' (Garden) and 'Square' appear frequently across different postal codes, highlighting the availability of varied green spaces for families and children.")
    st.markdown("<br><br>", unsafe_allow_html=True)
    




    st.markdown("**Kid-Friendly Events Registered per Year**<br><br>", unsafe_allow_html=True)
    st.write("This chart shows events for children or the whole family, registered from 2019 to 2025.")

    month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]

    # Ensure 'Month_debut' is properly formatted and convert it to categorical based on month_order
    df_faire['Month_debut'] = df_faire['Month_debut'].astype(str).fillna("Unknown")
    df_faire = df_faire[df_faire['Month_debut'].isin(month_order)]
    df_faire['Month_debut'] = pd.Categorical(df_faire['Month_debut'], categories=month_order, ordered=True)

    # Get unique years from 'Year_debut' for the dropdown selection
    available_years = sorted(df_faire['Year_debut'].unique())

    # Create a selectbox for the user to choose the year
    selected_year = st.selectbox("Select Year", available_years, index=available_years.index(2024) if 2024 in available_years else 0)

    # Filter events based on the selected year
    df_filtered = df_faire[df_faire['Year_debut'] == selected_year]

    # Count the number of events per month for the selected year, reindex to ensure all months are represented
    events_per_month = df_filtered['Month_debut'].value_counts().reindex(month_order).fillna(0)

    # Create an interactive area chart with Plotly
    fig = go.Figure()

    # Add a trace for the filled area and line
    fig.add_trace(go.Scatter(
        x=events_per_month.index,        # X-axis: Months
        y=events_per_month.values,       # Y-axis: Number of events
        mode='lines+markers',            # Show both lines and markers
        fill='tozeroy',                  # Fill area from line to Y=0
        line=dict(color='skyblue'),      # Line color
        marker=dict(size=8, color='blue'),# Marker size and color
        hovertemplate="Month: %{x}<br>Events: %{y}<extra></extra>"  # Custom hover info
    ))

    # Update layout settings for title, labels, and axis ticks
    fig.update_layout(
        title=f"Number of Events by Month in {selected_year}",  # Dynamic chart title based on the selected year
        xaxis_title="Month",                                    # X-axis label
        yaxis_title="Number of Events",                         # Y-axis label
        xaxis=dict(tickmode="array", tickvals=month_order),     # Set month order for X-axis
        yaxis=dict(tickformat="d"),                             # Display Y-axis as integer
        template="simple_white"                                 # Background style
    )

    # Display the interactive Plotly chart in Streamlit with a unique key
    st.plotly_chart(fig, key=f"events_chart_{selected_year}")
    st.write("In 2024, the peak in October suggests a period with high community engagement, potentially aligned with holidays, cultural celebrations, or seasonal festivals.")
    st.write("The events continue but decrease toward the year’s end, indicating fewer, but possibly significant, holiday events.")
    st.write("The months from January to August show limited activity, possibly reflecting a period where fewer public or community events are planned, or seasonal preferences for hosting events later in the year.")
    



    #st.write("Top 10 Most Populous Cities in France")
    
    # Clean up population data
    df['Population'] = df['Population'].astype(str).str.replace("habitants", "").str.replace("\xa0", "").str.replace(" ", "").astype(int)

    # Filter for the top 10 most populated cities
    df_top10 = df.head(10)

    # Plot with Plotly
    fig3 = px.bar(
        df_top10,
        x='City',
        y='Population',
        title='Top 10 Most Populous Cities in France',
        labels={'City': 'City', 'Population': 'Population'},
        text='Population'
    )

    # Customize the layout
    fig3.update_traces(marker_color='steelblue', textposition='inside')
    fig3.update_layout(xaxis_title="City", yaxis_title="Population")

    # Display in Streamlit
    st.plotly_chart(fig3)
    st.write("Paris has by far the largest population, followed by Marseille and Lyon, which are significantly less populated than Paris. Other cities like Toulouse, Nice, and Nantes follow but with much smaller populations. This chart illustrates the centralization of population in a few major urban areas in France, with a sharp drop-off after Paris, emphasizing its role as the country’s main urban hub.")


    # Check that the DataFrame is loaded correctly
    st.write("Population by Arrondissement in Paris")

    # Create a bar chart for population by arrondissement
    fig = px.bar(
        df_paris_data,
        x='Arrondissement',
        y='Population (2020)',
        title="Population by Arrondissement in Paris (2020)",
        labels={'Arrondissement': 'Arrondissement', 'Population (2020)': 'Population'},
        text='Population (2020)'  # Show values on top of bars
    )

    # Customize the chart for better readability
    fig.update_layout(
        xaxis_title="Arrondissement",
        yaxis_title="Population (2020)",
        xaxis=dict(type='category'),  
        template="plotly_white"
    )
    fig.update_traces(marker_color='lightskyblue', textposition='outside')  # Optional: color and text position

    # Display the interactive chart in Streamlit
    st.plotly_chart(fig)
    st.write("The 15th arrondissement has the highest population at around 227,746, followed by the 20th, 18th, and 19th arrondissements, each with populations exceeding 180,000. These areas likely serve as significant residential hubs in Paris.")
    st.write("The central arrondissements, particularly the 1st and 2nd, have much lower populations. This could be due to these areas focusing more on commercial, historical, and tourist activities rather than residential use.")
    st.write("The outer arrondissements, especially those in the northeast and south, tend to have higher populations, possibly because they offer more residential space and affordable living conditions compared to the historic and commercial centers.")

elif page == pages[3]: 
    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: black;  /* Adjust the color if needed */
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="centered-title">Recommendations</h1>
        """,
        unsafe_allow_html=True
    )

    st.write("Welcome to the recommendations section. In this section, you’ll find places and events that have been categorized as kid-friendly by Google Place API. Choose your arrondissement and start discovering for yourself!") 

    # Clean the zip_code column to ensure correct formatting
    df_kf_places_paris['zip_code'] = df_kf_places_paris['zip_code'].astype(str).str.replace(',', '').str.zfill(5)

    # List of arrondissement options based on postal codes
    arrondissements = [
        "75001", "75002", "75003", "75004", "75005", "75006", "75007", "75008", "75009",
        "75010", "75011", "75012", "75013", "75014", "75015", "75016", "75017", "75018", "75019", "75020"
    ]

    # Define recommendation types and map them to relevant data fields
    recommendation_options = {
        "Events": {
            "data": df_faire,
            "address_field": "Adresse du lieu",
            "postal_field": "Code postal",
            "name_field": "Titre"
        },
        "Park": {
            "data": df_kf_places_paris,
            "address_field": "vicinity",
            "postal_field": "zip_code",
            "name_field": "name",
            "type_filter": "park"
        },
        "Restaurant": {
            "data": df_kf_places_paris,
            "address_field": "vicinity",
            "postal_field": "zip_code",
            "name_field": "name",
            "type_filter": "restaurant"
        },
        "Museum": {
            "data": df_kf_places_paris,
            "address_field": "vicinity",
            "postal_field": "zip_code",
            "name_field": "name",
            "type_filter": "museum"
        },
        "Amusement Park": {
            "data": df_kf_places_paris,
            "address_field": "vicinity",
            "postal_field": "zip_code",
            "name_field": "name",
            "type_filter": "amusement_park"
        },
        "Zoo": {
            "data": df_kf_places_paris,
            "address_field": "vicinity",
            "postal_field": "zip_code",
            "name_field": "name",
            "type_filter": "zoo"
        }
    }

    # Streamlit Interface
    st.markdown('<p class="centered-text">Kid-Friendly Recommendations in Paris</p>', unsafe_allow_html=True)
    st.write("Select an arrondissement and type of recommendation to see kid-friendly options available.")

    # Dropdown for selecting an arrondissement
    selected_arrondissement = st.selectbox("Select Arrondissement", arrondissements)

    # Dropdown for selecting the type of recommendation
    selected_recommendation_type = st.selectbox("Select Recommendation Type", list(recommendation_options.keys()))

    # Filter and Display Results
    if selected_recommendation_type and selected_arrondissement:
        # Retrieve dataset and fields based on recommendation type
        recommendation_data = recommendation_options[selected_recommendation_type]["data"]
        address_field = recommendation_options[selected_recommendation_type]["address_field"]
        postal_field = recommendation_options[selected_recommendation_type]["postal_field"]
        name_field = recommendation_options[selected_recommendation_type]["name_field"]

        # Additional filtering for df_kf_places_paris by type
        if "type_filter" in recommendation_options[selected_recommendation_type]:
            type_filter = recommendation_options[selected_recommendation_type]["type_filter"]
            filtered_data = recommendation_data[
                (recommendation_data[postal_field] == selected_arrondissement) &
                (recommendation_data["type"] == type_filter)
            ]
        else:
            filtered_data = recommendation_data[recommendation_data[postal_field] == selected_arrondissement]

        # Display recommendations
        if not filtered_data.empty:
            st.write(f"Kid-Friendly {selected_recommendation_type} in {selected_arrondissement}:")
            for idx, row in filtered_data.iterrows():
                st.write(f"**{row[name_field]}**")
                st.write(f"Address: {row[address_field]}")
                st.write("---")
        else:
            st.write(f"No {selected_recommendation_type} found in {selected_arrondissement}.")
elif page == pages[4]:

    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: black;  /* Adjust the color if needed */
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="centered-title">Machine Learning</h1>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write("In this section, we will recommend restaurants that, although not officially categorized as kid-friendly, are predicted by a machine learning model analyzing customer reviews to be welcoming to children. This ensures you and your family can enjoy a great time together.")

    data["zip_code"] = data["zip_code"].astype(str)

    # Load vectorizers and models
    bow = joblib.load("count_vectorizer.joblib")
    naive_model = joblib.load("kids_friendly_model.joblib")
    tfidf_vectorizer = joblib.load("tfidf_vectorizer.joblib")
    logistic_model = joblib.load("kids_friendly_logistic2_model.joblib")

    # Initialize stop words and lemmatizer
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    # Helper functions for text processing
    def get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0]
        tag_dict = {"R": wordnet.ADV, "N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ}
        return tag_dict.get(tag, wordnet.NOUN)

    def tokenize(row):
        tokens = word_tokenize(row)
        return [word.lower() for word in tokens if word.isalpha()]

    def lemmatizer_with_pos(row):
        return [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in row]

    def remove_sw(row):
        return [word for word in row if (word not in stop_words and len(word) > 1)]

    # Prediction functions for each model
    def naive_model_predict(text):
        tokens = tokenize(text)
        tokens_lemmatized = lemmatizer_with_pos(tokens)
        tokens_clean = remove_sw(tokens_lemmatized)
        blob = " ".join(tokens_clean)
        text_array = bow.transform([blob])
        pred = naive_model.predict(text_array)
        return "Kid-Friendly Restaurant" if pred[0] == 1 else "Regular Restaurant"

    def logistic_model_predict(text):
        tokens = tokenize(text)
        tokens_lemmatized = lemmatizer_with_pos(tokens)
        tokens_clean = remove_sw(tokens_lemmatized)
        blob = " ".join(tokens_clean)
        text_array = tfidf_vectorizer.transform([blob])
        pred = logistic_model.predict(text_array)
        return "Kid-Friendly Restaurant" if pred[0] == 1 else "Regular Restaurant"

    # Streamlit interface
    st.title("Restaurant Selection in Paris")
    st.write("Choose an arrondissement and a restaurant to see if it's kid-friendly according to two different models.")

    # Arrondissement selection (by zip code)
    zip_codes = sorted(data["zip_code"].unique())
    chosen_zip_code = st.selectbox("Select an arrondissement (by zip code):", zip_codes)

    # Filter data based on chosen zip code
    filtered_data = data[data["zip_code"] == chosen_zip_code]

    # Display restaurants if any are found in the selected zip code
    if not filtered_data.empty:
        # Drop duplicates and create a display name for the selectbox
        restaurant_options = filtered_data[["unique_id", "name"]].drop_duplicates()
        restaurant_options["display_name"] = restaurant_options["unique_id"] + " - " + restaurant_options["name"]
        chosen_restaurant = st.selectbox("Select a restaurant:", restaurant_options["display_name"])

        # Extract unique_id and name from the selected restaurant
        chosen_unique_id = restaurant_options[restaurant_options["display_name"] == chosen_restaurant]["unique_id"].values[0]
        chosen_name = restaurant_options[restaurant_options["display_name"] == chosen_restaurant]["name"].values[0]

        # Get the selected restaurant info based on unique_id and name
        restaurant_info = filtered_data[(filtered_data["unique_id"] == chosen_unique_id) & (filtered_data["name"] == chosen_name)]

        # Check if reviews exist and pass them to both models
        if not restaurant_info.empty and "reviews" in restaurant_info.columns:
            review_text = restaurant_info.iloc[0]["reviews"]
            address = restaurant_info.iloc[0]["formatted_address"]

            # Display address
            st.write(f"Address: {address}")

            # Only predict if review_text is valid
            if isinstance(review_text, str) and review_text.strip():
                # Get predictions from both models
                naive_result = naive_model_predict(review_text)
                logistic_result = logistic_model_predict(review_text)

                # Display both results
                st.write(f"The restaurant '{chosen_name}' in {chosen_zip_code} is classified as:")
                st.write(f"**Naive Bayes Model Result**: {naive_result}")
                st.write(f"**Logistic Regression Model Result**: {logistic_result}")
            else:
                st.write("Review text is missing or invalid for the selected restaurant.")
        else:
            st.write("No reviews available for the selected restaurant.")
    else:
        st.write("No restaurants found in the selected arrondissement.")

elif page == pages[5]:

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: black;  /* Adjust the color if needed */
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        <h1 class="centered-title">API</h1>
        """,
        unsafe_allow_html=True
    ) 


    st.write("Welcome to the data download center! Here, you’ll find a variety of datasets that were used to build insights for this project. Each dataset focuses on different aspects of kid-friendly places and activities across Paris, including popular locations, population statistics, events, and trends over time. To make it easy for you to access and explore the data, simply select the dataset you wish to download.")
    st.write("You can analyze the information, replicate results, or explore new insights about family-friendly places and activities in Paris.")
    #st.markdown("<br><br>", unsafe_allow_html=True)
    

    # URL API
    api_base_url = "https://myapi-ayrr.onrender.com/api"
    

    # Streamlit Interface
    st.markdown(
    """
    <style>
    .centered-text {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True)
    st.markdown('<p class="centered-text">Kids Friendly Data - Download Center</p>', unsafe_allow_html=True)
    st.markdown("***Select a dataset to download:***")
    
    # List datasets to download
    datasets = {
            "Detailed Places": "download_detailed_places",
            "Trends 5 Years": "download_trends_5years",
            "Population France": "download_population_france",
            "Parks with Playground": "download_parks_with_playground",
            "Events": "download_faire",
            "Paris Population Data": "download_paris_data",
            "Trends Comparison": "download_trends_comparison",
            "General Scores": "download_gral_df_scores",
            "KF Places Paris": "download_kf_places_paris"
        }

    # Loop to create a button to download
    for name, endpoint in datasets.items():
        # Add a button
        if st.button(f"Download {name}"):
            # Requests
            response = requests.get(f"{api_base_url}/{endpoint}")
            
            if response.status_code == 200:
                st.success(f"{name} downloaded successfully!")
                # Download and save dataset
                st.download_button(
                    label=f"Download {name}",
                    data=response.content,
                    file_name=f"{name.replace(' ', '_').lower()}.csv",
                    mime="text/csv"
                )
            else:
                st.error(f"Failed to download {name}. Please try again.")
