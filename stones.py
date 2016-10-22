def main():
    num_test_cases = input()
    for test_case in range(0,num_test_cases):
        num_games = input()
        piles = []
        for game in range(0,num_games):
            piles_in_game = input()
            stones_in_piles = raw_input()
            piles += [int(x) for x in stones_in_piles.split()]
        turns = 0

        largest_pile = max(piles)#This is really one large game with different pile sizes.
        while(largest_pile>1):
            index_to_split = piles.index(largest_pile)
            avg_split_size = float(largest_pile)/3
            the_mod = (avg_split_size-1)%2
            smallest_pile_size = int(avg_split_size-the_mod)
            piles[index_to_split] = smallest_pile_size
            if the_mod ==0:
                piles.append(smallest_pile_size)
                piles.append(smallest_pile_size)
            elif the_mod<1:#2/3 modulus
                piles.append(smallest_pile_size)
                piles.append(smallest_pile_size + 2)
                pass
            else:#4/3 modulus
                piles.append(smallest_pile_size + 2)
                piles.append(smallest_pile_size + 2)
                pass
            turns+=1
            largest_pile = max(piles)
        if turns%2==0:
            print("Bob")
        else:
            print("Alice")

if __name__=="__main__":
    main()