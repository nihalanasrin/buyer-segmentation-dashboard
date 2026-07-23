import pandas as pd
clients = pd.read_csv("data/clients.csv")
print(clients[clients["country"]=="UK"])

