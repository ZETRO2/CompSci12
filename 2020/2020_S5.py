

def main():
    print("Enter the number of people and burgers (N):")
    N = int(input().strip())
    print("Enter the favorite burgers of each person (space-separated):")
    fav = list(map(int, input().strip().split()))

    if len(fav) != N:
        print("Error: You must enter exactly", N, "burger preferences.")
        return

    josh_fav = fav[-1]
    total_success = 0.0

    for coach_pick_index in range(N):
        fav_copy = fav[:]
        taken = [False] * N
        taken[coach_pick_index] = True

        available = {}
        for i in range(N):
            if not taken[i]:
                b = fav[i]
                available[b] = available.get(b, 0) + 1

        for i in range(1, N - 1):
            person_fav = fav[i]
            if available.get(person_fav, 0) > 0:
                available[person_fav] -= 1
                if available[person_fav] == 0:
                    del available[person_fav]
            else:
                total_remaining = sum(available.values())
                if total_remaining == 0:
                    continue
                if josh_fav in available:
                    total_success += (1.0 / N) * (1.0 / total_remaining)
                    available[josh_fav] -= 1
                    if available[josh_fav] == 0:
                        del available[josh_fav]
                else:
                    rand_keys = list(available.keys())
                    b = rand_keys[0]  
                    available[b] -= 1
                    if available[b] == 0:
                        del available[b]

        if josh_fav in available:
            total_success += 1.0 / N

    print("Probability that Josh gets his favorite burger:")
    print(f"{total_success:.8f}")

if __name__ == "__main__":
    main()
