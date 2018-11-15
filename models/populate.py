from models.base import session_factory
from models.place_model import Place
from models.user_model import User

def populate_database():
    session = session_factory()
    session.commit()
    session.close()


def query_places():
    session = session_factory()
    place_query = session.query(Place)
    session.close()
    return place_query.all()

def query_users():
    session = session_factory()
    user_query = session.query(User)
    session.close()
    return user_query.all()



if __name__ == "__main__":
    places = query_places()
    if len(places) == 0:
        populate_database()

        places = query_places()
    for place in places:
        print(f'"{place.placename}" has the following Users: ', end="")

        for user in place.users:
            print(f'{user.username}; ', end="")

        print('')