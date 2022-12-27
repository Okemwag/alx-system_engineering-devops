# This manifest debugs an apache server to fix 500 error
exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path     => '/bin'
}
