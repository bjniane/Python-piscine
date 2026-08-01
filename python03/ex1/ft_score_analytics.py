import sys


def score_analytics() -> None:
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3"
            " ft_score_analytics.py<score1> <score2> ..."
        )
        return
    else:
        my_list: list = []
        for i in range(1, len(sys.argv)):
            try:
                if sys.argv[i].isdigit():
                    my_list.append(int(sys.argv[i]))
                else:
                    raise ValueError(f"Invalid parameter: '{sys.argv[i]}'")
            except ValueError as e:
                print(e)
        if len(my_list) == 0:
            print(
                "No scores provided. Usage: python3"
                " ft_score_analytics.py<score1> <score2> ..."
            )
        else:
            print(f"Scores processed: {my_list}")
            print(f"Total players: {len(my_list)}")
            print(f"Total score: {sum(my_list)}")
            print(f"Average score: {sum(my_list) / len(my_list)}")
            print(f"High score: {max(my_list)}")
            print(f"Low score: {min(my_list)}")
            print(f"Score range: {max(my_list) - min(my_list)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    score_analytics()


if __name__ == "__main__":
    main()
