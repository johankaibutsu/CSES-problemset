#include <bits/stdc++.h>
 
using namespace std;
 
const int MaxN = 2 * 1e5;
 
struct Trio{
    int L, R, Index;
};
 
int N;
array<Trio, MaxN> Range;
array<bool, MaxN> Contain, BeContained;
 
int main(){
    cin >> N;
 
    for(int i = 0; i < N; i ++){
        cin >> Range[i].L >> Range[i].R;
        Range[i].Index = i;
    }
 
    sort(Range.begin(), Range.begin() + N, [&] (const Trio A, const Trio B){
        return (A.L == B.L? A.R > B.R : A.L < B.L);
    });
 
    int MinR = INT_MAX, MaxR = 0;
 
    for(int i = N - 1; i >= 0; i --){
        if(Range[i].R >= MinR){
            Contain[Range[i].Index] = true;
        }
 
        MinR = min(MinR, Range[i].R);
    }
 
    for(int i = 0; i < N; i ++){
        if(Range[i].R <= MaxR){
            BeContained[Range[i].Index] = true;
        }
 
        MaxR = max(MaxR, Range[i].R);
    }
 
    for(int i = 0; i < N; i ++){
        cout << Contain[i] << ' ';
    }
 
    cout << '\n';
 
    for(int i = 0; i < N; i ++){
        cout << BeContained[i] << ' ';
    }
}