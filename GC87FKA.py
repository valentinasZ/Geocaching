#task: find mistakes in c++ code and rewrite it in phyton
code  = '''string txt = "TO GET FINAL COORDINATES, CALCULATE abc AND xyz VALUES:";
int abc = 0;
int xyz = 999;
int i;

for (i=9; i>0; i--)

   abc += 5;

   xyz -= 7;

}
abc = xyz / i;
switch (abc) {

   case 0:

      abc += abc * 3;

      xyz -= abc;

   break;

 

   case 25:

      abc += 105;

      xyz -= abc * 2;

   break;

 

   case 45:

      abc = abc * 2;

      xyz -= abc * 2;

   break;

 

   default:

      abc += 75 * 3;

      xyz -= 200;

   break;

}


xyz -= txt.length() * 4;


while (i < 8) {

   abc += 3;

   xyz -= 5;

   i++;

}


xyz += abc;

xyz -= 100;

abc++;


cout << txt[9] << " 54 " << 50+i << txt[24] << abc << '\n';

cout << txt[4] << " 24 " << i/2 << txt[24] << xyz;'''

#solution
def GC87FKA(abc,xyz,txt):
    count = 0
    for i in range(0,9):
        abc+=5
        xyz-=7
    if abc==45:
        abc = abc*2
        xyz-=abc*2
    else:
        abc == abc
        xyz == xyz
    xyz -= len(txt)*4
    while count<8:
        abc+=3
        xyz-=5
        count+=1
    xyz+=abc-100
    abc+=1
    print (txt[9] + ' 54 ' + str(50+count)+txt[24]+str(abc))
    print (txt[4] + ' 24 ' + str(count/2)[::-1].replace('.','')+txt[24]+str(xyz))
GC87FKA(abc=0,xyz=999,txt = 'TO GET FINAL COORDINATES, CALCULATE abc AND xyz VALUES:')