import pandas as pd

# Step 1: Read the CSV file into a DataFrame
filename = 'lego_setsHB.csv'
df = pd.read_csv(filename)

# Step 2: Get general information about the dataset
print("Dataset Information:")
df.info()

print("\nDataset Description:")
print(df.describe())

# Step 3: Filter LEGO sets with star_rating >= 4
high_rating_df = df[df['star_rating'] >= 4]

# Step 4: Count the number of LEGO sets with star_rating >= 4
num_high_rating_sets = high_rating_df['prod_id'].count()
print("\nNumber of LEGO sets with star rating >= 4:", num_high_rating_sets)

# Step 5: Find the average list price for LEGO sets with star_rating >= 4
average_list_price = high_rating_df['list_price'].mean()
print("Average list price of LEGO sets with star rating >= 4:", average_list_price)