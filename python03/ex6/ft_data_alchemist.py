import random


def data_alchemist() -> None:
    player_names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                    'Gregory', 'john', 'kevin', 'Liam']

    print(f"Initial list of players: {player_names}")

    first_list = [player.capitalize() for player in player_names]
    print(f"New list with all names capitalized: {first_list}")

    second_list = [player for player in player_names if player == player.capitalize()]
    print(f"New list of capitalized names only: {second_list}")

    dic = {key: random.randrange(1, 1000) for key in first_list}
    print(f"Score dict: {dic}")

    result = round(sum(dic.values()) / len(dic), 2)
    print(f"Score average is {result}")

    second_dic = {name: score for name, score in dic.items() if score > result}
    print(f"High scores: {second_dic}")


def main() -> None:
    print("=== Game Data Alchemist ===")

    data_alchemist()


if __name__ == "__main__":
    main()