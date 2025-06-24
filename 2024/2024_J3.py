
N = int(input("Enter the number of participants: "))

scores = []
print("Enter each participant's score, one per line:")
for _ in range(N):
    score = int(input())
    scores.append(score)

unique_scores = []
for s in scores:
    if s not in unique_scores:
        unique_scores.append(s)
unique_scores.sort(reverse=True)

bronze_score = unique_scores[2]

bronze_count = 0
for s in scores:
    if s == bronze_score:
        bronze_count += 1

print(f"{bronze_score} {bronze_count}")
