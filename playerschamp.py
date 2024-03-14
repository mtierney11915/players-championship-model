import pandas as pd
import os
import streamlit as st

#2023
df23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23total.csv')
ttg23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23ttg.csv')
scr23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23scr.csv')
pp23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23pp.csv')
gir23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23gir.csv')
dd23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23dd.csv')
da23=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2023\P23Dacc.csv')

df23.rename(columns={'Player': 'PLAYER'}, inplace=True)
gir23.rename(columns={'PLAYER_ID': 'x'}, inplace=True)
dd23.rename(columns={'PLAYER_ID': 'y'}, inplace=True)
da23.rename(columns={'PLAYER_ID': 'z'}, inplace=True)

#Merges
dnew=pd.merge(df23,ttg23,on='PLAYER',how='left')
dnew=pd.merge(dnew,scr23,on='PLAYER',how='left')
dnew=pd.merge(dnew,pp23,on='PLAYER',how='left')
dnew=pd.merge(dnew,gir23,on='PLAYER',how='left')
dnew=pd.merge(dnew,dd23,on='PLAYER',how='left')
dnew=pd.merge(dnew,da23,on='PLAYER',how='left')

remove=['x','y','z','PLAYER_ID_x','PLAYER_ID_y','PLAYER_ID']
dnew.drop(columns=remove,inplace=True)
file_path=('P23final.csv')
dnew.to_csv(file_path, index=False)

#22
folder_path22 = r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2022'

# List to store DataFrames
dfs22 = []

# Loop through files in the folder
for filename in os.listdir(folder_path22):
    if filename.endswith('.csv'):
        file_paths = os.path.join(folder_path22, filename)

        # Read each file and append it to the list of DataFrames
        dfs22.append(pd.read_csv(file_paths, encoding='latin1'))
dnew22 = dfs22[0]  # Start with the first DataFrame in the list
for dff in dfs22[1:]:
    dnew22 = pd.merge(dnew22, dff, on='PLAYER', how='left')
    filepath22= 'P22final.csv'
    dnew22.to_csv(filepath22, index=False)

#21
folder_path21 = r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2021'

# List to store DataFrames
dfs21 = []

# Loop through files in the folder
for filename in os.listdir(folder_path21):
    if filename.endswith('.csv'):
        file_paths21 = os.path.join(folder_path21, filename)

        # Read each file and append it to the list of DataFrames
        dfs21.append(pd.read_csv(file_paths21, encoding='latin1'))
dnew21 = dfs21[0]  # Start with the first DataFrame in the list
for d in dfs21[1:]:
    dnew21 = pd.merge(dnew21, d, on='PLAYER', how='left')
    filepath21= 'P21finalnew.csv'
    dnew21.to_csv(filepath21, index=False)
#19
folder_path19 = r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2019'

# List to store DataFrames
dfs19 = []

# Loop through files in the folder
for filename in os.listdir(folder_path19):
    if filename.endswith('.csv'):
        file_paths19 = os.path.join(folder_path19, filename)
        # Read each file and append it to the list of DataFrames
        dfs19.append(pd.read_csv(file_paths19, encoding='latin1'))
dnew19 = dfs19[0]  # Start with the first DataFrame in the list
for dd in dfs19[1:]:
    dnew19 = pd.merge(dnew19, dd, on='PLAYER', how='left')
    filepath19= 'P19finalnews.csv'
    dnew19.to_csv(filepath19, index=False)


#18
folder_path18 = r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\2018'

# List to store DataFrames
dfs18 = []

# Loop through files in the folder
for filename in os.listdir(folder_path18):
    if filename.endswith('.csv'):
        file_paths18 = os.path.join(folder_path18, filename)
        # Read each file and append it to the list of DataFrames
        dfs18.append(pd.read_csv(file_paths18, encoding='latin1'))
dnew18 = dfs18[0]  # Start with the first DataFrame in the list
for b in dfs18[1:]:
    dnew18 = pd.merge(dnew18, b, on='PLAYER', how='left')
    filepath18= 'P18final.csv'
    dnew18.to_csv(filepath18, index=False)
#Combine all

file_pathsfinal = [
    r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Finals\P18final.csv',
    r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Finals\P19finalnews.csv',
    r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Finals\P21finalnew.csv',
    r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Finals\P22final.csv',
    r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Finals\P23final.csv'
]

# Initialize an empty list to store DataFrames
finaldfs = []

# Loop through file paths
for file_path in file_pathsfinal:
    # Load each file as a DataFrame and append it to the list of DataFrames
    dffinal = pd.read_csv(file_path)
    finaldfs.append(dffinal)
combined_df = pd.concat(finaldfs, ignore_index=True)

# Save combined DataFrame to CSV
combined_df.to_csv('combined_datas.csv', index=False)

#Merge and Read in Prediction Data
folderpred= r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Prediction Data'

predsdf=[]
for filename in os.listdir(folderpred):
    if filename.endswith('.csv'):
        file_pathspred = os.path.join(folderpred, filename)
        # Read each file and append it to the list of DataFrames
        predsdf.append(pd.read_csv(file_pathspred, encoding='latin1'))
prednew = predsdf[0]  # Start with the first DataFrame in the list
predttg=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\Data\Prediction Data\PpredDacc.csv')
for p in predsdf[1:]:
    prednew = pd.merge(prednew, p, on='PLAYER', how='left')
    print(prednew)
    filepathpred= 'Predictionraw.csv'
    prednew.to_csv(filepathpred, index=False)

st.title('2024 Players Championship Model Results')
st.dataframe(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\ShinyFinal.csv')

