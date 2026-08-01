import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "dylan", "charlie"]
    actions: list[str] = ["run", "eat", "sleep", "grab",
                          "move", "climb", "swim", "release"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        my_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while my_list:
        item = random.choice(my_list)
        my_list.remove(item)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_of_event: list[tuple[str, str]] = []
    for _ in range(10):
        event = next(gen)
        list_of_event.append(event)
    print(f"Built list of 10 events: {list_of_event}")

    for event in consume_event(list_of_event):
        # item = consume_event(list_of_event)
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_of_event}")


if __name__ == "__main__":
    main()
