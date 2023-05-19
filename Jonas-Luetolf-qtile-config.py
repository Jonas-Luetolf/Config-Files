import os
import subprocess
from libqtile import hook
from libqtile import qtile
from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder

mod = "mod1"

# Applications
terminal = "alacritty"
app_launcher = "rofi -show drun"
process_viewer = terminal + " htop"
screenshot_tool = "flameshot gui"

# Menus
display_menu = "bin/displayctl menu"
audio_input_menu = "bin/inctl"
audio_output_menu = "bin/sinkctl"
power_menu = "bin/powermenu"


# Colors
# TODO: implement colorschemes via Colorsheme class
colors = [
    ["#2e3440", "#2e3440"],
    ["#3b4252", "#3b4252"],
    ["#d8dee9", "#d8dee9"],
    ["#5e81ac", "#5e81ac"],
    ["#88c0d0", "#88c0d0"],
    ["#a3be8c", "#a3be8c"],
    ["#d08779", "#d08779"],
    ["#b48ead", "#b48ead"],
    ["#a3be8c", "#a3be8c"],
    ["#bf616a", "#bf616a"],
    ["#ebcb8b", "#ebcb8b"],
]

backgroundColor = "#2e3440"
foregroundColor = "#d8dee9"
workspaceColor = "#88c0d0"
foregroundColorTwo = "#3b4252"


# KEYBINDINGS
keys = [
    # Switch between windows
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    # Close windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    # Close, logout and reset Qtile
    Key([mod], "q", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Launch Applications
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"], "s", lazy.spawn(screenshot_tool), desc="Launch screenshot tool"
    ),
    # Launch Menus
    Key([mod, "shift"], "d", lazy.spawn(display_menu), desc="Launch display menu"),
    Key([mod, "shift"], "i", lazy.spawn(audio_input_menu), desc="Launch audio input menu"),
    Key([mod, "shift"], "o", lazy.spawn(audio_output_menu), desc="Launch audio output menu"),
    Key([mod, "shift"], "p", lazy.spawn(power_menu), desc="Launch display menu"),
    # Launch Launchers
    Key([mod], "p", lazy.spawn(app_launcher), desc="Launch app launcher"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Hardware/system control
    # Sound
    Key([mod], "v", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([mod, "shift"], "v", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),
    Key([mod], "t", lazy.group["terminal"].dropdown_toggle("terminal")),
    Key([mod], "s", lazy.group["htop"].dropdown_toggle("htop")),
]

groups = [
    Group("1", layout="MonadTall"),
    Group("2", layout="MonadTall"),
    Group("3", layout="MonadTall"),
    Group("4", layout="bMonadTall"),
    Group("5", layout="MonadTall"),
    Group("6", layout="MonadTall"),
    Group("7", layout="MonadTall"),
    Group("8", layout="MonadTall"),
    Group("9", layout="MonadTall"),
    Group("10", layout="MonadTall"),
    ScratchPad("terminal", [DropDown("terminal", terminal)]),
    ScratchPad("htop", [DropDown("htop", terminal + " -e htop")]),
]

dgroups_key_binder = simple_key_binder(mod)

layouts = [
    layout.MonadTall(
        border_focus=colors[3], border_normal=colors[0], border_width=2, margin=12
    ),
    # layout.TreeTab(border_focus = colors[4], margin = 2),
    layout.MonadWide(
        border_focus=colors[3], border_normal=colors[0], border_width=2, margin=12
    ),
]

widget_defaults = dict(
    font="Noto Sans Mono Nerd Font Bold", fontsize=14, padding=2, background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    padding=4,
                    active=colors[2],
                    inactive=colors[1],
                    highlight_color=[backgroundColor, workspaceColor],
                    highlight_method="line",
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=colors[5],
                ),
                widget.Chord(
                    chords_colors={
                        "launch": (foregroundColor, foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=50,
                    background=backgroundColor,
                    foreground=foregroundColorTwo,
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=14,
                    background=foregroundColorTwo,
                    foreground=foregroundColorTwo,
                ),
                widget.Net(
                    interface="wlo1",
                    format=" {down} ↓↑ {up}",
                    foreground=colors[7],
                    background=foregroundColorTwo,
                    padding=8,
                ),
                widget.Volume(
                    foreground=colors[4],
                    background=foregroundColorTwo,
                    fmt=": {}",
                    padding=8,
                ),
                widget.Battery(
                    charge_char="",
                    discharge_char="",
                    format="  {percent:2.0%} {char}",
                    foreground=colors[6],
                    background=foregroundColorTwo,
                    padding=8,
                ),
                widget.TextBox(
                    text="\u25e2",
                    padding=0,
                    fontsize=50,
                    background=foregroundColorTwo,
                    foreground=backgroundColor,
                ),
                widget.Systray(padding=8),
                widget.Clock(
                    format=" %a, %d. %m. %Y.",
                    foreground=colors[10],
                    background=backgroundColor,
                    padding=8,
                ),
                widget.Clock(
                    format=" %H:%M %S",
                    foreground=colors[5],
                    background=backgroundColor,
                    padding=8,
                ),
                widget.QuickExit(fmt=" ", foreground=colors[9], padding=8),
            ],
            20,
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

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[4],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="ssh-askpass"),  # ssh-askpass
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


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
