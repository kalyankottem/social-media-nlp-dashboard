# Social Media NLP Dashboard

## Description
This project is an interactive NLP-based dashboard for analyzing social media text data in real time. It processes user-generated content such as tweets, comments, and posts to extract actionable insights for organizations.

The dashboard performs sentiment analysis, trending hashtag detection, toxic content identification, and interactive data visualization.

---

## Problem Statement
Social media platforms generate massive volumes of unstructured text data. Organizations struggle to extract actionable insights such as public sentiment, trending topics, and toxic behavior in real time.

This project addresses that challenge by building a lightweight NLP-powered analytics dashboard.

---

## Objective
- Analyze user-generated social media content  
- Identify sentiment patterns  
- Detect trending keywords / hashtags  
- Flag toxic or abusive content  
- Visualize insights interactively  

---

## Features
### Sentiment Analysis
Classifies posts as:
- Positive  
- Negative  
- Neutral  

### Trending Hashtag Detection
Extracts and ranks most frequently used hashtags.

### Toxic Content Detection
Flags abusive or toxic messages using toxicity lexicon matching.

### Interactive Dashboard Visualizations
Displays:
- Sentiment Distribution Pie Chart  
- Trending Hashtag Bar Chart  
- Toxic Content Table  
- Full Post Analysis Table  

---

## Methodology
1. Load social media text data  
2. Preprocess text  
3. Perform sentiment classification  
4. Detect toxic keywords  
5. Extract hashtags using regex  
6. Aggregate insights  
7. Display results in interactive dashboard  

---

## Technologies Used
- Python  
- Streamlit  
- Pandas  
- Plotly  

---

## Output
The dashboard provides:
- Total Post Count  
- Toxic Post Count  
- Trending Hashtag Count  
- Sentiment Distribution Visualization  
- Trending Hashtag Visualization  
- Toxic Post Monitoring Table  
- Full Post Analysis Table  

---

## Applications
- Social Media Monitoring  
- Brand Reputation Analysis  
- Community Moderation  
- Trend Detection  
- Public Sentiment Tracking  

---

## Future Improvements
- Add CSV Upload Support  
- Connect Live Twitter / Reddit APIs  
- Replace Rule-Based Sentiment with ML Models  
- Use Transformer Models for Toxicity Detection  
- Deploy to Cloud for Real-Time Monitoring  

---

## Run Locally
```bash
python -m streamlit run app.py
```
