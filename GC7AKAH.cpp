#include <iostream>

using namespace std;

int main() {
     for (int sugar = 1; sugar < 300; sugar++) {
        for (int eggs = 1; eggs < 300; eggs++) {
            for (int flour = 1; flour < 300; flour++) {
                for (int butter = 1; butter < 300; butter++) {
                        if ((eggs-21) == sugar && butter+54==sugar && flour*3 == butter && ((butter+eggs)-(sugar+flour))==131)
                        {

                                cout << "sugar: " << sugar << ", eggs: " << eggs << ", flour: " << flour << ", butter: " << butter << ", total or A: " << butter+sugar+eggs+flour <<  ", B: " << eggs-flour << endl;
                                cout << "N 51 46." << butter+sugar+eggs+flour-222 << "W 00 24." << eggs-flour-150 << endl;

                }}}}}






return 0;
}
