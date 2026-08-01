import random


def gen_player_achievements(achievement_list: list[str]) -> set[str]:
    random_number = random.randint(1, len(achievement_list))
    current_list = achievement_list[:]
    player_achievement: list = []

    for _ in range(random_number):
        element = random.choice(current_list)
        player_achievement.append(element)
        current_list.remove(element)

    return set(player_achievement)


def achievement_tracker() -> None:
    achievement_list = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer',
        'Strategist', 'Unstoppable', 'Speed Runner',
        'Survivor', 'Treasure Hunter', 'First Steps',
        'Sharp Mind', 'Hidden Path Finder'
    ]

    Alice = gen_player_achievements(achievement_list)
    print(f"Player Alice: {Alice}")

    Bob = gen_player_achievements(achievement_list)
    print(f"Player Bob: {Bob}")

    Charlie = gen_player_achievements(achievement_list)
    print(f"Player Charlie: {Charlie}")

    Dylan = gen_player_achievements(achievement_list)
    print(f"Player Dylan: {Dylan}")
    print()

    all_distinct = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements: {all_distinct}\n")

    # Find achievements shared by all players
    common_achievement = Alice.intersection(Bob, Charlie, Dylan)
    print(f"Common achievements: {common_achievement}\n")

    # For each player, spot the achievements no one else has
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")
    print()

    all_list = set(achievement_list)
    print(f"Alice is missing: {all_list.difference(Alice)}")
    print(f"Bob is missing: {all_list.difference(Bob)}")
    print(f"Charlie is missing: {all_list.difference(Charlie)}")
    print(f"Dylan is missing: {all_list.difference(Dylan)}")


def main() -> None:
    print("=== Achievement Tracker System ===")
    achievement_tracker()


if __name__ == "__main__":
    main()
