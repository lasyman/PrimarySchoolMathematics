from pathlib import Path


def get_desktop_path():
    return get_user_path() / "Desktop"


def get_user_path():
    p = Path()
    return p.home()


if __name__ == "__main__":
    config_path = get_desktop_path() / "config"
    print(config_path.exists())
