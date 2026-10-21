#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_HOME="${XDG_CONFIG_HOME:-"$HOME/.config"}"
TARGET_DIR="${CONFIG_HOME%/}/qtile"

if [[ ! -f "$SCRIPT_DIR/config.py" || ! -d "$SCRIPT_DIR/settings" || ! -d "$SCRIPT_DIR/themes" ]]; then
    printf 'Error: no se encontró la configuración de Qtile junto a este script.\n' >&2
    exit 1
fi

if [[ "$SCRIPT_DIR" == "$TARGET_DIR" ]]; then
    printf 'La configuración ya está en %s; no hay nada que copiar.\n' "$TARGET_DIR"
    exit 0
fi

if [[ -e "$TARGET_DIR" && ! -d "$TARGET_DIR" ]]; then
    printf 'Error: %s existe y no es un directorio.\n' "$TARGET_DIR" >&2
    exit 1
fi

if [[ -d "$TARGET_DIR" ]]; then
    BACKUP_DIR="$(mktemp -d "${TARGET_DIR}.backup.XXXXXX")"
    cp -a "$TARGET_DIR/." "$BACKUP_DIR/"
    printf 'Copia de seguridad creada en: %s\n' "$BACKUP_DIR"
fi

mkdir -p "$TARGET_DIR"
cp -a "$SCRIPT_DIR/config.py" "$SCRIPT_DIR/autostart.sh" "$SCRIPT_DIR/config.json" "$TARGET_DIR/"
cp -a "$SCRIPT_DIR/settings" "$SCRIPT_DIR/themes" "$TARGET_DIR/"

printf 'Configuración de Qtile instalada en: %s\n' "$TARGET_DIR"
