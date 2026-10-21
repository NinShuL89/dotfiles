# Configuración de Qtile

Configuración modular de Qtile para Linux, organizada en archivos separados
para atajos, grupos, diseños, pantallas, temas y widgets. Está pensada para
adaptarse: revisa los comandos y dispositivos de tu equipo antes de usarla.

## Requisitos

- Qtile y `qtile-extras` (la barra usa widgets de `qtile-extras`).
- `xrandr` para detectar y configurar pantallas.
- `checkupdates` de `pacman-contrib` para mostrar actualizaciones de Arch Linux.
- Una fuente Nerd Font para ver correctamente los iconos; la configuración usa
  `UbuntuMono Nerd Font`.

Los atajos y el inicio automático también llaman a programas externos, como
`rofi`, `chromium`, `pcmanfm`, `sakura`, `scrot`, `pactl`, `brightnessctl`,
`jgmenu`, `picom`, `nm-applet`, `udiskie`, `nitrogen`, `cbatticon` y
`volumeicon`. Instala los que quieras utilizar o modifica sus comandos en los
archivos de configuración.

## Instalación

Desde la raíz de este repositorio, copia la configuración a tu directorio de
Qtile:

```bash
mkdir -p ~/.config
cp -r .config/qtile ~/.config/
```

Antes de iniciar Qtile, revisa especialmente `autostart.sh`, los comandos de
`settings/keys.py` y la detección de pantallas de `settings/screens.py`: pueden
depender de los nombres de tus monitores, interfaces y aplicaciones.

Para probarla dentro de una sesión X11, puedes usar Xephyr:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

## Estructura

| Archivo o directorio | Responsabilidad |
| --- | --- |
| `config.py` | Punto de entrada; importa los módulos y ejecuta el inicio automático. |
| `autostart.sh` | Inicia servicios de escritorio, paneles y fondo de pantalla. |
| `config.json` | Selecciona el tema de Qtile. |
| `settings/keys.py` | Atajos de teclado y comandos de aplicaciones. |
| `settings/groups.py` | Espacios de trabajo y atajos para cambiar entre ellos. |
| `settings/layouts.py` | Diseños de ventanas y reglas para ventanas flotantes. |
| `settings/mouse.py` | Acciones del ratón para mover y redimensionar ventanas. |
| `settings/screens.py` | Barra, widgets y configuración para varios monitores. |
| `settings/widgets.py` | Widgets, estado de red, actualizaciones, reloj y bandeja del sistema. |
| `settings/theme.py` | Carga la paleta elegida en `config.json`. |
| `settings/layouts/` | Iconos usados por el widget del diseño actual. |
| `themes/` | Paletas disponibles para la barra y los bordes de ventana. |

La tecla modificadora es `mod4` (normalmente la tecla Super/Windows). Entre los
atajos incluidos están `Super + j/k/h/l` para cambiar el foco, `Super + Tab`
para cambiar de diseño, `Super + Shift + f` para alternar el modo flotante,
`Super + Ctrl + r` para reiniciar Qtile y `Super + Ctrl + q` para cerrarlo.
Consulta `settings/keys.py` para la lista completa y para adaptar los comandos
a tus aplicaciones.

La barra principal muestra los espacios de trabajo, la ventana enfocada, las
actualizaciones de Arch, el estado y tráfico de red, el diseño actual, la hora
y la bandeja del sistema. Las pantallas adicionales usan una barra secundaria.

## Temas

El tema activo se configura en `config.json`. Por ejemplo:

```json
{
  "theme": "material-ocean"
}
```

El valor debe coincidir con el nombre de uno de los archivos JSON de `themes/`
(sin la extensión). Hay varias paletas disponibles, incluidas `dark-grey`,
`dracula`, `material-darker`, `material-ocean`, `monokai-pro`, `nord-wave`,
`nord`, `onedark` y `rosepine`.

## Personalización

- Edita `settings/keys.py` para cambiar atajos o aplicaciones.
- Edita `settings/groups.py` para modificar los espacios de trabajo.
- Edita `settings/layouts.py` para elegir diseños y reglas de ventanas.
- Edita `settings/widgets.py` para cambiar el contenido y apariencia de la barra.
- Edita `settings/screens.py` y `autostart.sh` para adaptar monitores y programas
  de inicio.
- Cambia `config.json` para seleccionar otra paleta.

Después de guardar cambios en la configuración, reinicia Qtile con `Super +
Ctrl + r`.
