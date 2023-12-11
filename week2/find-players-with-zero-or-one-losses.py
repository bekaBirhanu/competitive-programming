class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers_one_times = set()
        losers_more_times = set()
        for winner, loser in matches:
            winners.add(winner)
            if loser in losers_one_times:
                losers_more_times.add(loser)
            losers_one_times.add(loser)
            

        return [sorted(list(winners- losers_one_times)),sorted(list(losers_one_times-losers_more_times))]