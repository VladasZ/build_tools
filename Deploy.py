import Shell
import System

cask_map = {
    "toolbox": "jetbrains-toolbox",
    "teams": "microsoft-teams",
    "vk": "vk-messenger"
}

choco_map = {
    "toolbox": "jetbrainstoolbox",
    "teams": "microsoft-teams",
    "vk": "vkmessenger"
}

mac_only = [
    "postman",
    "daisydisk"
]

win_only = [
    "make",
    "putty",
    "winrar",
    "scanner",
    "winpcap",
    "procexp",
    "lightshot",
    "autohotkey",
    "lockhunter",
    "dependencywalker"
]

apps = [
    "transmission",
    "wireshark",
    "gitkraken",
    "telegram",
    "toolbox",
    "skype",
    "slack",
    # "deezer",
    "teams",
    "steam",
    "vk"
]


def installer():
    return "choco" if System.is_windows else "brew"


def platform_map():
    return choco_map if System.is_windows else cask_map


def platform_apps():
    return win_only if System.is_windows else mac_only


def unwrap(app):
    map = platform_map()
    if app in platform_map():
        return map[app]
    return app


def install(app):
    Shell.run([installer(), "install", unwrap(app)])


def all_apps():
    return apps + platform_apps()


def install_all():
    apps = all_apps()
    print("Installing:")
    print(apps)
    for app in apps:
        install(app)
