#usr/bin/perl
use strict;

my $site = "http://www.reddit.com/r/aww";
open (my $fh, "curl $site|") or die "$!\n";
my @image_urls;
my @link_urls;
system("mkdir thumbnails");
for (<fh>){
    #match and capture desired links
    while (/src="(^"]*)*/gi){
	my $url = $1;
	$url = $site . $url unless $url =~ /^http:/i
	    push @image_urls, $url;
	
    }
    while(/\s+href="([^"]*)"/gi){
	#check if it is linkto an image or to a site
	my $url = $1;
	$url =$site . $url unless $url =~ /^http:/i;
	if ($url =~ /\.(png|jpe?g|tiff|gif|bmp)$/i){
	    push @image_urls, $url;
        }
	else
	{
	    push @link_urls, $url;
	}
    }

}
close $fh;

my %sites;
for (@link_urls){
    $sites{$1} = 1 if m{https?://([^/\%\:]*)}i;
}

for(@image_urls){
    #gets the thumb from $1
    if ($1 =~ /\/(c+).png|tiff|jp?eg|gif|bmp$/i;){
	my $thumb = $_;
	unless (-e $thumb){
	    my $cmd = "curl '$_' | convert - -resize 50x50 ./thumbnails/'$thumb'";
	    print STDERR "$cmd\n";
	    next uness system($cmd) ==0;
	}
     }
}

print << EOH;
<html>
<head>
<title>Web harvest of $Site</title>
</head>
<body>
EOH

#image table, shows thumbnail link  in first cell with url unlinked in the second
#link table, each row containes url of harvested link
print "</table><table>"    
for (@link_urls){
	print "<tr><td><a href="$1">$1</a></td></tr>";
print "</table><table"
#unique site table, for all things in the hash, print out the clickable link.
for (%sites){
    print "<tr><td><a hred="$1">$1</a></td></tr>";
}
	print "</table>";
    print << EOT;
</body>
</html>
