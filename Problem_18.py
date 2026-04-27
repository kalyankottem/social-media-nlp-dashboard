import streamlit as st
import pandas as pd
import re
from collections import Counter
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Social Media NLP Dashboard",
    layout="wide"
)

st.title("📊 Social Media NLP Dashboard")

# -----------------------------
# SAMPLE SOCIAL MEDIA DATA
# -----------------------------
posts = [
    "I love this product! #awesome",
    "Worst service ever. Totally disappointed #bad",
    "Amazing customer support #happy",
    "This app is trash and useless",
    "Great experience using the platform #great",
    "Terrible bug in latest update #bug",
    "You are stupid and useless",
    "Fantastic service and smooth UI #awesome",
    "Awful experience with delivery #bad",
    "Love the new design #update"
]

df = pd.DataFrame({"Post": posts})

# -----------------------------
# SENTIMENT WORD LISTS
# -----------------------------
positive_words = {
    "love","amazing","great","awesome",
    "fantastic","happy","smooth"
}

negative_words = {
    "worst","bad","terrible","awful",
    "disappointed","trash","bug"
}

toxic_words = {
    "stupid","useless","idiot","hate"
}

# -----------------------------
# ANALYSIS FUNCTIONS
# -----------------------------
def analyze_sentiment(text):
    
    words = text.lower().split()
    
    pos = sum(word in positive_words for word in words)
    neg = sum(word in negative_words for word in words)
    
    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    return "Neutral"

def detect_toxic(text):
    return any(word in text.lower() for word in toxic_words)

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

# -----------------------------
# PROCESS DATA
# -----------------------------
df["Sentiment"] = df["Post"].apply(analyze_sentiment)
df["Toxic"] = df["Post"].apply(detect_toxic)

all_hashtags = []
for post in df["Post"]:
    all_hashtags.extend(extract_hashtags(post))

hashtag_counts = Counter(all_hashtags)

hashtag_df = pd.DataFrame(
    hashtag_counts.items(),
    columns=["Hashtag","Count"]
).sort_values(
    by="Count",
    ascending=False
)

# -----------------------------
# DASHBOARD METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Posts", len(df))
col2.metric("Toxic Posts", df["Toxic"].sum())
col3.metric("Trending Hashtags", len(hashtag_df))

# -----------------------------
# SENTIMENT CHART
# -----------------------------
sentiment_counts = df["Sentiment"].value_counts()

fig1 = px.pie(
    values=sentiment_counts.values,
    names=sentiment_counts.index,
    title="Sentiment Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# HASHTAG TREND CHART
# -----------------------------
fig2 = px.bar(
    hashtag_df,
    x="Hashtag",
    y="Count",
    title="Trending Hashtags"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# TOXIC CONTENT TABLE
# -----------------------------
st.subheader("⚠ Flagged Toxic Content")

st.dataframe(
    df[df["Toxic"] == True]
)

# -----------------------------
# FULL DATA TABLE
# -----------------------------
st.subheader("📄 Full Post Analysis")

st.dataframe(df)