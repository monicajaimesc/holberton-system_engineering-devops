# using strace to find out why Apache is returning a 500 e
exec { 'replace':
  command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
