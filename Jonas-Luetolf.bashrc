shopt -s checkwinsize

PS1="\[\e[1;30;42m\] \u\[\e[1;32;46m\]\[\e[1;30;46m\] \W\[\e[0m\e[1;36m\]\[\e[0m\]"


#exports
export PATH="$HOME/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/bin/AppImages/:$PATH"

if [ -f /bin/nvim ]; then
	export EDITOR="nvim"
	export VISUAL="nvim"
fi

#source other files
source ~/.aliasrc

if [ -f /etc/bash_completion ]; then
  source /etc/bash_completion
fi

if [ -f /usr/bin/zoxide ]; then
   eval "$(zoxide init bash)"   
   alias cd="z"
fi


shopt -s direxpand
shopt -s dirspell
shopt -s cdspell  

set -o vi
