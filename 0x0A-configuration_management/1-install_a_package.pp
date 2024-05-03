# Installing Flask, werkzeug from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => installed,
  provider => 'pip3',
}

