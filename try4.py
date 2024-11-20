import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load the CSV file into a DataFrame
df = pd.read_csv("C:/Users/HP/Desktop/calendar.csv")

# Convert 'date' to datetime and 'price' to numeric (removing '$' sign)
df["date"] = pd.to_datetime(df["date"])

# Assuming 'df' is your DataFrame
df["price"] = pd.to_numeric(
    df["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
)

# Filter only rows where 'available' is "t"
df_filtered = df[df["available"] == "t"]

def bro():
    print("Select from below options to view charts:")
    print("Enter 1 to view Price Over Time Matplotlib")
    print("Enter 2 to view Price Over Time(Seaborn Style) ")
    print("Enter 3 to view Datasheet information")
    print("Enter 4 to view Distribution of Availability pie chart")
    print("Enter 5 to view Distribution of Availability bar chart ")
    print("Enter 6 to exit")
    value=int(input("Please enter desired number:"))

    if value == 1:
        plt.figure(figsize=(12, 6))
        plt.plot(df_filtered["date"], df_filtered["price"], marker='o', linestyle='-', color='b')
        plt.title("Price Over Time (Available = 't')", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Price", fontsize=14)
        plt.xticks(rotation=45)
        plt.yticks(range(0, 301, 50))
        plt.grid(visible=True, linestyle='--', alpha=0.5)
        plt.show()
        choice=input("Press y to return to menu and x to exit:")
        if choice=="y":
            bro()
        else:
            exit()

    elif value == 2:
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_filtered, x="date", y="price", marker="o", color="g")
        plt.title("Price Over Time (Seaborn Style)", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Price", fontsize=14)
        plt.xticks(rotation=45)
        plt.yticks(range(0, 301, 50))
        plt.show()
        choice=input("Press y to return to menu and x to exit:")
        if choice=="y":
            bro()
        else:
            exit()

    elif value == 3:
        print("Datasheet information")
        print(df.info())
        choice=input("Press y to return to menu and x to exit:")
        if choice=="y":
            bro()
        else:
            exit()
        

    elif value == 4:
        available_counts = df["available"].value_counts()
        # Create the pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(available_counts, labels=available_counts.index, autopct='%1.1f%%', startangle=90, colors=["lightcoral", "lightskyblue"])
        plt.title("Distribution of Availability", fontsize=14)
        plt.show()
        choice=input("Press y to return to menu and x to exit:")
        if choice=="y":
            bro()
        else:
            exit()


    elif value == 5:
        available_counts = df["available"].value_counts()

        # Create the bar chart
        plt.figure(figsize=(8, 5))
        plt.bar(available_counts.index, available_counts.values, color=["lightcoral", "lightskyblue"])
        plt.title("Count of Availability (True or False)", fontsize=14)
        plt.xlabel("Availability Status", fontsize=12)
        plt.ylabel("Count", fontsize=12)
        plt.show()
        choice=input("Press y to return to menu and x to exit:")
        if choice=="y":
            bro()
        else:
            exit()

    elif value == 6:
        exit()

    else:
        print("Please enter the numer in the criteria")
        bro()
bro()


