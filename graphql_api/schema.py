import graphene
from graphene_django import DjangoObjectType
from graphql_api.models import Movie, Actor


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = ("id", "name", "date_of_birth")


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "name", "year", "actors")


class CreateActor(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        date_of_birth = graphene.Date()

    actor = graphene.Field(ActorType)

    @classmethod
    def mutate(cls, root, info, name, date_of_birth):
        actor = Actor(name=name, date_of_birth=date_of_birth)
        actor.save()
        return CreateActor(actor=actor)


class CreateMovie(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        year = graphene.Int()
        actors = graphene.List(graphene.String)

    movie = graphene.Field(MovieType)

    @classmethod
    def mutate(cls, root, info, name, year, actors):

        movie = Movie(name=name, year=year)
        movie.save()

        for _ in actors:
            actor = Actor.objects.get(name=_)
            movie.actors.add(actor.id)

        return CreateMovie(movie=movie)


class Query(graphene.ObjectType):

    all_movies = graphene.List(
        MovieType,
        since=graphene.Argument(graphene.Int, required=False, default_value={}),
        till=graphene.Argument(graphene.Int, required=False, default_value={})
    )

    def resolve_all_movies(root, info, since, till):

        movies = Movie.objects.all()
        res = []

        if since == {} and till == {}:
            return movies

        elif since != {} and till == {}:
            for _ in movies:
                if _.year >= since:
                    res.append(_)

        elif till != {} and since == {}:
            for _ in movies:
                if _.year <= till:
                    res.append(_)
        else:
            for _ in movies:
                if till >= _.year >= since:
                    res.append(_)

        return res


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    create_movie = CreateMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
