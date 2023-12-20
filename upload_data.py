from pymongo.mongo_client import MongoClient
import pandas as pd
import json



# unifrom resource indentifier.
uri = "mongodb+srv://datascience:datascience@cluster0.4vt0cq9.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# Creating database name and collection name

DATABASE_NAME="ML_PROJECT_DATASET"
COLLECTION_NAME="waferfault"





df=pd.read_csv(f"C:\TheBritishCollege\DataScience\Wafer_sensor_project\Data\wafer_dataset.csv")

df_as_json=json.load(df.T.to_json)

#  NOw dump data in database.
client[DATABASE_NAME][COLLECTION_NAME]=df_as_json


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)