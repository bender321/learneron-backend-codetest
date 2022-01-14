# Learneron backend codetest

The goal of this task is to create basic django app with GraphQL API using Graphene Django. Preferred database is MySQL but for simplicity any database can be used (for example SQLite). This repository includes already prepared django project with graphene and all dependencies already taken care of. You should fork this project and then proceed with the task there.

Your tasks:
1. Create django models Movie (name, year) and Actor (name, date of birth) and create migration
2. Create many-to-many relationship between Movie and Actor and create migration
3. Create DjangoObjectType for Movie and Actor
4. Create GraphQL Query to get all movies
5. Create GraphQL Mutation to add Actor (with name and date of birth as arguments, returning created Actor)
6. Create GraphQL Mutation to add Movie (with name, year and list of actor ids as arguments, returning created movie)
7. Add argument/arguments to optionally filter movies (in already existing query) by year range
