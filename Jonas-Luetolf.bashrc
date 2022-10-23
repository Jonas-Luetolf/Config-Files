BG1=75
FG1=0
BG2=252
FG2=0


PS1="$(tput setab $BG1)$(tput setaf $FG1)\u $(tput setaf $BG1)$(tput setab $BG2)$(tput setaf $FG2) \W$(tput setab 0)$(tput setaf $BG2)$(tput sgr0) "
#exports
export PS1
export PATH="$HOME.local/bin:$PATH"
export EDITOR="nvim"
export VISUAL="nvim"

#source other files
source ~/.aliasrc



if [ -f /etc/bash_completion ]; then
  source /etc/bash_completion
fi

shopt -s direxpand
shopt -s dirspell
shopt -s cdspell  

set colored-stats on


# show todo list
if  command -v todo-list &> /dev/null
then
    echo "My To-Do List:"
	todo-list show tasks	#replace tasks with your todo list name
fi
