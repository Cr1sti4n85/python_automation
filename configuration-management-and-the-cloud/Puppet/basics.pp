/*
This code block includes a class with three resources, a package, a file, and a service. All of them are related to the Network Time Protocol
*/

class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
  }
}

/*This resource ensures that the /etc/issue file has a set of permissions and a specific line in it. 
 If the file already exists and has the desired content, then Puppet will understand that no action has to be taken. If the file doesn't exist, then puppet will create it. If the contents or permissions don't match, Puppet will fix them.
*/
file { '/etc/issue':
  mode    => '0644',
  content => "Internal system \l \n",
}