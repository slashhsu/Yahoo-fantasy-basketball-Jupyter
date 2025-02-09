# Fantasy Basketball Analysis

## Overview
This project is focused on analyzing **Fantasy Basketball League** statistics using Python. It processes weekly player performance data, evaluates key metrics, and visualizes results using heatmaps for a better understanding of team strengths and weaknesses.

---

## Objectives
✅ Process and analyze fantasy basketball statistics.  
✅ Identify top-performing players and teams.  
✅ Visualize key metrics using heatmaps.  
✅ Generate actionable insights for fantasy league strategy.  

---

## Dataset
The dataset includes the following key statistics for each team:
- **FGM (Field Goals Made)**
- **FGA (Field Goals Attempted)**
- **FG% (Field Goal Percentage)**
- **FTM (Free Throws Made)**
- **FTA (Free Throws Attempted)**
- **FT% (Free Throw Percentage)**
- **3PTM (Three-Point Made)**
- **3PTA (Three-Point Attempted)**
- **3PT% (Three-Point Percentage)**
- **PTS (Total Points Scored)**
- **REB (Total Rebounds)**
- **AST (Assists)**
- **ST (Steals)**
- **BLK (Blocks)**
- **TO (Turnovers)**
- **DD (Double-Doubles)**

---

## Implementation
### **Technologies Used**
- **Python** – Data processing and visualization.
- **Pandas** – Data manipulation and transformation.
- **Matplotlib & Seaborn** – Creating visual representations.
- **Jupyter Notebook** – Running the analysis interactively.

### **Code Snippet**
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("fantasy_basketball_stats.csv")

# Generate Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(data.set_index("Team"), annot=True, cmap="RdYlGn", linewidths=0.5)
plt.title("Fantasy Basketball Week 8 Performance")
plt.show()
```

---

## Results & Insights
📌 **Certain teams excel in shooting efficiency, while others dominate rebounds and assists.**  
📌 **High turnovers negatively impact some teams' performance.**  
📌 **Teams with a balanced stat distribution perform better overall.**  
