class Voting:
    def eligibility(self, age):
        if age >= 18:
            return "Eligible for Voting"
        else:
            return "Not Eligible"