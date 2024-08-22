# Enable the user to login and open files without error.

exec { 'increase-file-limits-for-holberton-user':
  command => 'sed -i -e "/holberton hard/s/5/50000/" -e "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/bin'],
}
