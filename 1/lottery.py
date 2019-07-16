from random import randint

winners_count = int(input())
last = input().split()
last_number = int(last[0])
serie = 'AA' if len(last) == 1 else last[1].upper()
all_winners = []


for winner_num in range(1, winners_count + 1):
    if winners_count >= last_number:
        if winner_num > last_number:
            #print('skipping')
            continue
        number = winner_num
    else: 
        while True:
            number = randint(1, last_number)
            if not number in all_winners:
                all_winners.append(number)
                break
    
    print(f'Победитель номер {winner_num} - "{number:06d} {serie}"')