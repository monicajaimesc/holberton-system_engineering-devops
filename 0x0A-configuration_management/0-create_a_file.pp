# Create a file in /tmp
file {'/tmp/holberton':
 # Whether the file should exist, and if so what...
 ensure => file,
 path => '/tmp/holberton',
 mode => '0744',
 owner => 'www-data',
 group => 'www-data',
 # # The desired contents of a file, as a string...
 content => 'I love Puppet' 

}
