''' PROBLEM: Each participant enters a percent value. All the entries are sorted in ascending order.
   Starting from smallest entry, a virtual coin is tossed with win probability = that entry's percent value. 
   If toss result is favourable, that entry wins, otherwise the next entry gets picked and toss happens with the new % value. 
   (0% => picked first, but zero chances of winning, 100% = guaranteed win, but will only get picked if everyone else loses)
   For a given list of entries (percent values), which one has the maximum chance of winning? '''

x = 6.5
y = 10.568 
entries = [7.699999, 10.01, 17.12, 18, 6.7, 7, 7.7, 14, 9, 8.3, 16, 12.4, 9.69, x, 13.13, 10, 8.1, 17.85, \
           4.82, 15, 6.7, 4, 5, 7, 17.48, 12, 5, 8.88, 9.34, 7.7, 14, 5.15, 5.43, 12.81, \
            17.21, 18, 17, 9.2, 9.98, y, 9.9, 10, 6.7, 3, 9.5, 0.5, 8.5, 10.2, 6.9, 6.1, 15.49,\
               11, 6.48]
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
