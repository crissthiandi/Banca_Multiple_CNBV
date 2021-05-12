convert -delay 1 reducido.mp4 -loop 3 -dispose Background animation.gif
convert animation.gif -coalesce -fuzz 2% +dither -layers Optimize +map output.gif
gifsicle -O3 --lossy=80 --colors 256 animation.gif -o output_reduce.gif
gifsicle -O3 --lossy=80 --colors 256 output.gif -o output_reduce_2.gif
