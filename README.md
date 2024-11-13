Kid-Friendly Places in Paris

Project Overview This project is a data-driven Streamlit application designed to help parents and caregivers explore and discover kid-friendly places in Paris. The app provides insights and recommendations based on data about various locations, from restaurants to parks and events, making it easier for families to plan outings in the city.

Motivation As a new parent, I realized that exploring cities with young children often requires a shift in priorities. Many parents want to find spaces that are welcoming to children without compromising on the overall experience. The aim of this app is to address this need, especially for parents who are new to Paris or simply want to explore child-friendly spots more easily.

Features The app includes several interactive pages, each serving a different purpose:

Overview of the Project An introduction to the project and its objectives, along with some background on the motivation behind the app.

Data Exploration An overview of the datasets used in this project, including sources and data preprocessing details.

Data Analysis Detailed visual analysis of:

Population distribution by arrondissement in Paris. Monthly trends of Google searches for kid-friendly locations in Paris. Analysis of kid-friendly events, parks, and restaurants by arrondissement.

Recommendations Provides tailored recommendations for kid-friendly places in Paris. Users can filter by arrondissement and select the type of place they want to explore, such as restaurants, parks, museums, and more.

Machine Learning A predictive model is included to analyze restaurant reviews and predict whether a restaurant is kid-friendly, even if it isn’t explicitly categorized as such. This uses a natural language processing (NLP) model trained on review data to classify restaurants as kid-friendly or not.

Dataset Description The datasets were obtained from a variety of sources, including web scraping, Google Trends API, and public datasets. Key datasets include:

Population Data: Information on the population in France and Paris by arrondissement. Kid-Friendly Places Data: Data on various locations in Paris categorized as kid-friendly (e.g., restaurants, parks, museums). Event Data: A dataset containing family-friendly events in Paris.

Machine Learning Model The application uses a natural language processing (NLP) machine learning model to predict whether a restaurant would be welcoming to children based on customer reviews. Several models were tested, including:

Multinomial Naive Bayes with a bag-of-words approach. Logistic Regression with TF-IDF vectorization and SMOTE resampling to handle class imbalance. After testing and cross-validation, the model with the best performance was selected for deployment within the app.

Getting Started

Prerequisites

-Python 3.7+ -Streamlit -Pandas, Numpy -Scikit-learn -NLTK -Plotly (for interactive graphs)

Future Improvements

-Expand the dataset to cover more locations and add more recent data. -Incorporate additional NLP techniques to improve the predictive model. -Add more features, such as user feedback, to improve recommendation accuracy.

Application link:

https://kidsfriendlyapp.streamlit.app/

Project management:

https://trello.com/b/SnfNc1p3/final-projet-ironhack

Contributing If you would like to contribute, please submit a pull request or open an issue for any improvements, bug fixes, or feature requests.

Author Xinly ROY