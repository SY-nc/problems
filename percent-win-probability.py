''' PROBLEM: Each participant enters a percent value. All the entries are sorted in ascending order.
   Starting from smallest entry, a virtual coin is tossed with win probability = that entry's percent value. 
   If toss result is favourable, that entry wins, otherwise the next entry gets picked and toss happens with the new % value. 
   (0% => picked first, but zero chances of winning, 100% = guaranteed win, but will only get picked if everyone else loses)
   For a given list of entries (percent values), which one has the maximum chance of winning? '''

entries = [6.7, 10, 11, 10, 0.1, 9.98, 6.69, 1.7, 7, 9, 4, 10.99, 0.164, 3.9, 7.7, 5, 10, 6.84, 1.555, \
           10, 8.2, 10.9, 1.3333, 10.01, 11.11, 1, 5.5, 10, 0.4, 8, 12, 7.88, 7.6, 9.97, 6.84, \
            1.5, 0.8, 13.13, 4.67]
entries = sorted(entries)

prob_win = [0 for _ in range(len(entries))]
cumul = [0 for _ in range(len(entries))]    # cumul[i] = cumul. likelihood of winner being decided before (i+1)th entry 

sum = 0
lose_streak = 1
for i in range(0, len(entries)):
    prob_win[i] = (lose_streak)*entries[i]
    sum +=prob_win[i]/100
    cumul[i] = sum*100
    lose_streak = lose_streak*(100-entries[i])/100

prob_win = [round(prob, 5) for prob in prob_win]
max_prob = max(prob_win)
best_entry = prob_win.index(max_prob)
print(f"{entries[best_entry]} => {max_prob}")

sum_prob_win = 0
for prob in prob_win:
    sum_prob_win+=prob

#     current_wins = entries[i]/100
#     prob_win[i] = (prev_loses + current_wins)*100
