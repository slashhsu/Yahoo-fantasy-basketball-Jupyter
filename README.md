# Fantasy Basketball Analysis

## Overview
This project analyzes **Fantasy Basketball League** performance using Python, leveraging **web scraping**, advanced data manipulation, and visualization techniques. The goal is to extract real-time fantasy basketball data, assess team and player performance, identify key trends, and provide actionable insights for fantasy basketball strategies.

---

## Objectives
✅ Extract real-time fantasy basketball data using web scraping.  
✅ Process and analyze fantasy basketball statistics.  
✅ Identify top-performing players and teams.  
✅ Visualize key performance metrics using heatmaps and statistical plots.  
✅ Develop data-driven insights for fantasy team optimization.  

---

## Dataset
The dataset includes weekly performance statistics for multiple fantasy basketball teams. Key metrics include:
- **Field Goals (FGM, FGA, FG%)** – Shooting accuracy and efficiency.
- **Free Throws (FTM, FTA, FT%)** – Performance at the free-throw line.
- **Three-Point Shooting (3PTM, 3PTA, 3PT%)** – Long-range shooting capabilities.
- **Points (PTS)** – Total points scored by a team.
- **Rebounds (REB)** – Offensive and defensive rebounds.
- **Assists (AST)** – Playmaking abilities.
- **Steals (ST) & Blocks (BLK)** – Defensive capabilities.
- **Turnovers (TO)** – Ball security and possession control.
- **Double-Doubles (DD)** – Number of players achieving double digits in two statistical categories.

---

## Implementation
### **Technologies Used**
- **Python** – Web scraping, data processing, and visualization.
- **BeautifulSoup & Selenium** – Extracting real-time fantasy basketball data.
- **Pandas** – Data manipulation and transformation.
- **Matplotlib & Seaborn** – Advanced visualization techniques.
- **Jupyter Notebook** – Interactive analysis and reporting.

### **Code Workflow**
#### **1. Web Scraping & Data Extraction**
- Use **BeautifulSoup** and **Selenium** to scrape real-time fantasy basketball data.
- Extract relevant statistics from league websites.

#### **2. Data Cleaning & Transformation**
- Handle missing values and ensure proper data formatting.
- Calculate statistical insights such as **FG%, FT%, and 3PT%**.
- Aggregate team-level performance metrics.

#### **3. Data Visualization**
- Generate **heatmaps** to analyze team strengths and weaknesses.
- Create **bar charts and histograms** for key performance indicators.
- Use **scatter plots** to find correlations between different metrics.

![image](https://github.com/user-attachments/assets/35ffd39b-55c6-4d9b-9c14-146ecda1f47d)

---

## Code Example
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver

# Web Scraping Function
def scrape_fantasy_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    # Extract relevant data from the page (example placeholder)
    data = []  # Process extracted HTML content into structured data
    return pd.DataFrame(data)

# Load Data
data = scrape_fantasy_data("https://fantasy.nba.com")

# Data Cleaning and Transformation
data.fillna(0, inplace=True)
data['FG%'] = data['FGM'] / data['FGA']
data['FT%'] = data['FTM'] / data['FTA']
data['3PT%'] = data['3PTM'] / data['3PTA']

# Generate Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(data.set_index("Team"), annot=True, cmap="RdYlGn", linewidths=0.5)
plt.title("Fantasy Basketball Week 8 Performance")
plt.show()
```

---

## Results & Insights
📌 **Web scraping allows real-time fantasy basketball updates for better decision-making.**  
📌 **Certain teams excel in shooting efficiency, while others dominate rebounds and assists.**  
📌 **High turnovers negatively impact some teams' performance.**  
📌 **Teams with balanced statistical contributions tend to rank higher overall.**  
📌 **Defensive statistics (steals and blocks) show strong correlation with overall team success.**
