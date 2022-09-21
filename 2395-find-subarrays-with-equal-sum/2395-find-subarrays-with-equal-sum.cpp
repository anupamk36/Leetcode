class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        unordered_map <int,int> mp;
        for(int i=1;i<nums.size();i++){
            int sum = nums[i]+nums[i-1];
            mp[sum]++;
            if(mp[sum]>1) return true;
        }
        return false;
    }
};

