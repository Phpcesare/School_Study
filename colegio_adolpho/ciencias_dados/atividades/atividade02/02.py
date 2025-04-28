import pandas
pd = pandas

dfSPROUT_ranking = pd.read_csv('SPROUT_ranking.csv')
dfCountryRanking = pd.read_csv('Brazil_club_rankings.csv')

print(dfSPROUT_ranking.info())
print(dfCountryRanking.info())

print(dfCountryRanking.agg) ((
        'points': ['mean', 'max', 'min', 'std']
))

dfCountryRanking_ordenano = dfCountryRanking.sort_values('name')
dfJuncao = pd.merge(dfSPROUT_ranking, dfCountryRanking, on ='bestSproutPlayer', how='outer')
print(dfJuncao.info())