import os
import subprocess
from libqtile import hook
from libqtile import bar, widget, qtile
from libqtile.layout.xmonad import MonadWide, MonadTall, MonadThreeCol
from libqtile.layout.floating import Floating
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder

from wallpapers import QtileRandomWallpaper, QtileWallpaper
from colors import NORD

mod = "mod1"

# wallpaper = QtileRandomWallpaper("/home/jonas/Bilder/wallpapers/")
wallpaper = QtileWallpaper("/home/jonas/Bilder/wallpapers/0320.jpg")
colorScheme = NORD

if qtile.core.name == "x11":
    term = "urxvt"

elif qtile.core.name == "wayland":

    from libqtile.backend.wayland.inputs import InputConfig

    wl_input_rules = {
        "1267:12377:ELAN1300:00 04F3:3059 Touchpad": InputConfig(),
        "*": InputConfig(pointer_accel=True),
        "type:keyboard": InputConfig(kb_layout="ch"),
    }

# Applications
terminal = "alacritty"
browser = "brave"
app_launcher = "rofi -show drun"
process_viewer = terminal + " htop"
screenshot_tool = "flameshot gui"


# Menus
script_path = "/home/jonas/bin"
display_menu = f"{script_path}/displayctl menu"
audio_input_menu = f"{script_path}/inctl"
audio_output_menu = f"{script_path}/sinkctl"
power_menu = f"{script_path}/powermenu"
window_menu = "rofi -show window"

# Tools
calc = f"{script_path}/roficalc"
calc2 = "qalculate-gtk"
ssh_menu = f"{script_path}/ssh-menu"
search = f"{script_path}/search"

# KEYBINDINGS
keys = [
    # Switch focus between windows
    Key([mod], "Tab", lazy.spawn(window_menu), desc="open window menu"),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    # Move windows
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "F11", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    # Close windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    # Close, logout and reset Qtile
    Key([mod], "q", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Launch Applications
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "b", lazy.spawn(browser), desc="Launch browser"),
    Key(
        [mod, "shift"], "s", lazy.spawn(screenshot_tool), desc="Launch screenshot tool"
    ),
    # Launch Menus
    Key(
        [mod, "shift"],
        "i",
        lazy.spawn(audio_input_menu),
        desc="Launch audio input menu",
    ),
    Key(
        [mod, "shift"],
        "o",
        lazy.spawn(audio_output_menu),
        desc="Launch audio output menu",
    ),
    Key([mod, "shift"], "p", lazy.spawn(power_menu), desc="Launch power menu"),
    Key([mod, "shift"], "n", lazy.spawn("bin/nm-menu"), desc="Launch nm menu"),
    Key([mod, "shift"], "d", lazy.spawn(display_menu), desc="Launch display menu"),
    # Rofi scripts
    Key([mod], "F1", lazy.spawn(calc), desc="Launch calculator"),
    Key([mod], "F2", lazy.spawn(calc2), desc="Launch calculator"),
    Key([mod], "F3", lazy.spawn(ssh_menu), desc="Launch ssh menu"),
    Key([mod], "F4", lazy.spawn(search), desc="Launch search menu"),
    # Launch Launchers
    Key([mod], "p", lazy.spawn(app_launcher), desc="Launch app launcher"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Audio
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 5%")),
    # ScratchPads
    Key([mod], "t", lazy.group["terminal"].dropdown_toggle("terminal")),
    Key([mod], "s", lazy.group["htop"].dropdown_toggle("htop")),
]


groups = [
    Group("1", layout="MonadTall"),
    Group("2", layout="MonadTall"),
    Group("3", layout="MonadTall"),
    Group("4", layout="MonadTall"),
    Group("5", layout="MonadTall"),
    Group("6", layout="MonadTall"),
    Group("7", layout="MonadTall"),
    Group("8", layout="MonadTall"),
    Group("9", layout="MonadTall"),
    Group("10", layout="MonadTall"),
    ScratchPad("terminal", [DropDown("terminal", terminal)]),
    ScratchPad("htop", [DropDown("htop", process_viewer)]),
]

dgroups_key_binder = simple_key_binder(mod)


layouts = [
    MonadThreeCol(
        border_focus=colorScheme.workspaceColor,
        border_normal=colorScheme.backgroundColor,
        border_width=2,
        margin=17,
    ),
    MonadTall(
        border_focus=colorScheme.workspaceColor,
        border_normal=colorScheme.backgroundColor,
        border_width=2,
        margin=12,
    ),
    MonadWide(
        border_focus=colorScheme.workspaceColor,
        border_normal=colorScheme.backgroundColor,
        border_width=2,
        margin=12,
    ),
]


widget_defaults = dict(
    font="Noto Sans Mono Nerd Font Bold",
    fontsize=14,
    padding=2,
    background=colorScheme.backgroundColor,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    padding=4,
                    fontsize=20,
                    active=colorScheme.foregroundColor,
                    inactive=colorScheme.foregroundColorTwo,
                    highlight_color=[
                        colorScheme.backgroundColor,
                        colorScheme.workspaceColor,
                    ],
                    highlight_method="line",
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=colorScheme[5],
                    fontsize=20,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": (
                            colorScheme.foregroundColor,
                            colorScheme.foregroundColor,
                        ),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=50,
                    background=colorScheme.backgroundColor,
                    foreground=colorScheme.foregroundColorTwo,
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=14,
                    background=colorScheme.foregroundColorTwo,
                    foreground=colorScheme.foregroundColorTwo,
                ),
                widget.Net(
                    interface="wlo1",
                    format=" {down} ↓↑ {up}",
                    foreground=colorScheme[7],
                    background=colorScheme.foregroundColorTwo,
                    padding=8,
                    fontsize=20,
                ),
                widget.Volume(
                    foreground=colorScheme[4],
                    background=colorScheme.foregroundColorTwo,
                    fmt=": {}",
                    padding=8,
                    fontsize=20,
                ),
                widget.Battery(
                    charge_char="",
                    discharge_char="",
                    format="    {percent:2.0%} {char}",
                    foreground=colorScheme[6],
                    background=colorScheme.foregroundColorTwo,
                    padding=8,
                    fontsize=20,
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=50,
                    background=colorScheme.foregroundColorTwo,
                    foreground=colorScheme.backgroundColor,
                ),
                widget.Systray(padding=8),
                widget.Clock(
                    format=" %a, %d. %m. %Y.",
                    foreground=colorScheme[10],
                    background=colorScheme.backgroundColor,
                    padding=8,
                    fontsize=20,
                ),
                widget.Clock(
                    format=" %H:%M %S",
                    foreground=colorScheme[5],
                    background=colorScheme.backgroundColor,
                    padding=8,
                    fontsize=20,
                ),
                widget.QuickExit(fmt=" ", foreground=colorScheme[9], padding=8),
            ],
            30,
            margin=[10, 20, 0, 20],
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = Floating(
    border_focus=colorScheme[4],
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="ssh-askpass"),
        Match(wm_class="qalculate-gtk"),
        Match(wm_class="Main"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# Programms to start on log in
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


@hook.subscribe.startup
def start():
    wallpaper.set()


auto_minimize = True
wmname = "LG3D"
