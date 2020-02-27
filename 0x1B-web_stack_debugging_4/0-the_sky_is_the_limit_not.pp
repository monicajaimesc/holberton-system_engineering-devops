# using ApacheBench to simulate HTTP requests to a web server. 
# found that worker process and worker_connections shoul be incremented
exec { 'replace':
  command => "/bin/sed -i 's/worker_processes 4;/worker_processes 10;/g' /etc/nginx/nginx.conf"
}

# restart the service nginx
service { 'nginx':
  ensure  => running,
  restart => 'usr/sbin/service nginx restart',
}


