#include<bits/stdc++.h>
using namespace std;
int main()
{
    {
         int n;cin>>n;
         vector<int> v(n);
         for(int i=0;i<n;i++)
         {
             v[i]=i+1;
         }
         while(v.size()>1)
         {
             vector<int> jose;
             int j=1;
             for(int i=0;i<((v.size())/2);i++)
             {
                 cout<<v[j]<<" ";
                 jose.push_back(v[j-1]);
                 j=j+2;
             }
             if(v.size()%2==0)
             {
                 v=jose;
             }
             else
             {
                 reverse(jose.begin(),jose.end());
                 jose.push_back(v[(v.size()-1)]);
                 reverse(jose.begin(),jose.end());
                 v=jose;
             }
         }
         cout<<v[0]<<"\n";
    }
    return 0;
}