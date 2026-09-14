#The command node default installs the sudo and ntp classes on all default #nodes.

node default {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
} /


/*
The command node webserver.example.com installs the sudo, ntp, and apache classes on nodes with the fully-qualified domain name webserver.example.com
*/
node webserver.example.com {
  class { 'sudo': }
  class { 'ntp':
        servers => ['ntp1.example.com', 'ntp2.example.com']
  }
  class { 'apache': }
}