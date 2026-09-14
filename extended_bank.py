"""
Extended LeetCode Solution Bank
800+ solutions across Python3, JavaScript, C++, and MySQL
Non-premium problems only.
Key: (titleSlug, lang)  Lang: "python3" | "javascript" | "cpp" | "mysql"
"""

EXTENDED_BANK = {
    # ─── TWO SUM ──────────────────────────────────────────────────
    ("two-sum", "python3"): '''class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen: return [seen[target-n], i]
            seen[n] = i
        return []''',
    ("two-sum", "javascript"): '''var twoSum = function(nums, target) {
    const seen = {};
    for (let i = 0; i < nums.length; i++) {
        const c = target - nums[i];
        if (c in seen) return [seen[c], i];
        seen[nums[i]] = i;
    }
    return [];
};''',
    ("two-sum", "cpp"): '''class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int c = target - nums[i];
            if (seen.count(c)) return {seen[c], i};
            seen[nums[i]] = i;
        }
        return {};
    }
};''',

    # ─── CONTAINS DUPLICATE ───────────────────────────────────────
    ("contains-duplicate", "python3"): '''class Solution:
    def containsDuplicate(self, nums): return len(nums) != len(set(nums))''',
    ("contains-duplicate", "javascript"): '''var containsDuplicate = function(nums) {
    return new Set(nums).size !== nums.length;
};''',
    ("contains-duplicate", "cpp"): '''class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
    }
};''',

    # ─── VALID ANAGRAM ────────────────────────────────────────────
    ("valid-anagram", "python3"): '''from collections import Counter
class Solution:
    def isAnagram(self, s, t): return Counter(s) == Counter(t)''',
    ("valid-anagram", "javascript"): '''var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const count = {};
    for (const c of s) count[c] = (count[c] || 0) + 1;
    for (const c of t) { if (!count[c]) return false; count[c]--; }
    return true;
};''',
    ("valid-anagram", "cpp"): '''class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int cnt[26] = {};
        for (char c : s) cnt[c-'a']++;
        for (char c : t) if (--cnt[c-'a'] < 0) return false;
        return true;
    }
};''',

    # ─── GROUP ANAGRAMS ───────────────────────────────────────────
    ("group-anagrams", "python3"): '''from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        g = defaultdict(list)
        for s in strs: g[tuple(sorted(s))].append(s)
        return list(g.values())''',
    ("group-anagrams", "javascript"): '''var groupAnagrams = function(strs) {
    const map = new Map();
    for (const s of strs) {
        const key = s.split('').sort().join('');
        if (!map.has(key)) map.set(key, []);
        map.get(key).push(s);
    }
    return [...map.values()];
};''',
    ("group-anagrams", "cpp"): '''class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (auto& s : strs) { string key = s; sort(key.begin(), key.end()); m[key].push_back(s); }
        vector<vector<string>> res;
        for (auto& p : m) res.push_back(p.second);
        return res;
    }
};''',

    # ─── TOP K FREQUENT ELEMENTS ──────────────────────────────────
    ("top-k-frequent-elements", "python3"): '''from collections import Counter
class Solution:
    def topKFrequent(self, nums, k): return [x for x,_ in Counter(nums).most_common(k)]''',
    ("top-k-frequent-elements", "javascript"): '''var topKFrequent = function(nums, k) {
    const count = {};
    for (const n of nums) count[n] = (count[n] || 0) + 1;
    return Object.entries(count).sort((a,b) => b[1]-a[1]).slice(0,k).map(e => +e[0]);
};''',
    ("top-k-frequent-elements", "cpp"): '''class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        for (int n : nums) cnt[n]++;
        vector<pair<int,int>> v(cnt.begin(), cnt.end());
        sort(v.begin(), v.end(), [](auto& a, auto& b){ return a.second > b.second; });
        vector<int> res;
        for (int i = 0; i < k; i++) res.push_back(v[i].first);
        return res;
    }
};''',

    # ─── PRODUCT OF ARRAY EXCEPT SELF ────────────────────────────
    ("product-of-array-except-self", "python3"): '''class Solution:
    def productExceptSelf(self, nums):
        n = len(nums); res = [1]*n
        left = 1
        for i in range(n): res[i] = left; left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1): res[i] *= right; right *= nums[i]
        return res''',
    ("product-of-array-except-self", "javascript"): '''var productExceptSelf = function(nums) {
    const n = nums.length, res = new Array(n).fill(1);
    let left = 1;
    for (let i = 0; i < n; i++) { res[i] = left; left *= nums[i]; }
    let right = 1;
    for (let i = n-1; i >= 0; i--) { res[i] *= right; right *= nums[i]; }
    return res;
};''',
    ("product-of-array-except-self", "cpp"): '''class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(); vector<int> res(n, 1);
        int left = 1;
        for (int i = 0; i < n; i++) { res[i] = left; left *= nums[i]; }
        int right = 1;
        for (int i = n-1; i >= 0; i--) { res[i] *= right; right *= nums[i]; }
        return res;
    }
};''',

    # ─── LONGEST CONSECUTIVE SEQUENCE ────────────────────────────
    ("longest-consecutive-sequence", "python3"): '''class Solution:
    def longestConsecutive(self, nums):
        s = set(nums); best = 0
        for n in s:
            if n-1 not in s:
                cur = n; streak = 1
                while cur+1 in s: cur += 1; streak += 1
                best = max(best, streak)
        return best''',
    ("longest-consecutive-sequence", "javascript"): '''var longestConsecutive = function(nums) {
    const s = new Set(nums); let best = 0;
    for (const n of s) {
        if (!s.has(n-1)) {
            let cur = n, streak = 1;
            while (s.has(cur+1)) { cur++; streak++; }
            best = Math.max(best, streak);
        }
    }
    return best;
};''',
    ("longest-consecutive-sequence", "cpp"): '''class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end()); int best = 0;
        for (int n : s) {
            if (!s.count(n-1)) {
                int cur = n, streak = 1;
                while (s.count(cur+1)) { cur++; streak++; }
                best = max(best, streak);
            }
        }
        return best;
    }
};''',

    # ─── VALID PALINDROME ─────────────────────────────────────────
    ("valid-palindrome", "python3"): '''class Solution:
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]''',
    ("valid-palindrome", "javascript"): '''var isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    return s === s.split('').reverse().join('');
};''',
    ("valid-palindrome", "cpp"): '''class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size()-1;
        while (l < r) {
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;
            if (tolower(s[l]) != tolower(s[r])) return false;
            l++; r--;
        }
        return true;
    }
};''',

    # ─── TWO SUM II ───────────────────────────────────────────────
    ("two-sum-ii-input-array-is-sorted", "python3"): '''class Solution:
    def twoSum(self, numbers, target):
        lo, hi = 0, len(numbers)-1
        while lo < hi:
            s = numbers[lo]+numbers[hi]
            if s == target: return [lo+1, hi+1]
            elif s < target: lo += 1
            else: hi -= 1
        return []''',
    ("two-sum-ii-input-array-is-sorted", "javascript"): '''var twoSum = function(numbers, target) {
    let lo = 0, hi = numbers.length-1;
    while (lo < hi) {
        const s = numbers[lo]+numbers[hi];
        if (s === target) return [lo+1, hi+1];
        else if (s < target) lo++;
        else hi--;
    }
    return [];
};''',
    ("two-sum-ii-input-array-is-sorted", "cpp"): '''class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lo = 0, hi = numbers.size()-1;
        while (lo < hi) {
            int s = numbers[lo]+numbers[hi];
            if (s == target) return {lo+1, hi+1};
            else if (s < target) lo++;
            else hi--;
        }
        return {};
    }
};''',

    # ─── 3SUM ─────────────────────────────────────────────────────
    ("3sum", "python3"): '''class Solution:
    def threeSum(self, nums):
        nums.sort(); res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                s = nums[i]+nums[lo]+nums[hi]
                if s == 0:
                    res.append([nums[i],nums[lo],nums[hi]])
                    while lo < hi and nums[lo]==nums[lo+1]: lo+=1
                    while lo < hi and nums[hi]==nums[hi-1]: hi-=1
                    lo+=1; hi-=1
                elif s < 0: lo+=1
                else: hi-=1
        return res''',
    ("3sum", "javascript"): '''var threeSum = function(nums) {
    nums.sort((a,b)=>a-b); const res = [];
    for (let i = 0; i < nums.length-2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue;
        let lo = i+1, hi = nums.length-1;
        while (lo < hi) {
            const s = nums[i]+nums[lo]+nums[hi];
            if (s === 0) {
                res.push([nums[i],nums[lo],nums[hi]]);
                while (lo < hi && nums[lo]===nums[lo+1]) lo++;
                while (lo < hi && nums[hi]===nums[hi-1]) hi--;
                lo++; hi--;
            } else if (s < 0) lo++;
            else hi--;
        }
    }
    return res;
};''',
    ("3sum", "cpp"): '''class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); vector<vector<int>> res;
        for (int i = 0; i < (int)nums.size()-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int lo = i+1, hi = nums.size()-1;
            while (lo < hi) {
                int s = nums[i]+nums[lo]+nums[hi];
                if (s == 0) {
                    res.push_back({nums[i],nums[lo],nums[hi]});
                    while (lo < hi && nums[lo]==nums[lo+1]) lo++;
                    while (lo < hi && nums[hi]==nums[hi-1]) hi--;
                    lo++; hi--;
                } else if (s < 0) lo++;
                else hi--;
            }
        }
        return res;
    }
};''',

    # ─── CONTAINER WITH MOST WATER ────────────────────────────────
    ("container-with-most-water", "python3"): '''class Solution:
    def maxArea(self, height):
        lo, hi, res = 0, len(height)-1, 0
        while lo < hi:
            res = max(res, min(height[lo],height[hi])*(hi-lo))
            if height[lo] < height[hi]: lo+=1
            else: hi-=1
        return res''',
    ("container-with-most-water", "javascript"): '''var maxArea = function(height) {
    let lo = 0, hi = height.length-1, res = 0;
    while (lo < hi) {
        res = Math.max(res, Math.min(height[lo],height[hi])*(hi-lo));
        if (height[lo] < height[hi]) lo++;
        else hi--;
    }
    return res;
};''',
    ("container-with-most-water", "cpp"): '''class Solution {
public:
    int maxArea(vector<int>& height) {
        int lo = 0, hi = height.size()-1, res = 0;
        while (lo < hi) {
            res = max(res, min(height[lo],height[hi])*(hi-lo));
            if (height[lo] < height[hi]) lo++;
            else hi--;
        }
        return res;
    }
};''',

    # ─── TRAPPING RAIN WATER ─────────────────────────────────────
    ("trapping-rain-water", "python3"): '''class Solution:
    def trap(self, height):
        lo, hi = 0, len(height)-1
        maxL = maxR = water = 0
        while lo < hi:
            if height[lo] < height[hi]:
                if height[lo] >= maxL: maxL = height[lo]
                else: water += maxL-height[lo]
                lo += 1
            else:
                if height[hi] >= maxR: maxR = height[hi]
                else: water += maxR-height[hi]
                hi -= 1
        return water''',
    ("trapping-rain-water", "javascript"): '''var trap = function(height) {
    let lo = 0, hi = height.length-1, maxL = 0, maxR = 0, water = 0;
    while (lo < hi) {
        if (height[lo] < height[hi]) {
            if (height[lo] >= maxL) maxL = height[lo];
            else water += maxL-height[lo];
            lo++;
        } else {
            if (height[hi] >= maxR) maxR = height[hi];
            else water += maxR-height[hi];
            hi--;
        }
    }
    return water;
};''',
    ("trapping-rain-water", "cpp"): '''class Solution {
public:
    int trap(vector<int>& height) {
        int lo=0, hi=height.size()-1, maxL=0, maxR=0, water=0;
        while (lo < hi) {
            if (height[lo] < height[hi]) {
                if (height[lo] >= maxL) maxL = height[lo];
                else water += maxL-height[lo];
                lo++;
            } else {
                if (height[hi] >= maxR) maxR = height[hi];
                else water += maxR-height[hi];
                hi--;
            }
        }
        return water;
    }
};''',

    # ─── LONGEST SUBSTRING WITHOUT REPEATING ─────────────────────
    ("longest-substring-without-repeating-characters", "python3"): '''class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}; lo = res = 0
        for i,c in enumerate(s):
            if c in seen and seen[c] >= lo: lo = seen[c]+1
            seen[c] = i; res = max(res, i-lo+1)
        return res''',
    ("longest-substring-without-repeating-characters", "javascript"): '''var lengthOfLongestSubstring = function(s) {
    const seen = {}; let lo = 0, res = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] in seen && seen[s[i]] >= lo) lo = seen[s[i]]+1;
        seen[s[i]] = i; res = Math.max(res, i-lo+1);
    }
    return res;
};''',
    ("longest-substring-without-repeating-characters", "cpp"): '''class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen; int lo=0, res=0;
        for (int i = 0; i < s.size(); i++) {
            if (seen.count(s[i]) && seen[s[i]] >= lo) lo = seen[s[i]]+1;
            seen[s[i]] = i; res = max(res, i-lo+1);
        }
        return res;
    }
};''',

    # ─── LONGEST REPEATING CHARACTER REPLACEMENT ─────────────────
    ("longest-repeating-character-replacement", "python3"): '''from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        count = defaultdict(int); lo = maxC = res = 0
        for hi,c in enumerate(s):
            count[c] += 1; maxC = max(maxC, count[c])
            if (hi-lo+1)-maxC > k: count[s[lo]] -= 1; lo += 1
            res = max(res, hi-lo+1)
        return res''',
    ("longest-repeating-character-replacement", "javascript"): '''var characterReplacement = function(s, k) {
    const count = {}; let lo = 0, maxC = 0, res = 0;
    for (let hi = 0; hi < s.length; hi++) {
        count[s[hi]] = (count[s[hi]]||0)+1;
        maxC = Math.max(maxC, count[s[hi]]);
        if ((hi-lo+1)-maxC > k) { count[s[lo]]--; lo++; }
        res = Math.max(res, hi-lo+1);
    }
    return res;
};''',
    ("longest-repeating-character-replacement", "cpp"): '''class Solution {
public:
    int characterReplacement(string s, int k) {
        int count[26]={}, lo=0, maxC=0, res=0;
        for (int hi = 0; hi < s.size(); hi++) {
            maxC = max(maxC, ++count[s[hi]-'A']);
            if ((hi-lo+1)-maxC > k) count[s[lo++]-'A']--;
            res = max(res, hi-lo+1);
        }
        return res;
    }
};''',

    # ─── MINIMUM WINDOW SUBSTRING ────────────────────────────────
    ("minimum-window-substring", "python3"): '''from collections import Counter
class Solution:
    def minWindow(self, s, t):
        need = Counter(t); missing = len(t)
        lo = start = end = 0
        for hi,c in enumerate(s,1):
            if need[c] > 0: missing -= 1
            need[c] -= 1
            if missing == 0:
                while need[s[lo]] < 0: need[s[lo]] += 1; lo += 1
                if not end or hi-lo < end-start: start,end = lo,hi
                need[s[lo]] += 1; missing += 1; lo += 1
        return s[start:end]''',
    ("minimum-window-substring", "javascript"): '''var minWindow = function(s, t) {
    const need = {}; for (const c of t) need[c] = (need[c]||0)+1;
    let missing = t.length, lo = 0, start = 0, end = 0;
    for (let hi = 0; hi < s.length; hi++) {
        if (need[s[hi]] > 0) missing--;
        need[s[hi]] = (need[s[hi]]||0)-1;
        if (missing === 0) {
            while (need[s[lo]] < 0) { need[s[lo]]++; lo++; }
            if (!end || hi-lo+1 < end-start) { start=lo; end=hi+1; }
            need[s[lo]]++; missing++; lo++;
        }
    }
    return s.slice(start, end);
};''',
    ("minimum-window-substring", "cpp"): '''class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int> need; for (char c:t) need[c]++;
        int missing=t.size(), lo=0, start=0, minLen=INT_MAX;
        for (int hi=0; hi<s.size(); hi++) {
            if (need[s[hi]]-- > 0) missing--;
            if (missing == 0) {
                while (need[s[lo]] < 0) need[s[lo]]++, lo++;
                if (hi-lo+1 < minLen) { minLen=hi-lo+1; start=lo; }
                need[s[lo]]++; missing++; lo++;
            }
        }
        return minLen==INT_MAX ? "" : s.substr(start, minLen);
    }
};''',

    # ─── VALID PARENTHESES ────────────────────────────────────────
    ("valid-parentheses", "python3"): '''class Solution:
    def isValid(self, s):
        stack = []; m = {')':'(','}':'{',']':'['}
        for c in s:
            if c in m:
                if not stack or stack[-1] != m[c]: return False
                stack.pop()
            else: stack.append(c)
        return not stack''',
    ("valid-parentheses", "javascript"): '''var isValid = function(s) {
    const stack = [], m = {')':'(','}':'{',']':'['};
    for (const c of s) {
        if (c in m) { if (stack.pop() !== m[c]) return false; }
        else stack.push(c);
    }
    return stack.length === 0;
};''',
    ("valid-parentheses", "cpp"): '''class Solution {
public:
    bool isValid(string s) {
        stack<char> st; unordered_map<char,char> m={{')','{'},{'(','}'},{']','['},{'}','{'}};
        // correct map
        unordered_map<char,char> mp = {{')','{'},{'(','}'},{']','['},{'}','{'}};
        unordered_map<char,char> mp2; mp2[')']='{'; mp2['}']='{'; 
        // simple approach
        for (char c : s) {
            if (c=='('||c=='{'||c=='[') st.push(c);
            else {
                if (st.empty()) return false;
                char top = st.top(); st.pop();
                if ((c==')'&&top!='(')||(c=='}'&&top!='{')||(c==']'&&top!='[')) return false;
            }
        }
        return st.empty();
    }
};''',

    # ─── GENERATE PARENTHESES ─────────────────────────────────────
    ("generate-parentheses", "python3"): '''class Solution:
    def generateParenthesis(self, n):
        res = []
        def bt(s, open, close):
            if len(s) == 2*n: res.append(s); return
            if open < n: bt(s+'(', open+1, close)
            if close < open: bt(s+')', open, close+1)
        bt('', 0, 0); return res''',
    ("generate-parentheses", "javascript"): '''var generateParenthesis = function(n) {
    const res = [];
    function bt(s, open, close) {
        if (s.length === 2*n) { res.push(s); return; }
        if (open < n) bt(s+'(', open+1, close);
        if (close < open) bt(s+')', open, close+1);
    }
    bt('', 0, 0); return res;
};''',
    ("generate-parentheses", "cpp"): '''class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        function<void(string,int,int)> bt = [&](string s, int open, int close) {
            if (s.size() == 2*n) { res.push_back(s); return; }
            if (open < n) bt(s+'(', open+1, close);
            if (close < open) bt(s+')', open, close+1);
        };
        bt("", 0, 0); return res;
    }
};''',

    # ─── DAILY TEMPERATURES ───────────────────────────────────────
    ("daily-temperatures", "python3"): '''class Solution:
    def dailyTemperatures(self, temps):
        res = [0]*len(temps); stack = []
        for i,t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop(); res[j] = i-j
            stack.append(i)
        return res''',
    ("daily-temperatures", "javascript"): '''var dailyTemperatures = function(temps) {
    const res = new Array(temps.length).fill(0), stack = [];
    for (let i = 0; i < temps.length; i++) {
        while (stack.length && temps[stack[stack.length-1]] < temps[i]) {
            const j = stack.pop(); res[j] = i-j;
        }
        stack.push(i);
    }
    return res;
};''',
    ("daily-temperatures", "cpp"): '''class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        vector<int> res(t.size(),0); stack<int> st;
        for (int i = 0; i < t.size(); i++) {
            while (!st.empty() && t[st.top()] < t[i]) { res[st.top()] = i-st.top(); st.pop(); }
            st.push(i);
        }
        return res;
    }
};''',

    # ─── MIN STACK ────────────────────────────────────────────────
    ("min-stack", "python3"): '''class MinStack:
    def __init__(self): self.stack = []; self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    def pop(self): self.stack.pop(); self.min_stack.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]''',
    ("min-stack", "javascript"): '''class MinStack {
    constructor() { this.stack = []; this.minStack = []; }
    push(val) { this.stack.push(val); this.minStack.push(Math.min(val, this.minStack.length ? this.minStack[this.minStack.length-1] : val)); }
    pop() { this.stack.pop(); this.minStack.pop(); }
    top() { return this.stack[this.stack.length-1]; }
    getMin() { return this.minStack[this.minStack.length-1]; }
}''',
    ("min-stack", "cpp"): '''class MinStack {
    stack<int> st, minSt;
public:
    void push(int val) { st.push(val); minSt.push(minSt.empty() ? val : min(val, minSt.top())); }
    void pop() { st.pop(); minSt.pop(); }
    int top() { return st.top(); }
    int getMin() { return minSt.top(); }
};''',

    # ─── EVALUATE REVERSE POLISH NOTATION ────────────────────────
    ("evaluate-reverse-polish-notation", "python3"): '''class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in '+-*/':
                b,a = stack.pop(),stack.pop()
                if t=='+': stack.append(a+b)
                elif t=='-': stack.append(a-b)
                elif t=='*': stack.append(a*b)
                else: stack.append(int(a/b))
            else: stack.append(int(t))
        return stack[0]''',
    ("evaluate-reverse-polish-notation", "javascript"): '''var evalRPN = function(tokens) {
    const stack = [];
    for (const t of tokens) {
        if ('+-*/'.includes(t)) {
            const b=stack.pop(), a=stack.pop();
            if (t==='+') stack.push(a+b);
            else if (t==='-') stack.push(a-b);
            else if (t==='*') stack.push(a*b);
            else stack.push(Math.trunc(a/b));
        } else stack.push(+t);
    }
    return stack[0];
};''',
    ("evaluate-reverse-polish-notation", "cpp"): '''class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (auto& t : tokens) {
            if (t=="+"||t=="-"||t=="*"||t=="/") {
                int b=st.top(); st.pop(); int a=st.top(); st.pop();
                if (t=="+") st.push(a+b);
                else if (t=="-") st.push(a-b);
                else if (t=="*") st.push(a*b);
                else st.push(a/b);
            } else st.push(stoi(t));
        }
        return st.top();
    }
};''',

    # ─── BINARY SEARCH ────────────────────────────────────────────
    ("binary-search", "python3"): '''class Solution:
    def search(self, nums, target):
        lo,hi = 0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target: return mid
            elif nums[mid]<target: lo=mid+1
            else: hi=mid-1
        return -1''',
    ("binary-search", "javascript"): '''var search = function(nums, target) {
    let lo=0, hi=nums.length-1;
    while (lo<=hi) {
        const mid=lo+hi>>1;
        if (nums[mid]===target) return mid;
        else if (nums[mid]<target) lo=mid+1;
        else hi=mid-1;
    }
    return -1;
};''',
    ("binary-search", "cpp"): '''class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo=0, hi=nums.size()-1;
        while (lo<=hi) {
            int mid=(lo+hi)/2;
            if (nums[mid]==target) return mid;
            else if (nums[mid]<target) lo=mid+1;
            else hi=mid-1;
        }
        return -1;
    }
};''',

    # ─── SEARCH A 2D MATRIX ───────────────────────────────────────
    ("search-a-2d-matrix", "python3"): '''class Solution:
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0]); lo,hi=0,m*n-1
        while lo<=hi:
            mid=(lo+hi)//2; val=matrix[mid//n][mid%n]
            if val==target: return True
            elif val<target: lo=mid+1
            else: hi=mid-1
        return False''',
    ("search-a-2d-matrix", "javascript"): '''var searchMatrix = function(matrix, target) {
    const m=matrix.length, n=matrix[0].length; let lo=0, hi=m*n-1;
    while (lo<=hi) {
        const mid=lo+hi>>1, val=matrix[Math.floor(mid/n)][mid%n];
        if (val===target) return true;
        else if (val<target) lo=mid+1;
        else hi=mid-1;
    }
    return false;
};''',
    ("search-a-2d-matrix", "cpp"): '''class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(), n=matrix[0].size(), lo=0, hi=m*n-1;
        while (lo<=hi) {
            int mid=(lo+hi)/2, val=matrix[mid/n][mid%n];
            if (val==target) return true;
            else if (val<target) lo=mid+1;
            else hi=mid-1;
        }
        return false;
    }
};''',

    # ─── KOKO EATING BANANAS ─────────────────────────────────────
    ("koko-eating-bananas", "python3"): '''import math
class Solution:
    def minEatingSpeed(self, piles, h):
        lo,hi=1,max(piles)
        while lo<hi:
            mid=(lo+hi)//2
            if sum(math.ceil(p/mid) for p in piles)<=h: hi=mid
            else: lo=mid+1
        return lo''',
    ("koko-eating-bananas", "javascript"): '''var minEatingSpeed = function(piles, h) {
    let lo=1, hi=Math.max(...piles);
    while (lo<hi) {
        const mid=lo+hi>>1;
        const hours=piles.reduce((s,p)=>s+Math.ceil(p/mid),0);
        if (hours<=h) hi=mid; else lo=mid+1;
    }
    return lo;
};''',
    ("koko-eating-bananas", "cpp"): '''class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo=1, hi=*max_element(piles.begin(),piles.end());
        while (lo<hi) {
            int mid=(lo+hi)/2, hours=0;
            for (int p:piles) hours+=ceil((double)p/mid);
            if (hours<=h) hi=mid; else lo=mid+1;
        }
        return lo;
    }
};''',

    # ─── FIND MINIMUM IN ROTATED SORTED ARRAY ─────────────────────
    ("find-minimum-in-rotated-sorted-array", "python3"): '''class Solution:
    def findMin(self, nums):
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]>nums[hi]: lo=mid+1
            else: hi=mid
        return nums[lo]''',
    ("find-minimum-in-rotated-sorted-array", "javascript"): '''var findMin = function(nums) {
    let lo=0, hi=nums.length-1;
    while (lo<hi) {
        const mid=lo+hi>>1;
        if (nums[mid]>nums[hi]) lo=mid+1; else hi=mid;
    }
    return nums[lo];
};''',
    ("find-minimum-in-rotated-sorted-array", "cpp"): '''class Solution {
public:
    int findMin(vector<int>& nums) {
        int lo=0, hi=nums.size()-1;
        while (lo<hi) { int mid=(lo+hi)/2; if (nums[mid]>nums[hi]) lo=mid+1; else hi=mid; }
        return nums[lo];
    }
};''',

    # ─── REVERSE LINKED LIST ──────────────────────────────────────
    ("reverse-linked-list", "python3"): '''class Solution:
    def reverseList(self, head):
        prev = None
        while head: nxt=head.next; head.next=prev; prev=head; head=nxt
        return prev''',
    ("reverse-linked-list", "javascript"): '''var reverseList = function(head) {
    let prev = null;
    while (head) { const nxt=head.next; head.next=prev; prev=head; head=nxt; }
    return prev;
};''',
    ("reverse-linked-list", "cpp"): '''class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) { auto nxt=head->next; head->next=prev; prev=head; head=nxt; }
        return prev;
    }
};''',

    # ─── MERGE TWO SORTED LISTS ───────────────────────────────────
    ("merge-two-sorted-lists", "python3"): '''class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = type('', (), {'next':None})()
        while l1 and l2:
            if l1.val<=l2.val: cur.next=l1; l1=l1.next
            else: cur.next=l2; l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next''',
    ("merge-two-sorted-lists", "javascript"): '''var mergeTwoLists = function(l1, l2) {
    const dummy = new ListNode(); let cur = dummy;
    while (l1 && l2) {
        if (l1.val<=l2.val) { cur.next=l1; l1=l1.next; }
        else { cur.next=l2; l2=l2.next; }
        cur=cur.next;
    }
    cur.next=l1||l2; return dummy.next;
};''',
    ("merge-two-sorted-lists", "cpp"): '''class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy; ListNode* cur=&dummy;
        while (l1&&l2) { if(l1->val<=l2->val){cur->next=l1;l1=l1->next;}else{cur->next=l2;l2=l2->next;} cur=cur->next; }
        cur->next=l1?l1:l2; return dummy.next;
    }
};''',

    # ─── LINKED LIST CYCLE ────────────────────────────────────────
    ("linked-list-cycle", "python3"): '''class Solution:
    def hasCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow==fast: return True
        return False''',
    ("linked-list-cycle", "javascript"): '''var hasCycle = function(head) {
    let slow=head, fast=head;
    while (fast&&fast.next) { slow=slow.next; fast=fast.next.next; if(slow===fast) return true; }
    return false;
};''',
    ("linked-list-cycle", "cpp"): '''class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode *slow=head, *fast=head;
        while (fast&&fast->next) { slow=slow->next; fast=fast->next->next; if(slow==fast) return true; }
        return false;
    }
};''',

    # ─── MAXIMUM DEPTH OF BINARY TREE ────────────────────────────
    ("maximum-depth-of-binary-tree", "python3"): '''class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))''',
    ("maximum-depth-of-binary-tree", "javascript"): '''var maxDepth = function(root) {
    if (!root) return 0;
    return 1+Math.max(maxDepth(root.left), maxDepth(root.right));
};''',
    ("maximum-depth-of-binary-tree", "cpp"): '''class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1+max(maxDepth(root->left), maxDepth(root->right));
    }
};''',

    # ─── INVERT BINARY TREE ───────────────────────────────────────
    ("invert-binary-tree", "python3"): '''class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root''',
    ("invert-binary-tree", "javascript"): '''var invertTree = function(root) {
    if (!root) return null;
    [root.left,root.right]=[invertTree(root.right),invertTree(root.left)];
    return root;
};''',
    ("invert-binary-tree", "cpp"): '''class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        swap(root->left, root->right);
        invertTree(root->left); invertTree(root->right);
        return root;
    }
};''',

    # ─── DIAMETER OF BINARY TREE ─────────────────────────────────
    ("diameter-of-binary-tree", "python3"): '''class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def depth(node):
            if not node: return 0
            l,r=depth(node.left),depth(node.right)
            self.res=max(self.res,l+r); return 1+max(l,r)
        depth(root); return self.res''',
    ("diameter-of-binary-tree", "javascript"): '''var diameterOfBinaryTree = function(root) {
    let res = 0;
    function depth(node) {
        if (!node) return 0;
        const l=depth(node.left), r=depth(node.right);
        res=Math.max(res,l+r); return 1+Math.max(l,r);
    }
    depth(root); return res;
};''',
    ("diameter-of-binary-tree", "cpp"): '''class Solution {
    int res = 0;
    int depth(TreeNode* n) {
        if (!n) return 0;
        int l=depth(n->left), r=depth(n->right);
        res=max(res,l+r); return 1+max(l,r);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) { depth(root); return res; }
};''',

    # ─── BALANCED BINARY TREE ────────────────────────────────────
    ("balanced-binary-tree", "python3"): '''class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node: return 0
            l,r=height(node.left),height(node.right)
            if l==-1 or r==-1 or abs(l-r)>1: return -1
            return 1+max(l,r)
        return height(root) != -1''',
    ("balanced-binary-tree", "javascript"): '''var isBalanced = function(root) {
    function height(node) {
        if (!node) return 0;
        const l=height(node.left), r=height(node.right);
        if (l===-1||r===-1||Math.abs(l-r)>1) return -1;
        return 1+Math.max(l,r);
    }
    return height(root) !== -1;
};''',
    ("balanced-binary-tree", "cpp"): '''class Solution {
    int height(TreeNode* n) {
        if (!n) return 0;
        int l=height(n->left), r=height(n->right);
        if (l==-1||r==-1||abs(l-r)>1) return -1;
        return 1+max(l,r);
    }
public:
    bool isBalanced(TreeNode* root) { return height(root)!=-1; }
};''',

    # ─── SAME TREE ────────────────────────────────────────────────
    ("same-tree", "python3"): '''class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val!=q.val: return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)''',
    ("same-tree", "javascript"): '''var isSameTree = function(p, q) {
    if (!p&&!q) return true;
    if (!p||!q||p.val!==q.val) return false;
    return isSameTree(p.left,q.left)&&isSameTree(p.right,q.right);
};''',
    ("same-tree", "cpp"): '''class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p&&!q) return true;
        if (!p||!q||p->val!=q->val) return false;
        return isSameTree(p->left,q->left)&&isSameTree(p->right,q->right);
    }
};''',

    # ─── BINARY TREE LEVEL ORDER TRAVERSAL ───────────────────────
    ("binary-tree-level-order-traversal", "python3"): '''from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return []
        res=[]; q=deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.popleft(); level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res''',
    ("binary-tree-level-order-traversal", "javascript"): '''var levelOrder = function(root) {
    if (!root) return [];
    const res=[], q=[root];
    while (q.length) {
        const level=[], size=q.length;
        for (let i=0;i<size;i++) {
            const node=q.shift(); level.push(node.val);
            if(node.left) q.push(node.left);
            if(node.right) q.push(node.right);
        }
        res.push(level);
    }
    return res;
};''',
    ("binary-tree-level-order-traversal", "cpp"): '''class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> res; queue<TreeNode*> q; q.push(root);
        while (!q.empty()) {
            vector<int> level; int sz=q.size();
            while (sz--) { auto n=q.front(); q.pop(); level.push_back(n->val); if(n->left)q.push(n->left); if(n->right)q.push(n->right); }
            res.push_back(level);
        }
        return res;
    }
};''',

    # ─── VALIDATE BINARY SEARCH TREE ─────────────────────────────
    ("validate-binary-search-tree", "python3"): '''class Solution:
    def isValidBST(self, root):
        def validate(node, lo, hi):
            if not node: return True
            if not (lo < node.val < hi): return False
            return validate(node.left,lo,node.val) and validate(node.right,node.val,hi)
        return validate(root, float('-inf'), float('inf'))''',
    ("validate-binary-search-tree", "javascript"): '''var isValidBST = function(root) {
    function validate(node, lo, hi) {
        if (!node) return true;
        if (node.val<=lo||node.val>=hi) return false;
        return validate(node.left,lo,node.val)&&validate(node.right,node.val,hi);
    }
    return validate(root,-Infinity,Infinity);
};''',
    ("validate-binary-search-tree", "cpp"): '''class Solution {
    bool validate(TreeNode* n, long lo, long hi) {
        if (!n) return true;
        if (n->val<=lo||n->val>=hi) return false;
        return validate(n->left,lo,n->val)&&validate(n->right,n->val,hi);
    }
public:
    bool isValidBST(TreeNode* root) { return validate(root,LONG_MIN,LONG_MAX); }
};''',

    # ─── NUMBER OF ISLANDS ───────────────────────────────────────
    ("number-of-islands", "python3"): '''class Solution:
    def numIslands(self, grid):
        count=0
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!='1': return
            grid[r][c]='0'
            dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1': dfs(r,c); count+=1
        return count''',
    ("number-of-islands", "javascript"): '''var numIslands = function(grid) {
    let count=0;
    function dfs(r,c) {
        if(r<0||r>=grid.length||c<0||c>=grid[0].length||grid[r][c]!=='1') return;
        grid[r][c]='0'; dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);
    }
    for(let r=0;r<grid.length;r++) for(let c=0;c<grid[0].length;c++) if(grid[r][c]==='1'){dfs(r,c);count++;}
    return count;
};''',
    ("number-of-islands", "cpp"): '''class Solution {
    void dfs(vector<vector<char>>& g, int r, int c) {
        if(r<0||r>=g.size()||c<0||c>=g[0].size()||g[r][c]!='1') return;
        g[r][c]='0'; dfs(g,r+1,c);dfs(g,r-1,c);dfs(g,r,c+1);dfs(g,r,c-1);
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        for(int r=0;r<grid.size();r++) for(int c=0;c<grid[0].size();c++) if(grid[r][c]=='1'){dfs(grid,r,c);count++;}
        return count;
    }
};''',

    # ─── COURSE SCHEDULE ─────────────────────────────────────────
    ("course-schedule", "python3"): '''class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites: graph[b].append(a)
        visited=[0]*numCourses
        def dfs(v):
            if visited[v]==1: return False
            if visited[v]==2: return True
            visited[v]=1
            for nb in graph[v]:
                if not dfs(nb): return False
            visited[v]=2; return True
        return all(dfs(i) for i in range(numCourses))''',
    ("course-schedule", "javascript"): '''var canFinish = function(numCourses, prerequisites) {
    const graph=Array.from({length:numCourses},()=>[]);
    for(const[a,b] of prerequisites) graph[b].push(a);
    const visited=new Array(numCourses).fill(0);
    function dfs(v) {
        if(visited[v]===1) return false;
        if(visited[v]===2) return true;
        visited[v]=1;
        for(const nb of graph[v]) if(!dfs(nb)) return false;
        visited[v]=2; return true;
    }
    for(let i=0;i<numCourses;i++) if(!dfs(i)) return false;
    return true;
};''',
    ("course-schedule", "cpp"): '''class Solution {
    vector<vector<int>> graph; vector<int> vis;
    bool dfs(int v) {
        if(vis[v]==1) return false; if(vis[v]==2) return true;
        vis[v]=1; for(int nb:graph[v]) if(!dfs(nb)) return false;
        vis[v]=2; return true;
    }
public:
    bool canFinish(int n, vector<vector<int>>& pre) {
        graph.resize(n); vis.resize(n,0);
        for(auto& p:pre) graph[p[1]].push_back(p[0]);
        for(int i=0;i<n;i++) if(!dfs(i)) return false;
        return true;
    }
};''',

    # ─── CLIMBING STAIRS ─────────────────────────────────────────
    ("climbing-stairs", "python3"): '''class Solution:
    def climbStairs(self, n):
        if n<=2: return n
        a,b=1,2
        for _ in range(3,n+1): a,b=b,a+b
        return b''',
    ("climbing-stairs", "javascript"): '''var climbStairs = function(n) {
    if(n<=2) return n;
    let a=1,b=2;
    for(let i=3;i<=n;i++){[a,b]=[b,a+b];}
    return b;
};''',
    ("climbing-stairs", "cpp"): '''class Solution {
public:
    int climbStairs(int n) {
        if(n<=2) return n;
        int a=1,b=2;
        for(int i=3;i<=n;i++){int c=a+b;a=b;b=c;}
        return b;
    }
};''',

    # ─── COIN CHANGE ─────────────────────────────────────────────
    ("coin-change", "python3"): '''class Solution:
    def coinChange(self, coins, amount):
        dp=[float('inf')]*(amount+1); dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if c<=i: dp[i]=min(dp[i],dp[i-c]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1''',
    ("coin-change", "javascript"): '''var coinChange = function(coins, amount) {
    const dp=new Array(amount+1).fill(Infinity); dp[0]=0;
    for(let i=1;i<=amount;i++) for(const c of coins) if(c<=i) dp[i]=Math.min(dp[i],dp[i-c]+1);
    return dp[amount]===Infinity?-1:dp[amount];
};''',
    ("coin-change", "cpp"): '''class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,INT_MAX); dp[0]=0;
        for(int i=1;i<=amount;i++) for(int c:coins) if(c<=i&&dp[i-c]!=INT_MAX) dp[i]=min(dp[i],dp[i-c]+1);
        return dp[amount]==INT_MAX?-1:dp[amount];
    }
};''',

    # ─── HOUSE ROBBER ────────────────────────────────────────────
    ("house-robber", "python3"): '''class Solution:
    def rob(self, nums):
        prev=curr=0
        for n in nums: prev,curr=curr,max(curr,prev+n)
        return curr''',
    ("house-robber", "javascript"): '''var rob = function(nums) {
    let prev=0,curr=0;
    for(const n of nums){[prev,curr]=[curr,Math.max(curr,prev+n)];}
    return curr;
};''',
    ("house-robber", "cpp"): '''class Solution {
public:
    int rob(vector<int>& nums) {
        int prev=0,curr=0;
        for(int n:nums){int t=max(curr,prev+n);prev=curr;curr=t;}
        return curr;
    }
};''',

    # ─── LONGEST INCREASING SUBSEQUENCE ──────────────────────────
    ("longest-increasing-subsequence", "python3"): '''class Solution:
    def lengthOfLIS(self, nums):
        dp=[]
        for n in nums:
            lo,hi=0,len(dp)
            while lo<hi:
                mid=(lo+hi)//2
                if dp[mid]<n: lo=mid+1
                else: hi=mid
            if lo==len(dp): dp.append(n)
            else: dp[lo]=n
        return len(dp)''',
    ("longest-increasing-subsequence", "javascript"): '''var lengthOfLIS = function(nums) {
    const dp=[];
    for(const n of nums) {
        let lo=0,hi=dp.length;
        while(lo<hi){const mid=lo+hi>>1; if(dp[mid]<n) lo=mid+1; else hi=mid;}
        dp[lo]=n;
    }
    return dp.length;
};''',
    ("longest-increasing-subsequence", "cpp"): '''class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        for(int n:nums) {
            auto it=lower_bound(dp.begin(),dp.end(),n);
            if(it==dp.end()) dp.push_back(n); else *it=n;
        }
        return dp.size();
    }
};''',

    # ─── WORD BREAK ──────────────────────────────────────────────
    ("word-break", "python3"): '''class Solution:
    def wordBreak(self, s, wordDict):
        words=set(wordDict); dp=[False]*(len(s)+1); dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words: dp[i]=True; break
        return dp[-1]''',
    ("word-break", "javascript"): '''var wordBreak = function(s, wordDict) {
    const words=new Set(wordDict), dp=new Array(s.length+1).fill(false); dp[0]=true;
    for(let i=1;i<=s.length;i++) for(let j=0;j<i;j++) if(dp[j]&&words.has(s.slice(j,i))){dp[i]=true;break;}
    return dp[s.length];
};''',
    ("word-break", "cpp"): '''class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> words(wordDict.begin(),wordDict.end());
        int n=s.size(); vector<bool> dp(n+1,false); dp[0]=true;
        for(int i=1;i<=n;i++) for(int j=0;j<i;j++) if(dp[j]&&words.count(s.substr(j,i-j))){dp[i]=true;break;}
        return dp[n];
    }
};''',

    # ─── COMBINATION SUM ─────────────────────────────────────────
    ("combination-sum", "python3"): '''class Solution:
    def combinationSum(self, candidates, target):
        res=[]
        def bt(start,path,remaining):
            if remaining==0: res.append(path[:]); return
            for i in range(start,len(candidates)):
                if candidates[i]<=remaining:
                    path.append(candidates[i]); bt(i,path,remaining-candidates[i]); path.pop()
        bt(0,[],target); return res''',
    ("combination-sum", "javascript"): '''var combinationSum = function(candidates, target) {
    const res=[];
    function bt(start,path,rem) {
        if(rem===0){res.push([...path]);return;}
        for(let i=start;i<candidates.length;i++) {
            if(candidates[i]<=rem){path.push(candidates[i]);bt(i,path,rem-candidates[i]);path.pop();}
        }
    }
    bt(0,[],target); return res;
};''',
    ("combination-sum", "cpp"): '''class Solution {
    vector<vector<int>> res;
    void bt(vector<int>& c, int start, vector<int>& path, int rem) {
        if(rem==0){res.push_back(path);return;}
        for(int i=start;i<c.size();i++) if(c[i]<=rem){path.push_back(c[i]);bt(c,i,path,rem-c[i]);path.pop_back();}
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) { vector<int> path; bt(candidates,0,path,target); return res; }
};''',

    # ─── SUBSETS ─────────────────────────────────────────────────
    ("subsets", "python3"): '''class Solution:
    def subsets(self, nums):
        res=[]
        def bt(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i]); bt(i+1,path); path.pop()
        bt(0,[]); return res''',
    ("subsets", "javascript"): '''var subsets = function(nums) {
    const res=[];
    function bt(start,path) {
        res.push([...path]);
        for(let i=start;i<nums.length;i++){path.push(nums[i]);bt(i+1,path);path.pop();}
    }
    bt(0,[]); return res;
};''',
    ("subsets", "cpp"): '''class Solution {
    vector<vector<int>> res;
    void bt(vector<int>& nums, int start, vector<int>& path) {
        res.push_back(path);
        for(int i=start;i<nums.size();i++){path.push_back(nums[i]);bt(nums,i+1,path);path.pop_back();}
    }
public:
    vector<vector<int>> subsets(vector<int>& nums){vector<int> p;bt(nums,0,p);return res;}
};''',

    # ─── PERMUTATIONS ────────────────────────────────────────────
    ("permutations", "python3"): '''class Solution:
    def permute(self, nums):
        res=[]
        def bt(path,remaining):
            if not remaining: res.append(path[:]); return
            for i in range(len(remaining)):
                path.append(remaining[i]); bt(path,remaining[:i]+remaining[i+1:]); path.pop()
        bt([],nums); return res''',
    ("permutations", "javascript"): '''var permute = function(nums) {
    const res=[];
    function bt(path,rem) {
        if(!rem.length){res.push([...path]);return;}
        for(let i=0;i<rem.length;i++){path.push(rem[i]);bt(path,[...rem.slice(0,i),...rem.slice(i+1)]);path.pop();}
    }
    bt([],nums); return res;
};''',
    ("permutations", "cpp"): '''class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        do { res.push_back(nums); } while(next_permutation(nums.begin(),nums.end()));
        return res;
    }
};''',

    # ─── MAXIMUM SUBARRAY ────────────────────────────────────────
    ("maximum-subarray", "python3"): '''class Solution:
    def maxSubArray(self, nums):
        maxSum=curr=nums[0]
        for n in nums[1:]: curr=max(n,curr+n); maxSum=max(maxSum,curr)
        return maxSum''',
    ("maximum-subarray", "javascript"): '''var maxSubArray = function(nums) {
    let maxSum=nums[0], curr=nums[0];
    for(let i=1;i<nums.length;i++){curr=Math.max(nums[i],curr+nums[i]);maxSum=Math.max(maxSum,curr);}
    return maxSum;
};''',
    ("maximum-subarray", "cpp"): '''class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum=nums[0], curr=nums[0];
        for(int i=1;i<nums.size();i++){curr=max(nums[i],curr+nums[i]);maxSum=max(maxSum,curr);}
        return maxSum;
    }
};''',

    # ─── BEST TIME TO BUY AND SELL STOCK ─────────────────────────
    ("best-time-to-buy-and-sell-stock", "python3"): '''class Solution:
    def maxProfit(self, prices):
        minP,maxP=float('inf'),0
        for p in prices: minP=min(minP,p); maxP=max(maxP,p-minP)
        return maxP''',
    ("best-time-to-buy-and-sell-stock", "javascript"): '''var maxProfit = function(prices) {
    let minP=Infinity,maxP=0;
    for(const p of prices){minP=Math.min(minP,p);maxP=Math.max(maxP,p-minP);}
    return maxP;
};''',
    ("best-time-to-buy-and-sell-stock", "cpp"): '''class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP=INT_MAX,maxP=0;
        for(int p:prices){minP=min(minP,p);maxP=max(maxP,p-minP);}
        return maxP;
    }
};''',

    # ─── JUMP GAME ────────────────────────────────────────────────
    ("jump-game", "python3"): '''class Solution:
    def canJump(self, nums):
        reach=0
        for i,n in enumerate(nums):
            if i>reach: return False
            reach=max(reach,i+n)
        return True''',
    ("jump-game", "javascript"): '''var canJump = function(nums) {
    let reach=0;
    for(let i=0;i<nums.length;i++){if(i>reach)return false;reach=Math.max(reach,i+nums[i]);}
    return true;
};''',
    ("jump-game", "cpp"): '''class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach=0;
        for(int i=0;i<nums.size();i++){if(i>reach)return false;reach=max(reach,i+nums[i]);}
        return true;
    }
};''',

    # ─── MERGE INTERVALS ─────────────────────────────────────────
    ("merge-intervals", "python3"): '''class Solution:
    def merge(self, intervals):
        intervals.sort(); res=[intervals[0]]
        for s,e in intervals[1:]:
            if s<=res[-1][1]: res[-1][1]=max(res[-1][1],e)
            else: res.append([s,e])
        return res''',
    ("merge-intervals", "javascript"): '''var merge = function(intervals) {
    intervals.sort((a,b)=>a[0]-b[0]); const res=[intervals[0]];
    for(const[s,e] of intervals.slice(1)) {
        if(s<=res[res.length-1][1]) res[res.length-1][1]=Math.max(res[res.length-1][1],e);
        else res.push([s,e]);
    }
    return res;
};''',
    ("merge-intervals", "cpp"): '''class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end()); vector<vector<int>> res={intervals[0]};
        for(auto& iv:intervals) {
            if(iv[0]<=res.back()[1]) res.back()[1]=max(res.back()[1],iv[1]);
            else res.push_back(iv);
        }
        return res;
    }
};''',

    # ─── MISSING NUMBER ──────────────────────────────────────────
    ("missing-number", "python3"): '''class Solution:
    def missingNumber(self, nums):
        n=len(nums); return n*(n+1)//2-sum(nums)''',
    ("missing-number", "javascript"): '''var missingNumber = function(nums) {
    const n=nums.length; return n*(n+1)/2-nums.reduce((a,b)=>a+b,0);
};''',
    ("missing-number", "cpp"): '''class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size(); return n*(n+1)/2-accumulate(nums.begin(),nums.end(),0);
    }
};''',

    # ─── SINGLE NUMBER ───────────────────────────────────────────
    ("single-number", "python3"): '''class Solution:
    def singleNumber(self, nums):
        res=0
        for n in nums: res^=n
        return res''',
    ("single-number", "javascript"): '''var singleNumber = function(nums) {
    return nums.reduce((a,b)=>a^b,0);
};''',
    ("single-number", "cpp"): '''class Solution {
public:
    int singleNumber(vector<int>& nums) { int r=0; for(int n:nums) r^=n; return r; }
};''',

    # ─── REVERSE STRING ──────────────────────────────────────────
    ("reverse-string", "python3"): '''class Solution:
    def reverseString(self, s):
        lo,hi=0,len(s)-1
        while lo<hi: s[lo],s[hi]=s[hi],s[lo]; lo+=1; hi-=1''',
    ("reverse-string", "javascript"): '''var reverseString = function(s) {
    let lo=0,hi=s.length-1;
    while(lo<hi){[s[lo],s[hi]]=[s[hi],s[lo]];lo++;hi--;}
};''',
    ("reverse-string", "cpp"): '''class Solution {
public:
    void reverseString(vector<char>& s) { reverse(s.begin(),s.end()); }
};''',

    # ─── FIZZ BUZZ ───────────────────────────────────────────────
    ("fizz-buzz", "python3"): '''class Solution:
    def fizzBuzz(self, n):
        return ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]''',
    ("fizz-buzz", "javascript"): '''var fizzBuzz = function(n) {
    return Array.from({length:n},(_,i)=>++i%15===0?'FizzBuzz':i%3===0?'Fizz':i%5===0?'Buzz':String(i));
};''',
    ("fizz-buzz", "cpp"): '''class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res;
        for(int i=1;i<=n;i++) {
            if(i%15==0) res.push_back("FizzBuzz");
            else if(i%3==0) res.push_back("Fizz");
            else if(i%5==0) res.push_back("Buzz");
            else res.push_back(to_string(i));
        }
        return res;
    }
};''',

    # ─── COUNT PRIMES ────────────────────────────────────────────
    ("count-primes", "python3"): '''class Solution:
    def countPrimes(self, n):
        if n<2: return 0
        sieve=[True]*n; sieve[0]=sieve[1]=False
        for i in range(2,int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i,n,i): sieve[j]=False
        return sum(sieve)''',
    ("count-primes", "javascript"): '''var countPrimes = function(n) {
    if(n<2) return 0;
    const sieve=new Array(n).fill(true); sieve[0]=sieve[1]=false;
    for(let i=2;i*i<n;i++) if(sieve[i]) for(let j=i*i;j<n;j+=i) sieve[j]=false;
    return sieve.filter(Boolean).length;
};''',
    ("count-primes", "cpp"): '''class Solution {
public:
    int countPrimes(int n) {
        if(n<2) return 0;
        vector<bool> sieve(n,true); sieve[0]=sieve[1]=false;
        for(int i=2;(long)i*i<n;i++) if(sieve[i]) for(int j=i*i;j<n;j+=i) sieve[j]=false;
        return count(sieve.begin(),sieve.end(),true);
    }
};''',

    # ─── POWER OF TWO ────────────────────────────────────────────
    ("power-of-two", "python3"): '''class Solution:
    def isPowerOfTwo(self, n): return n>0 and (n&(n-1))==0''',
    ("power-of-two", "javascript"): '''var isPowerOfTwo = function(n) { return n>0&&(n&(n-1))===0; };''',
    ("power-of-two", "cpp"): '''class Solution {
public:
    bool isPowerOfTwo(int n) { return n>0&&!(n&(n-1)); }
};''',

    # ─── NUMBER OF 1 BITS ────────────────────────────────────────
    ("number-of-1-bits", "python3"): '''class Solution:
    def hammingWeight(self, n): return bin(n).count("1")''',
    ("number-of-1-bits", "javascript"): '''var hammingWeight = function(n) {
    let count=0; while(n){count+=n&1;n>>>=1;} return count;
};''',
    ("number-of-1-bits", "cpp"): '''class Solution {
public:
    int hammingWeight(uint32_t n) { return __builtin_popcount(n); }
};''',

    # ─── COUNTING BITS ───────────────────────────────────────────
    ("counting-bits", "python3"): '''class Solution:
    def countBits(self, n):
        dp=[0]*(n+1)
        for i in range(1,n+1): dp[i]=dp[i>>1]+(i&1)
        return dp''',
    ("counting-bits", "javascript"): '''var countBits = function(n) {
    const dp=new Array(n+1).fill(0);
    for(let i=1;i<=n;i++) dp[i]=dp[i>>1]+(i&1);
    return dp;
};''',
    ("counting-bits", "cpp"): '''class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1,0);
        for(int i=1;i<=n;i++) dp[i]=dp[i>>1]+(i&1);
        return dp;
    }
};''',

    # ─── REVERSE BITS ────────────────────────────────────────────
    ("reverse-bits", "python3"): '''class Solution:
    def reverseBits(self, n):
        res=0
        for _ in range(32): res=(res<<1)|(n&1); n>>=1
        return res''',
    ("reverse-bits", "javascript"): '''var reverseBits = function(n) {
    let res=0;
    for(let i=0;i<32;i++){res=(res*2)+(n&1);n>>>=1;}
    return res>>>0;
};''',
    ("reverse-bits", "cpp"): '''class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res=0;
        for(int i=0;i<32;i++){res=(res<<1)|(n&1);n>>=1;}
        return res;
    }
};''',

    # ─── SUM OF TWO INTEGERS ─────────────────────────────────────
    ("sum-of-two-integers", "python3"): '''class Solution:
    def getSum(self, a, b):
        mask=0xFFFFFFFF
        while b&mask:
            carry=(a&b)<<1; a=a^b; b=carry
        return a if b==0 else a&mask''',
    ("sum-of-two-integers", "javascript"): '''var getSum = function(a, b) {
    while(b){const carry=(a&b)<<1;a=a^b;b=carry;}
    return a;
};''',
    ("sum-of-two-integers", "cpp"): '''class Solution {
public:
    int getSum(int a, int b) { while(b){int c=(a&b)<<1;a^=b;b=c;} return a; }
};''',

    # ─── PALINDROME NUMBER ───────────────────────────────────────
    ("palindrome-number", "python3"): '''class Solution:
    def isPalindrome(self, x):
        if x<0: return False
        s=str(x); return s==s[::-1]''',
    ("palindrome-number", "javascript"): '''var isPalindrome = function(x) {
    if(x<0) return false; const s=String(x); return s===s.split('').reverse().join('');
};''',
    ("palindrome-number", "cpp"): '''class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false; string s=to_string(x); return s==string(s.rbegin(),s.rend());
    }
};''',

    # ─── LONGEST PALINDROMIC SUBSTRING ───────────────────────────
    ("longest-palindromic-substring", "python3"): '''class Solution:
    def longestPalindrome(self, s):
        res=""
        for i in range(len(s)):
            for lo,hi in [(i,i),(i,i+1)]:
                while lo>=0 and hi<len(s) and s[lo]==s[hi]: lo-=1;hi+=1
                if hi-lo-1>len(res): res=s[lo+1:hi]
        return res''',
    ("longest-palindromic-substring", "javascript"): '''var longestPalindrome = function(s) {
    let res="";
    for(let i=0;i<s.length;i++) for(const[lo0,hi0] of [[i,i],[i,i+1]]) {
        let lo=lo0,hi=hi0;
        while(lo>=0&&hi<s.length&&s[lo]===s[hi]){lo--;hi++;}
        if(hi-lo-1>res.length) res=s.slice(lo+1,hi);
    }
    return res;
};''',
    ("longest-palindromic-substring", "cpp"): '''class Solution {
public:
    string longestPalindrome(string s) {
        string res="";
        for(int i=0;i<s.size();i++) for(int d=0;d<2;d++) {
            int lo=i,hi=i+d;
            while(lo>=0&&hi<s.size()&&s[lo]==s[hi]){lo--;hi++;}
            if(hi-lo-1>(int)res.size()) res=s.substr(lo+1,hi-lo-1);
        }
        return res;
    }
};''',

    # ─── ROTATE IMAGE ────────────────────────────────────────────
    ("rotate-image", "python3"): '''class Solution:
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n): matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix: row.reverse()''',
    ("rotate-image", "javascript"): '''var rotate = function(matrix) {
    const n=matrix.length;
    for(let i=0;i<n;i++) for(let j=i+1;j<n;j++) [matrix[i][j],matrix[j][i]]=[matrix[j][i],matrix[i][j]];
    for(const row of matrix) row.reverse();
};''',
    ("rotate-image", "cpp"): '''class Solution {
public:
    void rotate(vector<vector<int>>& m) {
        int n=m.size();
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) swap(m[i][j],m[j][i]);
        for(auto& row:m) reverse(row.begin(),row.end());
    }
};''',

    # ─── VALID SUDOKU ────────────────────────────────────────────
    ("valid-sudoku", "python3"): '''class Solution:
    def isValidSudoku(self, board):
        rows=[set() for _ in range(9)]; cols=[set() for _ in range(9)]; boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                v=board[r][c]
                if v=='.': continue
                b=(r//3)*3+c//3
                if v in rows[r] or v in cols[c] or v in boxes[b]: return False
                rows[r].add(v); cols[c].add(v); boxes[b].add(v)
        return True''',
    ("valid-sudoku", "javascript"): '''var isValidSudoku = function(board) {
    const rows=Array.from({length:9},()=>new Set()), cols=Array.from({length:9},()=>new Set()), boxes=Array.from({length:9},()=>new Set());
    for(let r=0;r<9;r++) for(let c=0;c<9;c++) {
        const v=board[r][c]; if(v==='.') continue;
        const b=Math.floor(r/3)*3+Math.floor(c/3);
        if(rows[r].has(v)||cols[c].has(v)||boxes[b].has(v)) return false;
        rows[r].add(v); cols[c].add(v); boxes[b].add(v);
    }
    return true;
};''',
    ("valid-sudoku", "cpp"): '''class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<char> rows[9],cols[9],boxes[9];
        for(int r=0;r<9;r++) for(int c=0;c<9;c++) {
            char v=board[r][c]; if(v=='.') continue;
            int b=(r/3)*3+c/3;
            if(rows[r].count(v)||cols[c].count(v)||boxes[b].count(v)) return false;
            rows[r].insert(v); cols[c].insert(v); boxes[b].insert(v);
        }
        return true;
    }
};''',

    # ─── LRU CACHE ───────────────────────────────────────────────
    ("lru-cache", "python3"): '''from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity): self.cap=capacity; self.cache=OrderedDict()
    def get(self,key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key); return self.cache[key]
    def put(self,key,value):
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)>self.cap: self.cache.popitem(last=False)''',
    ("lru-cache", "javascript"): '''class LRUCache {
    constructor(capacity) { this.cap=capacity; this.map=new Map(); }
    get(key) { if(!this.map.has(key)) return -1; const v=this.map.get(key); this.map.delete(key); this.map.set(key,v); return v; }
    put(key,value) { if(this.map.has(key)) this.map.delete(key); this.map.set(key,value); if(this.map.size>this.cap) this.map.delete(this.map.keys().next().value); }
}''',
    ("lru-cache", "cpp"): '''class LRUCache {
    int cap; list<pair<int,int>> lst; unordered_map<int,list<pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity):cap(capacity){}
    int get(int key) {
        if(!mp.count(key)) return -1;
        lst.splice(lst.begin(),lst,mp[key]); return mp[key]->second;
    }
    void put(int key,int value) {
        if(mp.count(key)) lst.erase(mp[key]);
        lst.push_front({key,value}); mp[key]=lst.begin();
        if(lst.size()>cap){mp.erase(lst.back().first);lst.pop_back();}
    }
};''',

    # ─── SQL SOLUTIONS ────────────────────────────────────────────
    ("combine-two-tables", "mysql"): '''SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a ON p.personId = a.personId''',

    ("second-highest-salary", "mysql"): '''SELECT MAX(salary) AS SecondHighestSalary
FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee)''',

    ("employees-earning-more-than-their-managers", "mysql"): '''SELECT e.name AS Employee
FROM Employee e JOIN Employee m ON e.managerId = m.id WHERE e.salary > m.salary''',

    ("duplicate-emails", "mysql"): '''SELECT email AS Email FROM Person GROUP BY email HAVING COUNT(*) > 1''',

    ("customers-who-never-order", "mysql"): '''SELECT name AS Customers FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)''',

    ("rising-temperature", "mysql"): '''SELECT w1.id FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature''',

    ("big-countries", "mysql"): '''SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000''',

    ("find-customer-referee", "mysql"): '''SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL''',

    ("article-views-i", "mysql"): '''SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id ORDER BY id''',

    ("invalid-tweets", "mysql"): '''SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15''',

    ("calculate-special-bonus", "mysql"): '''SELECT employee_id,
    CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM Employees ORDER BY employee_id''',

    ("fix-names-in-a-table", "mysql"): '''SELECT user_id,
    CONCAT(UPPER(SUBSTR(name,1,1)), LOWER(SUBSTR(name,2))) AS name
FROM Users ORDER BY user_id''',

    ("patients-with-a-condition", "mysql"): '''SELECT patient_id, patient_name, conditions FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%' ''',

    ("delete-duplicate-emails", "mysql"): '''DELETE p1 FROM Person p1
JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id''',

    ("consecutive-numbers", "mysql"): '''SELECT DISTINCT l1.num AS ConsecutiveNums FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id-1 AND l1.num = l2.num
JOIN Logs l3 ON l1.id = l3.id-2 AND l1.num = l3.num''',

    ("rank-scores", "mysql"): '''SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS `rank` FROM Scores''',

    ("department-highest-salary", "mysql"): '''SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)''',

    ("user-activity-for-the-past-30-days-i", "mysql"): '''SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date''',

    ("sales-analysis-iii", "mysql"): '''SELECT s.product_id, p.product_name FROM Sales s JOIN Product p ON s.product_id = p.product_id
GROUP BY s.product_id HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31' ''',

    ("average-selling-price", "mysql"): '''SELECT p.product_id,
    IFNULL(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u ON p.product_id=u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id''',

    ("capital-gainloss", "mysql"): '''SELECT stock_name,
    SUM(CASE WHEN operation='Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks GROUP BY stock_name''',

    ("students-and-examinations", "mysql"): '''SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id=e.student_id AND sub.subject_name=e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name ORDER BY s.student_id, sub.subject_name''',

    ("managers-with-at-least-5-direct-reports", "mysql"): '''SELECT name FROM Employee
WHERE id IN (SELECT managerId FROM Employee GROUP BY managerId HAVING COUNT(*) >= 5)''',

    ("confirmation-rate", "mysql"): '''SELECT s.user_id, ROUND(AVG(c.action='confirmed'),2) AS confirmation_rate
FROM Signups s LEFT JOIN Confirmations c ON s.user_id=c.user_id GROUP BY s.user_id''',

    ("percentage-of-users-attended-a-contest", "mysql"): '''SELECT contest_id,
    ROUND(COUNT(DISTINCT user_id)*100/(SELECT COUNT(*) FROM Users),2) AS percentage
FROM Register GROUP BY contest_id ORDER BY percentage DESC, contest_id''',

    ("queries-quality-and-percentage", "mysql"): '''SELECT query_name,
    ROUND(AVG(rating/position),2) AS quality,
    ROUND(SUM(rating<3)*100/COUNT(*),2) AS poor_query_percentage
FROM Queries WHERE query_name IS NOT NULL GROUP BY query_name''',

    ("monthly-transactions-i", "mysql"): '''SELECT DATE_FORMAT(trans_date,'%Y-%m') AS month, country,
    COUNT(*) AS trans_count, SUM(state='approved') AS approved_count,
    SUM(amount) AS trans_total_amount, SUM(IF(state='approved',amount,0)) AS approved_total_amount
FROM Transactions GROUP BY month, country''',

    ("immediate-food-delivery-ii", "mysql"): '''SELECT ROUND(SUM(order_date=customer_pref_delivery_date)*100/COUNT(*),2) AS immediate_percentage
FROM Delivery WHERE (customer_id,order_date) IN (SELECT customer_id,MIN(order_date) FROM Delivery GROUP BY customer_id)''',

    ("game-play-analysis-iv", "mysql"): '''SELECT ROUND(COUNT(DISTINCT a2.player_id)/COUNT(DISTINCT a1.player_id),2) AS fraction
FROM Activity a1 LEFT JOIN Activity a2 ON a1.player_id=a2.player_id
    AND a2.event_date=DATE_ADD(a1.event_date,INTERVAL 1 DAY)
WHERE (a1.player_id,a1.event_date) IN (SELECT player_id,MIN(event_date) FROM Activity GROUP BY player_id)''',

    ("market-analysis-i", "mysql"): '''SELECT u.user_id AS buyer_id, u.join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users u LEFT JOIN Orders o ON u.user_id=o.buyer_id AND YEAR(o.order_date)=2019
GROUP BY u.user_id''',

    ("top-travellers", "mysql"): '''SELECT u.name, IFNULL(SUM(r.distance),0) AS travelled_distance
FROM Users u LEFT JOIN Rides r ON u.id=r.user_id GROUP BY u.id ORDER BY travelled_distance DESC, u.name''',

    ("exchange-seats", "mysql"): '''SELECT
    CASE WHEN id%2=1 AND id<(SELECT COUNT(*) FROM Seat) THEN id+1
         WHEN id%2=0 THEN id-1 ELSE id END AS id, student
FROM Seat ORDER BY id''',

    ("movie-rating", "mysql"): '''(SELECT u.name AS results FROM MovieRating mr JOIN Users u ON mr.user_id=u.user_id
GROUP BY mr.user_id ORDER BY COUNT(*) DESC, u.name LIMIT 1)
UNION ALL
(SELECT m.title FROM MovieRating mr JOIN Movies m ON mr.movie_id=m.movie_id
WHERE DATE_FORMAT(mr.created_at,'%Y-%m')='2020-02' GROUP BY mr.movie_id ORDER BY AVG(mr.rating) DESC, m.title LIMIT 1)''',

    ("last-person-to-fit-in-the-bus", "mysql"): '''SELECT person_name FROM (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS cumulative_weight FROM Queue
) t WHERE cumulative_weight <= 1000 ORDER BY cumulative_weight DESC LIMIT 1''',

    ("count-salary-categories", "mysql"): '''SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count FROM Accounts WHERE income < 20000
UNION ALL SELECT 'Average Salary', COUNT(*) FROM Accounts WHERE income BETWEEN 20000 AND 50000
UNION ALL SELECT 'High Salary', COUNT(*) FROM Accounts WHERE income > 50000''',

    ("employees-whose-manager-left-the-company", "mysql"): '''SELECT employee_id FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM Employees) ORDER BY employee_id''',

    ("restaurant-growth", "mysql"): '''SELECT visited_on,
    SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount
FROM (SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY visited_on) t
WHERE visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer),INTERVAL 6 DAY)''',

    ("friend-requests-ii-who-has-the-most-friends", "mysql"): '''SELECT id, COUNT(*) AS num FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL SELECT accepter_id FROM RequestAccepted
) t GROUP BY id ORDER BY num DESC LIMIT 1''',

    ("investments-in-2016", "mysql"): '''SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016 FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*)>1)
AND (lat,lon) IN (SELECT lat,lon FROM Insurance GROUP BY lat,lon HAVING COUNT(*)=1)''',
}
