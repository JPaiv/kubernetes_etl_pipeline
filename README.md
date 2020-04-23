KUBERNETES ETL PIPELINE

This code will process over 30 million French businesses, corporations and associations in Kubernetes and AWS.

# .bashrc

# ndt command completion
eval "$(nitor-dt-register-complete --enable-profile)"

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/juhopaivarinta/.sdkman"
[[ -s "/home/juhopaivarinta/.sdkman/bin/sdkman-init.sh" ]] && source "/home/juhopaivarinta/.sdkman/bin/sdkman-init.sh"

# Added by serverless binary installer
export PATH="$HOME/.serverless/bin:$PATH"

# Aliases for Sok servers

alias s11='ssh jpaivari@217.29.235.214'
alias s21='ssh jpaivari@217.29.235.215'
alias s12='ssh jpaivari@217.29.235.216'
alias s22='ssh jpaivari@217.29.235.217'
