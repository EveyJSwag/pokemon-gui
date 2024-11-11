#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import requests
import pprint
import mysql.connector
API_PREFIX = "https://pokeapi.co/api/v2/pokemon/%d"
INSERT_TEMPLATE = 'INSERT INTO TABLE Pokemon (PokemonID, PokemonName, HPYield, AttackYield, DefenseYield, SpAttackYield, SpDefenseYield, SpeedYield) VALUES (%d, %s, %d, %d, %d, %d, %d, %d);'
INSERT_TEMPLATE = 'INSERT INTO pokemonDB.Pokemon (pokemonid, pokemonname, hpyield, attackyield, defenseyield, spattackyield, spdefenseyield, speedyield) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
NUMBER_OF_POKEMON = 1025



'''mysql> CREATE TABLE Pokemon (
    -> PokemonID int,
    -> PokemonName varchar(255),
    -> HPYield int,
    -> AttackYield int,
    -> DefenseYield int,
    -> SpAttack int,
    -> SpDefenseYield int,
    -> SpeedYield int)'''



''''stats': [{'base_stat': 45,
            'effort': 0,
            'stat': {'name': 'hp', 'url': 'https://pokeapi.co/api/v2/stat/1/'}},
           {'base_stat': 49,
            'effort': 0,
            'stat': {'name': 'attack',
                     'url': 'https://pokeapi.co/api/v2/stat/2/'}},
           {'base_stat': 49,
            'effort': 0,
            'stat': {'name': 'defense',
                     'url': 'https://pokeapi.co/api/v2/stat/3/'}},
           {'base_stat': 65,
            'effort': 1,
            'stat': {'name': 'special-attack',
                     'url': 'https://pokeapi.co/api/v2/stat/4/'}},
           {'base_stat': 65,
            'effort': 0,
            'stat': {'name': 'special-defense',
                     'url': 'https://pokeapi.co/api/v2/stat/5/'}},
           {'base_stat': 45,
            'effort': 0,
            'stat': {'name': 'speed',
                     'url': 'https://pokeapi.co/api/v2/stat/6/'}}],'''

 
startId = 1

currentId = startId


mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="1234",
        database="pokemonDB")
mycursor = mydb.cursor()
while currentId < (NUMBER_OF_POKEMON + 1):
    currentRequest = requests.get(API_PREFIX % currentId).json()
    pokemonID = currentId
    pokemonName = currentRequest['name']
    pokemonStats = currentRequest['stats']
    hpYield        = 0
    attackYield    = 0
    defenseYield   = 0
    spAttackYield  = 0
    spDefenseYield = 0
    speedYield     = 0
    for pokemonStat in pokemonStats:
        if pokemonStat['stat']['name'] == 'hp':
            hpYield = pokemonStat['effort']
        if pokemonStat['stat']['name'] == 'attack':
            attackYield = pokemonStat['effort']
        if pokemonStat['stat']['name'] == 'defense':
            defenseYield = pokemonStat['effort']
        if pokemonStat['stat']['name'] == 'special-attack':
            spAttackYield = pokemonStat['effort']
        if pokemonStat['stat']['name'] == 'special-defense':
            spDefenseYield = pokemonStat['effort']
        if pokemonStat['stat']['name'] == 'speed':
            speedYield = pokemonStat['effort']
    values = (str(pokemonID),pokemonName,str(hpYield),str(attackYield),str(defenseYield),str(spAttackYield),str(spDefenseYield),str(speedYield))
    print(INSERT_TEMPLATE % values)
    mycursor.execute(INSERT_TEMPLATE, values)
    currentId+=1

mydb.commit()

