# puppet manifest to kill a process by name
exec { 'kill process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}