from operator import itemgetter
import math

class User:

    location = []
    interest = []
    username = ""
    likes = []
    matches = []

    def __init__(self, location, interest, username, likes=None, matches=None):
        self.location = location
        self.interest = interest
        if not likes:
            self.likes = []
        else:
            self.likes = likes
        if not matches:
            self.matches = []
        else:
            self.matches = matches
        self.username = username

    def get_nearby_users(self, radius, users):
        # Logic: Return users within the given radius
        users_inside_radius = []
        for user in users:
            distance = math.sqrt(((self.location[0] - user.location[0]) ** 2) + ((self.location[1] - user.location[1]) ** 2))
            if distance <= radius:
                users_inside_radius.append(user)
        return users_inside_radius

    # Calculate similarity score
    def get_similarity_score(self, user):

        interest_match_count = 0
        interests = user.interest
        for interest in interests:
            if interest in self.interest:
                interest_match_count += 1

        similarity_score = interest_match_count/(len(self.interest))

        return similarity_score

    def like_user(self, user):
        self.likes.append(user)

        # Check for matches and add users to corresponding lists
        if user in self.likes and self in user.likes:
            user.matches.append(self)
            self.matches.append(user)
            print("\nVOILA! That's a match!\n")

    def get_matches(self):
        return self.matches

    def get_potential_matches(self, users):

        potential_matches = []

        for user in users:
            score = self.get_similarity_score(user)
            potential_matches.append((user, score))

        potential_matches.sort(key=itemgetter(1), reverse=True)
        return potential_matches

