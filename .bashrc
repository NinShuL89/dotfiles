#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

neofetch

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# Pacman & AUR Helper(yay)
alias pacu='sudo pacman -Syyu'                 # Update only standard PKG's
alias yasa="yay -Sua --noconfirm"              # Update only AUR PKG's
alias yayu="yay -Syu --noconfirm"              # Update standard PKG's and AUR PKG's
alias unlck="sudo rm /var/lib/pacman/db.lck"   # Remove pacman lock
alias cln='sudo pacman -Rns $(pacman -Qtdq)'   # Remove orphaned packages
alias pacman='sudo pacman -S'				   # Helper

# Confirm before overwriting something
alias cp="cp -i"
alias mv='mv -i'
alias rm='rm -i'

# GitHub
alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias status='git status'
alias tag='git tag'
alias newtag='git tag -a'

