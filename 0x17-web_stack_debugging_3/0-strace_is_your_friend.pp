# automated puppet fix to find out why Apache is returning error

exec { 'fix-error':
  command => '/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/var/www/html/wp-settings.php',
}