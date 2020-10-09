
import Shell
import System

cask_map = {
    "toolbox" : "jetbrains-toolbox",
    "teams"   : "microsoft-teams",
    "vk"      : "vk-messenger"
}

choco_map = {
    "toolbox" : "jetbrainstoolbox",
    "teams"   : "microsoft-teams",
    "vk"      : "vkmessenger"
}

mac_only = [
    "postman",
    "daisydisk"
]

win_only = [
    "putty",
    "winrar",
    "scanner",
    "winpcap",
    "procexp",
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
  #  "deezer",
    "teams",
    "steam",
    "vk"
]


def unwrap(app):
    map = choco_map if System.is_windows else cask_map
    if app in map:
        return map[app]
    return app


def install(app):
    installer = "choco" if System.is_windows else "brew"
    Shell.run([installer, "install", unwrap(app)])


def all_apps():
    all = apps
    if System.is_windows:
        all += win_only
    else:
        all += mac_only
    return all


def install_all():
    apps = all_apps()
    print("Installing:")
    print(apps)
    for app in apps:
        install(app)
