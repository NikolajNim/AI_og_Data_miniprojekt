import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Kursusgang_5\recipeData.csv', encoding='latin-1')
print(len(df))
df.dropna(inplace=True)
print(len(df))
print(df.head)

df = pd.read_csv(r'Kursusgang_5\pokemon.txt', index_col="Name")
fig = plt.figure()
axis = df["Defense"].plot.hist()

# Scatter plot for Attack vs. Defense
plt.figure(figsize=(10, 6))
plt.scatter(df['Attack'], df['Defense'], color='blue', alpha=0.5)
plt.title('Attack vs. Defense')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.grid(True)

# Scatter plot for Speed vs. HP
plt.figure(figsize=(10, 6))
plt.scatter(df['Speed'], df['HP'], color='red', alpha=0.5)
plt.title('Speed vs. HP')
plt.xlabel('Speed')
plt.ylabel('HP')
plt.grid(True)

plt.show()

plt.show()


