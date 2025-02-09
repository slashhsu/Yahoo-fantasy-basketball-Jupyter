# Walmart E-Commerce Sales Analysis

## Overview
Walmart, the largest retail store in the United States, has significantly expanded its **e-commerce** operations. By the end of **2022**, e-commerce accounted for **$80 billion in sales**, making up **13% of Walmart's total revenue**. 

Public holidays such as the **Super Bowl, Labour Day, Thanksgiving, and Christmas** play a crucial role in influencing Walmart's sales patterns. This project aims to build a **data pipeline** to analyze **supply and demand fluctuations** around these holidays and conduct preliminary data analysis.

---

## Objectives
✅ Develop a data pipeline to analyze Walmart’s e-commerce sales trends.  
✅ Identify key factors affecting sales fluctuations around holidays.  
✅ Perform data transformations and aggregations to extract actionable insights.  
✅ Store cleaned and aggregated data for further analysis.  

---

## Data Sources
The project uses two primary data sources:

### **1. Grocery Sales (PostgreSQL Database)**
This dataset includes weekly sales for Walmart stores, with the following columns:
- **Index** – Unique row ID
- **Store_ID** – Store number
- **Date** – Week of sales
- **Weekly_Sales** – Sales for the given store
- **Dept** – Department number

### **2. Complementary Data (extra_data.parquet)**
This dataset contains external factors influencing sales:
- **IsHoliday** – Binary (1 if the week contains a public holiday, 0 otherwise)
- **Temperature** – Temperature during the sale period
- **Fuel_Price** – Cost of fuel in the region
- **CPI** – Consumer Price Index
- **Unemployment** – Unemployment rate
- **Markdown1-4** – Number of promotional markdowns
- **Store Size & Type** – Store category based on size

---

## Data Processing Pipeline
### **1. Extract Data**
- Load **grocery_sales** from PostgreSQL.
- Read **extra_data.parquet** into a Pandas DataFrame.
- Merge both datasets on the **index** column.

### **2. Transform Data**
- **Handle missing values** by filling NaNs with column means.
- Convert the **Date** column to DateTime format.
- Extract the **Month** from the Date column.
- Filter out records where **Weekly_Sales < 10,000**.
- Drop unnecessary columns including **Temperature, Fuel_Price, Markdowns, Size, and Type**.

### **3. Aggregate Data**
- Group by **Month** to calculate the average **Monthly Sales**.
- Store the transformed dataset as **clean_data**.
- Store the aggregated dataset as **agg_data**.

---

## Implementation
### **Technologies Used**
🛠 **PostgreSQL** – Storing and querying grocery sales data.  
🛠 **Pandas** – Data manipulation and transformation.  
🛠 **Parquet** – Handling structured complementary data.  
🛠 **CSV** – Storing cleaned and aggregated data outputs.  

### **Code Snippet**
```python
import pandas as pd

def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on='index')
    return merged_df

# Extract Data
merged_df = extract(grocery_sales, "extra_data.parquet")

# Transform Data
def transform(raw_data):
    raw_data.fillna({
        'CPI': raw_data['CPI'].mean(),
        'Weekly_Sales': raw_data['Weekly_Sales'].mean(),
        'Unemployment': raw_data['Unemployment'].mean(),
    }, inplace=True)
    raw_data["Date"] = pd.to_datetime(raw_data["Date"], format="%Y-%m-%d")
    raw_data["Month"] = raw_data["Date"].dt.month
    raw_data = raw_data.loc[raw_data["Weekly_Sales"] > 10000, :]
    raw_data = raw_data.drop(["index", "Temperature", "Fuel_Price", "MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "Size", "Type", "Date"], axis=1)
    return raw_data

clean_data = transform(merged_df)

# Aggregate Data
def avg_monthly_sales(clean_data):
    agg_data = clean_data.groupby("Month").agg(Avg_Sales=("Weekly_Sales", "mean")).reset_index().round(2)
    return agg_data

agg_data = avg_monthly_sales(clean_data)

# Save Data
clean_data.to_csv("clean_data.csv", index=False)
agg_data.to_csv("sales_per_month.csv", index=False)
```

---

## Results & Insights
📌 **Walmart's e-commerce sales spike around major holidays.**  
📌 **Consumer spending is influenced by economic indicators such as CPI and unemployment.**  
📌 **Stores in different regions exhibit varying sales trends depending on store size and promotions.**  
📌 **Analyzing holiday trends helps Walmart optimize inventory and supply chain strategies.**  
