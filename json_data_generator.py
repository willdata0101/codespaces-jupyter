import json
import random

games = []

platforms = ["NES", "SNES", "Genesis", "Arcade", "Game Boy"]
genres = ["Platformer", "RPG", "Shooter", "Puzzle", "Fighting"]

for i in range(250):
    games.append({
        "id": i + 1,
        "title": f"Neon Quest {i + 1}",
        "platform": random.choice(platforms),
        "release_year": random.randint(1983, 1995),
        "developer": {
            "name": f"Studio {random.randint(1, 25)}",
            "country": random.choice(["US", "Japan", "UK"])
        },
        "genre": random.choice(genres),
        "inventory": {
            "stock": random.randint(0, 100),
            "price": round(random.uniform(9.99, 79.99), 2)
        },
        "reviews": [
            {"source": "RetroMag", "score": round(random.uniform(6.0, 10.0), 1)}
        ]
    })

# Inject intentional errors
del games[17]["platform"]
games[42]["release_year"] = "1987"
del games[108]["developer"]["name"]
games[150]["inventory"]["stock"] = "available"
games[201]["reviews"][0]["score"] = "ten"

with open("retro_arcade_response.json", "w") as f:
    json.dump({"games": games}, f, indent=2)