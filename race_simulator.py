f1-race-strategy-sim/
│
├── race_simulator.py
├── README.md
└── requirements.txtif __name__ == "__main__":
    race_laps = 50

    strategy1 = [("Soft", 15), ("Medium", 20), ("Hard", 15)]
    strategy2 = [("Medium", 25), ("Medium", 25)]

    time1 = simulate_race(race_laps, strategy1)
    time2 = simulate_race(race_laps, strategy2)

    print("🏎 Race Strategy Simulator")
    print(f"Total Laps: {race_laps}\n")
    print("Strategy 1 (S-M-H):", round(time1, 2), "seconds")
    print("Strategy 2 (M-M):   ", round(time2, 2), "seconds")

    if time1 < time2:
        print("\n✅ Strategy 1 is faster!")
    elif time2 < time1:
        print("\n✅ Strategy 2 is faster!")
    else:
        print("\n🤝 Both strategies are equal!")

