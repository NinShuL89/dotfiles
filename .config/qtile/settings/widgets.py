import subprocess

def arch_updates():
    try:
        return subprocess.check_output(
                "checkupdates | wc -l",
                shell=True,
                text=True,
                ).strip()
    except Exception:
        return "0"

#from libqtile import widget
from settings.theme import colors
from libqtile.lazy import lazy
from qtile_extras import widget

# Function New Qtile

def network_status():
    try:
        #WIFI
        wifi = open("/sys/class/net/wlp4s0/operstate").read().strip()
        if wifi == "up":
            ssid = subproccess.check_output(
                    "iwgetid -r",
                    shell=True,
                    text=True
                ).strip()
            return f"󰖩 {ssid}"

        #Ethernet
        ethernet = open("/sys/class/net/enp5s0/operstate").read().strip()
        if ethernet == "up":
            return "󰈀 "
        return " Offline"
    except:
        return " Offline"


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=57,
    padding=0
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    separator(),
]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        distro="Arch_checkupdates",
        display_format="{updates}",
        no_update_string=0,
        mouse_callbacks={
            "Button1":lazy.spawn(
                "sakura -e bash -lc 'sudo pacman -Syu; echo; read -p'")
            },
        **base(bg='color4'), 
        ),

    powerline('color3', 'color4'),


#icon(bg="color3", text=' '),  # Icon: nf-fa-feed
#-- Icono y Nombre Dinamico 
        widget.GenPollText(
        func=network_status,
        update_interval=5,
        **base(bg='color3'),
        ),

#-- Velocidad Dinamica de todas las interfaces activas
        widget.Net(
            interface=None,
            format="{down:.1f}{down_suffix}{up:.1f}{up_suffix}",
            update_interval=1,
            **base(bg='color3'),
        ),

    powerline('color2', 'color3'),

    widget.CurrentLayout(
        mode="icon",
        custom_icon_paths=["~/.config/qtile/settings/layouts"], 
        **base(bg='color2'), 
        scale=0.65,
        padding=2,
    ),
#    widget.CurrentLayout(**base(bg='color2'), padding=5),
     powerline('color1', 'color2'),icon(bg="color1", fontsize=17, text='󰃰'), # Icon: nf-mdi-calendar_clock

    widget.Clock(
        format="%d-%b | %H:%M",
        update_interval=1,
        padding=14,
        **base(bg='color1'),
        ),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

     widget.CurrentLayout(**base(bg='color1'), scale=0.65, padding=5),
#    widget.CurrentLayout(   mode="icon", custom_icon_paths=["~/.config/qtile/settings/layouts"], **base(bg='color1'), scale=0.50   ),
     widget.CurrentLayout(**base(bg='color1'), padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
