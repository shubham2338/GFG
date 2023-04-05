//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int countSpecialNumbers(int N, vector<int> arr) {
        int res=0;
        int m=*max_element(arr.begin(),arr.end());
        unordered_map<int,int>mp;
        for(int i=0;i<N;i++){
            int e=arr[i];
            if(mp[e]<2){
                for(int j=e;j<=m;j+=e){
                    mp[j]++;
                }
            }
        }
        for(int i=0;i<N;i++){
            int e=arr[i];
            if(mp[e]>1)res++;
        }
        return res;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<int> arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        Solution ob;
        cout << ob.countSpecialNumbers(N, arr) << endl;
    }
    return 0;
}
// } Driver Code Ends