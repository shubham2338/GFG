//{ Driver Code Starts
// Program to find the maximum profit job sequence from a given array 
// of jobs with deadlines and profits 
#include<bits/stdc++.h>
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
}; 


// } Driver Code Ends
/*
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
};
*/

class Solution 
{
    public:
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        // your code here
        vector<vector<int>>v(n);
        int mx= 0; 
        // n= n*3;
       for(int i= 0; i<n;i++){
           
           v[i].push_back(arr[i].profit);
           v[i].push_back(arr[i].id); 
           v[i].push_back(arr[i].dead);
           
           mx = max(mx, arr[i].dead); 
           
       }
       sort(v.begin(), v.end());
       reverse(v.begin(), v.end());
       
       vector<int>vis(mx+1, 0);
       int sum = 0; 
      
       int cnt =0;
       for(int i= 0; i<n;i++){
               for(int j= v[i][2]; j>0; j--){
                   
               
               if(!vis[j] ){
                   vis[j] = 1;
                   
                   sum += v[i][0];
                   cnt++;
                   break; 
                  
               }
               
            }
       }
       
       vector<int> ans; 
       ans.push_back(cnt);
       ans.push_back(sum);
       return ans; 
    }
};

//{ Driver Code Starts.
// Driver program to test methods 
int main() 
{ 
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        Job arr[n];
        
        //adding id, deadline, profit
        for(int i = 0;i<n;i++){
                int x, y, z;
                cin >> x >> y >> z;
                arr[i].id = x;
                arr[i].dead = y;
                arr[i].profit = z;
        }
        Solution ob;
        //function call
        vector<int> ans = ob.JobScheduling(arr, n);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
	return 0; 
}



// } Driver Code Ends