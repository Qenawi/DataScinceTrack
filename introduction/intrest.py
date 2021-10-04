from collections import defaultdict

user_list = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

interest = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientist_who_like(target):
    return [user_id for user_id, user_interest in interest
            if user_interest == target]


# find all users who likes target
# build empty dict with list
user_id_by_interest = defaultdict(list)
# group interest by user "interest":[user id , user id ]
for user_id, interest in interest:
    user_id_by_interest[interest].append(user_id)


# find most popular interest by user
def most_common_interest_by_user(user):
    u_id = user["id"]
    user_name = user["name"]
    user_intrest = [item for item in user_id_by_interest
                    if u_id in user_id_by_interest[item]
                    ]
    bst = user_intrest[0]
    for i in user_intrest:
        if len(user_id_by_interest[i]) >= len(user_id_by_interest[bst]):
            bst = i

    return "user "+user_name+" top intrest is "+bst


print(most_common_interest_by_user(user_list[9]))
