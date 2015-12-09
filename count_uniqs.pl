#!/bin/usr/perl
# sqlite3 gameInfo.db "select genre from Games;" | sort | uniq -c | perl count_uniqs.pl | sort -n
# sqlite3 gameInfo.db "select appid, genre from Games;" | perl count_uniqs.pl

#%genres = ();

while(<>){
    $_ =~ /\s*(\d+)\|(.*)/;
    $appid = $1;
    #print $_;
    @genres = split /, /, $2;
    print "$appid\n" if $2 eq "";
    for $g (@genres){
        print "$g\n";
        #$genres{$g} += $count or $genres{$g} = $count;
    }
}

#for $key (keys %genres){
    #print "$genres{$key} $key\n";
#}
#print "\n", length(%genres)