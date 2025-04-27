import pandas as pd
weapons = pd.read_csv('skyrim_weapons.csv')
weapons['Type']
Skyrim = weapons.drop_duplicates().drop('Type', axis=1).drop('Speed', axis=1).drop('Perk', axis=1).drop('Upgrade', axis=1).drop('Gold', axis=1).sort_values('Category')
print(Skyrim)
Skyrim.to_csv('Armas_Skyrim.csv')