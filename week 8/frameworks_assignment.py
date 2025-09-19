import pandas as pd

# Load dataset (metadata.csv in the same folder)
df = pd.read_csv("metadata.csv")

# Preview
print(df.head())
print(df.shape)       # rows, cols
print(df.info())      # data types
print(df.isnull().sum().head(10))  # missing values check

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Example: create abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Drop rows with missing year (optional)
df_clean = df.dropna(subset=['year'])

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Publications by year
year_counts = df_clean['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# 2. Top journals
top_journals = df_clean['journal'].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top Journals Publishing COVID-19 Research")
plt.show()

# 3. Word cloud for titles
text = " ".join(df_clean['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# 4. Distribution by source
df_clean['source_x'].value_counts().plot(kind='bar')
plt.title("Publications by Source")
plt.show()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Year range filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

st.write("### Sample Data", filtered.head())

# Publications by year
st.write("### Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.write("### Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
st.pyplot(fig)

# Word cloud
st.write("### Word Cloud of Titles")
text = " ".join(filtered['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)


