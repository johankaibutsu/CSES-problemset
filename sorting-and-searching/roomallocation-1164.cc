#include <bits/stdc++.h>
#define pb push_back
#define endl '\n'
#define lli long long int
#define li long int
#define ld long double
#define vii vector<int, int>
#define pii pair<int, int>
using namespace std;
const lli mod = 1e9 + 7;

int main()
{
	int n, x, y;
	cin >> n;
	vector<pair<int, pii>> v;
	for (int i = 1; i <= n; i++)
	{
		cin >> x >> y;
		v.pb({x, {-1, i}});
		v.pb({y, {1, i}}); 
	}
	sort(v.begin(), v.end());

	vector<int> rooms;
	int occupied_rooms = 0, max_rooms = 0, in_or_out, ind;
	int ans[200005];
	for (auto ele : v)
	{
		in_or_out = ele.second.first;
		ind = ele.second.second;

		if (in_or_out == 1)
		{
			rooms.pb(ans[ind]);
		}
		else if (occupied_rooms == rooms.size())
		{
			ans[ind] = ++max_rooms;
		}
		else
		{
			ans[ind] = rooms[occupied_rooms++];
		}
	}
	cout << max_rooms << endl;
	for (int i = 1; i <= n; i++)
	{
		cout << ans[i] << " ";
	}
	return 0;
}