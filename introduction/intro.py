from collections import Counter
# mark: user list @given
users = [{"id": 0, "name": "hero0"},
         {"id": 1, "name": "hero1"},
         {"id": 2, "name": "hero2"},
         {"id": 3, "name": "hero3"},
         {"id": 4, "name": "hero4"},
         {"id": 5, "name": "hero5"},
         {"id": 6, "name": "hero6"},
         {"id": 7, "name": "hero7"},
         {"id": 8, "name": "hero8"},
         {"id": 9, "name": "hero9"}]
# mark: given paris of friends connections
friendship_paris = [{0, 1}, {0, 2}, {1, 2}, {1, 3}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {5, 7}, {6, 8}, {7, 8}, {8, 9}]

# create empty list for each id in users
friendships = {user["id"]: [] for user in users}

# get number of friends that user i / j has with one shot
for i, j in friendship_paris:
    friendships[i].append(j)
    friendships[j].append(i)


# get number of froends per user
def number_of_users(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


totalconnection = sum(number_of_users(user) for user in users)
most_connected_one = [(user["id"], number_of_users(user)) for user in users]
most_connected_one.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)

num_of_users = len(users)
avg_of_connections = totalconnection / num_of_users
print('avg_of_connections', avg_of_connections)


def find_name(user, key):
    if user["id"] == key:
        print(user["name"])


# most connected mone
[find_name(user, most_connected_one[0][0]) for user in users]
print('most_connected_one')


# get friend of friends
def f_o_f(user):
    u_id = user["id"]
    count = Counter(
        foaf_id
        # for each of my friend
        for friend_id in friendships[u_id]
        # find thoer friends
        for foaf_id in friendships[friend_id]
        # who arent me
        if foaf_id != u_id
        # and arent on of my friends
        and foaf_id not in friendships[u_id]
    )


print("fof:", f_o_f(users[0]))

# get friend of friends
