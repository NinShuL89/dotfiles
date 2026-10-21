# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from settings.theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
   #     Match(wmclass = "confirm"),
   #     Match(wmclass = "dialog"),
   #     March(wmclass = "download"),
   #     Match(wmclass = "error"),
   #     Match(wmclass = "file_progress"),
   #     Match(wmclass = "notification"),
   #     Match(wmclass = "splash"),
   #     Match(wmclass = "toolbar"),

        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        
        Match(title="branchdialog"),
        Match(title="pinentry"),
        
        Match(wm_class="ssh-askpass"),
    ],
    border_focus=colors["color4"][0],
    border_width=1,
)
