0707070000010000000006660000000000000000010000001352474640300000700000000237.start fplayback -i on -r off -f 1 -e on -h on -t on -a on -k on -s 1
tcur 0
fps 24
tset 0 10
frange 1 240
unitlength 1
unitmass 1
prompt '`strcat(oppwf(), " -> ")`'
0707070000010000000006660000000000000000010000001352474640300001300000001053.variables set -g ACTIVETAKE = 'Main'
set -g E = '2.7182818284590452354'
set -g EYE = 'stereo'
set -g HIP = 'E:/code/learn/scenes'
set -g HIPFILE = 'E:/code/learn/scenes/tests.hip'
set -g HIPNAME = 'tests'
set -g JOB = 'C:/Users/kris'
set -g PI = '3.1415926535897932384'
set -g POSE = 'C:/Users/kris/Documents/houdini17.0/poselib'
set -g PROJECT = 'arendi'
set -g SEQUENCE = 'sq_001'
set -g SHOT = 'sh0101'
set -g _HIP_SAVEPLATFORM = 'windows-x86_64-cl19.15'
set -g _HIP_SAVETIME = 'Wed Aug 14 10:57:39 2019'
set -g _HIP_SAVEVERSION = '17.0.352'
set -g status = '0'
0707070000010000000006660000000000000000010000001352474640300001100000000310.aliases alias bye 'quit'
alias cd 'opcf'
alias cp 'opcp'
alias h 'history'
alias hython 'python'
alias ls 'opls'
alias matramp 'opramp'
alias opcd 'opcf'
alias oppwd 'oppwf'
alias pwd 'oppwf'
alias rm 'oprm'
0707070000010000000006660000000000000000010000001352474640300001400000000021.takeconfig takename -g take
0707070000010000000006660000000000000000010000001352474640300001500000000000.hou.session 0707070000010000000006660000000000000000010000001352474640300001500000000204.OPlibraries E:/code/learn/hda/bake_geo.hda
E:/code/learn/hda/import_geo.hda
E:/code/learn/hda/import_pkg.hda
E:/code/learn/hda/OUT_bake_geo.hda
0707070000010000000006660000000000000000010000001352474640300001700000000000.OPpreferences 0707070000010000000006660000000000000000010000001352474640300002000000000012expression.func # 0 bytes
0707070000010000000006660000000000000000010000001352474640300001000000000646vex.def comment ""
position 0 4.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed off
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001100000000020vex.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001500000000041vex.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001000000000646mat.def comment ""
position 0 3.75
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001100000000020mat.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001500000000041mat.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001000000000641obj.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display on render on highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772535
  modify 1565773058
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001100000000020obj.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001500000000041obj.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001000000000002obj.net 1
0707070000010000000006660000000000000000010000001352474640300001000000000645out.def comment ""
position 0 1.5
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001100000000020out.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001500000000041out.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001000000000002out.net 1
0707070000010000000006660000000000000000010000001352474640300001100000000647part.def comment ""
position 0 5.25
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed off
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001200000000020part.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001600000000041part.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001100000000002part.net 1
0707070000010000000006660000000000000000010000001352474640300000700000000646ch.def comment ""
position 0 0.75
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001000000000020ch.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001400000000041ch.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300000700000000002ch.net 1
0707070000010000000006660000000000000000010000001352474640300001100000000646shop.def comment ""
position 0 2.25
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001200000000020shop.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001600000000041shop.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001100000000002shop.net 1
0707070000010000000006660000000000000000010000001352474640300001000000000643img.def comment ""
position 0 3
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772536
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001100000000020img.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300001500000000041img.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001700000000032img/comp1.init type = img
matchesdef = 0
0707070000010000000006660000000000000000010000001352474640300001600000000643img/comp1.def comment ""
position 0 0
connectornextid 0
flags =  lock off model off template off footprint off xray off bypass off display off render off highlight off unload off savedata off compress on colordefault on exposed on
outputsNamed3
{
}
inputsNamed3
{
}
inputs
{
}
stat
{
  create 1565772538
  modify 1565772560
  author kris@creative
  access 0777
}
color UT_Color RGB 0.8 0.8 0.8 
delscript ""
exprlanguage hscript
end
0707070000010000000006660000000000000000010000001352474640300001700000000020img/comp1.parm {
version 0.8
}
0707070000010000000006660000000000000000010000001352474640300002300000000041img/comp1.userdata     ___Version___    17.0.3520707070000010000000006660000000000000000010000001352474640300001600000000002img/comp1.net 1
0707070000010000000006660000000000000000010000001352474640300001000000000002img.net 1
0707070000010000000006660000000000000000010000001352474640300001000000000002vex.net 1
0707070000010000000006660000000000000000010000001352474640300001000000000002mat.net 1
0707070000010000000006660000000000000000010000001352474640300002600000000000.scenefilevisualizers 0707070000010000000006660000000000000000010000001352474640300001500000062534.application networkeditor -p '{\n}\n'performance -c on -d on -f on -g off -k on -m off -n on -o on -t off -v on -y on -u on -e off -r absolute -w tree panetab12
chopview -a 0 -c "" -k 1 -m 1 -b 1 -e 1 -f 0 -g 0 -H 1 -i 0 -j 1 -l 0 -n 1 -V 0 -y 0 -B 0 -s 0 -S 0.034375 -u 0 -v 0 -h -10 310 -r -1.5 1.5 Build.panetab13
imgdispopt -m 256 -P on -M on -A on -g 2.2 -G "* ^P ^Pz ^N ^M ^B ^V ^Af ^Nt" -B 1 -v split -V 2 2 -d h -a off -i 2 -b 0 0 0 -o "" -h on -H on -c 0.8 0.8 0.8 -C 1 1 1 -S 0.8 0.8 0.8 -R 6 -F dc -D "" -I "" -f "" -s off -r 256 256 -p on -l on -t on
imgview -z 1 -p (none) 0 -c 0 -l on -s off -i imgview2
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 1
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 2
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 3
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 4
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 5
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 6
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 7
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 8
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 9
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 10
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 11
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 12
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 13
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 14
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 15
imgview2d  -V on -L on -G on -H on -P off -m 0 -p 0 1 -b 1 1 0 -g 2.2 -d "" -c -1 -t off -i on -X on imgview2 16
imgviewtime -V on -L on -G on -H on -P off -r 24 -u fr -g 0 -f on -e on -b on -d imgview2
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 1
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 2
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 3
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 4
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 5
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 6
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 7
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 8
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 9
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 10
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 11
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 12
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 13
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 14
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 15
imgviewhist -V on -L on -G on -H on -P off -c -1 -h 0 -i on imgview2 16
viewerstow -b open -x open -l open -m hide -c hide -d open Build.panetab1.world
vieweroption -a 2 -h 0 -m 1 -r 'View: Mantra' Build.panetab1.world
viewergrouplist -g off -s 0 0 -c  on -t matchselect -m '*' -e on -p off -h on Build.panetab1.world
vieweroption -p 0 -P '+geo -cam -light -muscle -bone -null -blend -other' Build.panetab1.world
viewlayout -s 2 Build.panetab1.world
viewerinspect Build.panetab1.world mode ( objects ) object_properties ( ) prim_properties ( ) enable ( 0 ) magnify ( 1 )
viewtype -t perspective Build.panetab1.world.`vpname("Build.panetab1.world",2)`
viewtype -t ortho_top Build.panetab1.world.`vpname("Build.panetab1.world",1)`
viewtype -t ortho_front Build.panetab1.world.`vpname("Build.panetab1.world",3)`
viewtype -t ortho_right Build.panetab1.world.`vpname("Build.panetab1.world",4)`
viewname -l on -n aaaa3 Build.panetab1.world.`vpname("Build.panetab1.world",2)`
viewname -l on -n aaaa2 Build.panetab1.world.`vpname("Build.panetab1.world",1)`
viewname -l on -n aaaa1 Build.panetab1.world.`vpname("Build.panetab1.world",3)`
viewname -l on -n aaaa0 Build.panetab1.world.`vpname("Build.panetab1.world",4)`
viewname -l off -n persp1 Build.panetab1.world.`vpname("Build.panetab1.world",2)`
viewname -l off -n top1 Build.panetab1.world.`vpname("Build.panetab1.world",1)`
viewname -l off -n front1 Build.panetab1.world.`vpname("Build.panetab1.world",3)`
viewname -l off -n right1 Build.panetab1.world.`vpname("Build.panetab1.world",4)`
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r unique scene Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r scene selectscene Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L off -G on -B none -d uv -r unique ghostscene Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w on -s shade_wire -F off -l on -L on -G off -B none -d uv -r unique display Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w off -s wire -F off -l on -L off -G off -B none -d uv -r unique current Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s wire -F on -l on -L off -G on -B none -d uv -r unique template Build.panetab1.world.persp1
viewdisplay -B light -b off -d off -C 2 -e 1 -F on -f off -g on -G '*' -h off -H on -j off -J off -L on -n 0.2 -o on -O on -q on -r on -s off -t on -V 2 -z off -y off -x off -X off -U 4 -Y 4 -T on -R on -i on -D on -k off Build.panetab1.world.persp1
viewdisplay -Q on -m on -v on Build.panetab1.world.persp1
viewdisplay -W  off 0 0 Build.panetab1.world.persp1
viewdisplay -c on -l1 -K on -P points -p 3 Build.panetab1.world.persp1
viewdispopts -a on -b current -c 1 -C 60  -d  on -D 1 -g on -i on -n on -N 1000000 -o off -p 10 -P off -r off -R on -S 768 -m 0.05 -s on -u uv -w 0.1 -W 0.9 -x on -X off Build.panetab1.world.persp1
vieweffect -a 2 -A 4 -b on -B 1 -d on -D on off -e 0.8 -E -30 -30 -100 -f 1 -F 0 -g 2.2 -G 0 -h 1 -H on -i on -I 1 -j on -J 20 -K 2 -k 1 -l '' -m on -M 2048 -o off -O 3 -p off -P 3 -q 1 -Q 2 -r 2048 2048 -s 2 -t 100 -T 100 -u off -U off -v 256 256 256 -w 0.05 -W off -x 0.4 0.4 0.4 -X 0.2 0.2 0.2 -y 0.4 0.4 0.4 -Y 0.0025 0.0025 0.0025 -z 0.25 -Z 1 Build.panetab1.world.persp1
viewinfotext -m off Build.panetab1.world.persp1
viewlight  -a on -d on -e on -h off -l on -n 8 -s on Build.panetab1.world.persp1
viewbackground -b on -e on -q 1 -i off -m 0 0 -M 1 1 Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 persp Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 cam Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 top Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 front Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 right Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 bottom Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 back Build.panetab1.world.persp1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 left Build.panetab1.world.persp1
viewroto  -S file -F '$HH/pic/uvgrid_grey.pic' -C '' -a on -o 0 0 -s 1 1 -B 0.2 uv Build.panetab1.world.persp1
viewtransform Build.panetab1.world.persp1 version ( 3 )  flag ( F )  orthowidth ( 3.63908 )  focal ( 50 )  aperture ( 41.4214 )  window ( 0 1 0 1 )  winroll ( 0 )  clear ( 1 )  nearfar ( 0.106531 4332.83 )  aspect ( 1.33333 )  pixelaspect ( 1 )  txyz ( 0 0 5.39275 )  pxyz ( 0 0 0 )  rotation ( 0.707107 -0.353553 0.612372 0 0.866025 0.5 -0.707107 -0.353553 0.612372  )  homedistance ( 5.39275 )  homeadjboxwidth ( 3.63908 )  homeorthowidth ( 3.63908 )  homeradius ( 4.32744 )  homeaxis ( 0 )  homecustom ( 0.707107 -0.353553 0.612372 0 0.866025 0.5 -0.707107 -0.353553 0.612372  )  adjustlimits ( 3 )  
viewcamera -c '' Build.panetab1.world.persp1
vieworthogrid -d on -o 0 0 0 -s 0.2 0.2 -r 5 5 -R 1 Build.panetab1.world.persp1
viewuvgrid -r on -s 0.1 0.1 -P off -S 64 64 -O 0 0 -C on -t on Build.panetab1.world.persp1
viewagentopts  -L on -b 0 -d 1 -l 0 -m 4 -p 1000 -w 1 Build.panetab1.world.persp1
viewonionskin  -e on -a 4 -b 4 -i 6 -o 0.5 -A 1 1 1 -B 1 1 1 Build.panetab1.world.persp1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r unique scene Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r scene selectscene Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L off -G on -B none -d uv -r unique ghostscene Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w on -s shade_wire -F off -l on -L on -G off -B none -d uv -r unique display Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w off -s wire -F off -l on -L off -G off -B none -d uv -r unique current Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s wire -F on -l on -L off -G on -B none -d uv -r unique template Build.panetab1.world.top1
viewdisplay -B light -b off -d off -C 2 -e 1 -F on -f off -g on -G '*' -h off -H on -j off -J off -L on -n 0.2 -o on -O on -q on -r on -s off -t on -V 2 -z off -y off -x off -X off -U 4 -Y 4 -T on -R on -i on -D on -k off Build.panetab1.world.top1
viewdisplay -Q on -m on -v on Build.panetab1.world.top1
viewdisplay -W  off 0 0 Build.panetab1.world.top1
viewdisplay -c on -l1 -K on -P points -p 3 Build.panetab1.world.top1
viewdispopts -a on -b current -c 1 -C 60  -d  on -D 1 -g on -i on -n on -N 1000000 -o off -p 10 -P off -r off -R on -S 768 -m 0.05 -s on -u uv -w 0.1 -W 0.9 -x on -X off Build.panetab1.world.top1
vieweffect -a 2 -A 4 -b on -B 1 -d on -D on off -e 0.8 -E -30 -30 -100 -f 1 -F 0 -g 2.2 -G 0 -h 1 -H on -i on -I 1 -j on -J 20 -K 2 -k 1 -l '' -m on -M 2048 -o off -O 3 -p off -P 3 -q 1 -Q 2 -r 2048 2048 -s 2 -t 100 -T 100 -u off -U off -v 256 256 256 -w 0.05 -W off -x 0.4 0.4 0.4 -X 0.2 0.2 0.2 -y 0.4 0.4 0.4 -Y 0.0025 0.0025 0.0025 -z 0.25 -Z 1 Build.panetab1.world.top1
viewinfotext -m off Build.panetab1.world.top1
viewlight  -a on -d on -e on -h off -l on -n 8 -s on Build.panetab1.world.top1
viewbackground -b on -e on -q 1 -i off -m 0 0 -M 1 1 Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 persp Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 cam Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 top Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 front Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 right Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 bottom Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 back Build.panetab1.world.top1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 left Build.panetab1.world.top1
viewroto  -S file -F '$HH/pic/uvgrid_grey.pic' -C '' -a on -o 0 0 -s 1 1 -B 0.2 uv Build.panetab1.world.top1
viewtransform Build.panetab1.world.top1 version ( 3 )  flag ( Fo )  orthowidth ( 2.22222 )  focal ( 50 )  aperture ( 41.4214 )  window ( 0 1 0 1 )  winroll ( 0 )  clear ( 1 )  nearfar ( 0.1 3467.78 )  aspect ( 1.33333 )  pixelaspect ( 1 )  txyz ( 0 0 3.68246 )  pxyz ( 0 0 0 )  rotation ( 1 0 0 0 1.19209e-07 1 0 -1 1.19209e-07  )  homedistance ( 3.68246 )  homeadjboxwidth ( 2.22222 )  homeorthowidth ( 2.22222 )  homeradius ( 3.4641 )  homeaxis ( 0 )  homecustom ( 0.707107 -0.353553 0.612372 0 0.866025 0.5 -0.707107 -0.353553 0.612372  )  adjustlimits ( 3 )  
vieworthogrid -d on -o 0 0 0 -s 0.2 0.2 -r 5 5 -R 1 Build.panetab1.world.top1
viewuvgrid -r on -s 0.1 0.1 -P off -S 64 64 -O 0 0 -C on -t on Build.panetab1.world.top1
viewagentopts  -L on -b 0 -d 1 -l 0 -m 4 -p 1000 -w 1 Build.panetab1.world.top1
viewonionskin  -e on -a 4 -b 4 -i 6 -o 0.5 -A 1 1 1 -B 1 1 1 Build.panetab1.world.top1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r unique scene Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r scene selectscene Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L off -G on -B none -d uv -r unique ghostscene Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w on -s shade_wire -F off -l on -L on -G off -B none -d uv -r unique display Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w off -s wire -F off -l on -L off -G off -B none -d uv -r unique current Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s wire -F on -l on -L off -G on -B none -d uv -r unique template Build.panetab1.world.front1
viewdisplay -B light -b off -d off -C 2 -e 1 -F on -f off -g on -G '*' -h off -H on -j off -J off -L on -n 0.2 -o on -O on -q on -r on -s off -t on -V 2 -z off -y off -x off -X off -U 4 -Y 4 -T on -R on -i on -D on -k off Build.panetab1.world.front1
viewdisplay -Q on -m on -v on Build.panetab1.world.front1
viewdisplay -W  off 0 0 Build.panetab1.world.front1
viewdisplay -c on -l1 -K on -P points -p 3 Build.panetab1.world.front1
viewdispopts -a on -b current -c 1 -C 60  -d  on -D 1 -g on -i on -n on -N 1000000 -o off -p 10 -P off -r off -R on -S 768 -m 0.05 -s on -u uv -w 0.1 -W 0.9 -x on -X off Build.panetab1.world.front1
vieweffect -a 2 -A 4 -b on -B 1 -d on -D on off -e 0.8 -E -30 -30 -100 -f 1 -F 0 -g 2.2 -G 0 -h 1 -H on -i on -I 1 -j on -J 20 -K 2 -k 1 -l '' -m on -M 2048 -o off -O 3 -p off -P 3 -q 1 -Q 2 -r 2048 2048 -s 2 -t 100 -T 100 -u off -U off -v 256 256 256 -w 0.05 -W off -x 0.4 0.4 0.4 -X 0.2 0.2 0.2 -y 0.4 0.4 0.4 -Y 0.0025 0.0025 0.0025 -z 0.25 -Z 1 Build.panetab1.world.front1
viewinfotext -m off Build.panetab1.world.front1
viewlight  -a on -d on -e on -h off -l on -n 8 -s on Build.panetab1.world.front1
viewbackground -b on -e on -q 1 -i off -m 0 0 -M 1 1 Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 persp Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 cam Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 top Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 front Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 right Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 bottom Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 back Build.panetab1.world.front1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 left Build.panetab1.world.front1
viewroto  -S file -F '$HH/pic/uvgrid_grey.pic' -C '' -a on -o 0 0 -s 1 1 -B 0.2 uv Build.panetab1.world.front1
viewtransform Build.panetab1.world.front1 version ( 3 )  flag ( Fo )  orthowidth ( 2.22222 )  focal ( 50 )  aperture ( 41.4214 )  window ( 0 1 0 1 )  winroll ( 0 )  clear ( 1 )  nearfar ( 0.1 3467.78 )  aspect ( 1.33333 )  pixelaspect ( 1 )  txyz ( 0 0 3.68246 )  pxyz ( 0 0 0 )  rotation ( 1 0 0 0 1 0 0 0 1  )  homedistance ( 3.68246 )  homeadjboxwidth ( 2.22222 )  homeorthowidth ( 2.22222 )  homeradius ( 3.4641 )  homeaxis ( 0 )  homecustom ( 0.707107 -0.353553 0.612372 0 0.866025 0.5 -0.707107 -0.353553 0.612372  )  adjustlimits ( 3 )  
vieworthogrid -d on -o 0 0 0 -s 0.2 0.2 -r 5 5 -R 1 Build.panetab1.world.front1
viewuvgrid -r on -s 0.1 0.1 -P off -S 64 64 -O 0 0 -C on -t on Build.panetab1.world.front1
viewagentopts  -L on -b 0 -d 1 -l 0 -m 4 -p 1000 -w 1 Build.panetab1.world.front1
viewonionskin  -e on -a 4 -b 4 -i 6 -o 0.5 -A 1 1 1 -B 1 1 1 Build.panetab1.world.front1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r unique scene Build.panetab1.world.right1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L on -G off -B none -d uv -r scene selectscene Build.panetab1.world.right1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s shade -F off -l on -L off -G on -B none -d uv -r unique ghostscene Build.panetab1.world.right1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w on -s shade_wire -F off -l on -L on -G off -B none -d uv -r unique display Build.panetab1.world.right1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P on -p off -f off -o off -w off -s wire -F off -l on -L off -G off -B none -d uv -r unique current Build.panetab1.world.right1
viewdispset -m off always -n off always -c off always -u off always -x off always -N off always -C off always -b off always -M off always -v off always -V off always -U off always -h off -P off -p off -f off -o off -w off -s wire -F on -l on -L off -G on -B none -d uv -r unique template Build.panetab1.world.right1
viewdisplay -B light -b off -d off -C 2 -e 1 -F on -f off -g on -G '*' -h off -H on -j off -J off -L on -n 0.2 -o on -O on -q on -r on -s off -t on -V 2 -z off -y off -x off -X off -U 4 -Y 4 -T on -R on -i on -D on -k off Build.panetab1.world.right1
viewdisplay -Q on -m on -v on Build.panetab1.world.right1
viewdisplay -W  off 0 0 Build.panetab1.world.right1
viewdisplay -c on -l1 -K on -P points -p 3 Build.panetab1.world.right1
viewdispopts -a on -b current -c 1 -C 60  -d  on -D 1 -g on -i on -n on -N 1000000 -o off -p 10 -P off -r off -R on -S 768 -m 0.05 -s on -u uv -w 0.1 -W 0.9 -x on -X off Build.panetab1.world.right1
vieweffect -a 2 -A 4 -b on -B 1 -d on -D on off -e 0.8 -E -30 -30 -100 -f 1 -F 0 -g 2.2 -G 0 -h 1 -H on -i on -I 1 -j on -J 20 -K 2 -k 1 -l '' -m on -M 2048 -o off -O 3 -p off -P 3 -q 1 -Q 2 -r 2048 2048 -s 2 -t 100 -T 100 -u off -U off -v 256 256 256 -w 0.05 -W off -x 0.4 0.4 0.4 -X 0.2 0.2 0.2 -y 0.4 0.4 0.4 -Y 0.0025 0.0025 0.0025 -z 0.25 -Z 1 Build.panetab1.world.right1
viewinfotext -m off Build.panetab1.world.right1
viewlight  -a on -d on -e on -h off -l on -n 8 -s on Build.panetab1.world.right1
viewbackground -b on -e on -q 1 -i off -m 0 0 -M 1 1 Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 persp Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 cam Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 top Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 front Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 right Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 bottom Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 back Build.panetab1.world.right1
viewroto  -S file -F '' -C '' -a on -o 0 0 -s 1 1 -B 1 left Build.panetab1.world.right1
viewroto  -S file -F '$HH/pic/uvgrid_grey.pic' -C '' -a on -o 0 0 -s 1 1 -B 0.2 uv Build.panetab1.world.right1
viewtransform Build.panetab1.world.right1 version ( 3 )  flag ( Fo )  orthowidth ( 2.22222 )  focal ( 50 )  aperture ( 41.4214 )  window ( 0 1 0 1 )  winroll ( 0 )  clear ( 1 )  nearfar ( 0.1 3467.78 )  aspect ( 1.33333 )  pixelaspect ( 1 )  txyz ( 0 0 3.68246 )  pxyz ( 0 0 0 )  rotation ( 6.12323e-17 0 1 0 1 0 -1 0 6.12323e-17  )  homedistance ( 3.68246 )  homeadjboxwidth ( 2.22222 )  homeorthowidth ( 2.22222 )  homeradius ( 3.4641 )  homeaxis ( 0 )  homecustom ( 0.707107 -0.353553 0.612372 0 0.866025 0.5 -0.707107 -0.353553 0.612372  )  adjustlimits ( 3 )  
vieworthogrid -d on -o 0 0 0 -s 0.2 0.2 -r 5 5 -R 1 Build.panetab1.world.right1
viewuvgrid -r on -s 0.1 0.1 -P off -S 64 64 -O 0 0 -C on -t on Build.panetab1.world.right1
viewagentopts  -L on -b 0 -d 1 -l 0 -m 4 -p 1000 -w 1 Build.panetab1.world.right1
viewonionskin  -e on -a 4 -b 4 -i 6 -o 0.5 -A 1 1 1 -B 1 1 1 Build.panetab1.world.right1
viewsnapshotoption -s off -h off -a 1 -v '*' Build.panetab1.world
cplane -o 0 0 0 -n 4.37114e-08 1 -4.37114e-08 -x 1.91069e-15 4.37114e-08 1 -l n -s 0.1 0.1 -c 40 40 -r 10 10 -d off Build.panetab1.world
glcache -t 512 -v 2048
imgview -p '(' none -z 1 ')' 0 -c 0 -l on -s off -i imgview2
panepath -d Build -f -p panetab14 /obj/
panepath -d Build -f -p panetab1 /obj/
panepath -d Build -f -p panetab2 /obj/
panepath -d Build -f -p panetab3 /obj/
panepath -d Build -f -p panetab4 /img/comp1/
panepath -d Build -f -p panetab13 /ch/
panepath -d Build -f -p panetab11 /obj/
panepath -d Build -f -p panetab5 /obj/
panepath -d Build -f -p panetab6 /obj/
panepath -d Build -f -p panetab12 /obj/
panepath -d Build -f -p panetab7 /obj/
panepath -d Build -f -p panetab8 /obj/
panepath -d Build -f -p panetab9 /obj/
panepath -d Build -f -p panetab10 /obj/
desk set Build
radial menu set main
viewupdate -u always
audiopanel -s p ''
audiopanel -s r off
audiopanel -s s 24
audiopanel -s f 24
audiopanel -t p stop
audiopanel -t l off
audiopanel -t r on
audiopanel -o m off
audiopanel -o t on
audiopanel -o u on
audiopanel -o l 1
audiopanel -o r 1
audiopanel -o d 0
audiopanel -r d 0.2
audiopanel -m 0
audiopanel -a ''
audiopanel -f 1
audiopanel -O 0
colorsettings -D -A -g 2.2 -l "" -p -s -v -i -r -c -f
compproject -r 1920 1080 -a 1 -d fp16 -p 0 1 -P full -f 0 -F 0 -l on
texcache  -a off -r 2147483647 2147483647 -m 10000 -M 8180
shopvisible +I3D +VMantra +RIB
0707070000010000000006660000000000000000010000001352474640300000700000000060.takes HoudiniTakeFile 1.0
take name Main kids 0
   e
0707070000010000000006660000000000000000010000001352474640300001000000000007.styles NSJb{}0707070000010000000006660000000000000000010000001352474640300002000000000004.contextoptions [
]
0707070000010000000006660000000000000000010000001352474640300000500000000024.cwd opcf /
takeset Main
0707070000010000000006660000000000000000010000001352474640300001300000000000TRAILER!!! 