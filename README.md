
# Fake News Verify

This project is a web application that uses an LSTM model to predict whether a given news article is fake or real. It aims to help users distinguish between credible and fabricated news using AI technology.




## Project Explaination

- News Classification: We are using datasets which are categorized into two distinct classes: true news and fake news.

- NLP Techniques and EDA: Our approach involves applying advanced Natural Language Processing techniques, coupled with extensive Exploratory Data Analysis (EDA), to gain insights from the dataset and enhance model accuracy.

- Robust Model Building: Our focus is on constructing a robust machine learning model for news classification. We emphasize both the development of the model architecture and the selection of optimal hyperparameters to achieve the best possible performance.

- Performance Evaluation: We rigorously evaluate the model's performance using industry-standard metrics. This assessment ensures that our solution delivers accurate and reliable results.

- User-Friendly UI: We've designed an intuitive and user-friendly User Interface (UI) that enables users to conveniently input news articles for classification.

- Flask API Integration: To facilitate seamless interaction between the user and the model, we've integrated a Flask API. This backend API handles the classification and prediction tasks, ensuring smooth functionality.

By unifying these components, we've created a comprehensive solution that not only accurately classifies news articles but also provides an accessible and interactive experience for users. Our solution is a testament to the synergy between Python programming, sophisticated NLP techniques, and the power of LSTM models in the realm of news verification.





## Demo

![Animation](https://github.com/harsh7898/Fake_News_Verify/assets/46092423/29e8ec4b-7851-4a1e-81ea-fa6ee8b1e437)



## Installation

Installing libraries for the project

```bash
pip install pandas
pip install numpy
pip install matplotlib seaborn textblob plotly cufflinks
pip install nltk wordcloud
pip install scikit-learn tensorflow
pip install tensorflow
pip install flask
```


    
## Run Locally

Clone the project

```bash
  git clone https://github.com/harsh7898/Fake_News_Verify.git
```

Go to the project directory

```bash
  cd Fake_News_Verify
```


Start the server

```bash
  python app.py
```

