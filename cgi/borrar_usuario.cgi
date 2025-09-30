#!/usr/bin/perl
use DBI;

my $db=DBI->connect('dbi:mysql:database=gpsystems;host=localhost','administrador','admin');
my $q = $db->prepare("delete from gpsystems.users where state=1");
$q->execute();
$q->finish();
