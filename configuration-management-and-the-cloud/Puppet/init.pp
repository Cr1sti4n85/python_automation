/*
In Puppet, code that defines a resource begins with a lowercase letter, whereas code that defines a relationship begins with a capital letter. 
*/

class ntp {
  package { 'ntp':
    ensure => latest,
  } 
  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/etc/ntp.conf'],
  }
}

include ntp