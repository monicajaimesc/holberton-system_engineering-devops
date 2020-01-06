#!/usr/bin/env bash
# HTTP header response in nginx with puppet
exec { 'apt-get update':
  command => '/usr/bin/apt-get -y update',
}
Package { "ngnix":
        ensure => present,
        require => Exec['apt-get update']
}

service { "nginx":
  ensure  => running,
  require => Package['nginx'],
}

file_line { 'header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By "$HOSTNAME";',
  require => Package['nginx'],
}


