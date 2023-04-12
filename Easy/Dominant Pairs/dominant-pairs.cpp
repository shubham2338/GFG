//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++


class Solution{
public:
    int dominantPairs(int n,vector<int> &arr){
        // Code here
        sort(arr.begin(),arr.begin()+n/2);
        sort(arr.begin()+n/2,arr.end());
        int i=0;
        int j=n/2;
        int c=0;
        while(j<n && i<n/2){
            if(arr[i]>=arr[j]*5){
                c+=n/2-i;
                j++;
            }
            else i++;
        }
        return c;
    }  
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        Solution ob;
        cout<<ob.dominantPairs(n,arr)<<endl;
    }
}
// } Driver Code Ends