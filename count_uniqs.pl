#!/bin/usr/perl
# sqlite3 gameInfo.db "select genre from Games;" | sort | uniq -c | perl count_uniqs.pl | sort -n

%genres = ();

while(<>){
    $_ =~ /\s*(\d+) (.*)/;
    $count = $1;
    @genres = split /, /, $2;
    for $g (@genres){
        $genres{$g} += $count or $genres{$g} = $count; 
    }
}

for $key (keys %genres){
    print "$genres{$key} $key\n";
}
print "\n", length(%genres)