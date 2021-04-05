# Puppet file to make changes to a config file 
file { '/etc/ssh/ssh_config':
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/holberton',
}
