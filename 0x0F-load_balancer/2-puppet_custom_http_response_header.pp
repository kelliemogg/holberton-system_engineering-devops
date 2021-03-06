# configure http header with puppet
exec { 'update':
    command  => 'apt-get update',
    user     => 'root',
    provider => 'shell'
}
->

package { 'nginx':
    ensure   => present,
    name     => 'nginx',
    provider => 'apt'
}
->

exec { 'Add header':
    command  => 'sed -i "48i add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default',
    user     => 'root',
    provider => 'shell'
}

->
exec { 'Start nginx':
    command  => 'service nginx restart',
    user     => 'root',
    provider => 'shell'
}
