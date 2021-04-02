# Making a puppet file
file { '0-create_a_file.pp':
    ensure  => 'file',
    path    => '/tmp/holberton',
    content => 'I love Puppet',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744',
}
