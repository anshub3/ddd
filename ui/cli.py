# ui/cli.py

def get_player_action() -> str:
    return input("\n>> What do you do? ").strip()


def show_response(text: str):
    print("\n" + "=" * 50)
    print(text)
    print("=" * 50)
