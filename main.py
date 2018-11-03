from user import User

def main():
    # For testing let's take user1 as the reference user always and return his matches, likes etc.
    while (1):
        print("1 - Create test users\n2 - Get potential matches(user_feed)\n3 - Like users\n4 - Get matches\n")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            user1 = User(location=[0, 0], interest=['swimming', 'singing', 'movies', 'music', 'coding'], username='waqas')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user1.username,
                                                                                             user1.location,
                                                                                             user1.interest))
            user2 = User(location=[1, 2], interest=['eating', 'beatboxing', 'movies', 'music'], username='asgard')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user2.username,
                                                                                             user2.location,
                                                                                             user2.interest))
            user3 = User(location=[0, 10], interest=['skiing', 'acting', 'movies', 'music', 'writing'], username='thor')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user3.username,
                                                                                             user3.location,
                                                                                             user3.interest))
            user4 = User(location=[8, 9], interest=['hunting', 'travelling', 'movies', 'music', 'reading'], username='loki')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user4.username,
                                                                                             user4.location,
                                                                                             user4.interest))
            user5 = User(location=[0, 40], interest=['smoking', 'music', 'drinking'], username='hulk')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user5.username,
                                                                                             user5.location,
                                                                                             user5.interest))
            user6 = User(location=[2, 11], interest=['chatting', 'cricket', 'startup', 'music', 'business'], username='batman')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user6.username,
                                                                                             user6.location,
                                                                                             user6.interest))
            user7 = User(location=[1, 1], interest=['football', 'singing', 'movies', 'basketball', 'coding'], username='deadpool')
            print("\nUser created!\n Username - {}\n Location - {}\nInterests - {}\n".format(user7.username,
                                                                                             user7.location,
                                                                                             user7.interest))
            print("\nTest data created!\n")

        elif choice == 2:
            try:
                users = [user2, user3, user4, user5, user6, user7]
            except UnboundLocalError:
                print("Please create sample test data using option 1")
                continue
            distance = int(input("Enter 1 - Very near, 2 - Near, 3 - Further away : "))
            nearby_users = []

            # Algo: Get nearby users and then calculate the similarity score and sort them in descending order of it
            if distance == 1:
                nearby_users = user1.get_nearby_users(radius=5, users=users)
            elif distance == 2:
                nearby_users = user1.get_nearby_users(radius=10, users=users)
            elif distance == 3:
                nearby_users = user1.get_nearby_users(radius=50, users=users)
            potential_matches = (user1.get_potential_matches(nearby_users))
            print("\n Potential matches : \n")
            for user in potential_matches:
                print("\n Username - {}\n Location - {}\nInterests - {}\n".format(user[0].username,
                                                                                  user[0].location,
                                                                                  user[0].interest))

        elif choice == 3:
            try:
                users = [user2, user3, user4, user5, user6, user7]
            except UnboundLocalError:
                print("Please create sample test data using option 1")
                continue
            # Create test matches
            print("{} liked {}".format(user1.username, user2.username))
            user1.like_user(user2)
            print("{} liked {}".format(user1.username, user3.username))
            user1.like_user(user3)
            print("{} liked {}".format(user2.username, user1.username))
            user2.like_user(user1)
            print("{} liked {}".format(user1.username, user5.username))
            user1.like_user(user5)
            print("{} liked {}".format(user5.username, user1.username))
            user5.like_user(user1)

        elif choice == 4:
            try:
                matches = (user1.matches)
            except UnboundLocalError:
                print("Please create sample test data using option 1")
                continue
            # Return users matches
            print("\n Your matches : \n")
            for user in matches:
                print("\n Username - {}\n Location - {}\nInterests - {}\n".format(user.username,
                                                                                  user.location,
                                                                                  user.interest))
        else:
            print("\nEnter correct choice\n")

if __name__ == '__main__':
    main()
