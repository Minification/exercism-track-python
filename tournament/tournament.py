from typing import List
from collections import defaultdict, Counter
from operator import itemgetter

ROW_TEMPLATE = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

HEADER_ROW = ("Team", "MP", "W", "D", "L", "P")

WIN = "win"
DRAW = "draw"
LOSS = "loss"

WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

def tally(rows: List[str]) -> List[str]:
    RESULT_TO_OTHER_RESULT = {
        WIN: LOSS,
        DRAW: DRAW,
        LOSS: WIN
    }
    
    teams = defaultdict(Counter)
    for row in rows:
        team, other, result = row.split(";")
        teams[team][result] += 1
        teams[other][RESULT_TO_OTHER_RESULT[result]] += 1
    
    table = []
    # Data is added to the table alphabetically sorted
    for team, results in sorted(teams.items()):
        wins, draws, losses = results[WIN], results[DRAW], results[LOSS]
        matches_played = wins + draws + losses
        points = WIN_POINTS * wins + DRAW_POINTS * draws + LOSS_POINTS * losses
        table.append((team, matches_played, wins, draws, losses, points))
    # Sort by points (last tuple value), assumes stable sort!
    table.sort(key=itemgetter(-1), reverse=True)
    
    table.insert(0, HEADER_ROW)
    return [ROW_TEMPLATE.format(*row) for row in table]
