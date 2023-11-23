def print_ranking(users_data):
    print("{:<10} {:<10} {:<10}".format('Id', 'Name', 'Score'))
    print("-----------------------------------")
    for users in users_data.get_ranking_users():
        print("{:<10} {:<10} {:<10}".format(users.get_id(), users.get_name(), users.get_score()))
