#!/bin/bash

#
#Casey Gilray
#Make Tile shell Script
#1/5/13
#cgilray@gmail.com
#

export PATH="$PATH:/usr/local/netpbm/bin"
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/usr/local/netpbm/lib"
export RGBDEF="/usr/X11/share/X11/rgb.txt"
#check to make sure there are enough argumets
if [ $# -ne 2 ]; then
    echo "usage: $0 image1.ppm image2.ppm" >& 2
    exit 1
fi

#reseve names for base, back, and allocate space for temp files
BASE=`basename  $1 .ppm`
BACK=`basename  $2 .ppm`
echo "$BASE"
echo "$zBACK"
CORNER00=/tmp/$BASE$$-00.ppm
CORNER01=/tmp/$BASE$$-01.ppm
CORNER10=/tmp/$BASE$$-10.ppm
CORNER11=/tmp/$BASE$$-11.ppm
BASETOP=/tmp/$BASE$$-top.ppm
BASEBOTTOM=/tmp/$BASE$$-bottom.ppm
BASEBACK=/tmp/$BASE$$-back.ppm
MASK=/tmp/$BASE$$-mask.pbm
BASETILE=/tmp/$BASE$$-tile.ppm

#split files into width, height, half width and half height
INFO1=`pamfile $1`||exit 2
W1=`echo $INFO1| awk '{print $4}'`
echo "Width of image 1 is $W1"
W1H=`expr $W1 / 2`
H1=`echo $INFO1| awk '{print $6}'`
echo "Height of image 1 is $H1"
H1H=`expr $H1 / 2`
INFO2=`pamfile $2`||exit 2
W2=`echo $INFO2| awk '{print $4}'`
H2=`echo $INFO2| awk '{print $6}'`
echo "Width of image 2 is $W2"
echo "Height of image 2 is $H2"
#check if both arguments are square
if [ $W1 -ne $H1 ]; then
    echo "Image 1 must be square">& 2
    exit 2
fi
if [ $W2 -ne $H2 ]; then
    echo "Image 2 must be sqaure">& 2
    exit 2
fi
#check if both arguments are the same size
if [ $W1 -ne $W2 ]; then
    echo "Both images must be of the same size">& 2
    exit 2
fi
#Given steps to cut apart and mask the images
pamcut -left 0 -top 0 -width $W1H -height $H1H $1 > $CORNER00||exit 2
pamcut -left $W1H -top 0 -width $W1H -height $H1H $1> $CORNER01||exit 2
pamcut -left 0 -top $H1H -width $W1H -height $H1H $1> $CORNER10|| exit 2
pamcut -left $W1H -top $H1H -width $W1H -height $H1H $1> $CORNER11|| exit 2

pnmcat -leftright $CORNER11 $CORNER10 > $BASETOP
pnmcat -leftright $CORNER01 $CORNER00 > $BASEBOTTOM
pnmcat -topbottom $BASETOP $BASEBOTTOM > $BASEBACK 

ppmcolormask white < $BASEBACK > $MASK
pamcomp -alpha=$MASK $BASEBACK "$BACK.ppm" > $BASETILE

pnmtojpeg -quality=80 $BASETILE > $BASE-tile.jpg
pnmquant 256 < $BASETILE | ppmtogif > $BASE-tile.gif


`rm /tmp/$BASE*`
exit 0