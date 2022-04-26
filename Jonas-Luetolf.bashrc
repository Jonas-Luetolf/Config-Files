PS1="$(tput bold)$(tput setaf 71)\W $(tput setaf 192)>$(tput sgr0) "



#exports
export PS1
export PATH="$HOME/bin:$PATH"
export EDITOR="nvim"
export VISUAL="nvim"

#source other files
source ~/.aliasrc


# show todo list
if  command -v todo-list &> /dev/null
then
    echo "My To-Do List:"
	todo-list show -l tasks	#replace tasks with your todo list name
fi
