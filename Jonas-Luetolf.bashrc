shopt -s checkwinsize

PS1="\[\e[1;30;42m\] \u\[\e[1;32;46m\]\[\e[1;30;46m\] \W\[\e[0m\e[1;36m\]\[\e[0m\]"


#exports
export PATH="$HOME/bin:$PATH"
if [ -f /bin/nvim ]; then
	export EDITOR="nvim"
	export VISUAL="nvim"
fi

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
