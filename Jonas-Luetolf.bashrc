shopt -s checkwinsize

# Promt Colors - Nord Color Scheme
C_BLUE="129;161;193"    # #81a1c1
C_PURPLE="180;142;173"  # #b48ead
C_GREEN="163;190;140"   # #a3be8c
C_TEXT="46;52;64"       # #2e3440

# Coloring Helpers
FG() { echo "\[\e[38;2;$1m\]"; }
BG() { echo "\[\e[48;2;$1m\]"; }
RST="\[\e[0m\]"

# Git Repo Info
parse_git() {
source /usr/share/git/completion/git-prompt.sh
  __git_ps1 "%s"
}

# Prompt
PS1="${RST}\
$(FG $C_BLUE)$(FG $C_TEXT)$(BG $C_BLUE) \u \
$(FG "$C_BLUE")$(BG "$C_PURPLE")$(FG $C_TEXT)$(BG "$C_PURPLE") \W\
\$(git_branch=\$(parse_git); \
if [ -n \"\$git_branch\" ]; then \
  echo \"$(FG "$C_PURPLE")$(BG "$C_GREEN")$(FG $C_TEXT)$(BG "$C_GREEN")  \$git_branch ${RST}$(FG "$C_GREEN")\"; \
else \
  echo \"${RST}$(FG "$C_PURPLE")\"; \
fi)\
${RST} "

# Path Exports
export PATH="$HOME/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# Default Editor
if [ -f /bin/nvim ]; then
	export EDITOR="nvim"
	export VISUAL="nvim"
fi

# Aliases
source ~/.aliasrc

if [ -f /etc/bash_completion ]; then
  source /etc/bash_completion
fi

# Overwrite cd with zoxide
if [ -f /usr/bin/zoxide ]; then
   eval "$(zoxide init bash)"   
   alias cd="z"
fi

shopt -s direxpand
shopt -s dirspell
shopt -s cdspell  

# Rust
. "$HOME/.cargo/env"

# Fastfetch on startup
if [ -f /usr/bin/fastfetch ]; then
  fastfetch
fi
