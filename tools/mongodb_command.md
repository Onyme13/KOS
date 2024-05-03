# Summary of MongoDB Commands

mongo                # Start the MongoDB shell
show dbs             # List databases
use <database_name>  # Switch to a specific database
show collections     # List collections in the current database
db.collection.find().limit(5)  # Query data in a collection
exit                 # Exit the MongoDB shell


## Créer une collection
db.createCollection("nomDeLaCollection")

## Supprimer une collection
db.nomDeLaCollection.drop()

## Insérer un document
db.nomDeLaCollection.insert({champ1: "valeur1", champ2: "valeur2"})

## Insérer plusieurs documents
db.nomDeLaCollection.insertMany([
    {champ1: "valeur1", champ2: "valeur2"},
    {champ1: "valeur3", champ2: "valeur4"}
])

## Rechercher des documents
db.nomDeLaCollection.find({champ1: "valeur1"})

## Mettre à jour un document
db.nomDeLaCollection.update(
    { champ1: "valeur1" },  
    { $set: { champ2: "nouvelleValeur" } }
)

## Supprimer un document
db.nomDeLaCollection.remove({champ1: "valeur1"})

## Quitter le shell MongoDB
exit
