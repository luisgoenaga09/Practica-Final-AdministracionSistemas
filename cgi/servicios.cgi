#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);
use Socket;

print header();
print start_html(-title => 'Estado de los Servicios');

# Función para verificar el estado de un servicio
sub check_service {
    my ($port, $service_name) = @_;
    my ($name, $aliases, $protocol_number) = getprotobyname("tcp");
    socket(SOCKET, PF_INET, SOCK_STREAM, $protocol_number);
    
    if (connect(SOCKET, pack_sockaddr_in($port, inet_aton("localhost")))) {
        return "<p>$service_name  <strong>activo</strong>.</p>";
    } else {
        return "<p>$service_name <strong>inactivo</strong>.</p>";
    }
}

# Verificar el estado de los servicios
my @services = (
    { port => 443, name => 'HTTPS' },
    { port => 1024, name => 'SSH' },
    { port => 3306, name => 'MariaDB' },
    { port => 25, name => 'SMTP' },
    # Agrega más servicios según sea necesario
);

# Mostrar el estado de los servicios en la página web
print "<h1>Estado de los Servicios</h1>";
print "<div>";

foreach my $service (@services) {
    my $status = check_service($service->{port}, $service->{name});
    print $status;
}

print "</div>";
print end_html();

