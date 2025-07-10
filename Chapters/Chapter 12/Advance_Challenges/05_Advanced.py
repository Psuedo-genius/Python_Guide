# Build a mini leaderboard sorted by score
scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 92
}

# Step 2 & 3: Sort by score descending
sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

# Step 4: Display leaderboard
print(" Leaderboard:")
rank = 1
for name, score in sorted_scores:
    print(f"{rank}. {name} - {score}")
    rank += 1
