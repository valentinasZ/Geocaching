#include <iostream>

using namespace std;

int main()
{
    for (int A = 0; A < 10; A++) {
        for (int B = 0; B < 10; B++) {
            for (int C = 0; C < 10; C++) {
                for (int D = 0; D < 10; D++) {
                    for (int E = 0; E < 10; E++) {
                        for (int F = 0; F < 10; F++) {
                            for (int G = 0; G < 10; G++) {
                                for (int H = 0; H < 10; H++) {
                                    for (int K = 0; K < 10; K++) {
                                        for (int J = 0; J < 10; J++) {
                                            if ((A != B && A != C && A != D && A != E && A != F && A != G && A != H && A != K && A != J) &&
                                                (B != C && B != D && B != E && B != F && B != G && B != H && B != K && B != J) &&
                                                (C != D && C != E && C != F && C != G && C != H && C != K && C != J) &&
                                                (D != E && D != F && D != G && D != H && D != K && D != J) &&
                                                (E != F && E != G && E != H && E != K && E != J) &&
                                                (F != G && F != H && F != K && F != J) &&
                                                (G != H && G != K && G != J) &&
                                                (H != K && H != J) &&
                                                (K != J) &&
                                                (A + C) == (E + F + D) &&
                                                ((F+G+A)*2) == (H+C+J) &&
                                                ((D+E+B))==2*K &&
                                                (B + J + G) == (H + D + K) &&
                                                (E + B) == (G + C)
                                                ) {

                                                cout << "U: " << (A+B)-E << ", V: " << K-F << ", W: " << (H+J)-C << ", X: " << G+C << ", Y: " << (D+H)*2
                                                     << ", Z: " << J-D << endl;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}
