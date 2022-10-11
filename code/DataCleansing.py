# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:12:09 2022
Presentation > Infographic

@author: choi-1
"""

import sqlite3
import pandas as pd
import sweetviz as sv

# Function to convert names into initials
# Plan on later creating a CSV of Customer IDs and Full Customer Names 
def initials(name):
    if(name == "N/A"):
        return "N/A"
    else: 
        string = name.split()
        result = ""
        for i in range(len(string)):
            result += string[i][0].upper()
        return result
    return result;

conn = sqlite3.connect("C:\\Users\\choi-1\\AppData\\Roaming\\DBeaverData\\workspace6\\MCM\\blossom.db")

# Note need to have fields with spaces in them encapsulated by '' instead of ""    
myQuery = "select\
    	t.'Transaction ID',\
    	t.'Payment ID',\
        t.Date,\
        t.Time,\
    	t.'Source',\
    	t.'Event Type',\
    	t.'Gross Sales',\
    	t.'Net Sales',\
    	t.'Net Total',\
    	t.'Total Collected',\
    	t.'Discount Name',\
    	t.Discounts,\
    	t.Tip,\
    	t.'Service Charges',\
    	t.Tax,\
    	t.Fees,\
    	t.'Fee Percentage Rate',\
    	t.'Fee Fixed Rate',\
    	t.'Partial Refunds',\
    	t.Cash,\
    	t.Card,\
    	t.'Card Brand',\
    	t.'Card Entry Methods',\
    	t.'Gift Card Sales',\
    	t.'Square Gift Card',\
    	t.'Customer ID',\
    	t.'Customer Name',\
    	i.Category,\
    	i.Item,\
    	i.Qty,\
    	i.'Price Point Name',\
        i.'Modifiers Applied'\
    from\
    	transactions t\
    inner join items i on\
    	t.'Transaction ID' = i.'Transaction ID'"
    
dftmp = pd.read_sql_query(myQuery, conn)

conn.close()
df = pd.DataFrame(dftmp)
df = df.fillna("N/A")
mask = df["Fee Percentage Rate"] == "N/A"
df.loc[mask, "Fee Percentage Rate"] = 0
# print(df["Fee Percentage Rate"])

pd.set_option("display.max_columns", None)

 # Columns : 'Transaction ID', 'Payment ID', 'Date', 'Time', 'Source', 'Event Type',
 #           'Gross Sales', 'Net Sales', 'Net Total', 'Total Collected',
 #           'Discount Name', 'Discounts', 'Tip', 'Service Charges', 'Tax', 'Fees',
 #           'Fee Percentage Rate', 'Fee Fixed Rate', 'Partial Refunds', 'Cash',
 #           'Card', 'Card Brand', 'Card Entry Methods', 'Gift Card Sales',
 #           'Square Gift Card', 'Customer ID', 'Customer Name', 'Category', 'Item',
 #           'Qty', 'Price Point Name', 'Modifiers Applied'
 # print(df.columns)

# Unique Categories: 'Frappe Selection' 'Soft Serve' 'Hot Menu Selection' 'Latte Selection'
#                    'Float Selection' 'Parfait Selection' 'Shaved Ice Selection'
#                    'Tea Selection' 'Toppings' 'Kokuto Jelly Selection' 'Other' 'None'
#                    'Fruity Floral Matcha Latte' 'Bakery & Pastry' 'Ice Cream' 'Accessories'
#                    'Hot Foods' 'Seasonal ' 'Festival '
# print(df['Category'].unique())

# Updating entries to be cohesive with the new menu Categorization

# for ind in df.index:
#     if(df.iloc[ind]["Category"] == "Hot Menu Selection"):
#         print(df.iloc[ind]["Item"])


# Due to time constraints, I ended up using a very primitive method
# I am aware traversing through a dataframe is not optimal
# If I had more time, I would be researching masks and replace
# or subset and concat as a way to modify my DataFrame

# Subset, pd.concat
#df2 = df[["Item", "Category", "Modifiers Applied"]]

# Array of indexes that have been modified
#tmp = []

# WARNING use dataframe.loc['index','column'] = "my value" to replace data!
# Even if you use loc, dataframe.loc['index']['column'] is CHAIN referencing and will change the data!
""" REMINDER: FIX ITEM NAMES FOR OLD HOT DRINKS ie; Hot Matcha Late => Matcha Latte """
for ind in df.index:
     # If the "Category" is "Hot Menu Selection", it needs to be updated
     if(df.loc[ind, "Category"] == "Hot Menu Selection"):
         # If the "Item" contains the word "Latte" then set it to "Latte Selection" 
         # It is crucial to check for this first before looking for Teas because Teas were labeled in "Item"
         if("Latte" in df.loc[ind, "Item"]):
#             tmp.append(ind)
             df.loc[ind,"Category"] = "Latte Selection"
             # And adjust the modifier to contain the word "Hot"
             if((df.loc[ind, "Modifiers Applied"] == "") | (df.loc[ind, "Modifiers Applied"] == "N/A")):
                 df.loc[ind, "Modifiers Applied"] = "Hot"
             else:
                 df.loc[ind, "Modifiers Applied"] = str(df.loc[ind, "Modifiers Applied"]) + ", Hot"
         # If the "Item" contains the word "Matcha" or "Hojicha" set it to "Tea Selection"
         # Hot Matcha, Hot Plain Matcha, Hot Hojicha, Hot Plain Hojicha
         elif(("Matcha" in df.loc[ind, "Item"]) | ("Hojicha" in df.loc[ind, "Item"])):
#            tmp.append(ind)
             df.loc[ind, "Category"] = "Tea Selection"
             # And adjust the modifier to contain the word "Hot"
             if((df.loc[ind, "Modifiers Applied"] == "") | (df.loc[ind, "Modifiers Applied"] == "N/A")):
                 df.loc[ind, "Modifiers Applied"] = "Hot"
             else:
                 df.loc[ind, "Modifiers Applied"] = str(df.loc[ind, "Modifiers Applied"]) + ", Hot"
        # Ozenzai and Oshiruko stay in "Hot Menu Items"
         else: pass

# Looping through modified indexes to see that values have been updated correctly
#for i in tmp:
#    print(df.loc[i, "Category"])
#    print(df.loc[i, "Modifiers Applied"])

# Creating a new list to store the temperature of menu items
temp = []

for ind in df.index:
    # If Modifier contains Hot, set temperature to Hot
    if(("Hot" in df.loc[ind, "Modifiers Applied"]) | ("hot" in df.loc[ind]["Modifiers Applied"])):
        temp.append("Hot");
    # If Category is Hot Food, set temperature to hot
    elif(df.loc[ind, "Category"] == "Hot Foods"):
        temp.append("Hot");
    # If Category is Bakery & Pa stry, set temperature to Pastry
    elif(df.loc[ind, "Category"] == "Bakery & Pastry"):
        temp.append("Pastry");
    # If Category is Other or Topping, set temperature to Other
    elif((df.loc[ind, "Category"] == "Other") | (df.loc[ind, "Category"] == "Toppings")):
        temp.append("Other");
    # Else set temperature to Cold
    else: temp.append("Cold");

# Checking that the list's size is the same as the number of rows
# Ensures that every row has a column and that the data will align and correspond
# print(len(temp))
df['Temperature Type'] = temp
# Checking that the Column was added
# print(df.columns)

# Changing dtypes
# df supported dtypes: object, int64, float64, bool, datetime64, datedelta[ns], category

# Checking before
# print(df.dtypes)

df["Date"] = pd.to_datetime(df["Date"])
# If a date is not specified, pd.to_datetime will assign the current date
df["Time"] = pd.to_datetime(df["Time"])
# Removing the assigned Date from the 'Time' field
df["Time"] = [time.time() for time in df["Time"]]

# Error because "$" Decided to let Tableau handle the data type
# df["Gross Sales"] = df["Gross Sales"].astype("float")
# df["Net Sales"] = df["Net Sales"].astype("float")
# df["Net Total"] = df["Net Total"].astype("float")
# df["Total Collected"] = df["Total Collected"].astype("float")
# df["Discounts"] = df["Discounts"].astype("float")
# df["Tip"] = df["Tip"].astype("float")
# df["Service Charges"] = df["Service Charges"].astype("float")
# df["Tax"] = df["Tax"].astype("float")
# df["Fees"] = df["Fees"].astype("float")
# Cannot Convert N/A
df["Fee Percentage Rate"] = df["Fee Percentage Rate"].astype("float")
# df["Fee Fixed Rate"] = df["Fee Fixed Rate"].astype("float")
# df["Partial Refunds"] = df["Partial Refunds"].astype("float")
# df["Cash"] = df["Cash"].astype("float")
# df["Card"] = df["Card"].astype("float")
# df["Gift Card Sales"] = df["Gift Card Sales"].astype("float")
# df["Square Gift Card"] = df["Square Gift Card"].astype("float")
# df["Qty"] = df["Qty"].astype("int")


for ind in df.index:
    df.loc[ind, "Customer Name"] = initials(df.loc[ind, "Customer Name"])



# Checking changes were made
# print(df.dtypes)
# Checking that 'Time' no longer contains a Date value
# print(df['Date'].compare(df['Time']))

# Final Check before exporting to CSV and EDA via SweetViz
# print(df.info)
print(df.dtypes)

# Exporting CSV
# WARNING: WILL OVERWRITE EXISTING FILE
df.to_csv("E:\\!DataAnalyticsBootcamp\!Portfolio\Food Service - MCM\TransactionDetails.csv")
# Reading in the exported CSV via pandas to prep for sweetviz
tmp = pd.read_csv("E:\\!DataAnalyticsBootcamp\!Portfolio\Food Service - MCM\TransactionDetails.csv")
# Wait and chill, 133,782 rows so it may take a while
report = sv.analyze(tmp)
report.show_html("E:\!DataAnalyticsBootcamp\!Portfolio\Food Service - MCM\sweetvizanalysis.html")


# Note: reading from pandas.read_csv() would also produce a pandas DataFrame type compatible with sweetviz.analyze
# df = pd.read_csv("")

# SweetViz Data Quality Analysis
# report = sv.analyze(df)
# report.show_html(df)