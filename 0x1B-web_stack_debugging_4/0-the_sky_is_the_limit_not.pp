# Handle the high load

exec { 'modify_ulimit':
  command => "sed -i 's/^ULIMIT=\"-n [0-9]\+\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
  unless  => "grep -q '^ULIMIT=\"-n 4096\"' /etc/default/nginx",
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
