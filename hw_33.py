import pandas

titanic = pandas.read_csv('titanic.csv')
#print(titanic)

sex_stats = titanic.groupby(['Sex', 'Survived'])['PassengerId'].count()
pclass_stats = titanic.groupby(['Pclass', 'Survived'])['PassengerId'].count()

print(sex_stats)
print(pclass_stats)