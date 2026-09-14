"""
C++ LeetCode Solution Bank — auto-generated from LeetCode/C++/
"""

CPP_BANK = {
    'two-sum': '''class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>m;
        for(int i = 0; i < nums.size(); i++){
            if(m.count(target - nums[i])) return {m[target - nums[i]], i};
            m[nums[i]] = i;
        }
    }
};''',

    'add-two-numbers': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode* cur = &head;
        int carry = 0;
        while(l1 || l2 || carry){
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;
            
            ListNode* node = new ListNode((x + y + carry) % 10);
            cur->next = node;
            cur = node;
            
            carry = (x + y + carry) / 10;
            
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }
        return head.next;
    }
};''',

    'longest-substring-without-repeating-characters': '''class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int>m;
        int maxlen = 0;
        for(int i = 0, j = 0; j < s.size(); j++){
            m[s[j]]++;
            while(m[s[j]] > 1) m[s[i++]]--;
            maxlen = max(maxlen, j - i + 1);
        }
        return maxlen;
    }
};''',

    'median-of-two-sorted-arrays': '''class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        if(m > n) return findMedianSortedArrays(nums2, nums1);
        int lo = 0, hi = m, mid = (m + n + 1)/2;
        while(lo <= hi){
            int i = (lo + hi)/2;
            int j = mid - i;
            if(i < m && nums2[j - 1] > nums1[i]) 
                lo = i + 1;
            else if(i > 0  && nums1[i - 1] > nums2[j])
                hi = i - 1;
            else{
                int maxLeft = (i == 0) ? nums2[j - 1] : (j == 0) ? nums1[i - 1] : max(nums1[i - 1], nums2[j - 1]); 
                int minRight = (i == m) ? nums2[j] : (j == n) ? nums1[i] : min(nums1[i], nums2[j]);
                return (m + n) % 2 ? maxLeft : (maxLeft + minRight) / 2.0;
            }
        }
    }
};''',

    'longest-palindromic-substring': '''class Solution {
public:
	string longestPalindrome(string s) {
		if (s.size() == 0 || s.size() == 1) return s;
		string res;
		int maxlen = 0;
		for (int i = 0; i < s.size() - maxlen; i++) {
			for (int j = s.size() - 1; j >= i + maxlen; j--) {
				if (s[j] != s[i]) continue;
				string str = s.substr(i, j - i + 1);
				if (isPalindrome(str) && str.size() > maxlen) {
					maxlen = str.size();
					res = str;
				}
			}
		}
		return res;
	}

	bool isPalindrome(string s) {
		if (s.size() == 0 || s.size() == 1) return true;
		int i(0), j(s.size() - 1);
		while (s[i] == s[j] && i < j) i++, j--;
		return i >= j;
	}
};''',

    'zigzag-conversion': '''class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        vector<string>v(numRows, "");
        int d = 1;
        int row = 0;
        for(auto c: s){
            v[row].push_back(c);
            row += d;
            if(row == numRows - 1) d = -1;
            if(row == 0) d = 1;
        }
        string res;
        for(auto x: v) res.append(x);
        return res;
    }
};''',

    'reverse-integer': '''// My Solution
class Solution {
public:
    int reverse(int x) {
        string s = to_string(x);
        int base = 1;
        int i = s[0] == '-' ? 1 : 0;
        int res = 0;
        while(i < s.size()){
            if(base == 1000000000 && (s[i] - '0' > 2 || INT_MAX - (s[i] - '0') * base < res)) return 0;
            res += (s[i] - '0') * base;
            base *= 10;
            i++;
        }
        return s[0] == '-' ? -res : res;
    }
};

// Solution from https://discuss.leetcode.com/topic/6005/shortest-code-possible-in-c
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x) {
            res = res*10 + x%10;
            x /= 10;
        }
        return (res<INT_MIN || res>INT_MAX) ? 0 : res;
    }
};''',

    'string-to-integer-atoi': '''class Solution {
public:
	int myAtoi(string str) {
		if (str.size() == 0) return 0;
		int cur = 0;
		while (cur < str.size() && str[cur] == ' ') cur++;
		if (cur == str.size() || (!isdigit(str[cur]) && str[cur] != '+' && str[cur] != '-')) return 0;
		int end = cur + 1;
		while (isdigit(str[end])) end++;
		string s = str.substr(cur, end - cur);
		int num = 0;
		int base = 1;
		for (int i = s.size() - 1; i >= 0; i--) {
			if (s[i] == '+' || s[i] == '-') break;
			int add = base * (s[i] - '0');
			if (INT_MAX - num < add || (s.size() - i > 10 && s[i] != '0'))
				return s[0] == '-' ? INT_MIN : INT_MAX;
			num += add;
			base *= 10;
		}
		if (s[0] == '-') num = -num;
		return num;
	}
};''',

    'palindrome-number': '''class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x != 0 && x%10 == 0)) return false;
        int y = 0;
        while (x > y){
    	    y = y*10 + x%10;
    	    x = x/10;
        }
        return (x==y || x==y/10); 
    }
};''',

    'regular-expression-matching': '''// Solution 1. Recursion
class Solution {
public:
    bool isMatch(string s, string p) {
        if(p.empty()) return s.empty();
        if(s.empty()) return p.empty() || (p[1] == '*' ? isMatch(s, p.substr(2)) : false);
        if(p[0] != '.' && s[0] != p[0]) return p[1] == '*' ? isMatch(s, p.substr(2)) : false;
        if(p[1] == '*') return isMatch(s.substr(1), p) || isMatch(s, p.substr(2));
        return isMatch(s.substr(1), p.substr(1));
    }
};

// Solution 2. DP
class Solution {
public:
    bool isMatch(string s, string p) {
        /**
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
         */
        int m = s.size(), n = p.size();
        vector<vector<bool>> f(m + 1, vector<bool>(n + 1, false));
        
        f[0][0] = true;
        for (int i = 1; i <= m; i++)
            f[i][0] = false;
        // p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for (int j = 1; j <= n; j++)
            f[0][j] = j > 1 && '*' == p[j - 1] && f[0][j - 2];
        
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (p[j - 1] != '*')
                    f[i][j] = f[i - 1][j - 1] && (s[i - 1] == p[j - 1] || '.' == p[j - 1]);
                else
                    // p[0] cannot be '*' so no need to check "j > 1" here
                    f[i][j] = f[i][j - 2] || (s[i - 1] == p[j - 2] || '.' == p[j - 2]) && f[i - 1][j];
        
        return f[m][n];
    }
};''',

    'container-with-most-water': '''// My BF with optimization, O(n^2)
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0, minLeft = 0, minRight = 0;
        for(int i = height.size() - 1; i >= 0; i--){
            if(height[i] < minRight) continue;
            minLeft = 0;
            for(int j = 0; j < i; j++){
                if(height[j] < minLeft) continue;
                maxArea = max(maxArea, min(height[i], height[j]) * (i - j));
                minLeft = max(minLeft, height[j]);
            }
            minRight = max(minRight, height[i]);
        }
        return maxArea;
    }
};

// Brilliant O(n) from Stefan: https://discuss.leetcode.com/topic/16754/simple-and-fast-c-c-with-explanation
class Solution {
public:
    int maxArea(vector<int>& height) {
        int water = 0;
        int i = 0, j = height.size() - 1;
        while (i < j) {
            int h = min(height[i], height[j]);
            water = max(water, (j - i) * h);
            while (height[i] <= h && i < j) i++;
            while (height[j] <= h && i < j) j--;
        }
        return water;
    }
};''',

    'integer-to-roman': '''// Top-voted solution (https://discuss.leetcode.com/topic/12384/simple-solution).
class Solution {
public:
    string intToRoman(int num) {
        string M[] = {"", "M", "MM", "MMM"};
        string C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
    }
};

// While my solution is...
class Solution {
public:
    string intToRoman(int num) {
        //'I' = 1, 'X' = 10, 'C' = 100, 'M' = 1000, 'V' = 5, 'L' = 50, 'D' = 500;
        // Subtractive Notation
        // Number	 4	 9	 40     90      400     900
        // Notation	 IV	 IX	 XL	XC	CD      CM
        string res = "";
        while(num >= 1000){
            num -= 1000;
            res.push_back('M');
        }
        if(num >= 900){
            num -= 900;
            res.append("CM");
        }
        if(num >= 500){
            num -= 500;
            res.push_back('D');
        }
        if(num >= 400){
            num -= 400;
            res.append("CD");
        }
        while(num >= 100){
            num -= 100;
            res.push_back('C');
        }
        if(num >= 90){
            num -= 90;
            res.append("XC");
        }
        if(num >= 50){
            num -= 50;
            res.push_back('L');
        }
        if(num >= 40){
            num -= 40;
            res.append("XL");
        }
        while(num >= 10){
            num -= 10;
            res.push_back('X');
        }
        if(num >= 9){
            num -= 9;
            res.append("IX");
        }
        if(num >= 5){
            num -= 5;
            res.push_back('V');
        }
        if(num >= 4){
            num -= 4;
            res.append("IV");
        }
        while(num > 0){
            num -= 1;
            res.push_back('I');
        }
        return res;
    }
};''',

    'roman-to-integer': '''class Solution {
public:
    int romanToInt(string s) {
        // Rule:
        // 'I'= 1, 'X' = 10,'C' = 100, 'M' = 1000, 'V' = 5, 'L' = 50, 'D' = 500;
        // Adjacent(Left) >= Adjacent(Right): Right + Left;
        // Adjacent(Left) < Adjacent(Right): Right - Left;
        unordered_map<char,int>m({{'I',1}, {'X',10}, {'C',100}, {'M',1000}, {'V',5}, {'L',50}, {'D',500}});
        if(s.size() == 0) return 0;
        int sum = m[s[s.size() - 1]];
        for(int i = s.size() - 2; i >= 0; i--){
            if(m[s[i]] >= m[s[i + 1]]) sum += m[s[i]];
            else sum -= m[s[i]];
        }
        return sum;
    }
};''',

    'longest-common-prefix': '''// Solution 1
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return "";
        string res = strs[0];
        for(auto s: strs) res = match(res, s);
        return res;
    }
    
    string match(const string& pre, const string& s){
        int i = 0, len = min(pre.size(), s.size());
        for(; i < len; i++) if(s[i] != pre[i]) break;
        return pre.substr(0, i);
    }
};

// Solution 2
// Using sort and only compare the first string with the last string.
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return "";
        sort(strs.begin(), strs.end());
        string a = strs[0], b = strs.back();
        int i = 0;
        for(; i < min(a.size(), b.size()); i++) if(a[i] != b[i]) break;
        return a.substr(0, i);
    }
};''',

    '3sum': '''class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>>res;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < (int)nums.size() - 1; i++){
            if(i > 0 && nums[i - 1] == nums[i]) continue;
            int lo = i + 1;
            for(int hi = nums.size() - 1; hi > lo; hi--){
                if(hi < nums.size() - 1 && nums[hi] == nums[hi + 1]) continue;
                while(nums[lo] < -(nums[i] + nums[hi])) lo++;
                if(lo < hi && (nums[i] + nums[lo] + nums[hi]) == 0) res.push_back({nums[i], nums[lo], nums[hi]});
            }
        }
        return res;
    }
};


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>>res;
        for (int l = 0; l < n - 2; ++l) {
            if (l > 0 && nums[l] == nums[l - 1]) {
                continue;
            }
            int r = n - 1;
            int mid = l + 1;
            while (mid < r) {
                if (r < n - 1 && nums[r] == nums[r + 1]) {
                    --r;
                    continue;
                }
                
                while (r > mid && nums[l] + nums[mid] + nums[r] < 0) {
                    ++mid;
                }
                
                if (r > mid && nums[l] + nums[mid] + nums[r] == 0) {
                    res.push_back({nums[l], nums[mid], nums[r]});
                }
                --r;
            }
        }
        return res;
    }
};''',

    '3sum-closest': '''class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int diff = INT_MAX, res = 0;
        for(int i = 0; i < nums.size() - 2; i++){
            int lo = i + 1, hi = nums.size() - 1;
            while(lo < hi){
                int sum = nums[i] + nums[lo] + nums[hi];
                if(sum == target) return target;
                if(abs(sum - target) < diff) diff = abs(sum - target), res = sum;
                (sum > target) ? hi-- : lo++;
            }
        }
        return res;
    }
};''',

    'letter-combinations-of-a-phone-number': '''class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.size() == 0) return res;
        string s = "";
        unordered_map<char,vector<int>>m({{'2', {'a','b','c'}},
                                          {'3', {'d','e','f'}},
                                          {'4', {'g','h','i'}},
                                          {'5', {'j','k','l'}},
                                          {'6', {'m','n','o'}},
                                          {'7', {'p','q','r','s'}},
                                          {'8', {'t','u','v'}},
                                          {'9', {'w','x','y','z'}}});
        DFS(m, digits, 0, res, s);
        return res;
    }
    
    void DFS(unordered_map<char,vector<int>>& m, string& digits, int l, vector<string>& res, string& s){
        if(l == digits.size()){
            res.push_back(s);
            return;
        }
        for(int i = 0; i < m[digits[l]].size(); i++){
            s.push_back(m[digits[l]][i]);
            DFS(m, digits, l+1, res, s);
            s.pop_back();
        }
        return;
    } 
};

// Update
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string>res;
        if(digits.empty()) return res;
        vector<string>letter({"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"});
        string path = "";
        DFS(digits, 0, path, res, letter);
        return res;
    }
    
    void DFS(string digits, int pos, string& path, vector<string>& res, vector<string>& letter){
        if(pos == digits.size()){
            res.push_back(path);
            return;
        }
        for(auto c: letter[digits[pos] - '0']){
            path.push_back(c);
            DFS(digits, pos + 1, path, res, letter);
            path.pop_back();
        }
    }
};''',

    '4sum': '''class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>>res;
        vector<int>path;
        DFS(res, nums, 0, target, 0, 0, path);
        return res;
    }
    
    void DFS(vector<vector<int>>& res, vector<int>& nums, int pos, int target, int count, int sum, vector<int>& path){
        if(count == 4){
            if(sum == target) res.push_back(path);
            return;
        }
        for(int i = pos; i < nums.size(); i++){
            if(i != pos && nums[i] == nums[i - 1]) continue;
            if(sum + nums[i] + (3 - count) * nums[nums.size() - 1] < target) continue;
            if(sum + (4 - count)* nums[i] > target) break;
            path.push_back(nums[i]);
            DFS(res, nums, i + 1, target, count + 1, sum + nums[i], path);
            path.pop_back();
        }
    }
};''',

    'remove-nth-node-from-end-of-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow(head), *fast(head);
        while(n--) fast = fast->next;
        if(!fast) return head->next;
        while(fast->next) slow = slow->next, fast = fast->next;
        slow->next = slow->next->next;
        return head;
    }
};''',

    'valid-parentheses': '''class Solution {
public:
    bool isValid(string s) {
        stack<char>stk;
        for(auto c: s){
            if(stk.empty() && (c == ')' || c == ']' || c == '}')) return false;
            if(c == '(' || c == '[' || c == '{') stk.push(c);
            else{
                char left = stk.top();
                if((c == ')' && left != '(') || (c == ']' && left != '[') || (c == '}' && left != '{')) return false;
                stk.pop();
            }
        }
        return stk.empty();
    }
};''',

    'merge-two-sorted-lists': '''/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (!l1 || !l2) return l1 ? l1 : l2;
		ListNode head(0);
		ListNode* cur = &head;
		while (l1 && l2) {
			if (l1->val < l2->val) {
				cur->next = l1;
				l1 = l1->next;
			}
			else {
				cur->next = l2;
				l2 = l2->next;
			}
			cur = cur->next;
		}
		cur->next = l1 ? l1 : l2;
		return head.next;
	}
};''',

    'generate-parentheses': '''class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string>res;
        string path = "";
        DFS(res, n, 0, 0, path);
        return res;
    }
    
    void DFS(vector<string>& res, int n, int k, int left, string& path){
        if(left > n) return;
        if(k == n){
            if(left == 0) res.push_back(path);
            return;
        }
        path.push_back('(');
        DFS(res, n, k, left + 1, path);
        path.pop_back();
        
        if(left != 0){
            path.push_back(')');
            DFS(res, n, k + 1, left - 1, path);
            path.pop_back();
        }
    }
};''',

    'merge-k-sorted-lists': '''/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/

// Solution 1: O(n^2)
class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		if (lists.size() == 0) return NULL;
		for (int i = 0, j = 1; j < lists.size(); i++, j++)
			lists[j] = mergeTwoLists(lists[i], lists[j]);
		return *(lists.end() - 1);
	}

	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (!l1 || !l2) return l1 ? l1 : l2;
		ListNode head(0);
		ListNode* cur = &head;
		while (l1 && l2) {
			if (l1->val < l2->val) {
				cur->next = l1;
				l1 = l1->next;
			}
			else {
				cur->next = l2;
				l2 = l2->next;
			}
			cur = cur->next;
		}
		cur->next = l1 ? l1 : l2;
		return head.next;
	}
};

// Solution 2: O(nlogn)
class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		auto comp = [](int a, int b) { return a > b; };
		priority_queue<int, vector<int>, decltype(comp)>pq(comp);
		for (auto x : lists)
			while (x) pq.push(x->val), x = x->next;
		ListNode head(0);
		ListNode* cur = &head;
		while (!pq.empty()) {
			ListNode* node = new ListNode(pq.top());
			cur->next = node;
			cur = cur->next;
			pq.pop();
		}
		return head.next;
	}
};

// Or just store the ListNode* in priority_queue.
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto comp = [](ListNode* a, ListNode* b){ return a->val > b->val;};
        priority_queue<ListNode*, vector<ListNode*>, decltype(comp)>pq(comp);
        for(auto x: lists)
            while(x) pq.push(x), x = x->next;
        ListNode head(0);
        ListNode* cur = &head;
        while(!pq.empty()){
            cur->next = pq.top();
            cur = cur->next;
            pq.top()->next = NULL;
            pq.pop();
        }
        return head.next;
    }
};''',

    'swap-nodes-in-pairs': '''/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/
class Solution {
public:
	ListNode* swapPairs(ListNode* head) {
		if (!head || !head->next) return head;
		ListNode res(0);
		ListNode *pre = &res, *one = head, *two = head->next;
		while (one && two) {
			one->next = two->next;
			two->next = one;
			pre->next = two;
			pre = one;
			one = one->next;
			if (one) two = one->next;
		}
		return res.next;
	}
};''',

    'reverse-nodes-in-k-group': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// Solution 1.
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* pre = new ListNode(0);
        pre->next = head;
        ListNode* res = pre;
        ListNode* slow(head), *fast(head), *next;
        while(fast){
            int i = k - 1;
            while(fast && i--) fast = fast->next;
            if(fast){
                next = fast->next;
                reverse(pre, slow, fast, next);
                pre = slow;
                slow = next;
                fast = next;
            }
        }
        return res->next;
    }
    
    void reverse(ListNode* left, ListNode* start, ListNode* end, ListNode* right){
        ListNode* pre(left), *cur(start), *next;
        ListNode* tmp = start;
        while(cur != right){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        left->next = pre;
        tmp->next = right;
    }
};

// Solution 2.
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* pre = &dummy, *cur(head), *next, *tmp, *p, *ppre, *ccur;
        while(cur){
            p = cur;
            for(int i = 1; i < k && p; i++) p = p->next;
            if(!p) break;
            ppre = pre;
            ccur = cur;
            pre = p->next;
            tmp = p->next;
            while(cur != tmp){
                next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = next;
            }
            ppre->next = pre;
            pre = ccur;
        }
        return dummy.next;
    }
};''',

    'remove-duplicates-from-sorted-array': '''class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j = 0;
        while(j < nums.size()){
            while(j < nums.size() - 1 && nums[j] == nums[j + 1]) j++;
            nums[i++] = nums[j++];
        }
        return i;
    }
};''',

    'remove-element': '''class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0, j = 0;
        while(j != nums.size())
            if(nums[j] == val) j++;
            else nums[i++] = nums[j++];
        return i;
    }
};''',

    'implement-strstr': '''/**
 * Solution 1. 
 * Brute force, simple and easy.
 * Time complexity : O(n*m)
 * Space comlexity : O(1)
 * Run time : 109 ms
 */
class Solution {
public:
	int strStr(string haystack, string needle) {
		if (needle.size() == 0) return 0;
		for (int i = 0; i < haystack.size(); i++)
			if (haystack[i] == needle[0] && isEqual(haystack.substr(i), needle)) return i;
		return -1;
	}

	bool isEqual(string s1, string s2) {
		if (s1.size() < s2.size()) return false;
		for (int i = 0; i < s2.size(); i++)
			if (s1[i] != s2[i]) return false;
		return true;
	}
};

// Or move isEqual() function inside.
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size() == 0) return 0;
        for(int i = 0; i < haystack.size(); i++){
            int j = 0;
            for(;j < needle.size(); j++){
                if(i + j == haystack.size()) return -1;
                if(haystack[i + j] != needle[j]) break;
            }
            if(j == needle.size()) return i;
        }
        return -1;
    }
};

/**
 * Solution 2. 
 * In BF solution, we compare two strings everytime we meet the charactor needle[0], 
 * which can cause a lot of unnecessary calculations.
 * Is there a way to "shrink" the candidate substrings ?
 * We can use a hash table to count the number of occurrence of `char`s in needle, 
 * and only jump to comparison when substring in haystack has the same `char`s and occurrence with needle.
 * Time complexity : O(n)
 * Space complexity : O(n)
 * Run time : 6 ms
 */
class Solution {
public:
	int strStr(string haystack, string needle) {
		if (needle.size() == 0) return 0;
		unordered_map<char, int>m;
		for (auto x : needle) m[x]++;
		int count = needle.size();
		int begin = 0, end = 0;
		while (end < haystack.size()) {
			if (m[haystack[end++]]-- > 0) count--;
			if (count == 0) {
				int i = begin, j = 0;
				while (j < needle.size() && haystack[i] == needle[j]) i++, j++;
				if (j == needle.size()) return begin;
			}
			if (end - begin == needle.size() && m[haystack[begin++]]++ >= 0) count++;
		}
		return -1;
	}
};

/**
 * Solution 3. 
 * Finally, a "cheat" solution.
 * Time complexity : O(n)
 * Space complexity : O(1)  (not sure about that, correct me if I'm wrong)
 * Run time : 6 ms
 */
class Solution {
public:
	int strStr(string haystack, string needle) {
		return haystack.find(needle);
	}
};''',

    'next-permutation': '''// My BF O(n^2) solution
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int left = 0, right = -1;
        for(int i = nums.size() - 1; i >= 0; i--)
            for(int j = i - 1; j >= 0; j--)
                if(nums[j] < nums[i] && (j > left || right == -1)) left = j, right = i;
        if(right == -1) sort(nums.begin(), nums.end());
        else{
            swap(nums[left], nums[right]);
            sort(nums.begin() + left + 1, nums.end());
        }
    }
};

// O(n) Solution from Stefan: https://discuss.leetcode.com/topic/19264/1-4-11-lines-c
void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 1, k = i;
    while (i > 0 && nums[i-1] >= nums[i])
        i--;
    for (int j=i; j<k; j++, k--)
        swap(nums[j], nums[k]);
    if (i > 0) {
        k = i--;
        while (nums[k] <= nums[i])
            k++;
        swap(nums[i], nums[k]);
    }
}''',

    'search-in-rotated-sorted-array': '''// Solution 1.
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n == 0) return -1;
        int lo = 0, hi = n - 1;
        int mid = (lo + hi) / 2;
        while(lo < hi){
            if(nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
            mid = (lo + hi) / 2;
        }
        int pos = (target >= nums[0] && lo != 0) ? lower_bound(nums.begin(), nums.begin() + lo, target) - nums.begin() 
                                                 : lower_bound(nums.begin() + lo, nums.end(), target) - nums.begin();
        return nums[pos] == target ? pos : -1;
    }
};

// Solution 2.
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n == 0) return -1;
        int lo = 0, hi = n - 1;
        int mid = (lo + hi) / 2;
        while(lo < hi){
            if(nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
            mid = (lo + hi) / 2;
        }
        int ro = lo;
        lo = 0, hi = n - 1;
        mid = (lo + hi) / 2;
        while(lo <= hi){
            int realMid = (mid + ro) % n;
            if(nums[realMid] == target) return realMid; 
            if(nums[realMid] > target) hi = mid - 1;
            else lo = mid + 1;
            mid = (lo + hi) / 2;
        }
        return -1;
    }
};''',

    'search-for-a-range': '''class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int lo = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int hi = upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
        if(lo > hi) return {-1,-1};
        return {lo, hi};
    }
};''',

    'search-insert-position': '''class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size() - 1;
        int mid = lo + (hi - lo) / 2;
        while(lo <= hi){
            if(nums[mid] == target) return mid;
            if(nums[mid] > target) hi = mid - 1;
            else lo = mid + 1;
            mid = lo + (hi - lo) / 2;
        }
        return lo;
    }
};''',

    'valid-sudoku': '''class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        vector<unordered_map<char, int>>row(n);
        vector<unordered_map<char, int>>col(n);
        vector<vector<unordered_map<char, int>>>sub(n/3, vector<unordered_map<char, int>>(n/3));
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++){
                char c = board[i][j];
                if(c == '.') continue;
                if(row[i][c]++ > 0 || col[j][c]++ > 0 || sub[i/3][j/3][c]++ > 0) return false;
            }
        return true;
    }
};''',

    'count-and-say': '''class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        string s = countAndSay(n - 1);
        string res = "";
        for(int i = 0; i < s.size(); i++){
            int count = 1;
            while(i < s.size() - 1 && s[i] == s[i + 1]) i++, count++;
            res.append(to_string(count) + s[i]);
        }
        return res;
    }
};''',

    'combination-sum': '''class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>res;
        vector<int>comb;
        backtrack(res, candidates, 0, 0, target, comb);
        return res;
    }
    
    void backtrack(vector<vector<int>>& res, vector<int>& candidates, int pos, int sum, int target, vector<int>& comb){
        if(sum > target || pos == candidates.size()) return;
        if(sum == target){
            res.push_back(comb);
            return;
        }
        backtrack(res, candidates, pos + 1, sum, target, comb);
        comb.push_back(candidates[pos]);
        backtrack(res, candidates, pos, sum + candidates[pos], target, comb);
        comb.pop_back();
    }
};''',

    'combination-sum-ii': '''class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>>res;
        vector<int>path;
        DFS(res, candidates, 0, 0, target, path);
        return res;
    }
    
    void DFS(vector<vector<int>>& res, vector<int>& candidates, int pos, int sum, int target, vector<int>& path){
        if(sum >= target){
            if(sum == target) res.push_back(path);
            return;
        }
        for(int i = pos; i < candidates.size(); i++){
            if(i != pos && candidates[i] == candidates[i - 1]) continue;
            path.push_back(candidates[i]);
            DFS(res, candidates, i + 1, sum + candidates[i], target, path);
            path.pop_back();
        }
    }
};''',

    'first-missing-positive': '''// O(nlogn)
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i = 1;
        for(int x: nums) if(x == i) i++;
        return i;
    }
};

// O(n)
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.empty()) return 1;
        for(int i = 0; i < nums.size(); i++)
            while(nums[i] > 0  && nums[i] < nums.size() && nums[i] != nums[nums[i] - 1]) swap(nums[i], nums[nums[i] - 1]);
        for(int i = 0; i < nums.size(); i++) if(nums[i] != i + 1) return i + 1;
        return nums.size() + 1;
    }
};''',

    'trapping-rain-water': '''class Solution {
public:
    int trap(vector<int>& height) {
        int sum = 0, maxH = 0;
        stack<int>stk, idx;
        for(int i = 0; i < height.size(); i++){
            int h = min(maxH, height[i]);
            if(!stk.empty()){
                int temp = 0, preIdx = i, preH = h, curH = h;
                while(!stk.empty() && stk.top() < height[i]){
                    curH = stk.top();
                    temp += (h - preH) * (preIdx - idx.top()) - (curH - preH);
                    preH = stk.top();
                    stk.pop();
                    preIdx = idx.top();
                    idx.pop();
                }
                if(!stk.empty()) temp += (h - preH) * (preIdx - 1 - idx.top());
                sum += temp;
            }
            stk.push(height[i]);
            idx.push(i);
            maxH = max(maxH, height[i]);
        }
        return sum;
    }
};''',

    'multiply-strings': '''// Solution 1.
class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0") return "0";
        string res = "";
        for(int i = num2.size() - 1, zero = 0; i >= 0; i--, zero++)
            res=addStr(res, multiStr(num1, num2[i] - '0', zero));
        return res;
    }
    //string * multiple -> string
    string multiStr(string s, int multiple, int zero){
        int carry = 0;
        int n = 0;
        for(int i = s.size()-1; i >= 0; i--){
            n = (s[i]-'0') * multiple + carry;
            s[i] = n%10 + '0';
            carry = n/10;
        }
        if(carry) s = to_string(carry) + s;
        while(zero) s += "0", zero--;
        return s;
    }
    //string + string -> string
    string addStr(string num1, string num2) {
        string s = "";
        int carry = 0;
        for(int i = num1.size()-1, j = num2.size()-1; i >= 0 || j >= 0 || carry; i--, j--){
            int x = i < 0 ? 0 : num1[i] - '0';
            int y = j < 0 ? 0 : num2[j] - '0';
            s.push_back((x + y + carry) % 10 + '0');
            carry = (x + y + carry) / 10;
        }
        reverse(s.begin(), s.end());
        return s;
    }
};

// Solution 2.
class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int>pos(num1.size() + num2.size());
        for(int i = num1.size() - 1; i >= 0; i--){
            for(int j = num2.size() - 1; j >= 0; j--){
                int sum = (num1[i] - '0') * (num2[j] - '0') + pos[i + j + 1];
                pos[i + j + 1] = sum % 10;
                pos[i + j] += sum / 10;
            }
        }
        string res = "";
        for(auto x: pos) if(!(res == "" && x == 0)) res.push_back(x + '0');
        return res == "" ? "0" : res;
    }
};''',

    'wildcard-matching': '''// My TLE recursion (1611/1805).
class Solution {
public:
    bool isMatch(string s, string p) {
        if(p.empty()) return s.empty();
        if(s.empty()) return p.empty() || p[0] == '*' ? isMatch(s, p.substr(1)) : false;
        if(p[0] != '?' && p[0] != '*' && p[0] != s[0]) return false; 
        if(p[0] == '*'){
            for(int i = 0; i <= s.size(); i++)
                if(isMatch(s.substr(i), p.substr(1))) return true;
            return false;
        }
        return isMatch(s.substr(1), p.substr(1));
    }
};

// An O(n) C++ based on this [post](https://discuss.leetcode.com/topic/3040/linear-runtime-and-constant-space-solution).
class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0, ss = 0, star = -1;
        while(i < s.size()){
            if(j < p.size() && (p[j] == '?' || s[i] == p[j])){
                i++;
                j++;
            }
            else if(j < p.size() && p[j] == '*'){
                star = j;
                ss = i;
                j++;
            }
            else if(star != -1){
                j = star + 1;
                i = ++ss;
            }
            else return false;
        }
        while(j < p.size() && p[j] == '*') j++;
        return j == p.size();
    }
};''',

    'jump-game-ii': '''class Solution {
public:
    int jump(vector<int>& nums) {
        int minJump = nums.size();
        DFS(nums, 0, 0, minJump);
        return minJump;
    }
    
    void DFS(vector<int>& nums, int pos, int jump, int& minJump){
        if(pos == nums.size() - 1){
            minJump = min(minJump, jump);
            return;
        }
        int next = pos + 1, maxlen = 1 + nums[pos + 1];
        for(int i = 1; i <= nums[pos] && pos + i < nums.size(); i++)
            if(i + nums[pos + i] > maxlen || pos + i == nums.size() - 1) next = pos + i, maxlen = i + nums[next];
        DFS(nums, next, jump + 1, minJump);
    }
};''',

    'permutations': '''class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>res;
        DFS(res, nums, 0);
        return res;        
    }
    
    void DFS(vector<vector<int>>& res, vector<int>& nums, int pos){
        if(pos == nums.size() - 1){
            res.push_back(nums);
            return;
        }
        for(int i = pos; i < nums.size(); i++){
            swap(nums[pos], nums[i]);
            DFS(res, nums, pos + 1);
            swap(nums[pos], nums[i]);
        }
    }
};''',

    'permutations-ii': '''class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>>res;
        DFS(res, nums, 0);
        return res;        
    }
    
    void DFS(vector<vector<int>>& res, vector<int> nums, int pos){
        if(pos == nums.size() - 1){
            res.push_back(nums);
            return;
        }
        for(int i = pos; i < nums.size(); i++){
            if(i != pos && nums[i] == nums[pos]) continue;
            swap(nums[pos], nums[i]);
            DFS(res, nums, pos + 1);
        }
    }
};''',

    'rotate-image': '''// Detailed explanation with hand-draw graph can be found in discuss.
// In-place.
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        helper(matrix, 0, 0, matrix.size());
    }
    
    void helper(vector<vector<int>>& matrix, int row, int col, int size) {
        if (size == 0 || size == 1) return;
        int step = 0;
        while(step < size - 1){
            swap(matrix[row][col + step], matrix[row + step][col + size - 1]);
            swap(matrix[row][col + step], matrix[row + size - 1 - step][col]);
            swap(matrix[row + size - 1][col + size - 1 - step], matrix[row + size - 1 - step][col]);
            step++;
        }
        helper(matrix, row + 1, col + 1, size - 2);
    }
};

// Just for clear up, A common method to rotate the image from this post by @SHICHAOTAN:
// https://discuss.leetcode.com/topic/6796/a-common-method-to-rotate-the-image.
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}''',

    'group-anagrams': '''class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>>res;
        unordered_map<string, vector<string>>m;
        for(auto s: strs){
            string tmp = s;
            sort(tmp.begin(), tmp.end());
            m[tmp].push_back(s);
        }
        for(auto x: m) res.push_back(x.second);
        return res;
    }
};

// Implement an O(n) sort() function myself.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>>res;
        unordered_map<string, vector<string>>m;
        for(auto s: strs){
            string tmp = s;
            sortStr(tmp);
            m[tmp].push_back(s);
        }
        for(auto x: m) res.push_back(x.second);
        return res;
    }
    
    void sortStr(string& s){
        unordered_map<char, int>m;
        for(auto c: s) m[c]++;
        string res = "";
        for(int i = 0; i < 26; i++){
            while(m['a' + i]-- > 0) res.push_back('a' + i);
        }
        s = res;
    }
};''',

    'pow-x-n': '''// Iterative.
class Solution {
public:
    double myPow(double x, int n) {
        if(x == 1) return x;
        if(x == -1) return n % 2 ? -1 : 1;
        if(x < 1 && n == INT_MAX || n == INT_MIN) return 0;
        double res=1;
        if(n < 0) x = 1/x, n = -n;
        while(n > 0){
            res = res * x;
            n--;
        }
        return res;
    }
};

// Recursive.
class Solution {
public:
    double myPow(double x, int n) {
        if(x == 1) return 1;
        if(x == -1) return n % 2 ? -1 : 1;
        if(n == INT_MIN) return 0;
        if(n == 0) return 1;
        if(n < 0) return 1 / myPow(x, -n);
        if(n % 2) return x * myPow(x, n - 1);
        else{
            double d = myPow(x, n/2);
            return d * d;
        }
    }
};

// A more concise recursive solution from this thread:
// https://discuss.leetcode.com/topic/21837/5-different-choices-when-talk-with-interviewers
class Solution {
public:
    double myPow(double x, int n) {
        if(n==0) return 1;
        double t = myPow(x,n/2);
        if(n%2) return n<0 ? 1/x*t*t : x*t*t;
        else return t*t;
    }
};''',

    'maximum-subarray': '''class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // dp[i] = max(dp[i - 1] + A[i], A[i])
        vector<int>dp(nums.size());
        dp[0] = nums[0];
        int maxSum = dp[0];
        for(int i = 1; i < nums.size(); i++){
            dp[i] = max(dp[i - 1] + nums[i], nums[i]);
            maxSum = max(maxSum, dp[i]);
        }
        return maxSum;
    }
};

// Then we notice dp[i] only depends on dp[i - 1], so actually we only need one variable here to replace the array.
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp = nums[0];
        int maxSum = dp;
        for(int i = 1; i < nums.size(); i++){
            dp = max(dp + nums[i], nums[i]);
            maxSum = max(maxSum, dp);
        }
        return maxSum;
    }
};''',

    'spiral-matrix': '''// Final solution
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        if(matrix.size() == 0) return res;
        int minR = 0, maxR = matrix.size() - 1, minC = 0, maxC = matrix[0].size() - 1;
        while(minR <= maxR && minC <= maxC){
            for(int i = minC; i <= maxC; i++) res.push_back(matrix[minR][i]);
            minR++;
            for(int i = minR; i <= maxR; i++) res.push_back(matrix[i][maxC]);
            maxC--;
            for(int i = maxC; i >= minC && minR <= maxR; i--) res.push_back(matrix[maxR][i]);
            maxR--;
            for(int i = maxR; i >= minR && minC <= maxC; i--) res.push_back(matrix[i][minC]);
            minC++;
        }
        return res;
    }
};

// Solution 1.
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        if(matrix.size() == 0) return res;
        pair<int,int>d(0, 1);
        vector<vector<int>>visited(matrix.size(), vector<int>(matrix[0].size(), 0));
        DFS(matrix, 0, 0, d, res, visited);
        return res;
    }
    
    void DFS(vector<vector<int>>& matrix, int r, int c, pair<int,int>& d, vector<int>& res, vector<vector<int>>& visited){
        res.push_back(matrix[r][c]);
        if(res.size() == matrix.size() * matrix[0].size()) return;
        visited[r][c] = 1;
        int nextRow = r + d.first;
        int nextCol = c + d.second;
        if(nextRow == matrix.size() || nextCol == matrix[0].size() || nextCol < 0 || visited[nextRow][nextCol]) 
            d = nextDirection(d);
        DFS(matrix, r + d.first, c + d.second, d, res, visited);
    }
    
    //directions: right -> down -> left -> up;
    pair<int,int> nextDirection(pair<int,int>& d){
        pair<int, int>right(0, 1), down(1, 0), left(0, -1), up(-1, 0);
        return (d == right) ? down : (d == down) ? left : (d == left) ? up : right;
    }
};

// Solution 2.
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        if(matrix.empty()) return res;
        DFS(matrix, 0, 0, matrix.size(), matrix[0].size(), res);
        return res;
    }
    
    void DFS(vector<vector<int>>& matrix, int r, int c, int maxR, int maxC, vector<int>& res){
        if(r >= maxR || c >= maxC) return;
        for(int i = c; i < maxC; i++) res.push_back(matrix[r][i]);
        for(int i = r + 1; i < maxR; i++) res.push_back(matrix[i][maxC - 1]);
        for(int i = maxC - 2; i > c && r != maxR - 1; i--) res.push_back(matrix[maxR - 1][i]);
        for(int i = maxR - 1; i > r && c != maxC - 1; i--) res.push_back(matrix[i][c]);
        DFS(matrix, r + 1, c + 1, maxR - 1, maxC - 1, res);
    }
};

// Solution 3.
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        if(matrix.size() == 0) return res;
        DFS(matrix, 0, matrix.size() - 1, 0, matrix[0].size() - 1, res);
        return res;
    }
    
    void DFS(vector<vector<int>>& matrix, int minRow, int maxRow, int minCol, int maxCol, vector<int>& res){
        if(minRow > maxRow || minCol > maxCol) return;
        for(int i = minCol; i <= maxCol; i++) res.push_back(matrix[minRow][i]);
        minRow++;
        for(int i = minRow; i <= maxRow; i++) res.push_back(matrix[i][maxCol]);
        maxCol--;
        for(int i = maxCol; i >= minCol && minRow <= maxRow; i--) res.push_back(matrix[maxRow][i]);
        maxRow--;
        for(int i = maxRow; i >= minRow && minCol <= maxCol; i--) res.push_back(matrix[i][minCol]);
        minCol++;
        DFS(matrix, minRow, maxRow, minCol, maxCol, res);
    }
};''',

    'jump-game': '''class Solution {
public:
    bool canJump(vector<int>& nums) {
        int distance = 0;
        for(int i = 0; i < nums.size() - 1; i++){
            distance = max(distance, i + nums[i]);
            if(distance == i) return false;
        }
        return true;
    }
};''',

    'merge-intervals': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](Interval& a, Interval& b){ return a.start < b.start; });
        vector<Interval>res;
        for(int i = 0; i < intervals.size(); i++)
            if(res.empty() || res.back().end < intervals[i].start) res.push_back(intervals[i]);
            else res.back().end = max(res.back().end, intervals[i].end);
        return res;
    }
};''',

    'insert-interval': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval>res;
        for(auto x: intervals)
            if(x.end >= newInterval.start && x.start <= newInterval.end){
                newInterval.start = min(newInterval.start, x.start);
                newInterval.end = max(newInterval.end, x.end);
            }
        for(auto x: intervals) 
            if(x.end < newInterval.start || x.start > newInterval.end) res.push_back(x);
        for(int i = 0; i < res.size(); i++)
            if(res[i].start > newInterval.start){
                res.insert(res.begin() + i, newInterval);
                break;
            }
        if(res.empty() || res.back().end < newInterval.start) res.push_back(newInterval);
        return res;
    }
};''',

    'length-of-last-word': '''class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        while(i >= 0 && s[i] == ' ') i--;
        int j = i;
        while(j >= 0 && s[j] != ' ') j--;
        return i - j;
    }
};''',

    'spiral-matrix-ii': '''class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>>matrix(n, vector<int>(n, 0));
        if(n == 0) return matrix;
        spiral(matrix, 0, n - 1, 0, n - 1, 1, n);
        return matrix;
    }
    
    void spiral(vector<vector<int>>& matrix, int minRow, int maxRow, int minCol, int maxCol, int k, int n){
        if(k > n * n) return;
        if(k == n * n){
            matrix[minRow][minCol] = k;
            return;
        }
        for(int i = minCol; i <= maxCol; i++) matrix[minRow][i] = k++;
        minRow++;
        for(int i = minRow; i <= maxRow; i++) matrix[i][maxCol] = k++;
        maxCol--;
        for(int i = maxCol; i >= minCol; i--) matrix[maxRow][i] = k++;
        maxRow--;
        for(int i = maxRow; i >= minRow; i--) matrix[i][minCol] = k++;
        minCol++;
        spiral(matrix, minRow, maxRow, minCol, maxCol, k, n);
    }
};''',

    'permutation-sequence': '''// Solution 1. Backtracking
// Run Time: 266ms
class Solution {
public:
    string getPermutation(int n, int k) {
        string s = "", res = "";
        for(int i = 1; i <= n; i++) s.push_back(i + '0');
        string path = s;
        int count = 0;
        DFS(s, 0, count, n, k, path, res);
        return res;
    }
    
    void DFS(string& s, int pos, int& count, int n, int k, string& path, string& res){
        if(count >= k || pos == n){
            if(++count == k) res = path;
            return;
        }
        for(int i = 0; i < n; i++){
            if(s[i] == '0') continue;
            path[pos] = s[i];
            s[i] = '0';
            DFS(s, pos + 1, count, n, k, path, res);
            s[i] = path[pos];
        }
    }
};

// Solution 2. Using STL
// Run Time: 119ms
class Solution {
public:
    string getPermutation(int n, int k) {
        string s = "";
        for(int i = 1; i <= n; i++) s.push_back(i + '0');
        while(--k) next_permutation(s.begin(), s.end());
        return s;
    }
};

// Solution 3. Math, C++ version of this thread: https://discuss.leetcode.com/topic/17348/explain-like-i-m-five-java-solution-in-o-n
// Run time: 3ms
class Solution {
public:
    string getPermutation(int n, int k) {
        string s = "", res = "";
        vector<int>factorial(n + 1, 1);
        int sum = 1;
        for(int i = 1; i <= n; i++){
            s.push_back(i + '0');
            sum *= i;
            factorial[i] = sum;
        }
        k--;
        for(int i = 1; i <= n; i++){
            int index = k / factorial[n - i];
            res.push_back(s[index]);
            s.erase(s.begin() + index);
            k %= factorial[n - i];
        }
        return res;
    }
};''',

    'rotate-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 // Solution 1.
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next) return head;

        int len = 0;
        ListNode* p = head;
        while(p) p = p->next, len++;
        k = k % len;
        if(k == 0) return head;
        
        ListNode* slow = head;
        ListNode* fast = head;
        while(k > 0) fast = fast->next, k--;
        while(fast->next) fast = fast->next, slow = slow->next;
        
        ListNode* res = slow->next;
        
        slow->next = NULL;
        fast->next = head;
        
        return res;
    }
};

// Solution 2.
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !k) return head;
        ListNode* tail(head), *cur(head), *res;
        
        int len = 1;
        while(tail->next) tail = tail->next, len++;
        
        k = k % len;
        if(!k) return head;
        k = len - k;
        
        while(--k) cur = cur->next;
        
        res = cur->next;
        cur->next = NULL;
        tail->next = head;
        
        return res;
    }
};''',

    'unique-paths': '''class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>>dp(m, vector<int>(n));
        for(int i = 0; i < m; i++) dp[i][0] = 1;
        for(int i = 0; i < n; i++) dp[0][i] = 1;
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        return dp[m - 1][n - 1];
    }
};

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>>dp(m + 1, vector<int>(n + 1));
        dp[1][1] = 1;
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                dp[i][j] += dp[i -  1][j] + dp[i][j - 1];
            }
        }
        return dp[m][n];
    }
};

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int>dp(n);
        dp[0] = 1;
        for (int i = 0; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[j] += dp[j -  1];
            }
        }
        return dp[n - 1];
    }
};''',

    'unique-paths-ii': '''class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<int>dp(n);
        dp[0] = 1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }
};''',

    'minimum-path-sum': '''class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if(grid.empty()) return 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>>dp(m, vector<int>(n));
        dp[0][0] = grid[0][0];
        for(int i = 1; i < m; i++) dp[i][0] = grid[i][0] + dp[i - 1][0];
        for(int i = 1; i < n; i++) dp[0][i] = grid[0][i] + dp[0][i - 1];
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j];
        return dp[m - 1][n - 1];
    }
};''',

    'plus-one': '''class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1;
        while(i >= 0 && digits[i] == 9) digits[i--] = 0;
        if(i < 0) digits.push_back(0), i++;
        digits[i]++;
        return digits;
    }
};''',

    'add-binary': '''class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        string s = "";
        int i = a.size() - 1;
        int j = b.size() - 1;
        while(i >= 0 || j >= 0 || carry){
            int num1 = i < 0 ? 0 : a[i] - '0';
            int num2 = j < 0 ? 0 : b[j] - '0';
            int sum = num1 + num2 + carry;
            s.push_back(sum % 2 + '0');
            carry = sum / 2;
            i--;
            j--;
        }
        reverse(s.begin(), s.end());
        return s;
    }
};

// Shorter version.
class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1, j = b.size() - 1, carry = 0;
        string s = "";
        while(i >= 0 || j >= 0 || carry){
            int sum = (i < 0 ? 0 : a[i--] - '0') + (j < 0 ? 0 : b[j--] - '0') + carry;
            s = to_string(sum % 2) + s;
            carry = sum / 2;
        }
        return s;
    }
};''',

    'text-justification': '''class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string>res;
        if(maxWidth == 0) return {""};
        int i = 0, j = 0;
        while(j != words.size()){
            int len = -1;
            while(j < words.size() && len + words[j].size() + 1 <= maxWidth)
                len += words[j++].size() + 1;
            int space = maxWidth - len + j - i - 1;
            int k = i;
            while(space){
                words[k++] += " ";
                space--;
                if(j != words.size() && (k == j - 1 || k == j)) k = i;
                if(j == words.size() && k == j) k = j - 1;
            }
            string line = "";
            for(int l = i; l < j; l++)
                line += words[l];
            res.push_back(line);
            i = j;
        }
        return res;
    }
};''',

    'sqrt-x': '''// Solution 1. Binary Search
class Solution {
public:
    int mySqrt(int x) {
        if(x == 0) return x;
        int lo = 1, hi = x;
        while (true) {
            int mid = lo + (hi - lo)/2;
            if (mid > x/mid) hi = mid - 1;
            else if (mid + 1 > x/(mid + 1)) return mid;
            else lo = mid + 1;
        }
    }
};

// Solution 2. Newton's Method.
/**
 *  Guess Result        Quotient                             Average Result
 *         1          2 / 1 = 2                            (2 + 1) / 2 = 1.5
 *        1.5      2 / 1.5 = 1.3333                (1.3333 + 1.5) / 2 = 1.4167
 *      1.4167    2 / 1.4167 = 1.4118          (1.4167 + 1.4118) / 2 = 1.4142
 */
class Solution {
public:
    int mySqrt(int x) {
        long r = x;
        while (r*r > x)
            r = (r + x/r) / 2;
        return r;
    }
};''',

    'climbing-stairs': '''/**
 * Idea:
 * Get to stair n has two ways:
 * 1. Stand at stair n - 1, take step = 1 forward.
 * 2. Stand at stair n - 2, take step = 2 forward.
 * So the total ways to get to the stair(n) = total ways to stair(n - 1) + total ways to stair(n - 2).
 */
class Solution {
public:
    int climbStairs(int n) {
        vector<int>dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i < n + 1; i++)
            dp[i] = dp[i - 1] + dp[i - 2];
        return dp[n];
    }
};

// Then we notice that dp[i] only concerns with dp[i - 1] and dp[i - 2], 
// so we could use two variables to replace the array, reduce space to O(1).
class Solution {
public:
    int climbStairs(int n) {
        int one = 1, two = 1, three = 1;
        for(int i = 2; i < n + 1; i++){
            three = one + two;
            one = two;
            two = three;
        }
        return three;
    }
};''',

    'simplify-path': '''class Solution {
public:
    string simplifyPath(string path) {
        string res, s;
        stack<string>stk;
        stringstream ss(path);
        while(getline(ss, s, '/')) {
            if (s == "" || s == ".") continue;
            if (s == ".." && !stk.empty()) stk.pop();
            else if (s != "..") stk.push(s);
        }
        while(!stk.empty()){
            res = "/"+ stk.top() + res;
            stk.pop();
        }
        return res.empty() ? "/" : res;
    }
};''',

    'set-matrix-zeroes': '''// Top-down
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.empty()) return;
        int m = matrix.size(), n = matrix[0].size(), col0 = 1;
        for(int i = 0; i < m; i++){
            if(!matrix[i][0]) col0 = 0;
            for(int j = 1; j < n; j++)
                if(!matrix[i][j]) matrix[0][j] = matrix[i][0] = 0;
        }
        
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++)
                if(!matrix[i][0] || !matrix[0][j]) matrix[i][j] = 0;
            if(!col0) matrix[i][0] = 0;
        }
        for(auto& x: matrix[0]) if(!matrix[0][0]) x = 0;
        if(!col0) matrix[0][0] = 0;
    }
};

// Bottom-up
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.empty()) return;
        int m = matrix.size(), n = matrix[0].size(), col0 = 1;
        for(int i = 0; i < m; i++){
            if(!matrix[i][0]) col0 = 0;
            for(int j = 1; j < n; j++)
                if(!matrix[i][j]) matrix[0][j] = matrix[i][0] = 0;
        }
        
        for(int i = m - 1; i >= 0; i--){
            for(int j = n - 1; j > 0; j--)
                if(!matrix[i][0] || !matrix[0][j]) matrix[i][j] = 0;
            if(!col0) matrix[i][0] = 0;
        }
    }
};''',

    'search-a-2d-matrix': '''// Solution 1
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()) return false;
        int lo = 0, hi = matrix.size() - 1;
        int mid = lo + (hi - lo) / 2 + 1;
        while(lo < hi){
            if(matrix[mid][0] > target) hi = mid - 1;
            else lo = mid;
            mid = lo + (hi - lo) / 2 + 1;
        }
        auto p = lower_bound(matrix[lo].begin(), matrix[lo].end(), target);
        return p != matrix[lo].end() && *p == target;
    }
};

// Solution 2
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0) return false;
        int m = matrix.size(), n = matrix[0].size(), l = 0, r = m * n - 1;
        while(l <= r){
            int mid = l + (r - l) / 2;
            int val = matrix[mid/n][mid%n];
            if(val > target) r = mid - 1;
            else if(val < target) l = mid + 1;
            else return true;
        }
        return false;
    }
};''',

    'sort-colors': '''/**
 * 1. Put '0's to the low position.
 * 2. Put '2's to the high position.
 * 3. Jump '1's.
 */
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, high = nums.size()-1;
        for(int i = 0; i <= high;)
            if(nums[i] == 0) 
                swap(nums[i++], nums[low++]);
            else if(nums[i] == 2) 
                swap(nums[i], nums[high--]);
            else i++;
    }
};

// Shorter.
class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i = 0, j = 0, k = nums.size() - 1; j <= k;)
            if(nums[j] == 0) swap(nums[i++], nums[j++]);
            else if(nums[j] == 2) swap(nums[j], nums[k--]);
            else j++;
    }
};

// Another solution.
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, two = nums.size() - 1;
        for(int i = 0; i <= two; i++){
            while(nums[i] == 2 && i < two) swap(nums[i], nums[two--]);
            while(nums[i] == 0 && zero < i) swap(nums[i], nums[zero++]);
        }
    }
};

// And here is a O(k) space, O(k*n) time solution for k colors.
class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int>color(3);
        for(int i = 0; i < 3; i++){
            if(i > 0) color[i] = color[i - 1];
            for(int j = color[i]; j < nums.size(); j++)
                while(color[i] <= j && nums[j] == i) swap(nums[j], nums[color[i]++]);
        }
    }
};''',

    'minimum-window-substring': '''class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int>m;
        int i = 0, j = 0, count = 0, minLen = INT_MAX;
        string res = "";
        for(auto x: t) m[x]++, count++;
        while(j < s.size()){
            if(m[s[j++]]-- > 0) count--;
            if(count == 0){
                while(m[s[i]] < 0) m[s[i++]]++;
                int len = j - i;
                if(len < minLen){
                    minLen = len;
                    res = s.substr(i, len);
                }
                m[s[i++]]++;
                count++;
            }
        }
        return res;
    }
};''',

    'subsets': '''class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>res;
        backtrack(nums, 0, vector<int>(), res);
        return res;
    }
    
    void backtrack(vector<int>& nums, int k, vector<int> subset, vector<vector<int>>& res){
        if(k == nums.size()){
            res.push_back(subset);
            return;
        }
        backtrack(nums, k+1, subset, res);
        subset.push_back(nums[k]);
        backtrack(nums, k+1, subset, res);
    }
};''',

    'word-search': '''// Solution 1
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(board.size() == 0|| word.size() == 0) return true;
        bool find = false;
        vector<vector<int>>visited(board.size(), vector<int>(board[0].size(),0));
        for(int i = 0 ; i < board.size(); i++)
            for(int j = 0; j < board[0].size(); j++){
                if(board[i][j] == word[0]){
                     find = backtrack(i, j, board, word, visited);
                     if(find) return find;
                }
            }
        return find;
    }
    
    bool backtrack(int i, int j, vector<vector<char>>& board, string word, vector<vector<int>>& visited){
        if(word.size() == 0) return true;
        if(i < 0 || i > board.size() - 1 || j < 0 || j > board[0].size() - 1) return false;
        if(visited[i][j]) return false;
        bool find = false;
        if(board[i][j] == word[0]){
            word.erase(word.begin());
            visited[i][j] = 1;
            find = backtrack(i-1,j,board,word,visited) || backtrack(i,j-1,board,word,visited) 
                || backtrack(i+1,j,board,word,visited) || backtrack(i,j+1,board,word,visited);
            visited[i][j] = 0;
        }
       return find;
    }
};

// Solution 2
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(board.size() == 0) return false;
        bool found = false;
        int m = board.size(), n = board[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                if(board[i][j] == word[0]) backtrack(board, 1, i, j, m, n, word, found);
                if(found) return true;
            }
        return false;
    }
    
    void backtrack(vector<vector<char>>& board, int pos, int r, int c, int m, int n, string& word, bool& found){
        if(board[r][c] == '0' || found) return;
        if(pos == word.size()){
            found = true;
            return;
        }
        char tmp = board[r][c];
        board[r][c] = '0';
        if(r - 1 >= 0 && board[r - 1][c] == word[pos]) backtrack(board, pos + 1, r - 1, c, m, n, word, found);
        if(r + 1 < m  && board[r + 1][c] == word[pos]) backtrack(board, pos + 1, r + 1, c, m, n, word, found);
        if(c + 1 < n  && board[r][c + 1] == word[pos]) backtrack(board, pos + 1, r, c + 1, m, n, word, found);
        if(c - 1 >= 0 && board[r][c - 1] == word[pos]) backtrack(board, pos + 1, r, c - 1, m, n, word, found);
        board[r][c] = tmp;
    }
};

// Solution 3.
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(board.empty()) return false;
        int m = board.size(), n = board[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(board[i][j] == word[0] && BFS(board, i, j, m, n, 0, word)) return true;
        return false;
    }
    
    bool BFS(vector<vector<char>>& board, int r, int c, int m, int n, int len, string& word){
        if(len == word.size()) return true;
        if(r < 0 || c < 0 || r >= m || c >= n || board[r][c] == '#' || board[r][c] != word[len]) return false;
        char tmp = board[r][c];
        board[r][c] = '#';
        bool found =  BFS(board, r + 1, c, m, n, len + 1, word) || BFS(board, r, c + 1, m, n, len + 1, word) ||
                      BFS(board, r - 1, c, m, n, len + 1, word) || BFS(board, r, c - 1, m, n, len + 1, word);
        board[r][c] = tmp;
        return found;
    }
};''',

    'remove-duplicates-from-sorted-array-ii': '''class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() < 3) return nums.size();
        int i = 2, j = 2;
        while(j < nums.size())
            if(nums[j] > nums[i - 2]) nums[i++] = nums[j++];
            else j++;
        return i;
    }
};''',

    'remove-duplicates-from-sorted-list-ii': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode res(0);
        res.next = head;
        ListNode* pre = &res, *cur = head, *next = cur ? cur->next : NULL;
        while(cur){
            bool dup = false;
            while(next && next->val == cur->val){
                dup = true;
                next = next->next;
            }
            if(dup){
                cur = next;
                next = next ? next->next : NULL;
                pre->next = cur;
            }
            else{
                pre = cur;
                cur = next;
                next = next ? next->next : NULL;
            }
        }
        return res.next;
    }
};''',

    'remove-duplicates-from-sorted-list': '''// Recursive
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head || !head->next) return head;
        auto p = deleteDuplicates(head->next);
        head->next = p;
        return p->val == head->val ? p : head;
    }
};

// Non-recursive
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head || !head->next) return head;
        ListNode* pre = head, *cur = head->next;
        while(cur){
            pre->val == cur->val ? pre->next = cur->next : pre = cur;
            cur = cur->next;
        }
        return head;
    }
};''',

    'maximal-rectangle': '''class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0) return 0;
        int m = matrix.size(), n = matrix[0].size(), maxArea = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(matrix[i][j] == '1') maxArea = max(maxArea, BFS(matrix, i, j));
        return maxArea;
    }
    
    int BFS(vector<vector<char>>& matrix, int r, int c){
        int row = r - 1, maxArea = 0;
        while(row >= 0 && matrix[row][c] == '1') row--;
        for(int i = c; i >= 0 && matrix[r][i] == '1'; i--){
            for(int j = row + 1; j <= r; j++)
                if(matrix[j][i] == '0') row = max(row, j);
            maxArea = max(maxArea, (r - row) * (c - i + 1));
        }
        return maxArea;
    }
};''',

    'partition-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode left(0);
        ListNode right(0);
        ListNode* l = &left;
        ListNode* r = &right;
        ListNode* cur = head;
        while(cur){
            if(cur->val < x){
                l->next = cur;
                l = l->next;
            }
            else{
                r->next = cur;
                r = r->next;
            }
            cur = cur->next;
        }
        r->next = NULL;
        l->next = right.next;
        return left.next;
    }
};''',

    'merge-sorted-array': '''class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i = m - 1, j = n - 1; j >= 0;) nums1[i + j + 1] = (i < 0 || nums1[i] < nums2[j]) ? nums2[j--] : nums1[i--];
    }
};

// longer.
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1;
        while(i + j + 1 >= 0){
            nums1[i + j + 1] = i < 0 ? nums2[j--] : j < 0 ? nums1[i--] : nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
    }
};''',

    'subsets-ii': '''// Solution 1. Brute force, 153ms.
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>>res;
        backtrack(res, nums, 0, vector<int>());
        return res;
    }
private:
    void backtrack(vector<vector<int>>& res, vector<int>& nums, int pos, vector<int>comb){
        if(pos >= nums.size()){
            for(auto x: res) if(isEqual(x, comb)) return;
            res.push_back(comb);
            return;
        }
        backtrack(res, nums, pos + 1, comb);
        comb.push_back(nums[pos]);
        backtrack(res, nums, pos + 1, comb);
    }
    
    bool isEqual(vector<int>& v1, vector<int>& v2){
        if(v1.size() != v2.size()) return false;
        unordered_map<int, int>m;
        for(auto x: v1) m[x]++;
        for(auto x: v2) if(--m[x] < 0) return false;
        return true;
    }
};

// Solution 2. Sort first, 9ms.
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>>res;
        sort(nums.begin(), nums.end());
        vector<int>comb;
        backtrack(res, nums, 0, comb);
        return res;
    }
private:
    void backtrack(vector<vector<int>>& res, vector<int>& nums, int pos, vector<int>& comb){
        res.push_back(comb);
        for(int i = pos; i < nums.size(); i++){
            if(i == pos || nums[i] != nums[i - 1]){
                comb.push_back(nums[i]);
                backtrack(res, nums, i + 1, comb);
                comb.pop_back();
            }
        }
    }
};''',

    'decode-ways': '''// My solution.
class Solution {
public:
    int numDecodings(string s) {
        /** dp[i] = 
         * value                            Example
         * 0                                00, 30, 80 - invalid ending
         * dp[i-2]                          10, 20     - valid ending with 0
         * dp[i-2]                          08, 09     - s[i - 1] == '0'      
         * dp[i-1] + dp[i-2]                11, 16     - valid ending
         * dp[i-1]                          32, 56     - large ending, decrease i by 1
         */
        if(s.size() == 0 || s[0] == '0') return 0;
        vector<int>dp(s.size());
        dp[0] = 1;
        for(int i = 1; i < s.size(); i++){
            if(s[i] == '0'){
                if(s[i - 1] == '0' || s[i - 1] - '0' > 2) return 0;
                dp[i] = (i==1) ? dp[0] : dp[i - 2];
            }
            else if(s[i - 1] == '0') dp[i] = dp[i - 2];
            else if(stoi(s.substr(i - 1, 2)) <= 26) dp[i] = (i==1) ? dp[0] + 1 : dp[i - 1] + dp[i - 2];
            else dp[i] = dp[i - 1];
        }
        return dp[s.size()-1];
    }
};

// Solution from here: https://discuss.leetcode.com/topic/7025/a-concise-dp-solution
class Solution {
public:
    int numDecodings(string s) {
        if(s.empty() || s.front() == '0') return 0;
        int p1 = 1, p2 = 1;
        for(int i = 1; i < s.size(); i++){
            if(s[i] == '0') p1 = 0;
            if(s[i - 1] == '1' || s[i - 1] == '2' && s[i] < '7'){
                p1 = p1 + p2;
                p2 = p1 - p2;
            }
            else p2 = p1;
        }
        return p1;
    }
};''',

    'reverse-linked-list-ii': '''class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode* l = new ListNode(0);
        l->next = head;
        int x = m, y = n - m;
        while(--x) l = l->next;
        ListNode* pre = l->next, *cur = pre->next, *next;
        while(y--){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        l->next->next = cur;
        l->next = pre;
        return m == 1 ? pre : head;
    }
};''',

    'binary-tree-inorder-traversal': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 // Both recursive / iterative solutions are included.
 
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>res;
        /** 
         * Recursive.
         * inorder(res, root);
         * return res;
         */
        if(!root) return res;
        stack<TreeNode*>s;
        TreeNode* cur = root;
        while(!s.empty() || cur){
            while(cur->left){
                s.push(cur);
                cur = cur->left;
            }
            res.push_back(cur->val);
            cur = cur->right ? cur->right : NULL;
            while(!cur && !s.empty()){
                res.push_back(s.top()->val);
                cur = s.top()->right ? s.top()->right : NULL;
                s.pop();
            }
        }
        return res;
    }
    
    void inorder(vector<int>& res, TreeNode* root){
        if(!root) return;
        inorder(res, root->left);
        res.push_back(root->val);
        inorder(res, root->right);
    }
};''',

    'unique-binary-search-trees-ii': '''class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if(n == 0) return {};
        return DFS(1, n);
    }
    
    vector<TreeNode*> DFS(int l, int r){
        vector<TreeNode*>res;
        if(l > r) return {NULL};
        for(int i = l; i <= r; i++){
            auto left = DFS(l, i - 1);
            auto right = DFS(i + 1, r);
            for(auto x: left)
                for(auto y: right){
                    TreeNode* root = new TreeNode(i);
                    root->left = x;
                    root->right = y;
                    res.push_back(root);
                }    
        }
        return res;
    }
};''',

    'validate-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// Solution 1. BF, O(n^2)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(!root) return true;
        if(!isValid(root->left, root->val, true) || !isValid(root->right, root->val, false)) return false;
        return isValidBST(root->left) && isValidBST(root->right);
    }
    
    bool isValid(TreeNode* root, int bound, bool isLeft){
        return !root || (isLeft ? root->val < bound : root->val > bound ) && isValid(root->left, bound, isLeft) && isValid(root->right, bound, isLeft);
    }
};

// Solution 2. D & C, O(n)
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValid(root, NULL, NULL);
    }
    
    bool isValid(TreeNode* root, TreeNode* minNode, TreeNode* maxNode){
        if(!root) return true;
        if(minNode && root->val <= minNode->val || maxNode && root->val >= maxNode->val) return false;
        return isValid(root->left, minNode, root) && isValid(root->right, root, maxNode);
    }
};

// Solution 3. In-order, recursive, O(n).
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* pre = NULL;
        return isValid(root, pre);
    }
    
    bool isValid(TreeNode* root, TreeNode* &pre){
        if(!root) return true;
        if(!isValid(root->left, pre)) return false;
        if(pre && root->val <= pre->val) return false;
        pre = root;
        return isValid(root->right, pre);
    }
};

// Solution 4. In-order, iterative, O(n).
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*>s;
        TreeNode* pre = NULL;
        while(root || !s.empty()){
            while(root){
                s.push(root);
                root = root->left;
            }
            root = s.top();
            s.pop();
            if(pre && root->val <= pre->val) return false;
            pre = root;
            root = root->right;
        }
        return true;
    }
};''',

    'recover-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* pre = NULL, *one = NULL, *two = NULL;
        DFS(root, pre, one, two);
        swap(one->val, two->val);
    }
    
    void DFS(TreeNode* cur, TreeNode* &pre, TreeNode* &one, TreeNode* &two){
        if(!cur) return;
        DFS(cur->left, pre, one, two);
        if(pre && cur->val < pre->val){
            if(!one) one = pre;
            two = cur;
        }
        pre = cur;
        DFS(cur->right, pre, one, two);
    }
};''',

    'same-tree': '''// DFS
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p || !q) {
            return !p && !q;
        }
        if (p->val != q->val) {
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// BFS
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*>pq, qq;
        pq.push(p);
        qq.push(q);
        while(!pq.empty() && !qq.empty()) {
            auto a = pq.front();
            pq.pop();
            auto b = qq.front();
            qq.pop();
            if (!a || !b) {
                if (!a && !b) {
                    continue;
                } else {
                    return false;
                }
            }
            
            if (a->val != b->val) {
                return false;
            }
            
            pq.push(a->left);
            pq.push(a->right);
            
            qq.push(b->left);
            qq.push(b->right);
        }
        return true;
    }
};''',

    'symmetric-tree': '''// Recursive
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        vector<vector<TreeNode*>>v;
        dfs(root, v, 0);
        return check(v);
    }
    
    void dfs(TreeNode* root, vector<vector<TreeNode*>>& v, int level){
        if(level == v.size()) v.push_back({});
        v[level].push_back(root);
        if(!root) return;
        dfs(root->left, v, level + 1);
        dfs(root->right, v, level + 1);
    }
    
    bool check(vector<vector<TreeNode*>>& v){
        for(auto x: v){
            int l = 0, r = x.size() - 1;
            while(l < r){
                auto a = x[l++];
                auto b = x[r--];
                if((!a || !b) && (a || b) || (a && b) && (a->val != b->val)) return false;
            }
        }
        return true;
    }
};

// Iterative
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        vector<vector<TreeNode*>>v;
        queue<TreeNode*>cur, next;
        cur.push(root);
        int level = 0;
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop();
            if(v.size() == level) v.push_back({});
            v[level].push_back(p);
            if(p){
                next.push(p->left);
                next.push(p->right);
            }
            if(cur.empty()){
                level++;
                swap(cur, next);
            }
        }
        return check(v);
    }
    
    bool check(vector<vector<TreeNode*>>& v){
        for(auto x: v){
            int l = 0, r = x.size() - 1;
            while(l < r){
                auto a = x[l++];
                auto b = x[r--];
                if((!a || !b) && (a || b) || (a && b) && (a->val != b->val)) return false;
            }
        }
        return true;
    }
};''',

    'binary-tree-level-order-traversal': '''// Solution 1. BFS
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(!root) return res;
        deque<TreeNode*>cur;
        deque<TreeNode*>next;
        cur.push_back(root);
        int level = 0;
        res.push_back(vector<int>());
        while(!cur.empty()){
            TreeNode* node = cur.front();
            cur.pop_front();
            if(node->left) next.push_back(node->left);
            if(node->right) next.push_back(node->right);
            res[level].push_back(node->val);
            if(cur.empty() && !next.empty()){
                res.push_back(vector<int>());
                level++;
                swap(cur, next);
            }
        }
        return res;
    }
};

// Solution 2. DFS
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>res;
        DFS(res, root, 0);
        return res;
    }
    
    void DFS(vector<vector<int>>& res, TreeNode* root, int level){
        if(!root) return;
        if(level == res.size()) res.push_back(vector<int>());
        res[level].push_back(root->val);
        DFS(res, root->left, level + 1);
        DFS(res, root->right, level + 1);
    }
};''',

    'binary-tree-zigzag-level-order-traversal': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(!root) return res;
        deque<TreeNode*>cur, next;
        cur.push_back(root);
        vector<int>v;
        int level = 0;
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            v.push_back(p->val);
            if(p->left) next.push_back(p->left);
            if(p->right) next.push_back(p->right);
            if(cur.empty()){
                if(level++ % 2) reverse(v.begin(), v.end());
                res.push_back(v);
                v.clear();
                swap(cur, next);
            }
        }
        return res;
    }
};''',

    'maximum-depth-of-binary-tree': '''/**
* Definition for a binary tree node.
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
* };
*/
class Solution {
public:
	int maxDepth(TreeNode* root) {
		if (!root) return 0;
		return max(maxDepth(root->left), maxDepth(root->right)) + 1;
	}
};''',

    'construct-binary-tree-from-preorder-and-inorder-traversal': '''// First version:
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 0) return NULL;
        TreeNode* root = new TreeNode(preorder[0]);
        //Find root in inorder 
        int i = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        //preorder and inorder for each left and right subtree
        vector<int>inorderLeft(inorder.begin(), inorder.begin() + i);
        vector<int>inorderRight(inorder.begin() + i + 1, inorder.end());
        vector<int>preorderLeft(preorder.begin() + 1, preorder.begin() + 1 + i);
        vector<int>preorderRight(preorder.begin() + 1 + i, preorder.end());
        //Build tree
        root->left = buildTree(preorderLeft, inorderLeft);
        root->right = buildTree(preorderRight, inorderRight);
        return root;
    }
};

// Then I realized I don't need so much extra memory, and reduced run time from 62ms to 19ms.
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    
    TreeNode* helper(vector<int>& preorder, int pStart, int pEnd, vector<int>& inorder, int iStart, int iEnd) {
        if(pStart > pEnd) return NULL;
        TreeNode* root = new TreeNode(preorder[pStart]);
        int i = find(inorder.begin(), inorder.end(), preorder[pStart]) - inorder.begin();
        root->left = helper(preorder, pStart + 1, pStart + i - iStart, inorder, iStart, i - 1);
        root->right = helper(preorder, pStart + i - iStart + 1, pEnd, inorder, i + 1, iEnd);
        return root;
    }
};

// And it can be faster using unordered_map to store the indices first. Run time: from 19ms to 9ms.
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int>m;
        for(int i = 0; i < inorder.size(); i++) m[inorder[i]] = i;
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, m);
    }
    
    TreeNode* helper(vector<int>& preorder, int pStart, int pEnd, vector<int>& inorder, int iStart, int iEnd, unordered_map<int, int>& m) {
        if(pStart > pEnd) return NULL;
        TreeNode* root = new TreeNode(preorder[pStart]);
        int i = m[preorder[pStart]];
        root->left = helper(preorder, pStart + 1, pStart + i - iStart, inorder, iStart, i - 1, m);
        root->right = helper(preorder, pStart + i - iStart + 1, pEnd, inorder, i + 1, iEnd, m);
        return root;
    }
};''',

    'binary-tree-level-order-traversal-ii': '''class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>>v;
        dfs(root, v, 0);
        reverse(v.begin(), v.end());
        return v;
    }
    
    void dfs(TreeNode* root, vector<vector<int>>& v, int level){
        if(!root) return;
        if(level == v.size()) v.push_back({});
        v[level].push_back(root->val);
        dfs(root->left, v, level + 1);
        dfs(root->right, v, level + 1);
    }
};''',

    'convert-sorted-array-to-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.empty()) return NULL;
        TreeNode* root = new TreeNode(nums[nums.size() / 2]);
        vector<int>left(nums.begin(), nums.begin() + nums.size() / 2);
        vector<int>right(nums.begin() + nums.size() / 2 + 1, nums.end());
        root->left = sortedArrayToBST(left);
        root->right = sortedArrayToBST(right);
        return root;
    }
};''',

    'convert-sorted-list-to-binary-search-tree': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if(!head) return NULL;
        if(!head->next) return new TreeNode(head->val);
        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* pre = new ListNode(0);
        pre->next = slow;
        // Root is the mid position of the linked list
        while(fast){
            slow = slow->next;
            pre = pre->next;
            fast = fast->next ? fast->next->next : NULL;
        }
        TreeNode* root = new TreeNode(slow->val);
        pre->next = NULL;
        // Call recursively to left and right part of linked list
        root->left = sortedListToBST(head);
        root->right = sortedListToBST(slow->next);
        return root;
    }
};''',

    'balanced-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        bool res = true;
        dfs(root, res);
        return res;
    }
    
    int dfs(TreeNode* root, bool& res){
        if(!root) return 0;
        int l = dfs(root->left, res);
        int r = dfs(root->right, res);
        if(abs(l - r) > 1) res = false;
        return max(l, r) + 1;
    }
};''',

    'minimum-depth-of-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int l = minDepth(root->left);
        int r = minDepth(root->right);
        return root->left && root->right ? min(l, r) + 1 : l + r + 1;
    }
};''',

    'path-sum': '''class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        sum -= root->val;
        if(!sum && !root->left && !root->right) return true;
        return hasPathSum(root->left, sum) || hasPathSum(root->right, sum);
    }
};''',

    'path-sum-ii': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>>res;
        if(!root) return res;
        DFS(root, res, vector<int>(), 0, sum);
        return res;
    }
    
    void DFS(TreeNode* root, vector<vector<int>>& res, vector<int>path, int sum, int target){
        if(!root) return;
        path.push_back(root->val);
        sum += root->val;
        if(!root->left && !root->right){
            if(sum == target) res.push_back(path);
            return;
        }
        DFS(root->left, res, path, sum, target);
        DFS(root->right, res, path, sum, target);
    }
};''',

    'flatten-binary-tree-to-linked-list': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Recursive
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* l, *r;
        DFS(root, l, r);
    }
    
    TreeNode* DFS(TreeNode* root, TreeNode* l, TreeNode* r){
        if(!root) return NULL;
        l = DFS(root->left, l, r);
        if(l){
            l->right = root->right;
            root->right = root->left;
            root->left = NULL;
        }
        r = DFS(root->right, l, r);
        return r ? r : l ? l : root;
    }
};

// Iterative
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* p;
        while(root){
            if(root->left && root->right){
                p = root->left;
                while(p->right) p = p->right;
                p->right = root->right;
            }
            if(root->left) root->right = root->left;
            root->left = NULL;
            root = root->right;
        }
    }
};''',

    'populating-next-right-pointers-in-each-node': '''/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */

// Solution 1. Works for any knid of tree, O(n) space.
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        deque<TreeLinkNode*>cur;
        deque<TreeLinkNode*>next;
        cur.push_back(root);
        while(!cur.empty()){
            TreeLinkNode* node = cur.front();
            cur.pop_front();
            node->next = cur.empty() ? NULL : cur.front();
            if(node->left) next.push_back(node->left);
            if(node->right) next.push_back(node->right);
            if(cur.empty()) swap(cur, next);
        }
    }
};

// Solution 2. O(1) space.
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode* cur(root), *next;
        while(cur){
            next = cur->left;
            while(cur){
                if(cur->left){
                    cur->left->next = cur->right;
                    cur->right->next = cur->next ? cur->next->left : NULL;
                }
                cur = cur->next;
            }
            cur = next;
        }
    }
};''',

    'populating-next-right-pointers-in-each-node-ii': '''/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
 
// Solution 1. Works for any kind of tree, O(n) space. 
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        deque<TreeLinkNode*>cur;
        deque<TreeLinkNode*>next;
        cur.push_back(root);
        while(!cur.empty()){
            TreeLinkNode* node = cur.front();
            cur.pop_front();
            node->next = cur.empty() ? NULL : cur.front();
            if(node->left) next.push_back(node->left);
            if(node->right) next.push_back(node->right);
            if(cur.empty()) swap(cur, next);
        }
    }
};

// Solution 2. O(1) space.
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode head(0);
        TreeLinkNode* pre = &head, *cur;
        pre->next = root;
        while(pre->next){
            cur = pre->next;
            while(cur){
                if(cur->left){
                    pre->next = cur->left;
                    pre = pre->next;
                }
                if(cur->right){
                    pre->next = cur->right;
                    pre = pre->next;
                }
                cur = cur->next;
            }
            pre->next = NULL;
            pre = &head;
        }
    }
};''',

    'pascal-s-triangle': '''class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if(numRows == 0) return {};
        if(numRows == 1) return {{1}};
        auto v = generate(numRows - 1);
        auto lastRow = *(v.end() - 1);
        vector<int>res(1, 1);
        for(int i = 0; i < lastRow.size() - 1; i++) res.push_back(lastRow[i] + lastRow[i + 1]);
        res.push_back(1);
        v.push_back(res);
        return v;
    }
};''',

    'pascal-s-triangle-ii': '''class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex == 0) return {1};
        auto v = getRow(rowIndex - 1);
        int n = v.size();
        for(int i = 1; i < n; i++)
            v[i] = (i <= n/2) ? v[i] + v[n - i] : v[n - i];
        v.push_back(1);
        return v;
    }
};''',

    'triangle': '''// Bottom-up
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int>dp(n + 1);
        for(int i = n - 1; i >= 0; i--)
            for(int j = 0; j <= i; j++)
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
        return dp[0];
    }
};

// Top-down
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int>dp(n);
        for(int i = 0; i < n; i++){
            if(i != 0) dp[i] = dp[i - 1] + triangle[i][i];
            for(int j = i - 1; j > 0; j--)
                dp[j] = triangle[i][j] + min(dp[j], dp[j - 1]);
            dp[0] = dp[0] + triangle[i][0];
        }
        return *min_element(dp.begin(), dp.end());
    }
};''',

    'best-time-to-buy-and-sell-stock': '''/**Solution 1.
 * Use one array to record the last bought stock with min price at day `i`,  
 * use another array to record the max profit at day `i`.
 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) return 0;
        vector<int>buy(prices.size());
        vector<int>dp(prices.size());
        buy[0] = prices[0];
        dp[0] = 0;
        for(int i = 1; i < prices.size(); i++){
            buy[i] = min(buy[i - 1], prices[i]);
            dp[i] = max(dp[i - 1], prices[i] - buy[i - 1]);
        }
        return dp[prices.size() - 1];
    }
};

/**Solution 2.
 * But you may noticed that we only concern the relationship between day `i` and day `i - 1`, 
 * therefore, we can simply use two integers to replace the two arrays, reduced space complexity to O(1).
 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) return 0;
        int buy = prices[0], profit = 0;
        for(int i = 1; i < prices.size(); i++){
            buy = min(buy, prices[i]);
            profit = max(profit, prices[i] - buy);
        }
        return profit;
    }
};''',

    'binary-tree-maximum-path-sum': '''class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        DFS(root, maxSum);
        return maxSum;
    }
    
    int DFS(TreeNode* root, int& maxSum){
        if(!root) return 0;
        int left = max(0, DFS(root->left, maxSum));
        int right = max(0, DFS(root->right, maxSum));
        maxSum = max(maxSum, left + right + root->val);
        return max(left, right) + root->val;
    }
};''',

    'valid-palindrome': '''class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            while(i < j && !isalnum(s[i])) i++;
            while(i < j && !isalnum(s[j])) j--;
            if(tolower(s[i++]) != tolower(s[j--])) return false;
        }
        return true;
    }
};''',

    'word-ladder': '''class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        deque<string>cur;
        deque<string>next;
        cur.push_back(beginWord);
        int len = 2;
        while(!cur.empty()){
            string node = cur.front();
            cur.pop_front();
            for(auto& x: wordList){
                if(x == "" || !isNeighbor(node, x)) continue;
                if(x == endWord) return len;
                next.push_back(x);
                x = "";
            }
            if(cur.empty()){
                len++;
                swap(cur, next);
            }
        }
        return 0;
    }
    
    bool isNeighbor(string& a, string& b){
        int diff = 0;
        for(int i = 0; i < a.size(); i++) if(a[i] != b[i] && ++diff > 1) return false;
        return diff == 1;
    }
};

// Two-end.
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if(find(wordList.begin(), wordList.end(), endWord) == wordList.end()) return 0;
        unordered_set<string>visited0, visited1, *v0(&visited0), *v1(&visited1);
        deque<string>cur0, next0, cur1, next1, *cur, *next;
        cur0.push_back(beginWord);
        cur1.push_back(endWord);
        visited0.insert(beginWord);
        visited1.insert(endWord);
        int len = 2;
        bool b = true;
        while(!cur0.empty() && !cur1.empty()){
            cur = b ? &cur0 : &cur1;
            next = b ? &next0 : &next1;
            string node = cur->front();
            cur->pop_front();
            for(auto& x: wordList){
                if(v0->count(x) || !isNeighbor(node, x)) continue;
                if(v1->count(x)) return len;
                v0->insert(x);
                next->push_back(x);
            }
            if(cur->empty()){
                len++;
                swap(*cur, *next);
                swap(v0, v1);
                b = !b;
            }
        }
        return 0;
    }
    
    bool isNeighbor(string& a, string& b){
        int diff = 0;
        for(int i = 0; i < a.size(); i++) if(a[i] != b[i] && ++diff > 1) return false;
        return diff == 1;
    }
};''',

    'longest-consecutive-sequence': '''class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int maxlen = 0;
        unordered_map<int, int>m;
        for(auto x: nums){
            if(m[x]) continue;
            int left = m[x - 1];
            int right = m[x + 1];
            m[x + right] = m[x - left] = m[x] = left + right + 1;
            maxlen = max(maxlen, m[x]);
        }
        return maxlen;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int>m;
        int res = 0;
        for (int& x: nums) {
            if (m[x]) {
                continue;
            }
            int l = m[x - 1];
            int r = m[x + 1];
            m[x] = l + r + 1;
            m[x - l] = l + r + 1;
            m[x + r] = l + r + 1;
            res = max(res, m[x]);
        }
        return res;
    }
};''',

    'sum-root-to-leaf-numbers': '''// DFS
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(!root) return 0;
        int res = 0;
        dfs(root, res, 0);
        return res;
    }
    
    void dfs(TreeNode* root, int& res, int num){
        num = num * 10 + root->val;
        if(root->left) dfs(root->left, res, num);
        if(root->right) dfs(root->right, res, num);
        if(!root->left && !root->right) res += num;
    }
};

// BFS
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(!root) return 0;
        int res = 0;
        queue<pair<TreeNode*, int>>q;
        q.push({root, 0});
        while(!q.empty()){
            auto p = q.front();
            q.pop();
            int num = p.second * 10 + p.first->val;
            if(p.first->left) q.push({p.first->left, num});
            if(p.first->right) q.push({p.first->right, num});
            if(!p.first->left && !p.first->right) res += num;
        }
        return res;
    }
};''',

    'surrounded-regions': '''class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if(board.empty()) return;
        int m = board.size(), n = board[0].size();
        vector<vector<int>>visited(m, vector<int>(n, 0));
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                if(visited[i][j] || board[i][j] == 'X') continue;
                bool surrounded = DFS(board, visited, i, j, m, n);
                if(surrounded) replace(board, i, j, m, n);
            }
    }
    
    bool DFS(vector<vector<char>>& board, vector<vector<int>>& visited, int r, int c, int m, int n){
        if(r < 0 || r == m || c < 0 || c == n) return false;
        if(board[r][c] == 'X' || visited[r][c]) return true;
        visited[r][c] = 1;
        bool L = DFS(board, visited, r, c - 1, m, n);
        bool R = DFS(board, visited, r, c + 1, m, n); 
        bool U = DFS(board, visited, r - 1, c, m, n); 
        bool D = DFS(board, visited, r + 1, c, m, n); 
        return L && R && U && D;
    }
    
    void replace(vector<vector<char>>& board, int r, int c, int m, int n){
        if(r < 0 || r == m || c < 0 || c == n || board[r][c] == 'X') return;
        board[r][c] = 'X';
        replace(board, r + 1, c, m, n);
        replace(board, r - 1, c, m, n);
        replace(board, r, c + 1, m, n);
        replace(board, r, c - 1, m, n);
    }
};''',

    'palindrome-partitioning': '''class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>>res;
        vector<string>v;
        dfs(s, 0, v, res);
        return res;
    }
    
    void dfs(string s, int pos, vector<string>& v, vector<vector<string>>& res){
        if(pos >= s.size()){
            res.push_back(v);
            return;
        }
        
        for(int i = pos; i < s.size(); i++){
            int l = pos, r = i;
            bool b = true;
            while(l < r && b) if(s[l++] != s[r--]) b = false;
            if(b){
                v.push_back(s.substr(pos, i - pos + 1));
                dfs(s, i + 1, v, res);
                v.pop_back();
            }
        }
    }
};''',

    'clone-graph': '''/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
// DFS
class Solution {
private:
    unordered_map<UndirectedGraphNode*, UndirectedGraphNode*>m;
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if(!node) return NULL;
        if(m.count(node) == 0){
            m[node] = new UndirectedGraphNode(node->label);
            for(auto x: node->neighbors) m[node]->neighbors.push_back(cloneGraph(x));
        }
        return m[node];
    }
};

// BFS
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if(!node) return NULL;
        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*>m;
        UndirectedGraphNode* root = new UndirectedGraphNode(node->label);
        m[node] = root;
        deque<UndirectedGraphNode*>cur;
        deque<UndirectedGraphNode*>next;
        cur.push_back(node);
        while(!cur.empty()){
            UndirectedGraphNode* p = cur.front();
            cur.pop_front();
            for(auto x: p->neighbors){
                if(m.count(x) == 0){
                    UndirectedGraphNode* copy = new UndirectedGraphNode(x->label);
                    m[x] = copy;
                    next.push_back(x);
                }
                m[p]->neighbors.push_back(m[x]);
            }
            if(cur.empty()) swap(cur, next);
        }
        return root;
    }
};''',

    'gas-station': '''class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n(gas.size()), sum(0), total(0), res(0);
        for (int i = 0; i < n; ++i) {
            sum += gas[i] - cost[i];
            if (sum < 0) {
                res = i + 1;
                sum = 0;
            }
            total += gas[i] - cost[i];
        }
        return total >= 0 ? res : -1;
    }
};''',

    'single-number': '''class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for(auto& x: nums) res ^= x;
        return res;
    }
};''',

    'copy-list-with-random-pointer': '''/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        unordered_map<RandomListNode*, RandomListNode*>m;
        auto p = head;
        while(p){
            m[p] = new RandomListNode(p->label);
            p = p->next;
        }
        p = head;
        while(p){
            m[p]->next = m[p->next];
            m[p]->random = m[p->random];
            p = p->next;
        }
        return m[head];
    }
};''',

    'word-break': '''class Solution {
private:
    unordered_map<string, int>m;
    unordered_map<string, bool>dp;
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        for(auto x: wordDict) m[x]++;
        return DFS(s);
    }
    
    bool DFS(string s){
        if(dp.count(s)) return dp[s];
        if(s.empty()) return true;
        bool found = false;
        for(int i = 1; i <= s.size() && !found; i++)
            if(m.count(s.substr(0, i))) found |= DFS(s.substr(i));
        dp[s] = found;
        return found;
    }
};''',

    'linked-list-cycle': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        auto one = head, two = head;
        while(two && two->next){
            one = one->next;
            two = two->next->next;
            if(one == two) return true;
        }
        return false;
    }
};''',

    'linked-list-cycle-ii': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        auto one = head, two = head, meet = head;
        while(two && two->next){
            one = one->next;
            two = two->next->next;
            if(one == two){
                meet = one;
                break;
            }
        }
        if(!two || !two->next) return NULL;
        auto p = head;
        while(p != meet){
            p = p->next;
            meet = meet->next;
        }
        return p;
    }
};''',

    'reorder-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head) return;
        ListNode* slow = head, *fast = head;
        ListNode* pre = new ListNode(0);
        pre->next = slow;
        while(fast && fast->next){
            pre = pre->next;
            slow = slow->next;
            fast = fast->next->next;
        }
        if(fast) slow = slow->next, pre = pre->next;
        pre->next = NULL;
        ListNode* cur, *next;
        pre = NULL, cur = slow;
        while(cur){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        ListNode* h1 = head, *h2 = pre, *p1, *p2;
        while(h1 && h2){
            p1 = h1->next;
            p2 = h2->next;
            h1->next = h2;
            h2->next = p1;
            h1 = p1;
            h2 = p2;
        }
    }
};''',

    'binary-tree-preorder-traversal': '''class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int>res;
        stack<TreeNode*>s;
        auto p = root;
        while(p || !s.empty()){
            if(!p) p = s.top(), s.pop();
            res.push_back(p->val);
            if(p->right) s.push(p->right);
            p = p->left;
        }
        return res;
    }
};''',

    'binary-tree-postorder-traversal': '''// Iterative
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int>res;
        stack<TreeNode*>s;
        while(!s.empty() || root){
            if(root){
                s.push(root->left);
                res.push_back(root->val);
                root = root->right;
            }
            else{
                root = s.top();
                s.pop();
            }
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

// Recursive
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int>res;
        DFS(root, res);
        return res;
    }
    
    void DFS(TreeNode* root, vector<int>& res){
        if(!root) return;
        DFS(root->left, res);
        DFS(root->right, res);
        res.push_back(root->val);
    }
};''',

    'lru-cache': '''class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if(!m.count(key) || m[key] == -1) return -1;
        q.push_back(key);
        visited[key]++;
        return m[key];
    }
    
    void put(int key, int value) {
        if(!m.count(key)|| m[key] == -1) count++;
        else visited[key]++;
        if(count > capacity){
            while(visited[q.front()]) visited[q.front()]--, q.pop_front();
            m[q.front()] = -1;
            q.pop_front();
            count--;
        }
        q.push_back(key);
        m[key] = value;
    }

private:
    unordered_map<int, int>m;
    unordered_map<int, int>visited;
    deque<int>q;
    int count = 0;
    int capacity = 0;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */''',

    'reverse-words-in-a-string': '''// O(1) space.
class Solution {
public:
    void reverseWords(string &s) {
        // Reverse string
        reverse(s.begin(), s.end());
        // Reverse every word
        int i = 0, j = 0;
        while(i != s.size()){
            while(j < s.size() && s[j] != ' ') j++;
            reverse(s.begin() + i, s.begin() + j);
            i = j;
            while(i < s.size() && s[i] == ' ') i++, j++;
        }
        // Remove extra ' '
        i = 0, j = 0;
        while(j < s.size()){
            bool new_word = false;
            while(j < s.size() && s[j] == ' '){
                new_word = true;
                j++;
            }
            if(j == s.size()) break;
            if(new_word && i > 0) s[i++] = ' ';
            s[i++] = s[j++];
        }
        s = s.substr(0, i);
    }
};

// O(n) space.
class Solution {
public:
    void reverseWords(string &s) {
        string res = "";
        string word = "";
        int j = 0;
        for(int i = 0; i < s.size(); i++){
            while(s[i] == ' ') i++;
            j = i;
            while(s[j] != ' ') j++;
            word = s.substr(i, j - i);
            if(res != "" && word != "") word += " ";
            res = word + res;
            i = j;
        }
        s = res;
    }
};''',

    'min-stack': '''class MinStack {
private:
    stack<int>s;
    stack<int>min;
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int x) {
        s.push(x);
        if(min.empty() || x <= min.top()) min.push(x);
    }
    
    void pop() {
        if(s.top() == min.top()) min.pop();
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */''',

    'read-n-characters-given-read4': '''// Forward declaration of the read4 API.
int read4(char *buf);

// Solution 1.
class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int sum = 0;
        for(int i = 0; i < n; i += 4){
            sum += read4(buf);
            buf += 4;
        }
        return min(sum, n);
    }
};

// Solution 2.
class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int sum = 0, i = 4;
        while(sum < n && i == 4){
            i = read4(buf);
            buf += 4;
            sum += i;
        }
        return min(sum, n);
    }
};

// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int count = 0;
        while (n) {
            int x = read4(buf);
            count += min(x, n);
            n = max(0, n - x);
            buf += x;
            if (x < 4) {
                break;
            }
        }
        return count;
    }
};''',

    'read-n-characters-given-read4-ii-call-multiple-times': '''// Forward declaration of the read4 API.
int read4(char *buf);

// Solution 1.
class Solution {
private:
    int ptr = 0;
    char* tmp = new char[4];
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int cnt = 0;
        int k;
        while(cnt < n){
            if(ptr == 0) k = read4(tmp);
            if(k == 0) break;
            while(cnt < n && ptr < k){
                buf[cnt++] = tmp[ptr++];
            }
            if(ptr == k) ptr = 0;
        }
        return cnt;
    }
};

// Solution 2.
class Solution {
private:
    int p = 4;
    int i = 4;
    char tmp[4];
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int sum = 0;
        while(sum < n){
            if(p == i){
                i = read4(tmp);
                p = 0;
            }
            if(i == 0) break;
            *buf++ = tmp[p++];
            sum++;
        }
        return sum;
    }
};

// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int count = 0;
        while (n) {
            if (p == cnt) {
                cnt = read4(tmp);
                p = 0;
            }
            if (cnt == 0) {
                break;
            }
            *buf++ = tmp[p++];
            ++count;
            --n;
        }
        return count;
    }
    
private:
    int p = 4;
    int cnt = 4;
    char tmp[4];
};''',

    'longest-substring-with-at-most-two-distinct-characters': '''class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int maxlen = 0, i = 0, j = 0, next = 0;
        unordered_set<char>set;
        while(j < s.size()){
            j = i;
            while(j < s.size()){
                if(set.size() == 1) next = j;
                set.insert(s[j]);
                if(set.size() > 2){
                    maxlen = max(maxlen, j - i);
                    i = next;
                    set.clear();
                    break;
                }
                j++;
            }
        }
        maxlen = max(maxlen, j - i);
        return maxlen;
    }
};''',

    'one-edit-distance': '''class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int diff = abs((int)s.size() - (int)t.size());
        if(diff > 1) return false;
        int distance = 0;
        if(diff == 0){
            for(int i = 0; i < s.size(); i++) if(s[i] != t[i]) distance++;
        }
        else{
            int i = 0, j = 0;
            while(i < s.size() && j < t.size()){
                if(s[i] != t[j]){
                    s.size() > t.size() ? i++ : j++;
                    distance++;
                }
                else i++, j++;
            }
            if(i != s.size() || j != t.size()) distance++;
        }
        return distance == 1;
    }
};''',

    'find-peak-element': '''class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() == 1) {
            return 0;
        }
        int n = nums.size();
        
        if (nums[n - 2] < nums[n - 1]) {
            return n - 1;
        } else if (nums[1] < nums[0]) {
            return 0;
        }
        
        int l = 1, r = n - 2, mid;
        while (l <= r) {
            mid = l + (r - l)/2;
            if (nums[mid - 1] > nums[mid]) {
                r = mid - 1;
            } else if (nums[mid + 1] > nums[mid]) {
                l = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};''',

    'missing-ranges': '''class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string>res;
        if(nums.empty()){
            res.push_back((lower == upper) ? to_string(lower) : to_string(lower) + "->" + to_string(upper));
            return res;
        }
        int cur = lower;
        for(int i = 0; i < nums.size(); i++){
            if(i > 0 && nums[i] == nums[i - 1]) continue;
            string s = "";
            if(nums[i] > cur) s += to_string(cur++);
            if(nums[i] > cur) s += "->" + to_string(nums[i] - 1);
            cur = nums[i] + 1;
            if(!s.empty()) res.push_back(s);
        }
        if(nums.back() == upper - 1) res.push_back(to_string(upper));
        else if(nums.back() < upper) res.push_back(to_string(nums.back() + 1) + "->" + to_string(upper));
        return res;
    }
};''',

    'excel-sheet-column-title': '''class Solution {
public:
    string convertToTitle(int n) {
        string res;
        char c;
        while(n){
            c = 'A' + (n - 1) % 26;
            res = c + res;
            n = (n - 1) / 26;
        }
        return res;
    }
};

// Or
class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        while(n){
            res.push_back('A' + (n - 1)%26);
            n = (n - 1) / 26;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};''',

    'majority-element': '''// Solution 1
// Space: O(n)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int>m;
        for(auto x: nums) if(++m[x] > nums.size()/2) return x;
    }
};

// Solution 2
// [Boyer-Moore Majority Vote algorithm](https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html). 
// Space: O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        for(auto x: nums){
            if(count == 0) candidate = x;
            if(candidate == x) count++;
            else count--;
        }
        return candidate;
    }
};''',

    'excel-sheet-column-number': '''class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        for(auto c: s){
            res *= 26;
            res += c - 'A' + 1;
        }
        return res;
    }
};''',

    'binary-search-tree-iterator': '''/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// Solution 1. O(n) space.
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        load(s, root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }

    /** @return the next smallest number */
    int next() {
        int n = s.top();
        s.pop();
        return n;
    }
    
private:
    stack<int>s;
    
    void load(stack<int>& s, TreeNode* root){
        if(!root) return;
        load(s, root->right);
        s.push(root->val);
        load(s, root->left);
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
 
// Solution 2. O(h) space.
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        load(s, root);
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* node = s.top();
        s.pop();
        if(node->right) load(s, node->right);
        return node->val;
    }
    
private:
    stack<TreeNode*>s;
    
    void load(stack<TreeNode*>& s, TreeNode* root){
        if(!root) return;
        s.push(root);
        load(s, root->left);
    }
};''',

    'reverse-words-in-a-string-ii': '''class Solution {
public:
    void reverseWords(vector<char>& str) {
        for(int i = 0; i < str.size(); i++){
            int j = i + 1;
            while(j < str.size() && str[j] != ' ') j++;
            int a = i, b = j - 1;
            while(a < b) swap(str[a++], str[b--]);
            i = j;
        }
        reverse(str.begin(), str.end());
    }
};''',

    'number-of-1-bits': '''class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            if(n & 1) count++;
            n >>= 1;
        }
        return count;
    }
};''',

    'house-robber': '''class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n < 2) return n ? nums[0] : 0;
        vector<int>dp(n);
        dp[0] = nums[0], dp[1] = max(nums[0], nums[1]);
        for(int i = 2; i < n; i++)
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);
        return dp[n - 1];
    }
};''',

    'number-of-islands': '''class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        int res = 0, m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++res;
                    dfs(grid, i, j, m, n);
                }
            }
        }
        return res;
    }
    
    void dfs(vector<vector<char>>& grid, int r, int c, int& m, int& n) {
        if (r < 0 || c < 0 || r == m || c == n || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0';
        dfs(grid, r + 1, c, m, n);
        dfs(grid, r - 1, c, m, n);
        dfs(grid, r, c - 1, m, n);
        dfs(grid, r, c + 1, m, n);
    }
};''',

    'isomorphic-strings': '''class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char>ms, mt;
        for (int i = 0; i < s.size(); ++i) {
            if (ms.count(s[i]) && mt.count(t[i])) {
                if (ms[s[i]] != t[i]) {
                    return false;
                }
            } else if (ms.count(s[i]) || mt.count(t[i])) {
                return false;
            } else {
                ms[s[i]] = t[i];
                mt[t[i]] = s[i];
            }
        }
        return true;
    }
};''',

    'reverse-linked-list': '''// Iterative
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre(NULL), *cur(head), *next;
        while(cur){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
};

// Recursive
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* node = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return node;
    }
};''',

    'course-schedule': '''class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int>indegree(numCourses);
        vector<vector<int>>graph(numCourses);
        for(auto p: prerequisites){
            graph[p.second].push_back(p.first);
            indegree[p.first]++;
        }
        for(int i = 0; i < numCourses; i++){
            int j = 0;
            for(; j < numCourses; j++) if(indegree[j] == 0) break;
            if(j == numCourses) return false;
            indegree[j] = -1;
            for(auto x: graph[j]) indegree[x]--;
        }
        return true;
    }
};''',

    'implement-trie-prefix-tree': '''// Solution 1
// My cheat solution, it's not a tree, but maybe the shortest solution of all.
class Trie {
private:
    unordered_set<string>s;
public:
    Trie() {}
    
    void insert(string word) {
        s.insert(word);
    }
    
    bool search(string word) {
        return s.count(word);
    }
    
    bool startsWith(string prefix) {
        for(auto x: s){
            if(x.size() < prefix.size()) continue;
            int i = 0;
            while(i < prefix.size() && x[i] == prefix[i]) i++;
            if(i == prefix.size()) return true; 
        }
        return false;
    }
};

// Solution 2
// Normal solution.
struct TrieNode{
    bool isWord;
    vector<TrieNode*>next;
    TrieNode():isWord(false){
        next = vector<TrieNode*>(26, NULL);
    }
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* node = root;
        for(auto c: word){
            if(!node->next[c - 'a']) node->next[c - 'a'] = new TrieNode();
            node = node->next[c - 'a'];
        }
        node->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* node = find(word);
        return node && node->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* node = find(prefix);
        return node;
    }
private:
    TrieNode* root;
    
    TrieNode* find(string s){
        TrieNode* node = root;
        for(auto c: s){
            if(!node->next[c - 'a']) return NULL;
            node = node->next[c - 'a'];
        }
        return node;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */''',

    'minimum-size-subarray-sum': '''// Solution 1.
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int i = 0, j = 0, sum = 0, len = nums.size();
        while(j < nums.size()){
            while(j < nums.size() && sum < s) sum += nums[j++];
            if(i == 0 && sum < s) return 0;
            while(sum - nums[i]>= s) sum -= nums[i++];
            len = min(len, j - i);
            sum -= nums[i++];
        }
        return len;
    }
};

// Solution 2.
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int i = 0, j = 0, len = INT_MAX, sum = 0;
        while(j < nums.size()){
            sum += nums[j++];
            while(sum >= s){
                len = min(len, j - i);
                sum -= nums[i++];
            }
        }
        return len == INT_MAX ? 0 : len;
    }
};''',

    'course-schedule-ii': '''class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int>res;
        vector<int>indegree(numCourses);
        vector<vector<int>>graph(numCourses);
        for(auto p: prerequisites){
            graph[p.second].push_back(p.first);
            indegree[p.first]++;
        }
        for(int i = 0; i < numCourses; i++){
            int j = 0;
            for(; j < numCourses; j++) if(indegree[j] == 0) break;
            if(j == numCourses) return vector<int>();
            indegree[j] = -1;
            for(auto x: graph[j]) indegree[x]--;
            res.push_back(j);
        }
        return res;
    }
};''',

    'add-and-search-word-data-structure-design': '''// Solution 1. Hash Table, 62ms, 100%.
class WordDictionary {
public:
    WordDictionary() {}
    
    void addWord(string word) {
        words[word.size()].push_back(word);
    }
    
    bool search(string word) {
        for(auto s: words[word.size()]) if(isEqual(s, word)) return true;
        return false;
    }
    
private:
    unordered_map<int, vector<string>>words;
    
    bool isEqual(string a, string b){
        for(int i = 0; i < a.size(); i++){
            if(b[i] == '.') continue;
            if(a[i] != b[i]) return false;
        }
        return true;
    }
};

// Solution 2. Trie, 88ms.
struct TrieNode{
    bool isKey;
    TrieNode* next[26];
    TrieNode():isKey(false){
        memset(next, NULL, sizeof(next));
    }
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for(auto c: word){
            if(!node->next[c - 'a']) node->next[c - 'a'] = new TrieNode();
            node = node->next[c - 'a'];
        }
        node->isKey = true;
    }
    
    bool search(string word) {
        return helper(word, root);
    }

private:
    TrieNode* root;
    
    bool helper(string word, TrieNode* node){
        for(int i = 0; i < word.size(); i++){
            char c = word[i];
            if(c != '.'){
                if(!node->next[c - 'a']) return false;
                node = node->next[c - 'a'];
            }
            else{
                bool found = false;
                int j = 0;
                for(; j < 26; j++){
                    if(node->next[j]) found |= helper(word.substr(i + 1), node->next[j]);
                    if(found) return true;
                }
                if(j == 26) return false;
            }
        }
        return node->isKey;
    }
};''',

    'word-search-ii': '''// Solution 1
// Brute force
// Runime: 462 ms

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string>res;
        unordered_map<char, vector<string>>m;
        for(auto x: words) m[x[0]].push_back(x);
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[0].size(); j++)
                if(m[board[i][j]].size() > 0)
                    for(auto x: m[board[i][j]]){
                        bool found = false;
                        backtrack(board, 1, i, j, board.size(), board[0].size(), x, found);
                        if(found && find(res.begin(), res.end(), x) == res.end()) res.push_back(x);
                    } 
        return res;
    }
    
    void backtrack(vector<vector<char>>& board, int pos, int r, int c, int m, int n, string& word, bool& found){
        if(board[r][c] == '0' || found) return;
        if(pos == word.size()){
            found = true;
            return;
        }
        char tmp = board[r][c];
        board[r][c] = '0';
        if(r - 1 >= 0 && board[r - 1][c] == word[pos]) backtrack(board, pos + 1, r - 1, c, m, n, word, found);
        if(r + 1 < m  && board[r + 1][c] == word[pos]) backtrack(board, pos + 1, r + 1, c, m, n, word, found);
        if(c + 1 < n  && board[r][c + 1] == word[pos]) backtrack(board, pos + 1, r, c + 1, m, n, word, found);
        if(c - 1 >= 0 && board[r][c - 1] == word[pos]) backtrack(board, pos + 1, r, c - 1, m, n, word, found);
        board[r][c] = tmp;
    }
};

// Solution 2
// Add Trie, inspired by Trie implementation in this [thread](https://discuss.leetcode.com/topic/13463/maybe-the-code-is-not-too-much-by-using-next-26-c).
// Runtime: 35 ms. (Beats 95.58% of C++ solutions.)

struct TrieNode{
    string word;
    TrieNode* next[26];
};

class Solution {
private:
    TrieNode* root;
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string>res;
        buildTrie(words);
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[0].size(); j++)
                backtrack(board, res, i, j, board.size() - 1, board[0].size() - 1, root);
        return res;
    }
    
    void backtrack(vector<vector<char>>& board, vector<string>& res, int r, int c, int m, int n, TrieNode* p){
        if(r < 0 || c < 0 || r > m || c > n || board[r][c] == '0'|| !p->next[board[r][c] - 'a']) return;
        p = p->next[board[r][c] - 'a'];
        if(p->word.size() > 0){
            res.push_back(p->word);
            p->word = "";
        }
        char tmp = board[r][c];
        board[r][c] = '0';
        backtrack(board, res, r - 1, c, m, n, p);
        backtrack(board, res, r + 1, c, m, n, p);
        backtrack(board, res, r, c + 1, m, n, p);
        backtrack(board, res, r, c - 1, m, n, p);
        board[r][c] = tmp;
    }
    
    void buildTrie(vector<string>& words){
        root = new TrieNode();
        for(auto x: words){
            TrieNode* p = root;
            for(auto c: x){
                if(!p->next[c - 'a']) p->next[c - 'a'] = new TrieNode();
                p = p->next[c - 'a'];
            }
            p->word = x;
        }
    }
};''',

    'shortest-palindrome': '''class Solution {
public:
    string shortestPalindrome(string s) {
        string r = s;
        reverse(r.begin(), r.end());
        int i = 0, j = s.size();
        while(r.substr(i, j) != s.substr(0, j)) i++, j--;
        return r.substr(0, i) + s;
    }
};''',

    'kth-largest-element-in-an-array': '''// Solution 1. Sort, O(nlogn).
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), greater<int>());
        return nums[k - 1];
    }
};

// Solution 2. Partition, O(n).
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        k = nums.size() - k;
        int lo = 0, hi = nums.size() - 1;
        while(lo < hi){
            int p = partition(nums, lo, hi);
            if(p == k) break;
            if(p < k) lo = p + 1;
            else hi = p - 1;
        }
        return nums[k];
    }
    
private:
    int partition(vector<int>& nums, int lo, int hi){
        int pivot = nums[hi];    
        int i = lo;
        for(int j = lo; j < hi; j++)
            if(nums[j] <= pivot) swap(nums[i++], nums[j]);
        swap(nums[i], nums[hi]);
        return i;
    }
};


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int pos = partition(nums, n - 1);
        int target = n - k;
        if (pos == target) {
            return nums[pos];
        } else if (pos < target) {
            vector<int>r(nums.begin() + pos + 1, nums.end());
            return findKthLargest(r, k);
        } else {
            vector<int>l(nums.begin(), nums.begin() + pos);
            return findKthLargest(l, k - (n - pos));
        }
    }
    
     int partition(vector<int>& nums, int end) {
         int i = 0, j = 0;
         while (j != end) {
             if (nums[j] < nums[end]) {
                 swap(nums[i], nums[j]);
                 ++i;
             }
             ++j;
         }
         swap(nums[i], nums[end]);
         return i;
     }
};

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int target = n - k;
        int l = 0, r = n - 1;
        while (l <= r) {
            int p = partition(nums, l, r);
            if (p == target) {
                return nums[p];
            } else if (p < target) {
                l = p + 1;
            } else {
                r = p - 1;
            }
        }
    }
    
     int partition(vector<int>& nums, int l, int r) {
         int i = 0, j = 0;
         while (j != r) {
             if (nums[j] <= nums[r]) {
                 swap(nums[i], nums[j]);
                 ++i;
             }
             ++j;
         }
         swap(nums[i], nums[r]);
         return i;
     }
};''',

    'maximal-square': '''// See detailed explanation in discuss.
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return 0;
        int maxSquare = 0;
        for(int i = 0; i < matrix.size(); i++)
            for(int j = 0; j < matrix[0].size(); j++)
                if(matrix[i][j] != '0') maxSquare = max(maxSquare, findSquare(matrix, i, j));
        return maxSquare;
    }
    
    int findSquare(vector<vector<char>>& matrix, int r, int c){
        int row = r - 1;
        int col = c - 1;
        while(row >= 0 && col >= 0 && matrix[r][col] == '1' && matrix[row][c] == '1'){
            int i = row;
            int j = col;
            while(i < r && matrix[i][col] == '1') i++;
            while(j < c && matrix[row][j] == '1') j++;
            if(i != r || j != c) break;
            row--;
            col--;
        }
        return pow(r - row, 2);
    }
};''',

    'rectangle-area': '''class Solution {
public:
	int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
		int areaA = (C - A) * (D - B);
		int areaB = (G - E) * (H - F);
		if (C < E || A > G || B > H || D < F) return areaA + areaB;
		// Bottom left(I, J), Top right(K, L).
		int I = max(A, E);
		int J = max(B, F);
		int K = min(C, G);
		int L = min(D, H);
		int overlap = (K - I) * (L - J);
		return areaA + areaB - overlap;
	}
};''',

    'basic-calculator': '''class Solution {
public:
    int calculate(string s) {
        stack<int>stk, op;
        int res = 0, sign = 1;
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            if(isdigit(c)){
                int num = c - '0';
                while(i + 1 < s.size() && isdigit(s[i + 1])){
                    num = num * 10 + s[i + 1] - '0';
                    i++;
                }
                res += num * sign;
            }
            else if(c == '+') sign = 1;
            else if(c == '-') sign = -1;
            else if(c == '('){
                stk.push(res);
                op.push(sign);
                res = 0;
                sign = 1;
            }
            else if(c == ')'){
                res = res * op.top();
                op.pop();
                res += stk.top();
                stk.pop();
            }
        }
        return res;
    }
};''',

    'invert-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
// Solution 1. Recursive
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;
        invertTree(root->left);
        invertTree(root->right);
        swap(root->left, root->right);
        return root;
    }
};

// Solution 2. Iterative
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        stack<TreeNode*>s;
        TreeNode* p = root;
        while(!s.empty() || p){
            while(p){
                s.push(p);
                p = p->left;
            }
            while(!s.empty() && !p){
                p = s.top()->right;
                swap(s.top()->left, s.top()->right);
                s.pop();
            }
        }
        return root;
    }
};''',

    'basic-calculator-ii': '''// Lambda
class Solution {
private:
    unordered_map<char, function<int(int,int)>>m {{'+', [](int a, int b){ return a + b ;}},
                                                  {'-', [](int a, int b){ return a - b ;}},
                                                  {'*', [](int a, int b){ return a * b ;}},
                                                  {'/', [](int a, int b){ return a / b ;}}};
public:
    int calculate(string s) {
        stringstream ss("+" + s + "+");
        int sum(0), temp(0), num(0);
        char op;
        while(ss >> op){
            ss >> num;
            if(op == '+' || op == '-'){
                sum += temp;
                temp = m[op](0, num);
            }
            else temp = m[op](temp, num);
        }
        return sum;
    }
};

// Or
class Solution {
public:
    int calculate(string s) {
        stringstream ss('+' + s + '+');
        int temp = 0, num = 0, sum = 0;
        char op = ' ';
        while(ss >> op){
            ss >> num;
            if(op == '+'){
                sum += temp;
                temp = num;
            }
            if(op == '-'){
                sum += temp;
                temp = -num;
            }
            if(op == '*')
                temp *= num;
            if(op == '/')
                temp /= num;
        }
        return sum;
    }
};

// Using stack
class Solution {
public:
    int calculate(string s) {
        s += '+';
        stack<int>stk;
        int tmp = 0;
        char op = '+';
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            if(c == ' ') continue;
            if(isdigit(c)) tmp = tmp*10 + c - '0';
            if(!isdigit(c)){
                if(op == '+')
                    stk.push(tmp);
                else if(op == '-')
                    stk.push(-tmp);
                else if(op == '*'){
                    int n = stk.top();
                    stk.pop();
                    stk.push(n*tmp);
                }
                else if(op == '/'){
                    int n = stk.top();
                    stk.pop();
                    stk.push(n/tmp);
                }
                op = c;
                tmp = 0;
            }
        }
        int res = 0;
        while(!stk.empty()) res += stk.top(), stk.pop();
        return res;
    }
};''',

    'summary-ranges': '''class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string>res;
        for(int i = 0, j = 1; i < nums.size(); i = j, j = i + 1){
            while(j < nums.size() && nums[j] == nums[j - 1] + 1) j++;
            res.push_back((j == i + 1) ? to_string(nums[i]) : to_string(nums[i]) + "->" + to_string(nums[j - 1]));
        }
        return res;
    }
};''',

    'majority-element-ii': '''// Solution 1
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int>res;
        int c1 = 0, c2 = 0, count1 = 0, count2 = 0;
        for (int& x: nums) {
            if (x == c1) {
                ++count1;
            } else if (x == c2) {
                ++count2;
            } else if (count1 == 0) {
                c1 = x;
                ++count1;
            } else if (count2 == 0) {
                c2 = x;
                ++count2;
            } else {
                --count1;
                --count2;
            }
        }
        count1 = 0;
        count2 = 0;
        for (int& x: nums) {
            if (x == c1) {
                ++count1;
            } else if (x == c2) {
                ++count2;
            }
        }
        if (count1 > n / 3) {
            res.push_back(c1);
        }
        if (count2 > n / 3) {
            res.push_back(c2);
        }
        return res;
    }
};

// Solution 2
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int candidate1(0), candidate2(0), count1(0), count2(0);
        for(auto x: nums){
            if(count1 == 0 && x != candidate2) candidate1 = x;
            if(count2 == 0 && x != candidate1) candidate2 = x;
            if(x == candidate1) count1++;
            if(x == candidate2) count2++;
            if(x != candidate1 && x != candidate2) count1--, count2--;
        }
        int check1(0), check2(0);
        for(auto x: nums){
            if(x == candidate1) check1++;
            else if(x == candidate2) check2++;
        }
        if(check1 > nums.size()/3 && check2 > nums.size()/3) return {candidate1, candidate2};
        if(check1 > nums.size()/3) return {candidate1};
        if(check2 > nums.size()/3) return {candidate2};
        return vector<int>();
    }
};''',

    'kth-smallest-element-in-a-bst': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// Solution 1
class Solution {
public:
    int DFS(TreeNode* root, int k, int& val, bool& found){
       if(!root || found) return 0;
       int left = DFS(root->left, k, val, found) + 1;
       int right = DFS(root->right, k - left, val, found) + 1;
       if(k == left) val = root->val, found = true;
       return left + right - 1;
    }
    
    int kthSmallest(TreeNode* root, int k) {
        int val = 0;
        bool found = false;
        DFS(root, k, val, found);
        return val;
    }
};

// Solution 2
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<int>s;
        reversedInOrder(root, s);
        while(--k) s.pop();
        return s.top();
    }
    
    void reversedInOrder(TreeNode* root, stack<int>& s){
        if(!root) return;
        reversedInOrder(root->right, s);
        s.push(root->val);
        reversedInOrder(root->left, s);
    }
};''',

    'power-of-two': '''class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && !(n & (n - 1));
    }
};''',

    'palindrome-linked-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head || !head->next) return true;
        ListNode* slow(head), *fast(head);
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        if(fast) slow = slow->next; // if odd, move one step forward
        // Reverse second half
        ListNode* pre(NULL), *cur(slow), *next;
        while(cur){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        // Compare first half with reversed second half
        while(pre){
            if(pre->val != head->val) return false;
            pre = pre->next;
            head = head->next;
        }
        return true;
    }
};''',

    'lowest-common-ancestor-of-a-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// Solution 1.
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int Min = min(p->val, q->val);
        int Max = max(p->val, q->val);
        if(root->val <= Max && root->val >= Min) return root;
        if(root->val > Max) return lowestCommonAncestor(root->left, p, q);
        return lowestCommonAncestor(root->right, p, q);
    }
};

// Solution 2.
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root || root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        return left ? right ? root : left : right;
    }
};''',

    'lowest-common-ancestor-of-a-binary-tree': '''/**
* Definition for a binary tree node.
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
* };
*/
// Solution 1. Brute force, T(n) = T(n/2) + O(n); Time complexity : O(n)
class Solution {
public:
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		if (!root || root == p || root == q) return root;
		bool foundP = found(root->left, p);
		bool foundQ = found(root->right, q);
		if (foundP && foundQ || !foundP && !foundQ) return root;
		if (foundP) return lowestCommonAncestor(root->left, p, q);
		return lowestCommonAncestor(root->right, p, q);
	}

	bool found(TreeNode* root, TreeNode* target) {
		if (!root) return false;
		if (root == target) return true;
		return found(root->left, target) || found(root->right, target);
	}
};

// Solution 2. T(n) = 2T(n/2), Time complexity: O(n)
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        return left ? right ? root : left : right;
    }
};''',

    'product-of-array-except-self': '''class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>res(nums.size(), 1);
        for(int i = 1; i < nums.size(); i++)
            res[i] = res[i-1] * nums[i-1];
        int right = 1;
        for(int i = nums.size() - 1; i >= 0; i--){
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
};''',

    'sliding-window-maximum': '''class Solution {
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		vector<int>res;
		if (nums.size() == 0) return res;
		int start = 0;
		int end = k - 1;
		int maxIndex = findMax(nums, start, end);
		for (; end < nums.size(); start++, end++) {
			if (nums[end] > nums[maxIndex]) maxIndex = end;
			if (start > maxIndex) maxIndex = findMax(nums, start, end);
			res.push_back(nums[maxIndex]);
		}
		return res;
	}

	int findMax(vector<int>& nums, int start, int end) {
		int maxIndex = start;
		for (int i = start + 1; i <= end; i++)
			if (nums[i] > nums[maxIndex]) maxIndex = i;
		return maxIndex;
	}
};''',

    'search-a-2d-matrix-ii': '''// Solution 1. Binary Search, 103 ms.
// Do binary seach on **first** column to get a row position - `lo`, rows **after** `lo` won't contain the target value because rows are sorted.
// Do binary seach on **last** column to get a row position - `hi`, rows **before** `hi` won't contain the target value because rows are sorted.
// Do binary search on rows between `lo` and `hi`.
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        int lo = BS(matrix, 0, target), hi = BS(matrix, matrix[0].size() - 1, target);
        for(int i = min(lo, hi); i <= max(lo, hi); i++){
            auto it = lower_bound(matrix[i].begin(), matrix[i].end(), target);
            if(it != matrix[i].end() && *it == target) return true;
        }
        return false;
    }
    
    int BS(vector<vector<int>>& matrix, int col, int target){
        int lo = 0, hi = matrix.size() - 1, mid = lo + (hi - lo) / 2;
        while(lo <= hi){
            if(matrix[mid][col] > target) hi = mid - 1;
            else lo = mid + 1;
            mid = lo + (hi - lo) / 2;
        }
        return max(0, hi);
    }
};

// Solution 2. Start at top-right position and go left or go down, 59 ms.
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0) return false;
        int r = 0, c = matrix[0].size() - 1;
        while(r < matrix.size() && c >= 0){
            if(matrix[r][c] == target) return true;
            matrix[r][c] > target ? c-- : r++;
        }
        return false;
    }
};''',

    'shortest-word-distance-ii': '''class WordDistance {
public:
    WordDistance(vector<string> words) {
        for(int i = 0; i < words.size(); i++) m[words[i]].push_back(i);
    }
    
    int shortest(string word1, string word2) {
        auto v1 = m[word1];
        auto v2 = m[word2];
        int res = INT_MAX;
        while(!v1.empty() && !v2.empty()){
            res = min(res, abs(v1.back() - v2.back()));
            v1.back() > v2.back() ? v1.pop_back() : v2.pop_back();
        }
        return res;
    }

private:
    unordered_map<string, vector<int>>m;
};''',

    'strobogrammatic-number': '''class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char>m{{'6', '9'}, {'9', '6'}, {'1', '1'}, {'0', '0'}, {'8', '8'}};
        string s = "";
        for(auto x: num)
            if(!m.count(x)) return false;
            else s.push_back(m[x]);
        reverse(s.begin(), s.end());
        return s == num;
    }
};''',

    'strobogrammatic-number-ii': '''class Solution {
public:
    vector<string> findStrobogrammatic(int n) {
        return helper(n, n);
    }
    
    vector<string> helper(int m, int n){
        if(m == 0) return {""};
        if(m == 1) return {"0", "1", "8"};
        vector<string>v = helper(m - 2, n);
        vector<string>res;
        for(auto x: v){
            if(m != n) res.push_back('0' + x + '0');
            res.push_back('6' + x + '9');
            res.push_back('9' + x + '6');
            res.push_back('1' + x + '1');
            res.push_back('8' + x + '8');
        }
        return res;
    }
};''',

    'group-shifted-strings': '''class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        vector<vector<string>>res;
        for(int i = 0; i < strings.size(); i++){
            if(strings[i].empty()) continue;
            vector<string>vec({strings[i]});
            for(int j = i + 1; j < strings.size(); j++)
                if(isSameGroup(strings[i], strings[j])){
                    vec.push_back(strings[j]);
                    strings[j] = "";
                }
            res.push_back(vec);
        }
        return res;
    }
    
    bool isSameGroup(string a, string b){
        if(a.empty() || b.empty() || a.size() != b.size()) return false;
        int d = b[0] - a[0];
        d = d < 0 ? d + 26 : d;
        for(int i = 0; i < a.size(); i++)
            if(b[i] - 'a' != (a[i] - 'a' + d) % 26) return false;
        return true;
    }
};

// Update 26/11/18
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        vector<vector<string>>res;
        unordered_map<string, vector<string>>m;
        for (auto& s: strings) {
            m[helper(s)].push_back(s);
        }
        for (auto& v: m) {
            res.push_back(v.second);
        }
        return res;
    }
    
    string helper(string s) {
        if (s.size() <= 1) {
            return "a";
        }
        int diff = s[0] - 'a';
        string res;
        for (auto c: s) {
            if (c - diff < 'a') {
                c = c + (26 - diff);
            } else {
                c = c - diff;
            }
            res.push_back(c);
        }
        return res;
    }
};''',

    'flatten-2d-vector': '''class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        for(int i = 0; i < vec2d.size(); i++) q.push_back(vec2d[i].begin()), end.push_back(vec2d[i].end());
    }

    int next() {
        return *q.front()++;;
    }

    bool hasNext() {
        while(!q.empty() && (q.front() == end.front())) q.pop_front(), end.pop_front();
        return !q.empty();
    }

private:
    deque<vector<int>::iterator>q;
    deque<vector<int>::iterator>end;
};''',

    'meeting-rooms': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
// Solution 1.
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        if(intervals.empty()) return true;
        sort(intervals.begin(), intervals.end(),[](Interval& a,Interval& b){ return a.start < b.start; });
        for(int i = 0; i < intervals.size() - 1; i++) if(intervals[i].end > intervals[i + 1].start) return false;
        return true;
    }
};

// Solution 2.
class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        map<int, int>m;
        for(auto x: intervals) m[x.start]++, m[x.end]--;
        int sum = 0;
        for(auto x: m) if((sum += x.second) > 1) return false;
        return true;
    }
};''',

    'meeting-rooms-ii': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
// Solution 1.
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if(intervals.size() == 0) return 0;
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){ return a.start < b.start;});
        priority_queue<int, vector<int>, greater<int>>pq;
        pq.push(intervals[0].end);
        int room = 1;
        for(int i = 1; i < intervals.size(); i++){
            if(intervals[i].start < pq.top()) room++;
            else pq.pop();
            pq.push(intervals[i].end);
        }
        return room;
    }
};

// Solution 2.
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int>m;
        int room = 0, maxRoom = 0;
        for(auto x: intervals) m[x.start]++, m[x.end]--;
        for(auto x: m) room += x.second, maxRoom = max(maxRoom, room);
        return maxRoom;
    }
};

// Solution 3.
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int res = 0;
        sort(intervals.begin(), intervals.end(), [](Interval& a, Interval& b) {
            return a.start < b.start;
        });
        auto comp = [](Interval& a, Interval& b) {
            return a.end > b.end;
        };
        priority_queue<Interval, vector<Interval>, decltype(comp)>pq(comp);
        for (auto& i: intervals) {
            if (pq.empty() || pq.top().end > i.start) {
                ++res;
            } else {
                pq.pop();
            }
            pq.push(i);
        }
        return res;
    }
};''',

    'verify-preorder-sequence-in-binary-search-tree': '''class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        return dfs(preorder, 0, preorder.size(), INT_MIN, INT_MAX);
    }
    
    bool dfs(vector<int>& preorder, int l, int r, int minVal, int maxVal){
        if(l >= r) return true;
        int root = preorder[l], mid = r;
        for(int i = l; i < r; i++)
            if(preorder[i] < minVal || preorder[i] > maxVal) return false;
            else if(preorder[i] > root && mid == r) mid = i;
        return dfs(preorder, l + 1, mid, minVal, root) && dfs(preorder, mid, r, root, maxVal);
    }
};''',

    'binary-tree-paths': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// DFS
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string>res;
        if(!root) return res;
        DFS(root, res, "");
        return res;
    }
    
    void DFS(TreeNode* root, vector<string>& res, string path){
        path += to_string(root->val);
        if(root->left || root->right) path += "->";
        else{
            res.push_back(path);
            return;
        }
        if(root->left) DFS(root->left, res, path);
        if(root->right) DFS(root->right, res, path);
    }
};

// BFS
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string>res;
        if(!root) return res;
        deque<pair<TreeNode*, string>>cur;
        deque<pair<TreeNode*, string>>next;
        cur.push_back(make_pair(root, ""));
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            p.second += to_string(p.first->val);
            if(p.first->left || p.first->right) p.second += "->";
            else res.push_back(p.second);
            if(p.first->left) next.push_back(make_pair(p.first->left, p.second));
            if(p.first->right) next.push_back(make_pair(p.first->right, p.second));
            if(cur.empty()) swap(cur, next);
        }
        return res;
    }
};''',

    'add-digits': '''class Solution {
public:
    int addDigits(int num) {
        return num%9 ? num%9 : num ? 9 : 0; 
    }
};''',

    '3sum-smaller': '''class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        int count = 0;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++)
            for(int lo = i + 1, hi = nums.size() - 1; lo < hi; count += hi - lo++)
                while(lo < hi && nums[i] + nums[lo] + nums[hi] >= target) hi--;
        return count;
    }
};''',

    'graph-valid-tree': '''// Solution 1. DFS
class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        vector<vector<int>>graph(n);
        for(auto x: edges){
            graph[x.first].push_back(x.second);
            graph[x.second].push_back(x.first);
        }
        vector<int>visited(n);
        if(findCircle(graph, visited, -1, 0)) return false;
        for(auto x: visited) if(!x) return false;
        return true;
    }
    
    bool findCircle(vector<vector<int>>& graph, vector<int>& visited, int from, int node){
        if(visited[node]) return true;
        visited[node] = 1;
        bool circle = false;
        for(auto x: graph[node])
            if(x != from){
                circle |= findCircle(graph, visited, node, x);
                if(circle) return true;
            }
        return false;
    }
};

// Solution 2. Union Find
class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        if(edges.size() != n - 1) return false;
        vector<int>root(n, 0);
        for(int i = 0; i < n; i++) root[i] = i;
        for(int i = 0; i < edges.size(); i++){
            int x = edges[i].first;
            int y = edges[i].second;
            while(root[x] != x) x = root[x];
            while(root[y] != y) y = root[y];
            if(x == y) return false;
            root[y] = x;
        }
        return true;
    }
};''',

    'ugly-number': '''class Solution {
public:
    bool isUgly(int num) {
        return num ? !(num%2) ? isUgly(num/2) : !(num%3) ? isUgly(num/3) : !(num%5) ? isUgly(num/5) : num == 1 : false;
    }
};''',

    'ugly-number-ii': '''class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int>dp(n);
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for(int i = 1; i < n; i++){
            dp[i] = min(dp[p2] * 2, min(dp[p3] * 3, dp[p5] * 5));
            if(dp[i] == dp[p2] * 2) p2++;
            if(dp[i] == dp[p3] * 3) p3++;
            if(dp[i] == dp[p5] * 5) p5++;
        }
        return dp[n - 1];
    }
};''',

    'palindrome-permutation': '''class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int>m;
        int odd = 0;
        for(auto c: s) (m[c]++ % 2) ? odd-- : odd++;
        return odd <= 1;
    }
};''',

    'palindrome-permutation-ii': '''class Solution {
public:
    vector<string> generatePalindromes(string s) {
        vector<int>v(128);
        unordered_set<char>m;
        int odd = 0;
        for(auto c: s){
            ++v[c] % 2 ? odd++ : odd--;
            m.insert(c);
        }
        if(odd > 1) return {};
        vector<string> res;
        dfs(v, res, "", "", s.size(), m);
        return res;
    }
    
    void dfs(vector<int>& v, vector<string>& res, string a, string b, int remain, unordered_set<char>& m){
        if(remain == 0){
            reverse(b.begin(), b.end());
            res.push_back(a + b);
        }
        else if(remain == 1){
            for(auto i: m) if(v[i]) a.push_back(i);
            dfs(v, res, a, b, 0, m);
        }
        else{
            for(auto i: m){
                if(v[i] >= 2){
                    a.push_back(i);
                    b.push_back(i);
                    v[i] -= 2;
                    dfs(v, res, a, b, remain - 2, m);
                    v[i] += 2;
                    a.pop_back();
                    b.pop_back();
                }
            }
        }
    }
};''',

    'missing-number': '''class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = 0, i = 0;
        for(auto& x: nums) res ^= ++i ^ x;
        return res;
    }
};

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = 0, n = nums.size();
        for (int& x: nums) {
            sum += x;
        }
        return (1 + n) * n/2 - sum;
    }
};

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1, mid;
        while (l <= r) {
            mid = l + (r - l)/2;
            if (nums[mid] > mid) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};''',

    'alien-dictionary': '''class Solution {
public:
    string alienOrder(vector<string>& words) {
        if(words.empty()) return 0;
        unordered_map<char, unordered_set<char>>graph;
        unordered_map<char, int>degree;
        for(auto x: words) for(auto c: x) degree[c] = 0;
        for(int i = 0; i < words.size() - 1; i++){
            string a = words[i], b = words[i + 1];
            for(int j = 0; j < min(a.size(), b.size()); j++){
                if(a[j] == b[j]) continue;
                if(!graph[a[j]].count(b[j])){
                    graph[a[j]].insert(b[j]);
                    degree[b[j]]++;
                }
                break;
            }
        }
        string res = "";
        while(true){
            char c = '#';
            for(auto x: degree)
                if(x.second == 0) c = x.first;
            if(c == '#') break;
            degree[c] = -1;
            for(auto neigh: graph[c])
                degree[neigh]--;
            res += c;
        }
        if(res.size() != degree.size()) return "";
        return res;
    }
};''',

    'closest-binary-search-tree-value': '''class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        double minDiff = abs(root->val - target);
        int res = root->val;
        DFS(root, target, res, minDiff);
        return res;
    }
    
    void DFS(TreeNode* root, double target, int& res, double& minDiff){
        if(!root) return;
        if(abs(root->val - target) < minDiff) minDiff = abs(root->val - target), res = root->val;
        target > root->val ? DFS(root->right, target, res, minDiff) : DFS(root->left, target, res, minDiff);
    }
};''',

    'encode-and-decode-strings': '''class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res = "";
        for(auto s: strs)
            res += to_string(s.size()) + '#' + s;
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string>res;
        for(int i = 0; i < s.size();){
            int j = i;
            while(isdigit(s[j])) j++;
            int len = stoi(s.substr(i, j - i));
            res.push_back(s.substr(j + 1, len));
            i = j + len + 1;
        }
        return res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));''',

    'closest-binary-search-tree-value-ii': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        vector<int>res;
        priority_queue<pair<double, int>>pq;
        DFS(root, target, k, pq);
        while(!pq.empty()) res.push_back(pq.top().second), pq.pop();
        return res;
    }
    
    void DFS(TreeNode* root, double target, int k, priority_queue<pair<double, int>>& pq){
        if(!root) return;
        pq.push({abs(root->val - target), root->val});
        if(pq.size() > k) pq.pop();
        DFS(root->left, target, k, pq);
        DFS(root->right, target, k, pq);
    }
};''',

    'integer-to-english-words': '''class Solution { 
public:
    string numberToWords(int num) {
        if(num == 0) return "Zero";
        vector<string>thousands({"", " Thousand", " Million", " Billion"});
        string res = "";
        int i = 0;
        while(num){
            if(num % 1000) res = helper(num % 1000) + thousands[i] + (res.size() ? " " : "") + res;
            num /= 1000;
            i++;
        }
        return res;
    }
    
    string helper(int num){
        vector<string>lessThan20({"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"});
        vector<string>tens({"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"});
        if(num >= 100) return lessThan20[num / 100] + " Hundred" + (num % 100 ? " ": "") + helper(num % 100);
        else if(num >= 20) return tens[num / 10] + (num % 10 ? " ": "") + helper(num % 10);
        else return lessThan20[num];
    }
};''',

    'h-index': '''// Solution 1.
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int i = 0, j = citations.size() - 1;
        while(j >= 0 && citations[j] > i) i++, j--;
        return i;
    }
};

// Solution 2.
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int>buckets(n + 1);
        for(auto x: citations) x >= n ? buckets[n]++ : buckets[x]++;
        int count = 0;
        for(int i = n; i >= 0; i--){
            count += buckets[i];
            if(count >= i) return i;
        }
        return 0;
    }
};''',

    'h-index-ii': '''// O(n)
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int i = 0, j = citations.size() - 1;
        while(j >= 0 && citations[j] > i) i++, j--;
        return i;
    }
};

// Binary Search, O(logn)
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int lo = 0, len = citations.size(), hi = len - 1;
        int mid = lo + (hi - lo) / 2;
        while(lo <= hi){
            if(citations[mid] >= len - mid) hi = mid - 1;
            else lo = mid + 1;
            mid = lo + (hi - lo) / 2;
        }
        return len - lo;
    }
};''',

    'paint-fence': '''class Solution {
public:
    int numWays(int n, int k) {
        vector<int>dp(n + 1);
        dp[0] = 0, dp[1] = k, dp[2] = k * k;
        for(int i = 3; i <= n; i++) dp[i] = (dp[i - 2] + dp[i - 1]) * (k - 1);
        return dp[n];
    }
};''',

    'find-the-celebrity': '''// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        int i = 0, j = 1;
        while(j < n){
            if(knows(i, j)) i = j;
            j++;
        }
        for(int k = 0; k < n; k++){
            if(k == i) continue;
            if(!knows(k, i) || knows(i, k)){
                i = -1;
                break;
            }
        }
        return i;
    }
};''',

    'first-bad-version': '''// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
       int lower = 1, upper = n;
       while(lower < upper)
           if(isBadVersion(lower + (upper - lower)/2)) upper = lower + (upper - lower)/2;
           else lower = lower + (upper - lower)/2 + 1;
       return lower;
    }
};''',

    'perfect-squares': '''// Non-static DP, 89ms.
class Solution {
public:
    int numSquares(int n) {
        vector<int>dp(n + 1, INT_MAX);
        dp[0] = 0;
        for(int i = 1; i <= n; i++)
            for(int j = 1; j * j <= i; j++)
                dp[i] = min(dp[i], dp[i - j * j] + 1);
        return dp[n];
    }
};

// Static DP, 6ms.
class Solution {
public:
    int numSquares(int n) {
        static vector<int>dp(1, 0);
        for(int i = dp.size(); i <= n; i++){
            dp.push_back(INT_MAX);
            for(int j = 1; j * j <= i; j++)
                dp[i] = min(dp[i], dp[i - j * j] + 1);
        }
        return dp[n];
    }
};''',

    'wiggle-sort': '''class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++)
            if(i % 2 && nums[i - 1] > nums[i] || !(i % 2) && nums[i - 1] < nums[i]) swap(nums[i], nums[i - 1]);
    }
};''',

    'zigzag-iterator': '''class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        it1 = v1.begin();
        it2 = v2.begin();
        end1 = v1.end();
        end2 = v2.end();
    }

    int next() {
        if(it1 == end1) return *it2++;
        if(it2 == end2) return *it1++;
        int res = turn ? *it1++ : *it2++;
        turn = !turn;
        return res;
    }

    bool hasNext() {
        return it1 != end1 || it2 != end2;
    }

private:
    vector<int>::iterator it1, it2, end1, end2;
    bool turn = true;
};

// Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
// Solution: For k vectors, use two queues to store iterators and `end` iterators.
class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        auto it1 = v1.begin();
        auto it2 = v2.begin();
        auto end1 = v1.end();
        auto end2 = v2.end();
        it.push_back(it1);
        it.push_back(it2);
        end.push_back(end1);
        end.push_back(end2);
        /*  If given k vectors
        (vector<vector<int>>& v){
            for(auto x: v){
                auto i = v.begin(); 
                auto j = v.end();
                it.push_back(i);
                end.push_back(j);
            }
        }
        */
    }

    int next() {
        auto x = it.front();
        it.pop_front();
        int res = *x++;
        it.push_back(x);
        end.push_back(end.front());
        end.pop_front();
        return res;
    }

    bool hasNext() {
        while(!it.empty() && it.front() == end.front()){
            it.pop_front();
            end.pop_front();
        }
        return !it.empty();
    }

private:
    deque<vector<int>::iterator>it;
    deque<vector<int>::iterator>end;
};''',

    'expression-add-operators': '''class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string>res;
        backtrack(res, num, target, 0, 0, 0, "");
        return res;
    }
    
    void backtrack(vector<string>& res, string num, int target, int pos, long sum, long multiply, string path){
        if(pos == num.size()){
            if(target == sum) res.push_back(path);
            return;
        }
        for(int i = pos; i < num.size(); i++){
            if(i != pos && num[pos] == '0') break;
            long cur = stol(num.substr(pos, i - pos + 1));
            if(pos == 0){
                backtrack(res, num, target, i + 1, cur, cur, path + to_string(cur));
            }
            else{
                backtrack(res, num, target, i + 1, sum + cur, cur, path + "+" + to_string(cur));
                backtrack(res, num, target, i + 1, sum - cur, -cur, path + "-" + to_string(cur));
                backtrack(res, num, target, i + 1, sum - multiply + multiply * cur, multiply * cur, path + "*" + to_string(cur));    
            }
        }
    }
};''',

    'move-zeroes': '''// One line.
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for(int i = 0, j = 0; j < nums.size(); j++) if(nums[j] != 0) swap(nums[i++], nums[j]);
    }
};

// Three lines.
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0;
        for(auto x: nums) if(x) nums[j++] = x;
        while(j < nums.size()) nums[j++] = 0;
    }
};

// Without maintaining the relative order, min steps.
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = nums.size() - 1;
        while(i < j){
            while(i < j && nums[i] != 0) i++;
            while(i < j && nums[j] == 0) j--;
            swap(nums[i++], nums[j--]);
        }
    }
};''',

    'peeking-iterator': '''// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
private:
    deque<int>q;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if(q.empty()) q.push_front(Iterator::next());
        return q.front();
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
        if(!q.empty()){
            int t = q.front();
            q.pop_front();
            return t;
        }
        return Iterator::next();;
	}

	bool hasNext() const {
	    return Iterator::hasNext() || !q.empty();
	}
};''',

    'inorder-successor-in-bst': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 // BST.
 class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* candidate = NULL;
        while(root){
            if(root->val > p->val){
                candidate = root;
                root = root->left;
            }
            else root = root->right;
        }
        return candidate;
    }
};

// Any Binary Tree.
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        stack<TreeNode*>s;
        DFS(root, s);
        while(s.top() != p) s.pop();
        s.pop();
        return s.empty() ? NULL : s.top();
    }
    
    void DFS(TreeNode* root, stack<TreeNode*>& s){
        if(!root) return;
        DFS(root->right, s);
        s.push(root);
        DFS(root->left, s);
    }
};''',

    'walls-and-gates': '''class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if(rooms.size() == 0 || rooms[0].size() == 0) return;
        vector<vector<int>>visited(rooms.size(), vector<int>(rooms[0].size()));
        for(int i = 0; i < rooms.size(); i++)
            for(int j = 0; j < rooms[0].size(); j++)
                if(rooms[i][j] == 0) BFS(rooms, i, j, 0, visited);
    }
    
    void BFS(vector<vector<int>>& rooms, int r, int c, int step, vector<vector<int>>& visited){
        if(r < 0 || c < 0 || r >= rooms.size() || c >= rooms[0].size() || visited[r][c] || rooms[r][c] < step) return;
        if(rooms[r][c] != 0) rooms[r][c] = min(rooms[r][c], step);
        visited[r][c] = 1;
        BFS(rooms, r - 1, c, step + 1, visited);
        BFS(rooms, r + 1, c, step + 1, visited);
        BFS(rooms, r, c + 1, step + 1, visited);
        BFS(rooms, r, c - 1, step + 1, visited);
        visited[r][c] = 0;
    }
};

// Further optimize
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if(rooms.size() == 0 || rooms[0].size() == 0) return;
        for(int i = 0; i < rooms.size(); i++)
            for(int j = 0; j < rooms[0].size(); j++)
                if(rooms[i][j] == 0) BFS(rooms, i, j, 0);
    }
    
    void BFS(vector<vector<int>>& rooms, int r, int c, int step){
        if(r < 0 || c < 0 || r >= rooms.size() || c >= rooms[0].size() || rooms[r][c] < step) return;
        rooms[r][c] = step;
        BFS(rooms, r - 1, c, step + 1);
        BFS(rooms, r + 1, c, step + 1);
        BFS(rooms, r, c + 1, step + 1);
        BFS(rooms, r, c - 1, step + 1);
    }
};''',

    'game-of-life': '''/*
 Transition: Marks

 0 -> 0 : 0
 1 -> 1 : 1
 0 -> 1 : -1
 1 -> 0 : 2

Then update the board according to their marks.
*/

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size() - 1, n = board[0].size() - 1;
        for(int i = 0; i <= m; i++)
            for(int j = 0; j <= n; j++){
                int neigh = cntNeighbor(board, m, n, i, j), cur = board[i][j];
                board[i][j] = (neigh > 3 || neigh < 2) && cur ? 2 : (neigh == 3 && !cur) ? -1 : cur;
            }
        
        for(auto& x: board)
            for(auto& y: x)
                y = (y == 2) ? 0 : (y == -1) ? 1 : y;
    }
    
    int cntNeighbor(vector<vector<int>>& board, int m, int n,  int r, int c){
        int cnt = 0;
        for(int i = max(0, r - 1); i <= min(m, r + 1); i++)
            for(int j = max(0, c - 1); j <= min(n, c + 1); j++)
                if((i != r || j != c) && board[i][j] > 0) cnt++;
        return cnt;
    }
};

// Or use the 2-bit to store the new state, idea from Stefan's post:(https://discuss.leetcode.com/topic/26112/c-o-1-space-o-mn-time).
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size() - 1, n = board[0].size() - 1;
        for(int i = 0; i <= m; i++)
            for(int j = 0; j <= n; j++){
                int neigh = cntNeighbor(board, m, n, i, j);
                if((neigh == 2 && board[i][j]) || neigh == 3) board[i][j] |= 2;
            }
        
        for(auto& x: board)
            for(auto& y: x)
                y >>= 1;
    }
    
    int cntNeighbor(vector<vector<int>>& board, int m, int n,  int r, int c){
        int cnt = 0;
        for(int i = max(0, r - 1); i <= min(m, r + 1); i++)
            for(int j = max(0, c - 1); j <= min(n, c + 1); j++)
                if((i != r || j != c) && board[i][j] & 1) cnt++;
        return cnt;
    }
};



class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int count = getNeighbor(board, i, j);
                if (count == 3){
                    board[i][j] |= 2;
                } else if (count == 2){
                    int tmp = board[i][j];
                    board[i][j] <<= 1;
                    board[i][j] |= tmp;
                }
            }
        }
        for (auto& v: board) {
            for (int& x: v) {
                x >>= 1;
            }
        }
    }
    
    int getNeighbor(vector<vector<int>>& board, int r, int c) {
        int count = 0, m = board.size(), n = board[0].size();
        for (int i = max(0, r - 1); i <= min(r + 1, m - 1); ++i) {
            for (int j = max(0, c - 1); j <= min(c + 1, n - 1); ++j) {
                if (i == r && j == c) {
                    continue;
                }
                if (board[i][j] & 1 == 1) {
                    ++count;
                }
            }
        }
        return count;
    }
};''',

    'word-pattern': '''class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, string>c2s;
        unordered_map<string, char>s2c;
        stringstream ss(str);
        string s = "";
        int i = 0;
        while(ss>>s){
            if(i == pattern.size() || c2s.count(pattern[i]) && c2s[pattern[i]] != s || s2c.count(s) && s2c[s] != pattern[i]) return false;
            c2s[pattern[i]] = s;
            s2c[s] = pattern[i++];
        }
        return i == pattern.size();
    }
};''',

    'flip-game': '''class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string>res;
        for(int i = 1; i < s.size(); i++)
            if(s[i - 1] == '+' && s[i] == '+'){
                res.push_back(s);
                res.back()[i - 1] = '-';
                res.back()[i] = '-';
            }
        return res;
    }
};''',

    'flip-game-ii': '''class Solution {
public:
    bool canWin(string s) {
        for(int i = 1; i < s.size(); i++)
            if(s[i - 1] == '+' && s[i] == '+'){
                s[i - 1] = s[i] = '-';
                if(!canWin(s)) return true;
                s[i - 1] = s[i] = '+';
            }
        return false;
    }
};''',

    'find-median-from-data-stream': '''class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {}
    
    void addNum(int num) {
        (left.empty() || num <= left.top()) ? left.push(num) : right.push(num);
        if(left.size() > right.size() + 1){
            right.push(left.top());
            left.pop();
        }
        if(right.size() > left.size()){
            left.push(right.top());
            right.pop();
        }
    }
    
    double findMedian() {
        return left.size() > right.size()? left.top() : (left.top() + right.top()) / 2.0;
    }

private:
    priority_queue<int>left;
    priority_queue<int, vector<int>, greater<int>>right;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */''',

    'serialize-and-deserialize-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
// Solution 1. Cheat.
class Codec {
private:
    unordered_map<TreeNode*, string>tree2string;
    unordered_map<string, TreeNode*>string2tree;
    int count = 0;
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = to_string(count++);
        tree2string[root] = s;
        string2tree[s] = root;
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        return string2tree[data];
    }
};

// Solution 2. Normal BFS solution using deque.
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = "";
        if(!root) return s;
        deque<TreeNode*>cur;
        deque<TreeNode*>sub;
        cur.push_back(root);
        while(!cur.empty()){
            TreeNode* node = cur.front();
            cur.pop_front();
            s.append(node ? to_string(node->val) + "," : ",");
            if(node){
                sub.push_back(node->left);
                sub.push_back(node->right);
            }
            if(cur.empty()) swap(cur, sub);
        }
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data.size() == 0) return NULL;
        string s;
        stringstream ss(data);
        getline(ss, s, ',');
        TreeNode* root = new TreeNode(stoi(s));
        deque<TreeNode*>q;
        q.push_back(root);
        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop_front();
            getline(ss, s, ',');
            TreeNode* left = s.size() ? new TreeNode(stoi(s)) : NULL;
            getline(ss, s, ',');
            TreeNode* right = s.size() ? new TreeNode(stoi(s)) : NULL;
            node->left = left;
            node->right = right;
            if(left) q.push_back(left);
            if(right) q.push_back(right);
        }
        return root;
    }
};''',

    'binary-tree-longest-consecutive-sequence': '''// DFS
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        int maxlen = 0;
        DFS(NULL, root, 1, maxlen);
        return maxlen;
    }
    
    void DFS(TreeNode* from, TreeNode* cur, int len, int& maxlen){
        if(!cur) return;
        len = (from && cur->val == from->val + 1) ? len + 1 : 1;
        maxlen = max(maxlen, len);
        DFS(cur, cur->left, len, maxlen);
        DFS(cur, cur->right, len, maxlen);
    }
};

// BFS
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        if(!root) return 0;
        deque<pair<TreeNode*, int>>q;
        q.push_back({root, 1});
        int maxlen = 0;
        while(!q.empty()){
            auto p = q.front();
            q.pop_front();
            if(p.first->left) q.push_back({p.first->left, (p.first->left->val == p.first->val + 1) ? p.second + 1 : 1});
            if(p.first->right) q.push_back({p.first->right, (p.first->right->val == p.first->val + 1) ? p.second + 1 : 1});
            maxlen = max(maxlen, p.second);
        }
        return maxlen;
    }
};''',

    'longest-increasing-subsequence': '''// Solution 1. DP, O(n^2).
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int maxlen = 0;
        vector<int>dp(nums.size(), 1);
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < i; j++) 
                if(nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
            maxlen = max(maxlen, dp[i]);
        }
        return maxlen;
    }
};

// Solution 2. Binary search, O(nlogn).
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int>dp;
        for(int x: nums){
            int pos = lower_bound(dp.begin(), dp.end(), x) - dp.begin();
            if(pos == dp.size()) dp.push_back(x);
            else dp[pos] = x;
        }
        return dp.size();
    }
};''',

    'remove-invalid-parentheses': '''// Solution 1. Brute force, 196ms.
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string>res;
        int minMove = INT_MAX;
        backtrack(res, s, 0, 0, minMove);
        return res;
    }
    
    void backtrack(vector<string>& res, string s, int pos, int move, int& minMove){
        if(pos > s.size() || move > minMove) return;
        if(isValid(s)){
            if(move < minMove) res.clear(), res.push_back(s), minMove = move;
            else if(move == minMove && find(res.begin(), res.end(), s) == res.end()) res.push_back(s);
            return;
        }
        while(pos < s.size() && s[pos] != '(' && s[pos] != ')') pos++;
        if(pos >= s.size()) return;
        backtrack(res, s.substr(0, pos) + s.substr(pos + 1), pos, move + 1, minMove);
        backtrack(res, s, pos + 1, move, minMove);
    }
    
    bool isValid(string& s){
        int sum = 0;
        for(auto c: s){
            if(c == '(') sum++;
            else if(c == ')') sum--;
            if(sum < 0) return false;
        }
        return sum == 0;
    }
};

// Solution 2. BFS, 63ms.
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        unordered_set<string>visited;
        vector<string>res;
        deque<string>cur;
        deque<string>next;
        cur.push_back(s);
        while(!cur.empty()){
            s = cur.front();
            cur.pop_front();
            if(isValid(s)){
                res.push_back(s);
                continue;
            }
            for(int i = 0; i < s.size(); i++){
                if(s[i] != '(' && s[i] != ')') continue;
                string tmp = s.substr(0, i) + s.substr(i + 1);
                if(visited.count(tmp) == 0){
                    next.push_back(tmp);
                    visited.insert(tmp);
                }
            }
            if(cur.empty() && res.size() == 0) swap(cur, next);
        }
        return res;
    }
    
    bool isValid(string& s){
        int sum = 0;
        for(auto c: s){
            if(c == '(') sum++;
            else if(c == ')') sum--;
            if(sum < 0) return false;
        }
        return sum == 0;
    }
};''',

    'range-sum-query-immutable': '''class NumArray {
public:
    NumArray(vector<int> nums) {
        int sum = 0;
        for(auto x: nums){
            sum += x;
            dp.push_back(sum);
        }
    }
    
    int sumRange(int i, int j) {
        return i == 0 ? dp[j] : dp[j] - dp[i - 1];
    }
    
private:
    vector<int>dp;
};''',

    'range-sum-query-2d-immutable': '''// See detailed explanation of that problem in discuss.
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        for(int i = 0; i < matrix.size(); i++){
            dp.push_back(vector<int>());
            for(int j = 0; j < matrix[0].size(); j++)
                if(i == 0)
                    if(j == 0) dp[i].push_back(matrix[0][0]);
                    else dp[i].push_back(matrix[0][j] + dp[0][j - 1]);
                else
                    if(j == 0) dp[i].push_back(matrix[i][j] + dp[i - 1][0]);
                    else dp[i].push_back(matrix[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]);
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int a = (row1 == 0) ? 0 : dp[row1 - 1][col2];
        int b = (col1 == 0) ? 0 : dp[row2][col1 - 1];
        int c = (row1 == 0 || col1 == 0) ? 0 : dp[row1 - 1][col1 - 1];
        return dp[row2][col2] - a - b + c;
    }
    
private:
    vector<vector<int>>dp;
};

// Or a more concise one, 7 lines.
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return;
        }
        int m = matrix.size(), n = matrix[0].size();
        dp = vector<vector<int>>(m + 1, vector<int>(n + 1));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + matrix[i][j];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return dp[row2 + 1][col2 + 1] - dp[row2 + 1][col1] - dp[row1][col2 + 1] + dp[row1][col1];
    }
    
private:
    vector<vector<int>>dp;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */''',

    'number-of-islands-ii': '''class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        vector<int>res;
        vector<vector<int>>matrix(m, vector<int>(n));
        int tag = 0, count = 0;
        for(auto x: positions) addLand(matrix, m, n, x.first, x.second, tag, count, res);
        return res;
    }
    
    void addLand(vector<vector<int>>& matrix, int m, int n, int r, int c, int& tag, int& count, vector<int>& res){
        unordered_set<int>s;
        vector<int>dir(4);
        if(c - 1 >= 0) dir[0] = matrix[r][c - 1];
        if(c + 1 < n)  dir[1] = matrix[r][c + 1];
        if(r - 1 >= 0) dir[2] = matrix[r - 1][c];
        if(r + 1 < m)  dir[3] = matrix[r + 1][c];
        for(auto x: dir) if(x) s.insert(x);
        matrix[r][c] = s.empty() ? ++tag : *s.begin();
        count -= s.size() - 1;
        res.push_back(count);
        if(s.size() > 1){
            BFS(matrix, m, n, r, c - 1, *s.begin());
            BFS(matrix, m, n, r, c + 1, *s.begin());
            BFS(matrix, m, n, r - 1, c, *s.begin());
            BFS(matrix, m, n, r + 1, c, *s.begin());
        }
    }
    
    void BFS(vector<vector<int>>& matrix, int m, int n, int r, int c, int tag){
        if(r < 0 || c < 0 || r == m || c == n || matrix[r][c] == 0 || matrix[r][c] == tag) return;
        matrix[r][c] = tag;
        BFS(matrix, m, n, r, c - 1, tag);
        BFS(matrix, m, n, r, c + 1, tag);
        BFS(matrix, m, n, r - 1, c, tag);
        BFS(matrix, m, n, r + 1, c, tag);
    }
};''',

    'range-sum-query-mutable': '''// Yes, it passed the judge.
class NumArray {
public:
    NumArray(vector<int> nums) {
        this->nums = nums;
    }
    
    void update(int i, int val) {
        nums[i] = val;
    }
    
    int sumRange(int i, int j) {
        int sum = 0;
        for(int a = i; a <= j; a++) sum += nums[a];
        return sum;
    }
    
private:
    vector<int> nums;
};

// Segment Tree
class NumArray {
    struct SegmentTreeNode{
        int start;
        int end;
        int sum;
        SegmentTreeNode* left;
        SegmentTreeNode* right;
        SegmentTreeNode(int l, int r):start(l), end(r), sum(0), left(NULL), right(NULL){}
    };
    SegmentTreeNode* root;
    
    SegmentTreeNode* buildTree(vector<int>& nums, int start, int end){
        if(start > end) return NULL;
        SegmentTreeNode* p = new SegmentTreeNode(start, end);
        if(start == end){
            p->sum = nums[start];
        }
        else{
            int mid = start + (end - start) / 2;
            p->left = buildTree(nums, start, mid);
            p->right = buildTree(nums, mid + 1, end);
            p->sum = p->left->sum + p->right->sum;
        }
        return p;
    }
    
    void update(SegmentTreeNode* p, int i, int val){
        if(p->start == i && p->end == i){
            p->sum = val;
        }
        else{
            int mid = p->start + (p->end - p->start) / 2;
            if(i <= mid) update(p->left, i, val);
            else update(p->right, i, val);
            p->sum = p->left->sum + p->right->sum;
        }
    }
    
    int sumRange(SegmentTreeNode* p, int i, int j){
        if(p->start == i && p->end == j){
            return p->sum;
        }
        int mid = p->start + (p->end - p->start) / 2;
        if(j <= mid) 
            return sumRange(p->left, i, j);
        else if(i > mid) 
            return sumRange(p->right, i, j);
        else 
            return sumRange(p->left, i, mid) + sumRange(p->right, mid + 1, j);
    }
    
public:
    NumArray(vector<int> nums) {
        root = buildTree(nums, 0, nums.size() - 1);
    }
    
    void update(int i, int val) {
        update(root, i, val);
    }
    
    int sumRange(int i, int j) {
        return sumRange(root, i, j);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */


class NumArray {
    struct TreeNode {
        int start;
        int end;
        int sum;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int x, int y):start(x), end(y), sum(0), left(NULL), right(NULL) {}
    };
public:
    NumArray(vector<int> nums) {
        root = buildTree(nums, 0, nums.size() - 1);
    }
    
    void update(int i, int val) {
        dfs(root, i, val);
    }
    
    int sumRange(int i, int j) {
        return i == 0 ? getSum(root, j) : getSum(root, j) - getSum(root, i - 1);
    }
    
    int getSum(TreeNode* root, int idx) {
        if (root->end == idx) {
            return root->sum;
        }
        int mid = root->start + (root->end - root->start)/2;
        if (idx <= mid) {
            return getSum(root->left, idx);
        } else {
            return root->left->sum + getSum(root->right, idx);
        }
    }
    
    
    void dfs(TreeNode* root, int i, int val) {
        if (root->start == i && root->end == i) {
            root->sum = val;
            return;
        }
        
        int mid = root->start + (root->end - root->start)/2;
        
        if (i <= mid) {
            dfs(root->left, i, val);
        } else {
            dfs(root->right, i, val);
        }
        root->sum = root->left->sum + root->right->sum;
    }
    
    TreeNode* buildTree(vector<int>& nums, int start, int end) {
        if (start > end) {
            return NULL;
        }
        if (start == end) {
            TreeNode* node = new TreeNode(start, end);
            node->sum = nums[start];
            return node;
        }
        TreeNode* node = new TreeNode(start, end);
        int mid = start + (end - start)/2;
        node->left = buildTree(nums, start, mid);
        node->right = buildTree(nums, mid + 1, end);
        node->sum = node->left->sum + node->right->sum;
        return node;
    }
    
private:
    TreeNode* root;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */''',

    'best-time-to-buy-and-sell-stock-with-cooldown': '''class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n < 2) return 0;
        vector<int>buy(n), sell(n), rest(n);
        buy[0] = -prices[0];
        sell[0] = 0;
        rest[0] = 0;
        for(int i = 1; i < n; i++){
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i]);
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i]);
            rest[i] = max(rest[i - 1], sell[i - 1]);
        }
        return max(rest[n - 1], sell[n - 1]);
    }
};

// Since day `i` relies only on `i-1`, we can reduce the O(n) space to O(1). 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n < 2) return 0;
        int buy = -prices[0], sell = 0, rest = 0, preBuy, preSell;
        for(int i = 1; i < n; i++){
            preBuy = buy;
            preSell = sell;
            buy = max(buy, rest - prices[i]);
            sell = max(sell, preBuy + prices[i]);
            rest = max(rest, preSell);
        }
        return max(rest, sell);
    }
};''',

    'minimum-height-trees': '''/* From BF 1880ms to O(n) 35ms beats 99% */
// Solution 1. Brute Force, find the min height of starting from `root(i) = 0, 1, 2, ... n - 1` using BFS. 
// Easy to understand but will obviously costs a lot of time.
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int>res;
        vector<vector<int>>graph(n);
        // Build Graph
        for(auto x: edges){
            graph[x.first].push_back(x.second);
            graph[x.second].push_back(x.first);
        }
        int minHeight = INT_MAX;
        // BFS
        for(int i = 0; i < n; i++){
            if(graph[i].size() < 5 && n > 10000) continue; // Magic for passing the last TC.
            vector<int>visited(n);
            int height = 0;
            deque<int>cur;
            deque<int>sub;
            cur.push_back(i);
            
            while(!cur.empty() && height <= minHeight){
                int node = cur.front();
                cur.pop_front();
                visited[node] = 1;
                for(auto neigh: graph[node])
                    if(!visited[neigh]) sub.push_back(neigh);
                if(cur.empty()){
                    height++;
                    swap(cur, sub);
                }
            }
            if(height < minHeight){
                res.clear();
                minHeight = height;
                res.push_back(i);
            }
            else if(minHeight == height) res.push_back(i);
        }
        return res;
    }
};

// Solution 2.
/**
 * After reviewing the BF solution, I realized that the Minimum Height Node is exactly the mid point of the longest path in the graph. 
 * (Or 2 nodes if length is even.) 
 * So, idea is that, we use 3 passes in total to found the longest path in the graph:
 * 1. First pass, starting from any node, go as deep as we can until reach the leaf node `a`.
 * 2. Second pass, starting from node `a`, go as deep as we can until reach the leaf node `b`.
 * 3. The path between node `a` and `b` is the longest path of the graph, using DFS to find path `a` to `b`.
 * Then we simply return the mid node(odd) / nodes(even) of the longest path.
 * Time Complexity: O(n).
 * Here is the code, 35ms beats 99.17%.
 */
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int>res;
        vector<vector<int>>graph(n);
        // Build Graph
        for(auto x: edges){
            graph[x.first].push_back(x.second);
            graph[x.second].push_back(x.first);
        }
        int start = 0, end = 0;
        // BFS
        int root = 0;
        for(int i = 0; i < 2; i++){
            vector<int>visited(n);
            deque<int>cur;
            deque<int>sub;
            cur.push_back(root);
            while(!cur.empty()){
                int node = cur.front();
                cur.pop_front();
                visited[node] = 1;
                for(auto neigh: graph[node]) 
                    if(!visited[neigh]) sub.push_back(neigh);
                if(sub.empty()){
                    root = node;
                    if(i == 0) start = root;
                    if(i == 1) end = root;
                }
                if(cur.empty()) swap(cur, sub);
            }
        }
        // DFS
        vector<int>vec;
        vector<int>path;
        vector<int>visited(n);
        bool found = false;
        DFS(graph, visited, start, end, vec, path, found);
        if(path.size() % 2) res.push_back(path[path.size() / 2]);
        else{
            res.push_back(path[path.size() / 2]);
            res.push_back(path[path.size() / 2 - 1]);
        }
        return res;
    }
    
    void DFS(vector<vector<int>>& graph, vector<int>& visited, int node, int dest, vector<int>& vec, vector<int>& path, bool& found){
        if(visited[node]) return;
        visited[node] = 1;
        vec.push_back(node);
        if(node == dest){
            path = vec;
            found = true;
            return;
        }
        for(auto neigh: graph[node]){
            DFS(graph, visited, neigh, dest, vec, path, found);
            if(found) break;
        }
        vec.pop_back();
    }
};''',

    'sparse-matrix-multiplication': '''class Solution {
public:
	vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
		vector<vector<int>>res(A.size(), vector<int>(B[0].size()));
		for (int i = 0; i < A.size(); i++)
			for (int j = 0; j < B[0].size(); j++)
				res[i][j] = helper(A[i], B, j);
		return res;
	}

	int helper(vector<int>& v, vector<vector<int>>& B, int col) {
		int res = 0;
		for (int i = 0; i < v.size(); i++)
			if (v[i] != 0 && B[i][col] != 0)
				res += v[i] * B[i][col];
		return res;
	}
};

// Optimize
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>>res(A.size(), vector<int>(B[0].size()));
        for(int i = 0; i < A.size(); i++)
            for(int j = 0; j < A[0].size(); j++)
                if(A[i][j] != 0)
                for(int k = 0; k < B[0].size(); k++)
                    res[i][k] += A[i][j] * B[j][k];
        return res;
    }
};''',

    'super-ugly-number': '''// Solution 1. 
// Time: O(n*2k)
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int>dp(n);
        dp[0] = 1;
        vector<int>p(primes.size());
        for(int i = 1; i < n; i++){
            dp[i] = INT_MAX;
            for(int j = 0; j < p.size(); j++) dp[i] = min(dp[i], dp[p[j]] * primes[j]);
            for(int j = 0; j < p.size(); j++) if(dp[p[j]] * primes[j] == dp[i]) p[j]++;
        }
        return dp[n - 1];
    }
};

// Solution 2.
// Improve from 2 inner loops to one loop, idea from this post: 
// https://discuss.leetcode.com/topic/34841/java-three-methods-23ms-36-ms-58ms-with-heap-performance-explained
// Time: O(n*k)
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int>dp(n);
        vector<int>p(primes.size());
        vector<int>val(primes.size());
        int next = 1;
        for(int i = 0; i < n; i++){
            dp[i] = next;
            next = INT_MAX;
            for(int j = 0; j < val.size(); j++){
                if(dp[i] >= val[j]) val[j] = dp[p[j]++] * primes[j];
                next = min(next, val[j]);
            }
        }
        return dp[n - 1];
    }
};

// Solution 3.
// Also, I wrote the last heap version from the same post, but I think its time complexity is O(nklogk) rather than O(nlogk), 
// which is actually slower than above solution.
// Time: O(nklogk), 65ms. 
struct triple{
    int val;
    int prime;
    int p;
    triple(int x, int y, int z):val(x), prime(y), p(z){};
};

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int>dp(n);
        dp[0] = 1;
        auto cmp = [](triple* t1, triple* t2){ return t1->val > t2->val; };
        priority_queue<triple*, vector<triple*>, decltype(cmp)>pq(cmp);
        for(int i = 0; i < primes.size(); i++) pq.push(new triple(primes[i], primes[i], 1));
        for(int i = 1; i < n; i++){
            dp[i] = pq.top()->val;
            while(pq.top()->val == dp[i]){
                triple* t = pq.top();
                pq.pop();
                pq.push(new triple(t->prime * dp[t->p], t->prime, t->p + 1));
            }
        }
        return dp[n - 1];
    }
};''',

    'binary-tree-vertical-order-traversal': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(!root) return res;
        map<int, vector<int>>m;
        deque<pair<int, TreeNode*>>cur;
        deque<pair<int, TreeNode*>>next;
        cur.push_back(make_pair(0, root));
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            m[p.first].push_back(p.second->val);
            if(p.second->left) next.push_back(make_pair(p.first - 1, p.second->left));
            if(p.second->right) next.push_back(make_pair(p.first + 1, p.second->right));
            if(cur.empty()) swap(cur, next);
        }
        for(auto x: m) res.push_back(x.second);
        return res;
    }
};''',

    'count-of-smaller-numbers-after-self': '''class Solution {
    struct TreeNode{
        int val;
        int sum;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int x, int y): val(x), sum(y), left(NULL), right(NULL){}
    };
public:
    vector<int> countSmaller(vector<int>& nums) {
        TreeNode* root = NULL;
        vector<int>res(nums.size());
        for(int i = nums.size() - 1; i >= 0; i--) root = buildTree(root, i, nums[i], 0, res);
        return res;
    }
    
    TreeNode* buildTree(TreeNode* root, int i, int val, int count, vector<int>& res){
        if(!root){
            root = new TreeNode(val, 1);
            res[i] = count;
            return root;
        }
        if(val > root->val) root->right = buildTree(root->right, i, val, count + root->sum, res);
        else{
            root->sum++;
            root->left = buildTree(root->left, i, val, count, res);
        }
        return root;
    }
};''',

    'shortest-distance-from-all-buildings': '''class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int sum = 0, minDis = INT_MAX;
        for(auto x: grid)
            for(auto y: x) if(y == 1) sum++;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] == 0) BFS(grid, m, n, i, j, sum, minDis);
        return minDis == INT_MAX ? -1 : minDis;
    }
    
    void BFS(vector<vector<int>>& grid, int m, int n, int r, int c, int sum, int& minDis){
        int count = 0;
        vector<vector<int>>visited(m, vector<int>(n));
        vector<pair<int, int>>dir{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        deque<pair<int, int>>cur;
        deque<pair<int, int>>next;
        cur.push_back({r, c});
        visited[r][c] = 1;
        int level = 1, dis = 0;
        while(count < sum && !cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            for(int i = 0; i < 4; i++){
                int R = p.first + dir[i].first;
                int C = p.second + dir[i].second;
                if(R < 0 || C < 0 || R == m || C == n || visited[R][C]) continue;
                visited[R][C] = 1;
                if(grid[R][C] == 1){
                    dis += level;
                    count++;
                }
                if(grid[R][C] == 0) next.push_back({R, C});
            }
            if(cur.empty()){
                level++;
                swap(cur, next);
            }
        }
        if(count == sum) minDis = min(minDis, dis);
    }
};''',

    'maximum-product-of-word-lengths': '''// Solution 1. Straight forward, 165ms
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int maxlen = 0;
        for(int i = 0; i < words.size(); i++)
            for(int j = i + 1; j < words.size(); j++){
                if(words[i].size() * words[j].size() <= maxlen) continue;
                if(noCommon(words[i], words[j])) maxlen = max(maxlen, (int)(words[i].size() * words[j].size()));
            }
        return maxlen;
    }
    
    bool noCommon(string& a, string& b){
        for(auto x: a) 
            for(auto y: b)
                if(x == y) return false;
        return true;
    }
};

// Solution 2. Bit Manipulation, 43ms
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int maxlen = 0;
        vector<int>val(words.size());
        for(int i = 0; i < words.size(); i++)
            for(auto c: words[i]) val[i] |= (1 << (c - 'a'));
        
        for(int i = 0; i < words.size(); i++)
            for(int j = i + 1; j < words.size(); j++)
                if((val[i] & val[j]) == 0 && words[i].size() * words[j].size() > maxlen)
                    maxlen = max(maxlen, (int)(words[i].size() * words[j].size()));
        return maxlen;
    }
};''',

    'number-of-connected-components-in-an-undirected-graph': '''// DFS
class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        vector<vector<int>>graph(n);
        vector<int>visited(n);
        for(auto x: edges){
            graph[x.first].push_back(x.second);
            graph[x.second].push_back(x.first);
        }
        int label = 0;
        for(int i = 0; i < n; i++){
            if(visited[i]) continue;
            label++;
            DFS(graph, i, visited);
        }
        return label;
    }
    
    void DFS(vector<vector<int>>& graph, int root, vector<int>& visited){
        if(visited[root]) return;
        visited[root] = 1;
        for(auto neigh: graph[root])
            if(!visited[neigh]) DFS(graph, neigh, visited);
    }
};

// BFS
class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        vector<vector<int>>graph(n);
        vector<int>visited(n);
        for(auto x: edges){
            graph[x.first].push_back(x.second);
            graph[x.second].push_back(x.first);
        }
        int label = 0;
        for(int i = 0; i < n; i++){
            if(visited[i]) continue;
            label++;
            deque<int>q;
            q.push_back(i);
            while(!q.empty()){
                int node = q.front();
                q.pop_front();
                visited[node] = 1;
                for(auto neigh: graph[node])
                    if(!visited[neigh]) q.push_back(neigh);
            }
        }
        return label;
    }
};''',

    'maximum-size-subarray-sum-equals-k': '''// Brute Force, O(n^2).
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int len = 0;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            for(int j = i; j < nums.size(); j++){
                sum += nums[j];
                if(sum == k) len = max(len, j - i + 1);
            }
        }
        return len;
    }
};

// O(n).
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        int sum = 0;
        int maxlen = 0;
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            if(!m.count(sum)) m[sum] = i;
            if(sum == k) maxlen = i + 1;
            else if(m.count(sum - k) > 0) maxlen = max(maxlen, i - m[sum - k]);
        }
        return maxlen;
    }
};''',

    'longest-increasing-path-in-a-matrix': '''class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return 0;
        int m = matrix.size() , n = matrix[0].size();
        vector<vector<int>>dp(m, vector<int>(n));
        vector<vector<int>>visited(m, vector<int>(n));
        int maxlen = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                maxlen = max(maxlen, DFS(matrix, visited, dp, i, j, m, n));
        return maxlen;
    }
    
    int DFS(vector<vector<int>>& matrix, vector<vector<int>>& visited, vector<vector<int>>& dp, int r, int c, int m, int n){
        if(visited[r][c]) return 0;
        if(dp[r][c]) return dp[r][c];
        visited[r][c] = 1;
        int up(1), down(1), left(1), right(1);
        if(r - 1 >= 0 && matrix[r - 1][c] > matrix[r][c])     up = DFS(matrix, visited, dp, r - 1, c, m, n) + 1;
        if(r + 1 < m  && matrix[r + 1][c] > matrix[r][c])   down = DFS(matrix, visited, dp, r + 1, c, m, n) + 1;
        if(c - 1 >= 0 && matrix[r][c - 1] > matrix[r][c])   left = DFS(matrix, visited, dp, r, c - 1, m, n) + 1;
        if(c + 1 < n  && matrix[r][c + 1] > matrix[r][c])  right = DFS(matrix, visited, dp, r, c + 1, m, n) + 1;
        visited[r][c] = 0;
        dp[r][c] = max(up, max(down, max(left, right)));
        return dp[r][c];
    }
};''',

    'verify-preorder-serialization-of-a-binary-tree': '''class Solution {
public:
    bool isValidSerialization(string preorder) {
        if(preorder == "#") return true;
        stringstream ss(preorder);
        stack<int>stk;
        string s = "";
        while(getline(ss, s, ',')){
            if(s == "#" && stk.empty()) return false;
            if(!stk.empty()) stk.top()++;
            if(!stk.empty() && stk.top() == 2) stk.pop();
            if(s != "#") stk.push(0);
            if(stk.empty() && !ss.eof()) return false;
        }
        return stk.empty();
    }
};''',

    'reconstruct-itinerary': '''class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>>m;
        vector<string>res;
        for(auto x: tickets) m[x.first].push(x.second);
        DFS("JFK", res, m);
        reverse(res.begin(), res.end());
        return res;
    }
    
    void DFS(string cur, vector<string>& res, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& m){
        while(!m[cur].empty()){
            string s = m[cur].top();
            m[cur].pop();
            DFS(s, res, m);
        }
        res.push_back(cur);
    }
};''',

    'largest-bst-subtree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int largestBSTSubtree(TreeNode* root) {
        int res = 0;
        dfs(root, res);
        return res;
    }
    
    vector<int> dfs(TreeNode* root, int& res){
        if(!root) return {INT_MAX, INT_MIN, 0};
        auto l = dfs(root->left, res);
        auto r = dfs(root->right, res);
        int count = (l[2] == -1 || r[2] == -1 || l[1] >= root->val || r[0] <= root->val) ? -1 : l[2] + r[2] + 1;
        res = max(res, count);
        return {min(root->val, min(l[0], r[0])), max(root->val, max(l[1], r[1])), count};
    }
};''',

    'increasing-triplet-subsequence': '''class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int c1 = INT_MAX, c2 = INT_MAX;
        for(auto x: nums)
            if(x <= c1) c1 = x;
            else if(x <= c2) c2 = x;
            else return true;
        return false;
    }
};''',

    'palindrome-pairs': '''class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>>res;
        buildTrie(words);
        for(int i = 0; i < words.size(); i++){
            string s = words[i];
            for(auto x: Trie[s]) if(isPalindrome(x.first) && i != x.second) res.push_back({i, x.second});
            for(int j = 0; j <= s.size(); j++)
                if(m.count(s.substr(0, j)) && isPalindrome(s.substr(j)) && i != m[s.substr(0, j)]) 
                    res.push_back({i, m[s.substr(0, j)]});
        }    
        return res;
    }
    
private:
    unordered_map<string, vector<pair<string, int> > >Trie;
    unordered_map<string, int>m;
    void buildTrie(vector<string>& words){
        for(int i = 0; i < words.size(); i++){
            string s = words[i];
            reverse(s.begin(), s.end());
            m[s] = i;
            for(int j = 0; j < s.size(); j++) Trie[s.substr(0, j)].push_back({s.substr(j), i});
        }
    }
    
    bool isPalindrome(string s){
        int i = 0, j = s.size() - 1;
        while(i < j) if(s[i++] != s[j--]) return false;
        return true;
    }
};''',

    'nested-list-weight-sum': '''/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        return dfs(nestedList, 1);
    }
    
    int dfs(vector<NestedInteger>& nestedList, int depth) {
        int res = 0;
        for(auto x: nestedList)
            res += x.isInteger() ? x.getInteger() * depth : dfs(x.getList(), depth + 1);
        return res;
    }
};''',

    'longest-substring-with-at-most-k-distinct-characters': '''class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int>m;
        int i = 0, j = 0, cnt = 0, maxlen = 0;
        while(j < s.size()){
            if(m[s[j++]]++ == 0) cnt++;
            if(cnt <= k) maxlen = max(maxlen, j - i);
            while(cnt > k) if(--m[s[i++]] == 0) cnt--;
        }
        return maxlen;
    }
};

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int count = 0, j = 0, res = 0;
        unordered_map<char, int>m;
        for (int i = 0; i < s.size(); ++i) {
            if (m[s[i]]++ == 0) {
                ++count;
            }
            
            while (count > k) {
                if (--m[s[j++]] == 0) {
                    --count;
                }
            }
            res = max(res, i - j + 1);
        }
        return res;
    }
};''',

    'flatten-nested-list-iterator': '''/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        this->nestedList = &nestedList;
    }

    int next() {
        int n = q.front();
        q.pop_front();
        return n;
    }

    bool hasNext() {
        while(q.empty() && i < nestedList->size()){
            if((*nestedList)[i].isInteger())
                q.push_back((*nestedList)[i].getInteger());
            else{
                NestedIterator* it = new NestedIterator((*nestedList)[i].getList());
                while(it->hasNext()) q.push_back(it->next());
            }
            i++;
        }
        return !q.empty();
    }

private:
    vector<NestedInteger>* nestedList;
    deque<int>q;
    int i = 0;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */''',

    'reverse-string': '''class Solution {
public:
	string reverseString(string s) {
		reverse(s.begin(), s.end());
		return s;
	}
};''',

    'top-k-frequent-elements': '''// Solution 1. MaxHeap, O(nlogn).
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        for(auto x: nums) m[x]++;
        priority_queue<pair<int, int>>pq;
        for(auto p: m) pq.push({p.second, p.first});
        vector<int>res;
        while(k--) res.push_back(pq.top().second), pq.pop();
        return res;
    }
};

// O(nlog(n - k)).
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        for(auto x: nums) m[x]++;
        priority_queue<pair<int, int>>pq;
        vector<int>res;
        for(auto p: m){
            pq.push({p.second, p.first});
            if(pq.size() > m.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};

// Solution 2. MinHeap, O(nlogk).
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        for(auto x: nums) m[x]++;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>pq;
        for(auto p: m){
            pq.push({p.second, p.first});
            if(pq.size() > k) pq.pop();
        }
        vector<int>res;
        while(k--) res.push_back(pq.top().second), pq.pop();
        return res;
    }
};

// Solution 3. Bucket Sort, O(n).
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        for(auto x: nums) m[x]++;
        vector<int>res;
        vector<vector<int>>bucket(nums.size() + 1);
        for(auto p: m) bucket[p.second].push_back(p.first);
        for(int i = bucket.size() - 1; res.size() < k; i--)
            for(auto j: bucket[i]) res.push_back(j);
        return res;
    }
};''',

    'design-tic-tac-toe': '''class TicTacToe {
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        this->board.resize(n, vector<int>(n));
    }
    
    int move(int row, int col, int player) {
        board[row][col] = player;
        return checkWin(row, col, board.size(), player);
    }

private:
    vector<vector<int>>board;
    int checkWin(int row, int col, int n, int player){
        int r = 0, c = 0, i = 0, j = 0, x = 0, y = n - 1;
        while(r < n && board[r][col] == player) r++;
        while(c < n && board[row][c] == player) c++;
        if(row == col)  while(i < n && board[i][j] == player) i++, j++;
        if(row == n - col - 1) while(x < n && board[x][y] == player) x++, y--;
        return r == n || c == n || i == n || x == n ? player : 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */''',

    'android-unlock-patterns': '''class Solution {
public:
    int numberOfPatterns(int m, int n) {
        vector<vector<int>>g({{1,2,3,4,5,6,7,8,9}, 
                              {2,4,5,6,8},
                              {1,5,3,7,9,4,6},
                              {2,5,6,4,8},
                              {1,2,5,8,7,3,9},
                              {1,2,3,4,6,7,8,9},
                              {2,3,5,8,9,1,7},
                              {4,5,8,2,6},
                              {7,5,9,1,3,4,6},
                              {5,6,8,2,4}});
        
        int a = 0, b = 0, c = 0;
        vector<int>visited(10);
        dfs(g, m, n, 1, "1", a, visited);
        dfs(g, m, n, 2, "2", b, visited);
        dfs(g, m, n, 5, "5", c, visited);
        return a*4 + b*4 + c;
    }
    
    void dfs(vector<vector<int>> g, int m, int n, int from, string s, int& res, vector<int> visited) {
        if (s.size() > n) {
            return;
        }
        if (s.size() >= m) {
            ++res;
        }
        visited[from] = 1;
        unblock(g, from);
        for (int& x: g[from]) {
            if (!visited[x]) {
                s.push_back(x + '0');
                dfs(g, m, n, x, s, res, visited);
                s.pop_back();
                visited[x] = 0;
            }
        }
        visited[from] = 0;
    }
    
    
    void unblock(vector<vector<int>>& g, int num) {
        if (num == 2) {
            g[1].push_back(3);
            g[3].push_back(1);
        } else if (num == 4) {
            g[1].push_back(7);
            g[7].push_back(1);
        } else if (num == 5) {
            g[1].push_back(9);
            g[9].push_back(1);
            g[3].push_back(7);
            g[7].push_back(3);
            g[4].push_back(6);
            g[6].push_back(4);
            g[2].push_back(8);
            g[8].push_back(2);
        } else if (num == 6) {
            g[9].push_back(3);
            g[3].push_back(9);
        } else if (num == 8) {
            g[7].push_back(9);
            g[9].push_back(7);
        }
    }
};''',

    'russian-doll-envelopes': '''class Solution {
public:
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        sort(envelopes.begin(), envelopes.end(), [](pair<int, int>& p1, pair<int, int>& p2){
            return p1.first == p2.first ? p1.second > p2.second : p1.first < p2.first;
        });
        vector<int>dp;
        for(auto x: envelopes){
            int pos = lower_bound(dp.begin(), dp.end(), x.second) - dp.begin();
            if(pos == dp.size()) dp.push_back(x.second);
            else dp[pos] = x.second;
        }
        return dp.size();
    }
};''',

    'design-twitter': '''class Twitter {
private:
    vector<pair<int,int>>posts;
    unordered_map<int, unordered_map<int, int>>follows;
public:
    Twitter() {}
    
    void postTweet(int userId, int tweetId) {
        posts.push_back(make_pair(userId, tweetId));
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int>feed;
        int count = 0;
        for(int i = posts.size() - 1; i >= 0 && count < 10; i--)
            if(posts[i].first == userId || follows[userId][posts[i].first])
                feed.push_back(posts[i].second), count++;
        return feed;
    }
    
    void follow(int followerId, int followeeId) {
        follows[followerId][followeeId] = 1;
    }
    
    void unfollow(int followerId, int followeeId) {
        follows[followerId][followeeId] = 0;
    }
};''',

    'logger-rate-limiter': '''class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {}
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (!m.count(message) || timestamp - m[message] >= 10) {
            m[message] = timestamp;
            return true;
        } else {
            return false;
        }
    }
    
private:
    map<string, int>m;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */''',

    'sort-transformed-array': '''class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        vector<int>res;
        int i = 0, j = nums.size() - 1;
        while(i <= j){
            int x = a * nums[i] * nums[i] + b * nums[i] + c;
            int y = a * nums[j] * nums[j] + b * nums[j] + c;
            if(a * x > a * y){
                i++;
                res.push_back(x);
            }
            else{
                j--;
                res.push_back(y);
            }
        }
        if(a > 0 || a == 0 && b > 0) reverse(res.begin(), res.end());
        return res;
    }
};''',

    'bomb-enemy': '''class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        int maxKill = 0;
        for(int i = 0; i < grid.size(); i++)
            for(int j = 0; j < grid[0].size(); j++)
                if(grid[i][j] == '0') maxKill = max(maxKill, getKills(grid, i, j));
        return maxKill;
    }
    
    int getKills(vector<vector<char>>& grid, int r, int c){
        int m = grid.size(), n = grid[0].size(), count = 0;
        int up = r - 1, down = r + 1, left = c - 1, right = c + 1;
        while(up >= 0 && grid[up][c] != 'W') if(grid[up--][c] == 'E') count++;
        while(down < m && grid[down][c] != 'W') if(grid[down++][c] == 'E') count++;
        while(left >= 0 && grid[r][left] != 'W') if(grid[r][left--] == 'E') count++;
        while(right < n && grid[r][right] != 'W') if(grid[r][right++] == 'E') count++;
        return count;
    }
};''',

    'design-hit-counter': '''class HitCounter {
private:
    deque<int>q;
public:
    /** Initialize your data structure here. */
    HitCounter() {}
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        q.push_back(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        while(!q.empty() && q.front() <= timestamp - 300) q.pop_front();
        return q.size();
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */''',

    'nested-list-weight-sum-ii': '''/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int maxDepth = getDepth(nestedList);
        return dfs(nestedList, maxDepth);
    }
    
    int getDepth(vector<NestedInteger>& nestedList) {
        int depth = 1;
        for(auto x: nestedList)
            if(!x.isInteger()) depth = max(depth, 1 + getDepth(x.getList()));
        return depth;
    }
    
    int dfs(vector<NestedInteger>& nestedList, int depth){
        int res = 0;
        for(auto x: nestedList)
            res += x.isInteger() ? x.getInteger() * depth : dfs(x.getList(), depth - 1);
        return res;
    }
};''',

    'plus-one-linked-list': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        ListNode* p = reverse(head);
        ListNode* tmp = p;
        while(p->val + 1 == 10){
            p->val = 0;
            if(!p->next) p->next = new ListNode(0);
            p = p->next;
        }
        p->val += 1;
        return reverse(tmp);
    }
    
    ListNode* reverse(ListNode* head){
        ListNode* pre = NULL, *cur = head, *next;
        while(cur){
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
};''',

    'find-k-pairs-with-smallest-sums': '''// Solution 1. MinHeap, time: O(m * n * log(m*n))
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        auto comp = [](pair<int, int>& p1, pair<int, int>& p2){ return p1.first + p1.second > p2.first + p2.second; };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)>pq(comp);
        for(auto x: nums1) 
            for(auto y: nums2) pq.push({x, y});
        vector<pair<int, int>>res;
        while(k-- && !pq.empty()) res.push_back(pq.top()), pq.pop();
        return res;
    }
};

// Solution 2. MaxHeap, time: O(m * n * log(k)).
class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        auto comp = [](pair<int, int>& p1, pair<int, int>& p2){ return p1.first + p1.second < p2.first + p2.second; };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)>pq(comp);
        for(auto x: nums1) 
            for(auto y: nums2){
                pq.push({x, y});
                if(pq.size() > k) pq.pop();
            }
        vector<pair<int, int>>res;
        while(!pq.empty()) res.push_back(pq.top()), pq.pop();
        return res;
    }
};''',

    'combination-sum-iv': '''class Solution {
private:
    unordered_map<int, int>m;
public:
    int combinationSum4(vector<int>& nums, int target) {
        if(target == 0) return 1;
        if(m.count(target) > 0) return m[target];
        int sum = 0;
        for(auto  x: nums)
            if(target >= x)
                sum += combinationSum4(nums, target - x);
        m[target] = sum;
        return sum;
    }
};''',

    'kth-smallest-element-in-a-sorted-matrix': '''// Solution 1. MinHeap
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int, vector<int>, greater<int>>pq;
        for(auto x: matrix)
            for(auto y: x) pq.push(y);
        while(--k) pq.pop();
        return pq.top();
    }
};

// Solution 2. Multiset
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        multiset<int>s;
        for(auto x: matrix)
            for(auto y: x) s.insert(y);
        auto p = s.begin();
        while(--k) p++;
        return *p;
    }
};''',

    'insert-delete-getrandom-o-1': '''// 92ms, O(n) getRandom()
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(s.count(val)) return false;
        s.insert(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(!s.count(val)) return false;
        s.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        auto p = s.begin();
        advance(p, rand() % s.size());
        return *p;
    }

private:
    unordered_set<int>s;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

// 48ms, O(1)
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}    
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(m.count(val)) return false;
        m[val] = v.size();
        v.push_back(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(!m.count(val)) return false;
        int num = v.back();
        m[num] = m[val];
        v[m[val]] = num;
        v.pop_back();
        m.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return v[rand() % v.size()];
    }

private:
    unordered_map<int, int>m;
    vector<int>v;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */''',

    'linked-list-random-node': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
    ListNode* head;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int cnt = 1;
        ListNode* p = head, *res;
        while(p){
            if(rand() % cnt == 0) res = p;
            p = p->next;
            cnt++;
        }
        return res->val;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int count = 1;
        ListNode* p = head;
        int res = p->val;
        while (p->next) {
            p = p->next;
            ++count;
            int num = rand() % count + 1;
            if (num == count) {
                res = p->val;
            }
        }
        return res;
    }

private:
    ListNode* head;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */''',

    'decode-string': '''class Solution {
public:
    string decodeString(string s) {
        if(s.empty()) return "";
        string res = "";
        int i = 0, j = 0;
        while(j < s.size()){
            while(j < s.size() && isalpha(s[j])) j++;
            res += s.substr(i, j - i);
            i = j;
            if(j == s.size()) break;
            while(isdigit(s[j])) j++;
            int k = stoi(s.substr(i, j - i));
            int cnt = 1;
            i = j + 1;
            while(cnt != 0)
                if(s[++j] == ']') cnt--;
                else if(s[j] == '[') cnt++;
            while(k--) res += decodeString(s.substr(i, j - i));
            i = ++j;
        }
        return res;
    }
};''',

    'random-pick-index': '''class Solution {
public:
    Solution(vector<int> nums) {
        this->nums = nums;
    }
    
    int pick(int target) {
        int res = -1, count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != target) continue;
            if(res == -1) res = i, count++;
            else{
                count++;
                if(rand() % count == 0) res = i;
            }
        }
        return res;
    }
    
private:
    vector<int>nums;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */''',

    'evaluate-division': '''class Solution {
private:
    unordered_map<string, unordered_map<string, double>>weight;
    unordered_map<string, vector<string>>graph;
public:
    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) {
        vector<double>res;
        for(int i = 0; i < values.size(); i++){
            auto p = equations[i];
            weight[p.first][p.second] = values[i];
            weight[p.second][p.first] = 1 / values[i];
            graph[p.first].push_back(p.second);
            graph[p.second].push_back(p.first);
        }
        for(int i = 0; i < queries.size(); i++){
            unordered_set<string>visited;
            deque<pair<string, double>>cur;
            deque<pair<string, double>>next;
            cur.push_back({queries[i].first, 1});
            double d = -1.0;
            if(graph.count(queries[i].first))
                while(!cur.empty()){
                    auto node = cur.front();
                    cur.pop_front();
                    visited.insert(node.first);
                    if(node.first == queries[i].second){
                        d = node.second;
                        break;
                    }
                    for(auto neigh: graph[node.first])
                        if(visited.count(neigh) == 0)
                            next.push_back({neigh, node.second * weight[node.first][neigh]});
                    if(cur.empty()) swap(cur, next);
                }
            res.push_back(d);
        }
        return res;
    }
};

class Solution {
public:
    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) {
        vector<double>res;
        unordered_map<string, vector<string>>g;
        unordered_map<string, unordered_map<string, double>>w;
        // Build graph
        for (int i = 0; i < equations.size(); ++i) {
            string a = equations[i].first;
            string b = equations[i].second;
            g[a].push_back(b);
            g[b].push_back(a);
            w[a][b] = values[i];
            w[b][a] = 1/values[i];
        }
        
        for (auto& q: queries) {
            string from = q.first;
            string dest = q.second;
            
            if (!g.count(from) || !g.count(dest)) {
                res.push_back(-1);
                continue;
            }
            
            // BFS
            unordered_set<string>visited;
            queue<pair<string, double>>cur, next;
            cur.push({from, 1});
            bool found = false;
            while(!cur.empty()) {
                auto node = cur.front();
                cur.pop();
                
                string s = node.first;
                double val = node.second;
                
                visited.insert(s);
                
                if (s == dest) {
                    res.push_back(val);
                    found = true;
                    break;
                }
                
                for (auto& x: g[s]) {
                    if (!visited.count(x)) {
                        next.push({x, val * w[s][x]});
                    }
                }
                if (cur.empty()) {
                    swap(cur, next);
                }
            }
            if (!found) {
                res.push_back(-1);
            }
        }
        return res;
    }
};''',

    'remove-k-digits': '''class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.size(), remain = n - k;
        if(remain == 0) return "0";
        string s = "";
        for(auto x: num){
            while(n > remain && !s.empty() && s.back() - '0' > x - '0'){
                s.pop_back();
                n--;
            }
            s.push_back(x);
        }
        int i = 0;
        while(i < s.size() && s[i] == '0') i++;
        return s.substr(i, remain) == "" ? "0" : s.substr(i, remain);
    }
};''',

    'sum-of-left-leaves': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Recursive
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        return !root ? 0 : (root->left && !root->left->left && !root->left->right ? root->left->val : 0) + 
                           sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
};

// Iterative
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root) return 0;
        stack<TreeNode*>s;
        int sum = 0;
        while(!s.empty() || root){
            while(root){
                s.push(root);
                root = root->left;
                if(root && !root->left && !root->right) sum += root->val;
            }
            root = s.top()->right;
            s.pop();
        }
        return sum;
    }
};''',

    'valid-word-abbreviation': '''class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int i = 0, j = 0;
        while(i < word.size() && j < abbr.size())
            if(isdigit(abbr[j])){ 
                if(abbr[j] == '0') return false;
                int k = j + 1;
                while(k < abbr.size() && isdigit(abbr[k])) k++;
                i += stoi(abbr.substr(j, k - j));
                j = k;
            }
            else if(word[i++] != abbr[j++]) return false;
        return i == word.size() && j == abbr.size();
    }
};''',

    'longest-palindrome': '''class Solution {
public:
    int longestPalindrome(string s) {
        int odd = 0;
        unordered_map<char, int>m;
        for(auto c: s) odd += m[c]++ % 2 ? -1 : 1;
        return min(s.size(), s.size() - odd + 1);
    }
};''',

    'minimum-unique-word-abbreviation': '''class Solution {
public:
    string minAbbreviation(string target, vector<string>& dictionary) {
        string res = "";
        bool found = false;
        for(int i = 0; i <= target.size() && !found; i++) DFS(dictionary, i, 0, target, res, found, vector<int>());
        return res;
    }
    // k: number of letters to pick
    // vec: indices of letters picked
    void DFS(vector<string>& dictionary, int k, int pos, string target, string& res, bool& found, vector<int> vec){
        if(k == 0){  
            int i = 0;
            for(; i < dictionary.size(); i++){
                if(dictionary[i].size() != target.size()) continue;  // word of different length won't cause conflict
                int count = 0;
                for(int x: vec) if(target[x] == dictionary[i][x]) count++;
                if(vec.empty() || count == vec.size()) break;  // encounter a conflict word
            }
            if(i == dictionary.size()){
                found = true;
                if(vec.empty()){
                    res = to_string(target.size());
                    return;
                }
                // translate 'vec' into abbreviation(string)
                string s = "";
                sort(vec.begin(), vec.end());
                for(int j = 0; j < vec.size(); s += target[vec[j]], j++)
                    if(j == 0) s += (vec[0] == 0) ? "" : to_string(vec[0]);
                    else s += (vec[j] - vec[j - 1] - 1 == 0) ? "" : to_string(vec[j] - vec[j - 1] - 1);
                if(vec.back() != target.size() - 1) s += to_string(target.size() - vec.back() - 1);
                if(res.empty() || length(res) > length(s)) res = s;
            }
            return;
        }
        if(pos == target.size()) return;
        DFS(dictionary, k, pos + 1, target, res, found, vec);
        vec.push_back(pos);
        DFS(dictionary, k - 1, pos + 1, target, res, found, vec);
    }
    
    int length(string& s){
        int len = 0;
        for(int i = 0; i < s.size(); i++, len++)
            if(isdigit(s[i])) while(i + 1 < s.size() && isdigit(s[i + 1])) i++;
        return len;
    }
};''',

    'fizz-buzz': '''class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>res;
        for(int i = 1; i < n + 1; i++){
            string s = to_string(i);
            if(i % 15 ==0) s = "FizzBuzz";
            else if(i % 3 == 0) s = "Fizz";
            else if(i % 5 == 0) s = "Buzz";
            res.push_back(s);
        }
        return res;
    }
};''',

    'partition-equal-subset-sum': '''class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
        int sum = 0;
        for(auto x: nums) sum += x;
        if(sum % 2) return false;
        vector<vector<bool>>dp(nums.size(), vector<bool>(sum / 2 + 1, false));
        dp[0][0] = true;
        for(int i = 1; i < nums.size(); i++)
            for(int j = 0; j < sum / 2 + 1; j++)
                dp[i][j] = dp[i - 1][j] || ((j >= nums[i]) ? dp[i - 1][j - nums[i]] : 0);
        return dp[nums.size() - 1][sum / 2];
    }
};''',

    'pacific-atlantic-water-flow': '''class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int>>res;
        if(matrix.empty()) return res;
        int m = matrix.size(), n = matrix[0].size();
        dir = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                bool reachP = false, reachA = false;
                DFS(res, matrix, i, j, m, n, reachP, reachA);
                if(reachP && reachA) res.push_back({i, j});
            }
        return res;
    }
    
    void DFS(vector<pair<int, int>>& res, vector<vector<int>>& matrix, int r, int c, int m, int n, bool& reachP, bool& reachA){
        if(matrix[r][c] == -1 || reachP && reachA) return;
        int tmp = matrix[r][c];
        matrix[r][c] = -1;
        for(int i = 0; i < 4; i++){
            int R = r + dir[i].first, C = c + dir[i].second;
            if(R < 0 || C < 0) reachP = true;
            else if(R == m || C == n) reachA = true;
            else if(matrix[R][C] <= tmp) DFS(res, matrix, R, C, m, n, reachP, reachA);
        }
        matrix[r][c] = tmp;
    }
    
private:
    vector<pair<int, int>>dir;
};''',

    'sentence-screen-fitting': '''class Solution {
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        int count = 0, n = sentence.size(), idx = 0;
        for (int i = 0; i < rows; ++i) {
            int slot = cols;
            while (slot > 0 && slot >= sentence[idx].size()) {
                slot -= sentence[idx].size() + 1;
                ++idx;
                if (idx == n) {
                    ++count;
                    idx = 0;
                }
            }
        }
        return count;
    }
};''',

    'minimum-genetic-mutation': '''class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        int step = 1;
        deque<string>cur;
        deque<string>next;
        cur.push_back(start);
        while(!cur.empty()){
            string node = cur.front();
            cur.pop_front();
            for(auto& s: bank){
                if(s == "" || !isNeighbor(node, s)) continue;
                if(s == end) return step;
                next.push_back(s);
                s = "";
            }
            if(cur.empty()){
                step++;
                swap(cur, next);
            }
        }
        return -1;
    }
    
    bool isNeighbor(const string& a, const string& b){
        int diff = 0;
        for(int i = 0; i < a.size(); i++) if(a[i] != b[i] && ++diff > 1) return false;
        return diff == 1;
    }
};''',

    'non-overlapping-intervals': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), [](Interval& a, Interval& b){ return a.start < b.start; });
        int count = 0;
        for(int i = 1,  j = 0; i < intervals.size(); i++){
            int pre = i;
            if(intervals[i].start < intervals[j].end){
                count++;
                if(intervals[i].end > intervals[j].end) pre = j;
            }
            j = pre;
        }
        return count;
    }
};''',

    'find-right-interval': '''/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<int> findRightInterval(vector<Interval>& intervals) {
        vector<int>res;
        map<int, int>m;
        for(int i = 0; i < intervals.size(); i++) m[intervals[i].start] = i;
        for(auto i: intervals){
            auto p = m.lower_bound(i.end);
            res.push_back(p == m.end() ? -1 : (*p).second);
        }
        return res;
    }
};''',

    'find-all-anagrams-in-a-string': '''class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int>res;
        unordered_map<char, int>m;
        for(auto c: p) m[c]++;
        int i = 0, j = 0, count = p.size();
        while(j < s.size()){
            if(m[s[j++]]-- > 0) count--;
            while(count == 0){
                if(j - i == p.size()) res.push_back(i);
                if(m[s[i++]]++ == 0) count++;
            }
        }
        return res;
    }
};''',

    'arranging-coins': '''class Solution {
public:
    int arrangeCoins(int n) {
        int i = 1;
        while(n >= i) n -= i, i++;
        return i - 1;
    }
};

// Math solution from this thread https://discuss.leetcode.com/topic/65655/c-1-line-code
class Solution {
public:
    int arrangeCoins(int n) {
        return floor(-0.5+sqrt((double)2*n+0.25));
    }
};''',

    'sequence-reconstruction': '''class Solution {
public:
    bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
        int n = org.size();
        unordered_map<int, unordered_set<int>>graph;
        vector<int>indegree(n + 1, -1);
        for(auto v: seqs)
            for(int i = 0; i < v.size(); i++){
                if(v[i] > n || v[i] < 0) return false;
                if(indegree[v[i]] == -1) indegree[v[i]] = 0;
                if(i + 1 < v.size() && graph[v[i]].insert(v[i + 1]).second)
                    if(v[i + 1] > n || v[i + 1] < 0) return false;
                    else indegree[v[i + 1]] += indegree[v[i + 1]] < 0 ? 2 : 1;
            }
        for(int i = 0; i < n - 1; i++)
            if(indegree[org[i]] || !indegree[org[i + 1]]) return false;
            else for(auto x: graph[org[i]]) indegree[x]--;
        return indegree[org.back()] == 0;
    }
};''',

    'delete-node-in-a-bst': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        TreeNode* head = new TreeNode(0);
        head->left = root;
        dfs(head, root, key);
        return head->left;
    }
    
    void dfs(TreeNode* pre, TreeNode* cur, int key){
        if(!cur) return;
        cur->val > key ? dfs(cur, cur->left, key) : cur->val < key ? dfs(cur, cur->right, key) : helper(pre, cur);
    }
    
    void helper(TreeNode* pre, TreeNode* cur){
        TreeNode* p = cur->left;
        while(p && p->right) p = p->right;
        p ? p->right = cur->right : cur->left = cur->right;
        cur == pre->left ? pre->left = cur->left : pre->right = cur->left;
    }
};


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) {
            return NULL;
        }
        TreeNode* head = new TreeNode(0);
        head->left = root;
        TreeNode* parent;
        TreeNode* node = dfs(root, head, key, parent);
        if (!node) {
            return root;
        }
        
        TreeNode* l = node->left;
        TreeNode* r = node->right;
        TreeNode* p = r;
        while (p && p->left) {
            p = p->left;
        }
        if (!r) {
            r = l;
        } else if (p) {
            p->left = l;
        }
        if (node == parent->left) {
            parent->left = r;
        } else {
            parent->right = r;
        }
        return head->left;
    }
    
    TreeNode* dfs(TreeNode* cur, TreeNode* pre, int key, TreeNode*& parent) {
        if (!cur) {
            return NULL;
        }
        if (cur->val == key) {
            parent = pre;
            return cur;
        }
        
        if (cur->val > key) {
            return dfs(cur->left, cur, key, parent);
        } else {
            return dfs(cur->right, cur, key, parent);
        }
    }
};''',

    'sort-characters-by-frequency': '''class Solution {
public:
    string frequencySort(string s) {
        string res = "";
        unordered_map<char, int>m;
        for(auto c: s) m[c]++;
        auto comp = [](pair<int, char>& a, pair<int, char>& b){ return a.first < b.first; };
        priority_queue<pair<int, char>, vector<pair<int, char>>, decltype(comp)>pq(comp);
        for(auto x: m) pq.push({x.second, x.first});
        while(!pq.empty()){
            auto p = pq.top();
            pq.pop();
            while(p.first--) res += p.second;
        }
        return res;
    }
};''',

    'hamming-distance': '''class Solution {
public:
    int hammingDistance(int x, int y) {
        int n = x^y;
        int d = 0;
        while(n) n &= n-1, d++;
        return d;
    }
};''',

    'unique-substrings-in-wraparound-string': '''class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int>dp(26);
        int len = 0;
        for(int i = 0; i < p.size(); i++){
            len = (i > 0 && (p[i] - p[i - 1] == 1 || p[i] - p[i - 1] == -25)) ? len + 1 : 1;
            dp[p[i] - 'a'] = max(dp[p[i] - 'a'], len);
        }
        int sum = 0;
        for(int x: dp) sum += x;
        return sum;
    }
};''',

    'matchsticks-to-square': '''class Solution {
public:
    bool makesquare(vector<int>& nums) {
        int sum = 0, maxlen = 0, n = nums.size();
        for(int x: nums) sum += x, maxlen = max(maxlen, x);
        int size = sum / 4;
        if(sum == 0 || sum % 4 || maxlen > size ) return false;
        vector<int>visited(n, 0);
        return DFS(nums, visited, 0, 0, size, n, 0, false);
    }
    
    bool DFS(vector<int>& nums, vector<int>& visited, int pos, int length, int size, int n, int count, bool newSide){
        if(length > size) return false;
        if(length == size) count++, length = 0, newSide = true;
        if(count == 3) return true;
        
        length += nums[pos];
        visited[pos] = 1;
        
        for(int i = newSide ? 0 : pos + 1; i < n; i++)
            if(!visited[i] && DFS(nums, visited, i, length, size, n, count, false))
                return true;  
        
        visited[pos] = 0;
        return false;
    }
};''',

    'total-hamming-distance': '''// O(n)
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int distance = 0;
        for(int i = 0; i < 32; i++){
            int one = 0, zero = 0;
            for(auto x: nums) (x & (1 << i)) ? one++ : zero++;
            distance += one * zero;
        }
        return distance;
    }
};

// Brute Force, O(n^2), TLE
/*
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int distance = 0;
        for(int i = 0; i < nums.size(); i++)
            for(int j = i + 1; j < nums.size(); j++)
                distance += helper(nums[i] ^ nums[j]);
        return distance;
    }
    
    int helper(int c){
        int sum = 0;
        while(c){
            sum++;
            c &= c - 1;
        }
        return sum;
    }
};
*/''',

    'license-key-formatting': '''class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        stringstream ss(S);
        string s = "", tmp = "", res = "";
        while(getline(ss, tmp, '-')) s += tmp;
        for(auto& c: s) c = toupper(c);
        int i = 0, step = (s.size() % K == 0) ? K : s.size() % K;
        while(i < s.size()){
            res += s.substr(i, step) + '-';
            i += step;
            step = K;
        }
        res.pop_back();
        return res;
    }
};''',

    'find-permutation': '''class Solution {
public:
    vector<int> findPermutation(string s) {
        vector<int>res;
        for(int i = 1; i <= s.size() + 1; i++) res.push_back(i);
        for(int i = 0; i < s.size(); i++){
            int j = i;
            while(j < s.size() && s[j] == 'D') j++;
            reverse(res.begin() + i, res.begin() + j + 1);
            i = j;
        }
        return res;
    }
};''',

    'predict-the-winner': '''class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        vector<int>score(2);
        return solve(nums, score, 0, 0, nums.size() - 1);
    }
    
    bool solve(vector<int>& nums, vector<int>& score, int player, int l, int r) {
        if (l >= r) {
            return score[0] >= score[1];
        }
        
        if (player == 0) {
            // Pick left
            score[0] += nums[l];
            if (solve(nums, score, player ^ 1, l + 1, r)) {
                score[0] -= nums[l];
                return true;
            }
            score[0] -= nums[l];
            // Pick right
            score[0] += nums[r];
            if (solve(nums, score, player ^ 1, l, r - 1)) {
                score[0] -= nums[r];
                return true;
            }
            score[0] -= nums[r];
        } else {
            // Pick left
            score[1] += nums[l];
            if (!solve(nums, score, player ^ 1, l + 1, r)) {
                score[1] -= nums[l];
                return false;
            }
            score[1] -= nums[l];
            // Pick right
            score[1] += nums[r];
            if (!solve(nums, score, player ^ 1, l, r - 1)) {
                score[1] -= nums[r];
                return false;
            }
            score[1] -= nums[r];
        }
        return player;
    }
};''',

    'max-consecutive-ones-ii': '''class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, l = 0, r = 0, count = 0;
        while(r < nums.size()){
            if(nums[r++] == 0) count++;
            while(count > 1) if(nums[l++] == 0) count--;
            res = max(res, r - l);
        }
        return res;
    }
};''',

    'robot-room-cleaner': '''/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */
class Solution {
public:
    void cleanRoom(Robot& robot) {
        unordered_set<string>visited;
        dfs(robot, 0, 0, visited);
    }
    
    // Robot always facing UP
    void dfs(Robot& R, int r, int c, unordered_set<string>& visited) {
        if (visited.count(tostr(r, c))) {
            return;
        }
        R.clean();
        visited.insert(tostr(r, c));
        
        // Go through each direction, robot ALWAYS ends with UP
        
        // Up
        if (R.move()) {
            dfs(R, r - 1, c, visited);
            R.turnLeft();
            R.turnLeft();
            R.move();
            R.turnLeft();
            R.turnLeft();
        }
        
        // Left
        R.turnLeft();
        if (R.move()) {
            R.turnRight();
            dfs(R, r, c - 1, visited);
            R.turnRight();
            R.move();
            R.turnLeft();
            R.turnLeft();
        } 
        R.turnRight();
        
        // Right
        R.turnRight();
        if (R.move()) {
            R.turnLeft();
            dfs(R, r, c + 1, visited);
            R.turnLeft();
            R.move();
            R.turnLeft();
            R.turnLeft();
        }
        R.turnLeft();
        
        // Down
        R.turnLeft();
        R.turnLeft();
        if (R.move()) {
            R.turnLeft();
            R.turnLeft();
            dfs(R, r + 1, c, visited);
            R.move();
            R.turnLeft();
            R.turnLeft();
        }
        R.turnLeft();
        R.turnLeft();
    }
    
    string tostr(int r, int c) {
        return to_string(r) + "," + to_string(c);
    }
};''',

    'the-maze': '''class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>>visited(m, vector<int>(n));
        return dfs(maze, start[0], start[1], destination, visited, m, n);
    }
    
    bool dfs(vector<vector<int>>& maze, int r, int c, vector<int>& destination, vector<vector<int>>& visited, int m, int n) {
        if (r == destination[0] && c == destination[1]) {
            return true;
        }
        if (visited[r][c]) {
            return false;
        }
        visited[r][c] = 1;
        bool res = false;
        // left
        int left = c;
        while (left - 1 >= 0 && maze[r][left - 1] == 0) --left;
        if (left != c) {
            res |= dfs(maze, r, left, destination, visited, m, n);
        }
        // right
        int right = c;
        while (right + 1 < n && maze[r][right + 1] == 0) ++right;
        if (right != c) {
            res |= dfs(maze, r, right, destination, visited, m, n);
        }
        // up
        int up = r;
        while (up - 1 >= 0 && maze[up - 1][c] == 0) --up;
        if (up != r) {
            res |= dfs(maze, up, c, destination, visited, m, n);
        }
        // down
        int down = r;
        while (down + 1 < m && maze[down + 1][c] == 0) ++down;
        if (down != r) {
            res |= dfs(maze, down, c, destination, visited, m, n);
        }
        
        return res;
    }
};''',

    'target-sum': '''// Backtracking
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int count = 0;
        backtrack(nums, S, 0, 0, count);
        return count;
    }
    
    void backtrack(vector<int>& nums, int S, int sum, int pos, int& count){
        if(pos == nums.size()){
            if(sum == S) count++;
            return;
        }
        backtrack(nums, S, sum + nums[pos], pos + 1, count);
        backtrack(nums, S, sum - nums[pos], pos + 1, count);
    }
};

// DP
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for(auto x: nums) sum += x;
        if(sum < S || -sum > S) return 0;
        vector<int>cur(2 * sum + 1);
        vector<int>next(2 * sum + 1);
        cur[sum] = 1;
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < 2 * sum + 1; j++){
                if(cur[j] != 0){
                    next[j + nums[i]] += cur[j];
                    next[j - nums[i]] += cur[j];
                    cur[j] = 0;
                }
            }
            swap(cur, next);
        }
        return cur[sum + S];
    }
};''',

    'next-greater-element-i': '''class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        unordered_map<int, int>m;
        stack<int>s;
        for(auto x: nums){
            while(!s.empty() && s.top() < x){
                m[s.top()] = x;
                s.pop();
            }
            s.push(x);
        }
        for(auto& x: findNums) x = m.count(x) ? m[x] : -1;
        return findNums;
    }
};''',

    'diagonal-traverse': '''class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        if(matrix.empty()) return res;
        int m = matrix.size(), n = matrix[0].size();
        vector<pair<int, int>>dir({{-1, 1}, {1, -1}});
        DFS(matrix, res, 0, 0, m, n, dir, 0);
        return res;
    }
    
    void DFS(vector<vector<int>>& matrix, vector<int>& res, int r, int c, int m, int n, vector<pair<int, int>>& dir, int d){
        if(res.size() == m * n) return;
        res.push_back(matrix[r][c]);
        int R = r + dir[d].first;
        int C = c + dir[d].second;
        if(R < 0 || C < 0 || R >= m || C >= n){
            d = (d + 1) % 2;
            if(R < 0 || R >= m) R = r, C = c + 1;
            if(C < 0 || C >= n) R = r + 1, C = c;
        }
        DFS(matrix, res, R, C, m, n, dir, d);
    }
};''',

    'the-maze-iii': '''class Solution {
public:
    string findShortestWay(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>>visited(m, vector<int>(n, INT_MAX));
        int minDis = -1;
        string res;
        dfs(maze, ball[0], ball[1], hole, visited, m, n, 0, "", minDis, res);
        return res.empty() ? "impossible" : res;
    }
    
    void dfs(vector<vector<int>>& maze, int r, int c, vector<int>& destination, vector<vector<int>>& visited, int m, int n, 
             int path, string cur, int& minDis, string& res) {
        if (path > visited[r][c]) {
            return;
        }
        visited[r][c] = path;
        // left
        int left = c;
        int leftPath = path;
        string curLeft = cur + "l";
        while (left - 1 >= 0 && maze[r][left - 1] == 0) {
            --left;
            ++leftPath;
            
            if (r == destination[0] && left == destination[1]) {
                updateResult(leftPath, curLeft, minDis, res);
                return;
            }
        }
        if (left != c) {
            dfs(maze, r, left, destination, visited, m, n, leftPath, curLeft, minDis, res);
        }
        // right
        int right = c;
        int rightPath = path;
        string curRight = cur + "r";
        while (right + 1 < n && maze[r][right + 1] == 0) {
            ++right;
            ++rightPath;
            
            if (r == destination[0] && right == destination[1]) {
                updateResult(rightPath, curRight, minDis, res);
                return;
            }
        }
        if (right != c) {
            dfs(maze, r, right, destination, visited, m, n, rightPath, curRight, minDis, res);
        }
        // up
        int up = r;
        int upPath = path;
        string curUp = cur + "u";
        while (up - 1 >= 0 && maze[up - 1][c] == 0) {
            --up;
            ++upPath;
            
            if (up == destination[0] && c == destination[1]) {
                updateResult(upPath, curUp, minDis, res);
                return;
            }
        }
        if (up != r) {
            dfs(maze, up, c, destination, visited, m, n, upPath, curUp, minDis, res);
        }
        // down
        int down = r;
        int downPath = path;
        string curDown = cur + "d";
        while (down + 1 < m && maze[down + 1][c] == 0) {
            ++down;
            ++downPath;
            
            if (down == destination[0] && c == destination[1]) {
                updateResult(downPath, curDown, minDis, res);
                return;
            }
        }
        if (down != r) {
            dfs(maze, down, c, destination, visited, m, n, downPath, curDown, minDis, res);
        }
    }
    
    void updateResult(int path, string cur, int& minDis, string& res) {
        if (minDis == -1 || path < minDis) {
            minDis = path;
            res = cur;
        } else if (path == minDis && cur < res) {
            res = cur;   
        }
    }
};''',

    'next-greater-element-ii': '''// Solution 1. Brute force, O(n^2)
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int>res;
        for(int i = 0; i < nums.size(); i++){
            int j = (i + 1) % n;
            while(j != i){
                if(nums[j] > nums[i]) break;
                ++j %= n;
            }
            res.push_back(j == i ? -1 : nums[j]);
        }
        return res;
    }
};

// Solution 2. Using a stack and a deque, O(n)
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int>res(nums.size(), -1);
        stack<int>s; // decreasing sequence
        deque<int>q; // Increasing sequence
        for(int i = 0; i < nums.size(); i++){
            if(q.empty() || nums[i] > q.back()) q.push_back(nums[i]);
            while(!s.empty() && nums[i] > nums[s.top()]){
                res[s.top()] = nums[i];
                s.pop();
            }
            s.push(i);
        }
        while(!s.empty()){
            while(!q.empty() && nums[s.top()] >= q.front()) q.pop_front();
            if(!q.empty()) res[s.top()] = q.front();
            s.pop();
        }
        return res;
    }
};

// Solution 3.
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        deque<vector<int>>q;
        vector<int>res(n, -1);
        for (int i = 0; i < n*2; ++i) {
            while (!q.empty() && q.back()[0] < nums[i%n]) {
                auto v = q.back();
                q.pop_back();
                res[v[1]] = nums[i%n];
            }
            q.push_back({nums[i%n], i%n});
        }
        return res;
    }
};''',

    'the-maze-ii': '''class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        vector<vector<vector<int>>>dp(maze.size(), vector<vector<int>>(maze[0].size(), vector<int>(4, INT_MAX)));
        int minDis = INT_MAX;
        for(int i = 0; i < 4; i++)
            DFS(maze, i, start[0], start[1], destination[0], destination[1], minDis, 0, dp);
        return minDis == INT_MAX ? -1 : minDis;
    }
    
    bool DFS(vector<vector<int>>& maze, int d, int a, int b, int x, int y, int& minDis, int dis, vector<vector<vector<int>>>& dp){
        if(a < 0 || b < 0 || a == maze.size() || b == maze[0].size() || maze[a][b] == 1) return false;
        if(dis >= minDis || dis >= dp[a][b][d]) return true;
        dp[a][b][d] = min(dp[a][b][d], dis);
        if(!DFS(maze, d, a + directions[d].first, b + directions[d].second, x, y, minDis, dis + 1, dp)){
            if(a == x && b == y){
                minDis = min(minDis, dis);
                return true;
            }
            for(auto dir: nextDir(d))
                DFS(maze, dir, a + directions[dir].first, b + directions[dir].second, x, y, minDis, dis + 1, dp);
        }
        return true;
    }
    
private:
    vector<pair<int, int>>directions;
    vector<int> nextDir(int d){
        if(d == 0 || d == 3) return {1, 2};
        if(d == 1 || d == 2) return {0, 3};
    }
};


class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>>visited(m, vector<int>(n, INT_MAX));
        int minDis = -1;
        dfs(maze, start[0], start[1], destination, visited, m, n, 0, minDis);
        return minDis;
    }
    
    void dfs(vector<vector<int>>& maze, int r, int c, vector<int>& destination, vector<vector<int>>& visited, int m, int n, 
             int path, int& minDis) {
        if (r == destination[0] && c == destination[1]) {
            if (minDis == -1) {
                minDis = path;
            } else {
                minDis = min(minDis, path);
            }
        }
        if (path >= visited[r][c]) {
            return;
        }
        visited[r][c] = path;
        // left
        int left = c;
        int leftPath = path;
        while (left - 1 >= 0 && maze[r][left - 1] == 0) {
            --left;
            ++leftPath;
        }
        if (left != c) {
            dfs(maze, r, left, destination, visited, m, n, leftPath, minDis);
        }
        // right
        int right = c;
        int rightPath = path;
        while (right + 1 < n && maze[r][right + 1] == 0) {
            ++right;
            ++rightPath;
        }
        if (right != c) {
            dfs(maze, r, right, destination, visited, m, n, rightPath, minDis);
        }
        // up
        int up = r;
        int upPath = path;
        while (up - 1 >= 0 && maze[up - 1][c] == 0) {
            --up;
            ++upPath;
        }
        if (up != r) {
            dfs(maze, up, c, destination, visited, m, n, upPath, minDis);
        }
        // down
        int down = r;
        int downPath = path;
        while (down + 1 < m && maze[down + 1][c] == 0) {
            ++down;
            ++downPath;
        }
        if (down != r) {
            dfs(maze, down, c, destination, visited, m, n, downPath, minDis);
        }
    }
};''',

    'most-frequent-subtree-sum': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        vector<int>res;
        unordered_map<int, int>m;
        DFS(root, m);
        int maxFreq = 0;
        for(auto x: m)
            if(x.second > maxFreq) res.clear(), res.push_back(x.first), maxFreq = x.second;
            else if(x.second == maxFreq) res.push_back(x.first);
        return res;
    }
    
    int DFS(TreeNode* root, unordered_map<int, int>& m){
        if(!root) return 0;
        int l = DFS(root->left, m);
        int r = DFS(root->right, m);
        int sum = root->val + l + r;
        m[sum]++;
        return sum;
    }
};''',

    'find-bottom-left-tree-value': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        int res = 0, maxLevel = -1;
        DFS(root, 0, maxLevel, res);
        return res;
    }
    
    void DFS(TreeNode* root, int level, int& maxLevel, int& res){
        if(!root) return;
        DFS(root->left, level + 1, maxLevel, res);
        DFS(root->right, level + 1, maxLevel, res);
        if(level > maxLevel) res = root->val;
        maxLevel = max(maxLevel, level);
    }
};''',

    'find-largest-value-in-each-tree-row': '''// BFS
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if(!root) return {};
        vector<int>res;
        deque<TreeNode*>cur, next;
        cur.push_back(root);
        int val = INT_MIN;
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            if(p->left) next.push_back(p->left);
            if(p->right) next.push_back(p->right);
            val = max(val, p->val);
            if(cur.empty()){
                swap(cur, next);
                res.push_back(val);
                val = INT_MIN;
            }
        }
        return res;
    }
};

// DFS
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int>res;
        DFS(root, res, 0);
        return res;
    }
    
    void DFS(TreeNode* root, vector<int>& res, int level){
        if(!root) return;
        if(res.size() == level) res.push_back(root->val);
        res[level] = max(res[level], root->val);
        DFS(root->left, res, level + 1);
        DFS(root->right, res, level + 1);
    }
};''',

    'continuous-subarray-sum': '''class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        k = abs(k);
        int sum = 0;
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            if(i < nums.size() - 1 && nums[i] == 0 && nums[i + 1] == 0) return true;
            if(k != 0 && sum % k == 0 && i > 0) return true;
            for(int j = 0; k != 0 && j*k < sum; j++)
                if(m.count(sum - j*k) > 0 && i - m[sum - j*k] > 0) return true;
            m[sum] = i;
        }
        return false;
    }
};''',

    'longest-word-in-dictionary-through-deleting': '''class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        vector<int>p(d.size());
        int maxlen = 0;
        string res = "";
        for(auto c: s)
            for(int i = 0; i < d.size(); i++){
                if(p[i] == d[i].size()) continue;
                if(c == d[i][p[i]]) p[i]++;
            }
        for(int i = 0; i < p.size(); i++){
            if(p[i] != d[i].size()) continue;
            if(p[i] == maxlen && d[i].compare(res) < 0) res = d[i];
            if(p[i] > maxlen){
                maxlen = p[i];
                res = d[i];
            }
        }
        return res;
    }
};''',

    'contiguous-array': '''class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        for(auto& x: nums) if(!x) x = -1;
        unordered_map<int, int>m;
        m[0] = -1;
        int sum = 0, maxlen = 0;
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            if(m.count(sum)) maxlen = max(maxlen, i - m[sum]);
            else m[sum] = i;
        }
        return maxlen;
    }
};''',

    'lonely-pixel-i': '''class Solution {
public:
    int findLonelyPixel(vector<vector<char>>& picture) {
        if(picture.empty()) return 0;
        int m = picture.size(), n = picture[0].size();
        int count = 0;
        for(int i = 0; i < m; i++){
            bool B = true;
            for(int j = 0; j < n && B; j++){
                if(picture[i][j] == 'B'){
                    B = false;
                    int r = 0, c = j + 1;
                    for(; r < m; r++) if(r != i && picture[r][j] == 'B') break;
                    for(; c < n; c++) if(picture[i][c] == 'B') break;
                    if(r == m && c == n) count++;
                }
            }
        }
        return count;
    }
};''',

    'encode-and-decode-tinyurl': '''class Solution {
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        v.push_back(longUrl);
        return to_string(v.size() - 1);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return v[stoi(shortUrl)];
    }
    
private:
    vector<string>v;
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));

// Best answer (joke).
class Solution {
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        return longUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return shortUrl;
    }
};''',

    'construct-binary-tree-from-string': '''class Solution {
public:
    TreeNode* str2tree(string s) {
        if(s.empty()) return NULL;
        int i = 0;
        while(i < s.size() && (isdigit(s[i]) || s[i] == '-')) i++;
        TreeNode* root = new TreeNode(stoi(s.substr(0, i)));
        int j = i, k = 0;
        while(j < s.size()){
            if(s[j] == '(') k++;
            else if(s[j] == ')') k--;
            if(k == 0){
                if(!root->left) root->left = str2tree(s.substr(i + 1, j - i - 1));
                else root->right = str2tree(s.substr(i + 1, j - i - 1));
                i = j + 1;
            }
            j++;
        }
        return root;
    }
};''',

    'convert-bst-to-greater-tree': '''class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        int sum = 0;
        DFS(root, sum);
        return root;
    }
    
    void DFS(TreeNode* root, int& sum){
        if(!root) return;
        DFS(root->right, sum);
        sum = (root->val += sum);
        DFS(root->left, sum);
    }
};''',

    'single-element-in-a-sorted-array': '''class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int lo = 0, hi = nums.size() - 1;
        int mid = (lo + hi) / 2;
        while(lo < hi - 2){
            if(nums[mid] == nums[mid + 1]) mid++;
            if((hi - mid) % 2) lo = mid + 1;
            else hi = mid;
            mid = (lo + hi) / 2;
        }
        return nums[lo] == nums[lo + 1] ? nums[hi] : nums[lo];
    }
};''',

    'reverse-string-ii': '''class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.size();
        for(int i = 0; i < n; i += 2*k)
            reverse(s.begin() + i, s.begin() + min(i + k, n));
        return s;
    }
};''',

    '01-matrix': '''class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<pair<int, int>>dir({{0, 1}, {1, 0}, {-1, 0}, {0, -1}});
        deque<pair<int, int>>q;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(matrix[i][j]) matrix[i][j] = INT_MAX;
                else q.push_back({i, j});
        //BFS
        while(!q.empty()){
            auto p = q.front();
            q.pop_front();
            for(auto x: dir){
                int r = p.first + x.first;
                int c = p.second + x.second;
                if(r < 0 || c < 0 || r == m || c == n) continue;
                if(matrix[r][c] >= matrix[p.first][p.second] + 1){
                    matrix[r][c] = matrix[p.first][p.second] + 1;
                    q.push_back({r, c});
                }
            }
        }
        return matrix;
    }
};''',

    'diameter-of-binary-tree': '''class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        int left = DFS(root->left);
        int right = DFS(root->right);
        return max(left + right, max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)));
    }
    
    int DFS(TreeNode* root){
        if(!root) return 0;
        return 1 + max(DFS(root->left), DFS(root->right));
    }
};

// Update(08/28/2017):
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxLen = 0;
        DFS(root, maxLen);
        return maxLen;
    }

private:
    int DFS(TreeNode* root, int& maxLen){
        if(!root) return 0;
        int left = DFS(root->left, maxLen);
        int right = DFS(root->right, maxLen);
        maxLen = max(maxLen, left + right);
        return max(left, right) + 1;
    }
};''',

    'friend-circles': '''class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        vector<int>Tags(M.size());
        int tag = 0;
        for(int i = 0; i < M.size(); i++){
            if(Tags[i]) continue;
            Tags[i] = ++tag;
            for(int j = 0; j < M[0].size(); j++){
                if(j == i || M[i][j] == 0) continue;
                if(M[i][j]){
                    M[i][j] = M[j][i] = 0;
                    DFS(Tags, M, j, tag);
                }
            }
        }
        return tag;
    }
    
    void DFS(vector<int>& Tags, vector<vector<int>>& M, int row, int tag){
        Tags[row] = tag;
        for(int i = 0; i < M[row].size(); i++){
            if(M[row][i]){
                M[row][i] = M[i][row] = 0;
                DFS(Tags, M, i, tag);
            }
        }
    }
};''',

    'binary-tree-longest-consecutive-sequence-ii': '''class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        int maxlen = 0;
        DFS(root, maxlen);
        return maxlen;
    }
    
    pair<int, int> DFS(TreeNode* root, int& maxlen){
        if(!root) return {0, 0};
        int iL = 1, dL = 1, iR = 1, dR = 1;
        auto l = DFS(root->left, maxlen);
        auto r = DFS(root->right, maxlen);
        if(root->left && root->left->val == root->val + 1) iL += l.first;
        if(root->left && root->left->val == root->val - 1) dL += l.second;
        if(root->right && root->right->val == root->val + 1) iR += r.first;
        if(root->right && root->right->val == root->val - 1) dR += r.second;
        maxlen = max(maxlen, max(iL + dR - 1, iR + dL - 1));
        return {max(iL, iR), max(dL, dR)};
    }
};''',

    'brick-wall': '''class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        if(wall.size() == 0 || wall[0].size() == 0) return 0;
        unordered_map<int, int>m;
        for(auto x: wall){
            int len = 0;
            for(int i = 0; i < x.size() - 1; i++){
                len += x[i];
                m[len]++;
            }
        }
        int n = wall.size();
        int res = n;
        for(auto x: m) res = min(res, n - x.second);
        return res;
    }
};''',

    'next-greater-element-iii': '''class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        stack<char>q;
        stack<int>idx;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (q.empty() || q.top() <= s[i]) {
                q.push(s[i]);
                idx.push(i);
            } else {
                int pos = -1;
                while (!q.empty() && q.top() > s[i]) {
                    pos = idx.top();
                    q.pop();
                    idx.pop();
                }
                swap(s[i], s[pos]);
                sort(s.begin() + i + 1, s.end());
                long l = stol(s);
                if (l > INT_MAX) return -1;
                return l;
            }
        }
        return -1;
    }
};

class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        next_permutation(s.begin(), s.end());
        auto res = stol(s);
        return (res > INT_MAX || res <= n) ? -1 : res;
        return -1;
    }
};''',

    'subarray-sum-equals-k': '''class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        unordered_map<int, int>m;
        int sum = 0;
        for(auto x: nums){
            m[sum]++;
            sum += x;
            if(m.count(sum - k) > 0) count += m[sum - k];
        }
        return count;
    }
};''',

    'longest-line-of-consecutive-one-in-matrix': '''class Solution {
public:
    int longestLine(vector<vector<int>>& M) {
        if(M.empty()) return 0;
        int maxlen = 0, m = M.size(), n = M[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(M[i][j]) BFS(M, i, j, m, n, maxlen);
        return maxlen;
    }
    
    void BFS(vector<vector<int>>& M, int r, int c, int m, int n, int& maxlen){
        int h = 1, v = 1, d_left = 1, d_right = 1;
        for(int i = c + 1; i < n && M[r][i]; i++) h++;
        for(int i = r + 1; i < m && M[i][c]; i++) v++;
        for(int i = r + 1, j = c - 1; i < m && j >= 0 && M[i][j]; i++, j--) d_left++;
        for(int i = r + 1, j = c + 1; i < m && j < n && M[i][j]; i++, j++) d_right++;
        maxlen = max(maxlen, max(max(h, v), max(d_left, d_right)));
    }
};''',

    'array-nesting': '''class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int maxDepth = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == -1) continue;
            DFS(nums, i, 0, maxDepth);
        }
        return maxDepth;
    }
    
    void DFS(vector<int>& nums, int num, int depth, int& maxDepth){
        if(nums[num] == -1){
            maxDepth = max(maxDepth, depth);
            return;
        }
        int next = nums[num];
        nums[num] = -1;
        DFS(nums, next, depth + 1, maxDepth);
    }
};''',

    'reshape-the-matrix': '''class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size(), n = nums[0].size();
        if(m * n != r * c) return nums;
        vector<vector<int>>res(r, vector<int>(c));
        int row = 0, col = 0;
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++){
                res[i][j] = nums[row][col++];
                if(col == n) col = 0, row++;
            }
        return res;
    }
};

// Or
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size(), n = nums[0].size();
        if(m * n != r * c) return nums;
        vector<vector<int>>res(r, vector<int>(c));
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                res[i][j] = nums[(i * c + j) / n][(i * c + j) % n];
        return res;
    }
};''',

    'permutation-in-string': '''class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int count = s1.size();
        unordered_map<char, int>m;
        for(auto c: s1) m[c]++;
        int l = 0, r = 0;
        while(r < s2.size()){
            if(m[s2[r++]]-- > 0) count--;
            while(count == 0){
                if(r - l == s1.size()) return true;
                if(m[s2[l++]]++ == 0) count++;
            }  
        }
        return false;
    }
};''',

    'subtree-of-another-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(!s) return !t;
        return isEqual(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t);
    }
    
    bool isEqual(TreeNode* p, TreeNode* t){
        if(!p || !t) return !p && !t;
        return p->val == t->val && isEqual(p->left, t->left) && isEqual(p->right, t->right);
    }
};''',

    'kill-process': '''class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        vector<int>res;
        unordered_map<int, vector<int>>g;
        for(int i = 0; i < pid.size(); i++) g[ppid[i]].push_back(pid[i]);
        // BFS
        deque<int>q;
        q.push_back(kill);
        while(!q.empty()){
            auto p = q.front();
            q.pop_front();
            for(auto child: g[p]) q.push_back(child);
            res.push_back(p);
        }
        // DFS
        // DFS(g, kill, res);
        return res;
    }
    
    void DFS(unordered_map<int, vector<int>>& g, int kill, vector<int>& res){
        res.push_back(kill);
        for(auto child: g[kill]) DFS(g, child, res);
    }
};''',

    'delete-operation-for-two-strings': '''class Solution {
public:
    int minDistance(string word1, string word2) {
        // dp[i][j] = word1[i - 1] == word2[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
        vector<vector<int>>dp(word1.size() + 1, vector<int>(word2.size() + 1));
        for(int i = 0; i <= word1.size(); i++)
            for(int j = 0; j <= word2.size(); j++)
                dp[i][j] = (!i || !j) ? 0 : (word1[i - 1] == word2[j - 1]) ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
        int LCS = dp[word1.size()][word2.size()];
        return (word1.size() - LCS) + (word2.size() - LCS);
    }
};''',

    'minimum-index-sum-of-two-lists': '''class Solution {
public:
	vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
		vector<string>res;
		unordered_map<string, int>m;
		int min = INT_MAX;
		for (int i = 0; i < list1.size(); i++) m[list1[i]] = i;
		for (int i = 0; i < list2.size(); i++)
			if (m.count(list2[i]) != 0)
				if (m[list2[i]] + i < min) min = m[list2[i]] + i, res.clear(), res.push_back(list2[i]);
				else if (m[list2[i]] + i == min) res.push_back(list2[i]);
				return res;
	}
};''',

    'construct-string-from-binary-tree': '''class Solution {
public:
    string tree2str(TreeNode* t) {
        if(!t) return "";
        string l = tree2str(t->left);
        string r = tree2str(t->right);
        if(!t->left && !t->right) return to_string(t->val);
        if(!t->right) return to_string(t->val) + "(" + l + ")";
        return to_string(t->val) + "(" + l + ")" + "(" + r + ")";
    }
};''',

    'valid-triangle-number': '''class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int count = 0, n = nums.size();
        for(int i = 0; i < n; i++)
            for(int j = i + 1; j < n; j++)
                for(int k = j + 1; k < n; k++)
                    if(nums[i] + nums[j] > nums[k]) count++;
        return count;
    }
};

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int count = 0, n = nums.size();
        for(int i = n - 1; i > 1; --i) {
            int l = 0, r = i - 1;
            while (l < r) {
                if (nums[l] + nums[r] > nums[i]) {
                    count += r - l;
                    --r;
                } else {
                    ++l;
                }
            }
        }
        return count;
    }
};''',

    'add-bold-tag-in-string': '''struct TrieNode{
    bool isWord = false;
    unordered_map<char, TrieNode*>next;
};

class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        string t = "";
        buildTrie(dict);
        for(int i = 0; i < s.size(); i++){
            auto p = root;
            int j = i;
            while(j < s.size() && p->next.count(s[j]))
                p = p->next[s[j++]];
            if(p != root && p->isWord){
                int pos = j;
                for(int k = i + 1; k < pos; k++){
                    int l = k;
                    auto v = root;
                    while(l < s.size() && v->next.count(s[l]))
                        v = v->next[s[l++]];
                    pos = max(pos, l);
                }
                t += '(' + s.substr(i, pos - i) + ')';
                i = pos - 1;
            }
            else t.push_back(s[i]);
        }
        string res = "";
        for(int i = 0; i < t.size(); i++){
            if(i + 1 < t.size() && t[i] == ')' && t[i + 1] == '(') i += 2;
            (t[i] == '(') ? res += "<b>" : (t[i] == ')') ? res += "</b>" : res += t[i];
        }
        return res;
    }
    
private:
    TrieNode* root;
    void buildTrie(vector<string>& dict){
        root = new TrieNode();
        for(auto x: dict){
            auto p = root;
            for(auto c: x){
                if(!p->next.count(c))
                    p->next[c] = new TrieNode();
                p = p->next[c];
            }
            p->isWord = true;
        }
    }
};''',

    'task-scheduler': '''// Solution 1. priority_queue.
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int>m;
        for(auto x: tasks) m[x]++;
        priority_queue<pair<int, char>>pq;
        for(auto x: m) pq.push(make_pair(x.second, x.first));
        int sum = 0;
        while(!pq.empty()){
            int time = 0;
            vector<pair<int, char>>v;
            for(int i = 0; i < n + 1; i++)
                if(!pq.empty()){
                    v.push_back(pq.top());
                    pq.pop();
                    time++;
                }
            for(auto x: v) if(--x.first) pq.push(x);
            sum += !pq.empty() ? n + 1 : time;
        }
        return sum;
    }
};

// Solution 2. Math
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int>m;
        int count = 0;
        for(auto x: tasks){
            m[x]++;
            count = max(count, m[x]);
        }
        int ans = (count-1) * (n + 1);
        for(auto x: m) if(x.second == count) ans++;
        return max((int)tasks.size(), ans);
    }
};''',

    'smallest-range': '''class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        vector<int>res(2);
        auto comp = [](vector<int>& a, vector<int>& b){ return a[0] > b[0]; };
        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)>pq(comp);
        int lo = 0, hi = 0, minRange = INT_MAX;
        for(int i = 0; i < nums.size(); i++) hi = max(hi, nums[i][0]), pq.push({nums[i][0], 0, i});
        while(true){
            auto v = pq.top();
            pq.pop();
            lo = v[0];
            if(hi - lo < minRange){
                minRange = min(minRange, hi - lo);
                res[0] = lo;
                res[1] = hi;
            }
            if(++v[1] == nums[v[2]].size()) break;
            v[0] = nums[v[2]][v[1]];
            pq.push(v);
            hi = max(hi, v[0]);
        }
        return res;
    }
};''',

    'sum-of-square-numbers': '''class Solution {
public:
    bool judgeSquareSum(int c) {
        for(int a = 0, b = sqrt(c); a <= sqrt(c); a++, b = sqrt(c - a * a))
            if(b * b == c - a * a) return true;
        return false;
    }
};''',

    'design-log-storage-system': '''class LogSystem {
private:
    unordered_map<int, string>log;
    unordered_map<string, int>time{{"Year", 4}, {"Month", 7}, {"Day", 10}, {"Hour", 13}, {"Minute", 16}, {"Second", 19}};

public:
    LogSystem() {}
    
    void put(int id, string timestamp) {
        log[id] = timestamp;
    }
    
    vector<int> retrieve(string s, string e, string gra) {
        vector<int>res;
        int l = time[gra];
        s = s.substr(0, l);
        e = e.substr(0, l);
        for(auto x: log){
            string t = x.second.substr(0, l);
            if(s.compare(t) <= 0 && e.compare(t) >= 0) res.push_back(x.first);
        }
        return res;
    }
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * vector<int> param_2 = obj.retrieve(s,e,gra);
 */''',

    'exclusive-time-of-functions': '''class Solution {
private:
    struct Log{
        int id;
        int time;
        int append;
        Log(int x, int y, int z): id(x), time(y), append(z){}
    };
    
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int>res(n);
        stack<Log*>s;
        int id = 0, time = 0;
        string op = "", str = "";
        for(int i = 0; i < logs.size(); i++){
            stringstream ss(logs[i]);
            getline(ss, str, ':');
            id = stoi(str);
            getline(ss, str, ':');
            op = str;
            getline(ss, str, ':');
            time = stoi(str);
            Log* l = new Log(id, time, 0);
            if(op == "start"){
                if(!s.empty()) s.top()->append += l->time - s.top()->time;
                s.push(l);
            }
            else{
                res[id] += l->time - s.top()->time + 1 + s.top()->append;
                s.pop();
                if(!s.empty()) s.top()->time = l->time + 1;
            }
        }
        return res;
    }
};''',

    'average-of-levels-in-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double>res;
        if(!root) return res;
        deque<TreeNode*>cur;
        deque<TreeNode*>next;
        cur.push_back(root);
        double sum = 0;
        int n = 0;
        while(!cur.empty()){
            TreeNode* p = cur.front();
            cur.pop_front();
            sum += p->val;
            n++;
            if(p->left) next.push_back(p->left);
            if(p->right) next.push_back(p->right);
            if(cur.empty()){
                res.push_back(sum / n);
                swap(cur, next);
                sum = n = 0;
            }
        }
        return res;
    }
};''',

    'decode-ways-ii': '''class Solution {
public:
    int numDecodings(string s) {
        if(s.empty() || s.front() == '0') return 0;
        int mod = pow(10, 9) + 7;
        long p1 = (s[0] == '*') ? 9 : 1, p2 = 1, t;
        for(int i = 1; i < s.size(); i++){
            if(s[i] == '0') p1 = 0;
            
            if(s[i - 1] != '*' && s[i] != '*'){
                if(s[i - 1] == '1' || s[i - 1] == '2' && s[i] < '7'){
                    p1 = p1 + p2;
                    p2 = p1 - p2;
                }
                else p2 = p1;
            }
            else{
                if(s[i - 1] == '*' && s[i] == '*'){
                    t = p1;
                    p1 = p1 * 9 + p2 * (9 + 6);
                    p2 = t;
                }
                else if(s[i] == '*'){
                    if(s[i - 1] == '1'){
                        t = p1;
                        p1 = p1 * 9 + p2 * 9;
                        p2 = t;
                    }
                    else if(s[i - 1] == '2'){
                        t = p1;
                        p1 = p1 * 9 + p2 * 6;
                        p2 = t;
                    }else{
                        t = p1;
                        p1 = p1 * 9;
                        p2 = t;
                    }
                }
                else{
                    if(s[i] == '0'){
                        t = p1;
                        p1 = p2 * 2;
                        p2 = t;
                    }
                    else if(s[i] < '7'){
                        t = p1;
                        p1 = p1 + p2 * 2;
                        p2 = t;
                    }
                    else{
                        p1 = p1 + p2;
                        p2 = p1 - p2;
                    }
                }
            }
            p1 = p1 % mod;
        }
        return p1;
    }
};''',

    'design-search-autocomplete-system': '''class AutocompleteSystem {  
public:
    AutocompleteSystem(vector<string> sentences, vector<int> times) {
        root = new TrieNode();
        reset();
        for(int i = 0; i < sentences.size(); i++) buildTrie(sentences[i], times[i]);
    }
    
    vector<string> input(char c) {
        vector<string>res;
        if(c == '#'){
            buildTrie(sentence, 1);
            reset();
            return res;
        }
        sentence.push_back(c);
        cur = cur->next[c];
        if(!cur) cur = new TrieNode();
        dfs(sentence, cur);
        while(!pq.empty()){
            res.push_back(pq.top().first);
            pq.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
    
private:
    struct TrieNode{
        int time;
        unordered_map<char, TrieNode*>next;
        TrieNode():time(0){}
    };
    TrieNode* root;
    TrieNode* cur;
    string sentence;
    
    struct Compare{
        bool operator() (pair<string, int>& p1, pair<string, int>& p2){ 
            return p1.second == p2.second ? p1.first < p2.first : p1.second > p2.second; 
        }
    };
    priority_queue<pair<string, int>, vector<pair<string, int>>, Compare>pq;
    
    void buildTrie(string s, int time){
        auto p = root;
        for(auto c: s){
            if(!p->next[c]) p->next[c] = new TrieNode();
            p = p->next[c];
        }
        p->time += time;
    }
    
    void dfs(string& s, TrieNode* p){
        if(p->time){
            pq.push({s, p->time});
            while(pq.size() > 3) pq.pop();
        }
        for(auto x: p->next){
            s.push_back(x.first);
            dfs(s, x.second);
            s.pop_back();
        }
    }
    
    void reset(){
        cur = root;
        sentence = "";
    }
};

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * vector<string> param_1 = obj.input(c);
 */''',

    'maximum-average-subarray-i': '''class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum = 0, maxSum;
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            if(i == k - 1) maxSum = sum;
            if(i >= k){
                sum -= nums[i - k];
                maxSum = max(maxSum, sum);
            }
        }
        return (double)maxSum / k;
    }
};''',

    'set-mismatch': '''class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size(), sum = 0, dup = 0, miss = 0;
        vector<int>count(n, 0);
        for(int i = 0; i < n; sum += nums[i++]) if(++count[nums[i] - 1] > 1) dup = nums[i];
        miss = n * (n + 1) / 2 - sum + dup;
        return {dup, miss};
    }
};''',

    'palindromic-substrings': '''class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for(int i = 0; i < s.size(); i++)
            for(int j = i; j < s.size(); j++)
                if(isPanlindrome(s.substr(i, j - i + 1))) count++;
        return count;
    }
    
    bool isPanlindrome(string s){
        int i = 0, j = s.size() - 1;
        while(i < j) if(s[i++] != s[j--]) return false;
        return true;
    }
};''',

    'replace-words': '''// Solution 1. Hash Table, 163 ms.
class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        unordered_map<int, unordered_set<string>>m;
        for(string& s: dict) m[s.size()].insert(s);
        string res = "";
        for(int i = 0, j = 0; i < sentence.size(); i = j + 1, j = i){
            string word = "";
            for(; j < sentence.size() && sentence[j] != ' '; j++){
                string prefix = sentence.substr(i, j - i + 1);
                if(m[prefix.size()].count(prefix) && word.empty()) word = prefix;
            }
            if(word.empty() && j != i) word = sentence.substr(i, j - i);
            res += word + " ";
        }
        res.pop_back();
        return res;
    }
};

// Solution 2. Trie, 58 ms.
struct TrieNode{
    bool isKey;
    TrieNode* next[26];
    TrieNode(): isKey(false){
        memset(next, NULL, sizeof(next));
    }
};

class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        root = new TrieNode();
        for(string& s: dict) buildTrie(s);
        string res = "";
        for(int i = 0; i < sentence.size();){
            pair<string, int> nextWord = match(sentence, i);
            res += nextWord.first + " ";
            i = nextWord.second + 1;
        }
        res.pop_back();
        return res;
    }

private:    
    TrieNode* root;
    
    void buildTrie(string& s){
        auto p = root;
        for(char c: s){
            if(!p->next[c - 'a']) p->next[c - 'a'] = new TrieNode();
            p = p->next[c - 'a'];
        }
        p->isKey = true;
    }
    
    pair<string, int> match(string& sentence, int pos){
        auto p = root;
        int i = pos;
        while(i < sentence.size() && sentence[i] != ' ' && !p->isKey && p->next[sentence[i] - 'a']){
            p = p->next[sentence[i] - 'a'];
            i++;
        }
        int j = i;
        while(i < sentence.size() && sentence[i] != ' ') i++;
        if(p->isKey) return {sentence.substr(pos, j - pos), i};
        return {sentence.substr(pos, i - pos), i};
    }
};''',

    'find-duplicate-subtrees': '''class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int>m;
        vector<TreeNode*>res;
        DFS(root, m, res);
        return res;
    }
    
    string DFS(TreeNode* root, unordered_map<string, int>& m, vector<TreeNode*>& res){
        if(!root) return "";
        string s = to_string(root->val) + "," + DFS(root->left, m, res) + "," + DFS(root->right, m, res);
        if(m[s]++ == 1) res.push_back(root);
        return s;
    }
};''',

    'two-sum-iv-input-is-a-bst': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        unordered_map<int, int>m;
        return DFS(root, m, k);
    }
    
    bool DFS(TreeNode* root, unordered_map<int, int>& m, int k){
        if(!root) return false;
        if(m.count(k - root->val)) return true;
        m[root->val]++;
        return DFS(root->left, m, k) || DFS(root->right, m, k);
    }
};''',

    'maximum-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return DFS(nums, 0, nums.size());
    }
    
    TreeNode* DFS(vector<int>& nums, int l, int r){
        if(l == r) return NULL;
        int maxPos = l;
        for(int i = l; i < r; i++) if(nums[i] > nums[maxPos]) maxPos = i;
        TreeNode* root = new TreeNode(nums[maxPos]);
        root->left = DFS(nums, l, maxPos);
        root->right = DFS(nums, maxPos + 1, r);
        return root;
    }
};

// O(n)
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        deque<TreeNode*>q;
        for(auto x: nums){
            TreeNode* p = new TreeNode(x);
            while(!q.empty() && q.back()->val < x) p->left = q.back(), q.pop_back();
            if(!q.empty() && q.back()->val > x) q.back()->right = p;
            q.push_back(p);
        }
        return q.front();
    }
};''',

    'judge-route-circle': '''class Solution {
public:
    bool judgeCircle(string moves) {
        int v = 0, h = 0;
        unordered_map<char, int>m{{'R', 1}, {'L', -1}, {'U', -1}, {'D', 1}};
        for(auto x: moves)
            if(x == 'L' || x == 'R') h += m[x];
            else v += m[x];
        return v == 0 && h == 0;
    }
};''',

    'find-k-closest-elements': '''class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int>res;
        int pos = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
        int i = pos - 1, j = pos;
        while(k--)
            (i >= 0 && (j == arr.size() || abs(arr[i] - x) <= abs(arr[j] - x))) ? i-- : j++;
        res.assign(arr.begin() + i + 1, arr.begin() + j);
        return res;
    }
};''',

    'split-array-into-consecutive-subsequences': '''class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int>m, f;
        for(auto x: nums) m[x]++;
        for(auto x: nums){
            if(!m[x]) continue;
            else if(f[x]){
                f[x]--;
                f[x + 1]++;
            }
            else if(m[x + 1] && m[x + 2]){
                m[x + 1]--;
                m[x + 2]--;
                f[x + 3]++;
            }
            else return false;
            m[x]--;
        }
        return true;
    }
};

class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int>m, t;
        for (int& x: nums) {
            ++m[x];
        }
        
        for (int& x: nums) {
            if (!m[x]) {
                continue;
            }
            --m[x];
            if (t[x]) {
                --t[x];
                ++t[x + 1];
            } else if (m[x + 1] && m[x + 2]) {
                --m[x + 1];
                --m[x + 2];
                ++t[x + 3];
            } else {
                return false;
            }
        }
        return true;
    }
};''',

    'maximum-width-of-binary-tree': '''// BFS
class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        if(!root) return 0;
        int maxWidth = 1;
        deque<pair<TreeNode*, int>>cur;
        deque<pair<TreeNode*, int>>next;
        cur.push_back({root, 1});
        while(!cur.empty()){
            auto p = cur.front();
            cur.pop_front();
            if(p.first->left) next.push_back({p.first->left, p.second * 2});
            if(p.first->right) next.push_back({p.first->right, p.second * 2 + 1});
            if(cur.empty() && !next.empty()){
                swap(cur, next);
                maxWidth = max(maxWidth, cur.back().second - cur.front().second + 1);
            }
        }
        return maxWidth;
    }
};

// DFS
class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        int maxWidth = 0;
        vector<int>v;
        DFS(root, v, 1, 0, maxWidth);
        return maxWidth;
    }
    
    void DFS(TreeNode* root, vector<int>& v, int tag, int level, int& maxWidth){
        if(!root) return;
        if(v.size() == level) v.push_back(tag);
        maxWidth = max(maxWidth, tag - v[level] + 1);
        DFS(root->left, v, tag * 2, level + 1, maxWidth);
        DFS(root->right, v, tag * 2 + 1, level + 1, maxWidth);
    }
};''',

    'equal-tree-partition': '''class Solution {
public:
    bool checkEqualTree(TreeNode* root) {
        vector<int>v;
        int sum = DFS(root, v);
        v.pop_back();
        return !(sum % 2) && find(v.begin(), v.end(), sum / 2) != v.end();
    }
    
    int DFS(TreeNode* root, vector<int>& v){
        if(!root) return 0;
        int l = DFS(root->left, v);
        int r = DFS(root->right, v);
        int sum = root->val + l + r;
        v.push_back(sum);
        return sum;
    }
};''',

    'non-decreasing-array': '''class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count = 0;
        for(int i = 1, j = 0; i < nums.size(); i++, j++)
            if(nums[j] > nums[i]){
                count++;
                if(j > 0 && nums[j - 1] > nums[i]) nums[i] = nums[j];
                else nums[j] = nums[i];
            }
        return count <= 1;
    }
};''',

    'trim-a-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        while(root && (root->val < L || root->val > R)) root = root->val < L ? root->right : root->left;
        if(!root) return NULL;
        root->left = trimBST(root->left, L, R);
        root->right = trimBST(root->right, L, R);
        return root;
    }
};''',

    'maximum-swap': '''// Solution 1.
// Time: O(n^2)
class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        for(int i = 0; i < s.size(); i++){
            int digit = s[i] - '0';
            int index = i;
            for(int j = s.size() - 1; j > i; j--){
                if(s[j] - '0' > digit){
                    digit = s[j] - '0';
                    index = j;
                }
            }
            if(digit != s[i] - '0'){
                swap(s[i], s[index]);
                return stoi(s);
            }
        }
        return num;
    }
};

// Solution 2.
// Time: O(n)
class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        vector<int>bucket(10);
        for(int i = 0; i < s.size(); i++)
            bucket[s[i] - '0'] = i;
        for(int i = 0; i < s.size(); i++)
            for(int  j = 9; j > s[i] - '0'; j--)
                if(bucket[j] > i){
                    swap(s[i], s[bucket[j]]);
                    return stoi(s);
                }
        return num;
    }
};''',

    'second-minimum-node-in-a-binary-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int findSecondMinimumValue(TreeNode* root) {
        int res = INT_MAX;
        DFS(root, root->val, res);
        return res == INT_MAX ? -1 : res;
    }
    
    void DFS(TreeNode* root, int val, int& res){
        if(!root) return;
        if(root->val != val) res = min(res, root->val);
        if(root->val == val) DFS(root->left, val, res), DFS(root->right, val, res);
    }
};''',

    'number-of-longest-increasing-subsequence': '''class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int>len(n, 1);
        vector<int>cnt(n, 1);
        int maxlen = 1, res = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]){
                    if(len[i] == len[j] + 1) cnt[i] += cnt[j];
                    if(len[i] < len[j] + 1){
                        len[i] = len[j] + 1;
                        cnt[i] = cnt[j];
                    }
                }
            }
            if(len[i] == maxlen) res += cnt[i];
            if(len[i] > maxlen){
                maxlen = len[i];
                res = cnt[i];
            }
        }
        return res;
    }
};''',

    'longest-continuous-increasing-subsequence': '''class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        int i = 0, j = 1, maxlen = 1;
        while(j < nums.size()){
            while(j < nums.size() && nums[j] > nums[j - 1]) j++;
            maxlen = max(maxlen, j - i);
            i = j++;
        }
        return maxlen;
    }
};''',

    'implement-magic-dictionary': '''// Solution 1. Hash Table
class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {}
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for(auto x: dict) m[x.size()].push_back(x);
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        for(auto x: m[word.size()])
            if(oneEditDistance(x, word)) return true;
        return false;
    }
    
private:
    unordered_map<int, vector<string>>m;
    bool oneEditDistance(string& a, string& b){
        int diff = 0;
        for(int i = 0; i < a.size() && diff <= 1; i++)
            if(a[i] != b[i]) diff++;
        return diff == 1;
    }
};

// Solution 2. Trie
class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        root = new TrieNode();
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for(auto x: dict) buildTrie(x);
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        TrieNode* p = root;
        int diff = 0;
        for(int i = 0; i < word.size(); i++){
            char c = word[i];
            for(int j = 0; j < 26; j++){
                if(p->next[j] == p->next[c - 'a']) continue;
                if(p->next[j] && find(p->next[j], word.substr(i + 1))) return true;
            }
            if(p->next[c - 'a']) p = p->next[c - 'a'];
        }
        return false;
    }

private:
    struct TrieNode{
        bool isWord;
        TrieNode* next[26];
        TrieNode():isWord(false){
            memset(next, NULL, sizeof(next));
        }
    };
    TrieNode* root;
    
    void buildTrie(string s){
        TrieNode* p = root;
        for(auto c: s){
            if(!p->next[c - 'a']) p->next[c - 'a'] = new TrieNode();
            p = p->next[c - 'a'];
        }
        p->isWord = true;
    }
    
    bool find(TrieNode* p, string s){
        for(auto c: s)
            if(p->next[c - 'a']) p = p->next[c - 'a'];
            else return false;
        return p->isWord;
    }
};

class MagicDictionary {
    struct TrieNode {
        char val;
        vector<TrieNode*> next;
        bool isWord;
        TrieNode(char c): val(c), next(vector<TrieNode*>(26)), isWord(false) {}
    };
public:
    /** Initialize your data structure here. */
    MagicDictionary() {}
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        root = new TrieNode(' ');
        for (auto& s: dict) {
            buildTrie(s);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        return dfs(root, word, 0, true);
    }
    
private:
    TrieNode* root;
    
    bool dfs(TrieNode* p, string& word, int pos, bool canModify) {
        if (pos == word.size()) {
            return !canModify && p->isWord;
        }
        bool find = false;
        char c = word[pos];
        if (p->next[c - 'a']) {
            find |= dfs(p->next[c - 'a'], word, pos + 1, canModify);
        } 
        
        if (canModify) {
            for (auto node: p->next) {
                if (node && node->val != c) {
                    find |= dfs(node, word, pos + 1, false);
                }
            }
        }
        return find;
    }
    
    void buildTrie(string& s) {
        TrieNode* p = root;
        for (auto c: s) {
            if (!p->next[c - 'a']) {
                p->next[c - 'a'] = new TrieNode(c);
            }
            p = p->next[c - 'a'];
        }
        p->isWord = true;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */''',

    'map-sum-pairs': '''class MapSum {
    struct TrieNode{
        int sum;
        TrieNode* next[26];
        TrieNode(): sum(0){
            memset(next, NULL, sizeof(next));
        }
    };
    
    unordered_map<string, int>m;
    TrieNode* root;
    
public:
    /** Initialize your data structure here. */
    MapSum() {
        root = new TrieNode();
    }
    
    void insert(string key, int val) {
        bool replace = false;
        if(m.count(key)) replace = true;
        TrieNode* p = root;
        for(char c: key){
            if(!p->next[c - 'a']) p->next[c - 'a'] = new TrieNode();
            p = p->next[c - 'a'];
            p->sum += replace ? val - m[key] : val;
        }
        m[key] = val;
    }
    
    int sum(string prefix) {
        TrieNode* p = root;
        for(char c: prefix){
            if(!p->next[c - 'a']) return 0;
            p = p->next[c - 'a'];
        }
        return p->sum;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */''',

    '24-game': '''class Solution {
public:
    bool judgePoint24(vector<int>& nums) {
        unordered_set<string>res;
        string ops = "+-*/";
        dfs(nums, "", ops, res);
        for (auto& x: res) {
            auto v = getResult(x);
            if (!v.empty() && abs(v.back() - 24) < 0.0001) {
                return true;
            }
        }
        return false;
    }
    
    // Generate all possible permutations
    void dfs(vector<int>& nums, string s, string& ops, unordered_set<string>& res) {
        for (int& x: nums) {
            if (x == 0) {
                continue;
            }
            int tmp = x;
            s.push_back(x + '0');
            x = 0;
            
            if (s.size() == 7) {
                res.insert(s);
                s.pop_back();
                x = tmp;
                return;
            }
            
            for (auto c: ops) {
                s.push_back(c);
                dfs(nums, s, ops, res);
                s.pop_back();
            }
            s.pop_back();
            x = tmp;
        }
    }
    
    // Generate all possible results from string 's'
    vector<double> getResult(string s) {
        int n = s.size();
        if (n == 1) {
            return {s[0] - '0'};
        }
        vector<double>res;
        for (int i = 1; i <= n - 2; i += 2) {
            vector<double> l = getResult(s.substr(0, i));
            vector<double> r = getResult(s.substr(i + 1));
            char op = s[i];
            
            for (auto& x: l) {
                for (auto& y: r) {
                    if (op == '/' && !y) {
                        continue;
                    }
                    double val = helper(op, x, y);
                    res.push_back(val);
                    if (s.size() == 7 && abs(val - 24) < 0.0001) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
    
    double helper(char op, double a, double b) {
        if (op == '+') {
            a += b;
        } else if (op == '-') {
            a -= b;
        } else if (op == '*') {
            a *= b;
        } else {
            a /= b;
        }
        return a;
    }
};''',

    'valid-palindrome-ii': '''class Solution {
public:
    bool validPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while(i <= j && s[i] == s[j]) i++, j--;
        return i > j || isValid(s.substr(i, j - i)) || isValid(s.substr(i + 1, j - i));
    }
    
    bool isValid(string s){
        int i = 0, j = s.size() - 1;
        while(i <= j && s[i] == s[j]) i++, j--;
        return i > j;
    }
};''',

    'next-closest-time': '''class Solution {
public:
    string nextClosestTime(string time) {
        string cur = time.substr(0, 2) + time.substr(3);
        unordered_set<char>nums;
        for(auto c: cur) nums.insert(c);
        if(nums.size() == 1) return time;
        int minDis = 24 * 60;
        string next = "";
        string res = "";
        DFS(nums, cur, 0, minDis, next, res);
        res.insert(res.begin() + 2, ':');
        return res;
    }

    void DFS(unordered_set<char>& nums, string& cur, int pos, int& minDis, string& next, string& res){
        if(pos == 2 && stoi(next.substr(0, 2)) >= 24) return;
        if(pos == 4){
            if(stoi(next.substr(2)) > 59) return;
            int dis = distance(cur, next);
            if(dis < minDis){
                minDis = dis;
                res = next;
            }
            return;
        }
        
        for(auto c: nums){
            next.push_back(c);
            DFS(nums, cur, pos + 1, minDis, next, res);
            next.pop_back();
        }
    }
    
    int distance(string& cur, string& next){
        int a = stoi(cur.substr(0, 2)) * 60 + stoi(cur.substr(2));
        int b = stoi(next.substr(0, 2)) * 60 + stoi(next.substr(2));
        return a < b ? b - a : b - a + 24 * 60;
    }
};''',

    'k-empty-slots': '''class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        set<int>s;
        for(int i = 0; i < flowers.size(); i++){
            int l = -1, r = -1;
            if(s.empty()){
                s.insert(flowers[i]);
                continue;
            }
            auto up = s.upper_bound(flowers[i]);
            auto low = up;
            low--;
            if(up == s.end())
                l = flowers[i] - *low - 1;
            else if(up == s.begin())
                r = *up - flowers[i] - 1;
            else{
                l = flowers[i] - *low - 1;
                r = *up - flowers[i] - 1;
            }
            if(l == k || r == k) return i + 1;
            s.insert(flowers[i]);
        }
        return -1;  
    }
};''',

    'redundant-connection': '''// Solution 1
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int tag = 1;
        unordered_map<int, int>id;
        unordered_map<int, vector<int>>g;
        for(auto x: edges){
            int u = x[0], v = x[1];
            g[u].push_back(v);
            g[v].push_back(u);
            if(id[u] && id[v] && id[u] == id[v]) return x;
            else if(!id[u] && !id[v]) id[u] = id[v] = tag++;
            else if(id[u]) DFS(g, id, v, id[u]);
            else id[u] = id[v];
        }
    }
    
    void DFS(unordered_map<int, vector<int>>& g, unordered_map<int, int>& id, int root, int tag){
        if(id[root] == tag) return;
        id[root] = tag;
        for(auto x: g[root]) DFS(g, id, x, tag);
    }
};

// Solution 2
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        if (edges.empty()) {
            return {};
        }
        vector<vector<int>>g(1001);
        vector<int>visited(1001);
        for (auto& e: edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
            
            if (!dfs(g, e[0], e[1], visited)) {
                return e;
            }
        }
        return {};
    }
    
    bool dfs(vector<vector<int>>& g, int node, int from, vector<int>& visited) {
        if (visited[node]) {
            return false;
        }
        visited[node] = 1;
        bool res = true;
        for (int& x: g[node]) {
            if (x != from) {
                res &= dfs(g, x, node, visited);
            }
        }
        visited[node] = 0;
        return res;
    }
};

// Solution 3
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int>root(1001);
        
        for (int i = 0; i < 1001; ++i) {
            root[i] = i;
        }
        
        for(auto& pair: edges) {
            int a = pair[0];
            int b = pair[1];

            while (a != root[a]) a = root[a];
            while (b != root[b]) b = root[b];
            
            if (a == b) {
                return pair;
            } else {
                root[a] = b;
            }
        }
        return {};
    }
};''',

    'redundant-connection-ii': '''class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        vector<int>res;
        unordered_map<int, int>parent;
        unordered_map<int, vector<int>>g;
        // c0: the last edge to form a circle
        // c1, c2: parents of the node who has two parents
        vector<int>c0, c1, c2;
        int rootCandidate = 0, root = 0, count = 0;
        for(auto x: edges){
            int u = x[0], v = x[1];
            if(parent[v] > 0){
                c1 = x;
                c2 = {parent[v], v};
            }
            if(!parent[u]){
                rootCandidate++;
                parent[u] = -1;
            }
            if(parent[v] == -1) rootCandidate--;
            parent[v] = u;
            if(rootCandidate == 0) c0 = x, rootCandidate = -1; // No valid root can be found, circle detected
            g[u].push_back(v);
        }
        for(auto x: parent) if(x.second == -1) root = x.first;
        int nodes = parent.size();
        vector<int>visited(nodes + 1);
        return !root ? c0 : (!hasCircle(g, -1, root, c1, visited, count) && count == nodes) ? c1 : c2;
    }
    
    bool hasCircle(unordered_map<int, vector<int>>& g, int from, int root, vector<int>c, vector<int>& visited, int& count){
        if(from == c[0] && root == c[1]) return false;
        if(visited[root]) return true;
        count++;
        visited[root] = 1;
        bool foundCircle = false;
        for(auto x: g[root]) foundCircle |= hasCircle(g, root, x, c, visited, count);
        return foundCircle;
    }
};''',

    'repeated-string-match': '''class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int i = 0, j = 0, count = 1;
        while(j < B.size()){
            while(i < A.size() && A[i] != B[j]) i++;
            if(i == A.size() || count > 1) return -1;
            while(j < B.size() && A[i++] == B[j++]){
                if(j == B.size()) return count;
                if(i == A.size()) i = 0, count++;
            }
            j = 0;
        }
    }
};''',

    'longest-univalue-path': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        int maxlen = 0;
        DFS(root, maxlen);
        return maxlen;
    }
    
    int DFS(TreeNode* root, int& maxlen){
        if(!root) return 0;
        int left = DFS(root->left, maxlen);
        int right = DFS(root->right, maxlen);
        if(!root->left || root->left->val != root->val) left = 0;
        if(!root->right || root->right->val != root->val) right = 0;
        maxlen = max(maxlen, left + right);
        return max(left, right) + 1;
    }
};''',

    'knight-probability-in-chessboard': '''class Solution {
private:
    unordered_map<int, unordered_map<int, unordered_map<int, double>>>dp;
public:
    double knightProbability(int N, int K, int r, int c) {
        if(dp.count(r) && dp[r].count(c) && dp[r][c].count(K)) return dp[r][c][K];
        if(r < 0 || r >= N || c < 0 || c >= N) return 0;
        if(K == 0) return 1;
        double total = knightProbability(N, K - 1, r - 1, c - 2) + knightProbability(N, K - 1, r - 2, c - 1) 
                     + knightProbability(N, K - 1, r - 1, c + 2) + knightProbability(N, K - 1, r - 2, c + 1) 
                     + knightProbability(N, K - 1, r + 1, c + 2) + knightProbability(N, K - 1, r + 2, c + 1) 
                     + knightProbability(N, K - 1, r + 1, c - 2) + knightProbability(N, K - 1, r + 2, c - 1);
        double res = total / 8;
        dp[r][c][K] = res;
        return res;
    }
};''',

    'maximum-sum-of-3-non-overlapping-subarrays': '''class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        // dp[i] is the sum of subarray of in range [i , i + k)
        // nextMax[i] is the maximum value in dp[i : dp.size() - 1]
        // nextIdx[i] is the index of nextMax[i]
        int n = nums.size(), sum = 0, maxRight = 0, idx = 0, maxSum = 0;
        vector<int>res, dp(n - k + 1), nextMax(n - k + 1), nextIdx(n - k + 1);
        // Using a sliding window to get the sum of subarray in range [i , i + k)
        for(int i = 0; i < n; i++){
            sum += nums[i];
            if(i >= k) sum -= nums[i - k];
            if(i >= k - 1) dp[i - k + 1] = sum;
        }
        // Starting from end of dp array to get the maximum value after current position
        for(int i = dp.size() - 1; i >= 0; i--){
            if(dp[i] > maxRight) maxRight = dp[i], idx = i;
            nextMax[i] = maxRight;
            nextIdx[i] = idx;
        }
        // Using two pointers i, j to find the result
        // The third entry is determined by nextMax[j + k]
        for(int i = 0; i <= n - 3 * k; i++)
            for(int j = i + k; j <= n - 2 * k; j++){
                sum = dp[i] + dp[j] + nextMax[j + k];
                if(sum > maxSum){
                    maxSum = sum;
                    res = {i, j, nextIdx[j + k]};
                }
            }
        return res;
    }
};''',

    'employee-importance': '''// BFS
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*>m;
        for(auto x: employees) m[x->id] = x;
        int sum = 0;
        deque<Employee*>q;
        q.push_back(m[id]);
        while(!q.empty()){
            auto p = q.front();
            q.pop_front();
            for(auto x: p->subordinates) q.push_back(m[x]);
            sum += p->importance;
        }
        return sum;
    }
};

// DFS
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*>m;
        for(auto x: employees) m[x->id] = x;
        int sum = 0;
        DFS(m, id, sum);
        return sum;
    }
    
    void DFS(unordered_map<int, Employee*>& m, int id, int& sum){
        sum += m[id]->importance;
        for(auto x: m[id]->subordinates) DFS(m, x, sum);
    }
};''',

    'top-k-frequent-words': '''class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        vector<string>res;
        unordered_map<string, int>m;
        auto comp = [](pair<int, string>& a, pair<int, string>& b){ return a.first == b.first ? a.second < b.second : a.first > b.first; };
        priority_queue<pair<int, string>, vector<pair<int, string> >, decltype(comp)>pq(comp);
        for(auto x: words) m[x]++;
        for(auto x: m){
            pq.push({x.second, x.first});
            if(pq.size() > k) pq.pop();
        }
        while(!pq.empty()) res.push_back(pq.top().second), pq.pop();
        reverse(res.begin(), res.end());
        return res;
    }
};''',

    'binary-number-with-alternating-bits': '''class Solution {
public:
    bool hasAlternatingBits(int n) {
        while(n)
            if(!((n & 1) ^ ((n >> 1) & 1))) return false;
            else n >>= 1;
        return true;
    }
};''',

    'number-of-distinct-islands': '''// Solution 1.
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_map<int, vector<vector<int>>>mp;
        int count = 0, m = grid.size(), n = grid[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] == 1){
                    int area = 0;
                    DFS(grid, i, j, m, n, area);
                    bool equal = false;
                    for(auto x: mp[area]){
                        int S = 0;
                        vector<vector<int>>visited(m, vector<int>(n));
                        DFS(grid, i, j, x[0], x[1], m, n, S, visited);
                        if(S == area){ equal = true; break; }
                    }
                    if(!equal) count++, mp[area].push_back({i, j});
                }
        return count;
    }
    
    void DFS(vector<vector<int>>& grid, int r, int c, int m, int n, int& area){
        if(r < 0 || c < 0 || r == m || c == n || !grid[r][c] || grid[r][c] == 2) return;
        area++;
        grid[r][c] = 2;
        for(int i = 0; i < 4; i++) DFS(grid, r + d[i][0], c + d[i][1], m, n, area);
    }
    
    void DFS(vector<vector<int>>& grid, int r, int c, int R, int C, int m, int n, int& S, vector<vector<int>>& visited){
        if(r < 0 || c < 0 || R < 0 || C < 0 || r == m || R == m || c == n || C == n || visited[r][c]) return;
        if(!grid[r][c] && !grid[R][C] || grid[r][c] != grid[R][C]) return;
        S++;
        visited[r][c] = 1;
        for(int i = 0; i < 4; i++) DFS(grid, r + d[i][0], c + d[i][1], R + d[i][0], C + d[i][1], m, n, S, visited);
    }

private:
    vector<vector<int>>d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
};

// Solution 2. Using set.
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        int count = 0, m = grid.size(), n = grid[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] == 1){
                    vector<vector<int>>island;
                    DFS(grid, i, j, i, j, m, n, island);
                    s.insert(island);
                }
        return s.size();
    }
    
    void DFS(vector<vector<int>>& grid, int i, int j, int r, int c, int m, int n, vector<vector<int>>& island){
        if(r < 0 || c < 0 || r == m || c == n || !grid[r][c] || grid[r][c] == 2) return;
        island.push_back({r - i, c - j});
        grid[r][c] = 2;
        for(int k = 0; k < 4; k++) DFS(grid, i, j, r + d[k][0], c + d[k][1], m, n, island);
    }
    
private:
    set<vector<vector<int>>>s;
    vector<vector<int>>d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
};''',

    'max-area-of-island': '''class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if(grid.empty()) return 0;
        int maxArea = 0, m = grid.size(), n = grid[0].size();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j]){
                    int area = 0;
                    DFS(grid, i, j, m, n, area, maxArea);
                }
        return maxArea;
    }
    
    void DFS(vector<vector<int>>& grid, int r, int c, int m, int n, int& area, int& maxArea){
        if(r < 0 || c < 0 || r == m || c == n || grid[r][c] == 0){
            maxArea = max(maxArea, area);
            return;
        }
        area++;
        grid[r][c] = 0;
        DFS(grid, r + 1, c, m, n, area, maxArea);
        DFS(grid, r - 1, c, m, n, area, maxArea);
        DFS(grid, r, c + 1, m, n, area, maxArea);
        DFS(grid, r, c - 1, m, n, area, maxArea);
    }
};''',

    'count-binary-substrings': '''class Solution {
public:
    int countBinarySubstrings(string s) {
        int count = 0;
        for(int i = 0, j = 0; i < s.size(); j = i){
            int a = 0, b = 0;
            while(j < s.size() && s[j] == s[i]) j++, a++;
            i = j;
            while(j < s.size() && s[j] == s[i]) j++, b++;
            count += min(a, b);
        }
        return count;
    }
};''',

    'degree-of-an-array': '''class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int>idx, cnt;
        int degree = 0, minlen = nums.size();
        for(int i = 0; i < nums.size(); i++){
            if(!idx.count(nums[i])) idx[nums[i]] = i;
            if(++cnt[nums[i]] == degree) minlen = min(minlen, i - idx[nums[i]] + 1);
            if(cnt[nums[i]] > degree){
                degree = cnt[nums[i]];
                minlen = i - idx[nums[i]] + 1;
            }
        }
        return minlen;
    }
};''',

    'insert-into-a-binary-search-tree': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        dfs(root, val);
        return root;
    }
    
    void dfs(TreeNode*& root, int val) {
        if (!root) {
            root = new TreeNode(val);
            return;
        }
        if (root->val > val) {
            dfs(root->left, val);
        } else {
            dfs(root->right, val);
        }
    }
};''',

    'subarray-product-less-than-k': '''class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int count = 0, product = 1;
        for(int i = 0, j = 0, pre = 0; j < nums.size(); i++, pre = j, j = max(i, j)){
            while(j < nums.size() && product * nums[j] < k) product *= nums[j++];
            count += (long)(j - pre) * (1 + (j - pre)) / 2 + (j - pre) * (pre - i);
            product = max(product / nums[i], 1);
        }
        return count;
    }
};''',

    '1-bit-and-2-bit-characters': '''class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0, n = bits.size();
        while(i < n - 1) i += bits[i] + 1;
        return i != n;
    }
};''',

    'maximum-length-of-repeated-subarray': '''class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        // dp[i][j] is the maximum length of subarray ending with A[i] and B[j]
        // dp[i][j] = (A[i] == B[j]) ? dp[i - 1][j - 1] + 1 : 0;
        int m = A.size(), n = B.size();
        vector<vector<int>>dp(m, vector<int>(n));
        int maxlen = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                if(i == 0 || j == 0) dp[i][j] = (A[i] == B[j]);
                else dp[i][j] = (A[i] == B[j]) ? dp[i - 1][j - 1] + 1 : 0;
                maxlen = max(maxlen, dp[i][j]);
            }
        return maxlen;
    }
};''',

    'longest-word-in-dictionary': '''class Solution {
public:
    string longestWord(vector<string>& words) {
        string res = "";
        unordered_map<int, unordered_set<string>>m;
        for(auto s: words) m[s.size()].insert(s);
        for(auto s: words){
            int i = 1;
            while(i < s.size() && m[i].count(s.substr(0, i))) i++;
            if(i == s.size() && s.size() >= res.size()) res = s.size() > res.size() ? s : min(s, res);
        }
        return res;
    }
};''',

    'candy-crush': '''class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        while (crush(board, m, n)) {
            drop(board, m, n);
        }
        return board;
    }
    
    bool crush(vector<vector<int>>& board, int m, int n) {
        vector<vector<int>>copy(board);
        bool canBeCrushed = false;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 0) {
                    continue;
                }
                int r = i, c = j, count = 0;
                // check horizontal
                while (c < n && board[i][c] == board[i][j]) {
                    ++count;
                    ++c;
                }
                if (count >= 3) {
                    canBeCrushed = true;
                    while (c > j) {
                        copy[i][--c] = 0;
                    }
                }
                count = 0;
                // check vertical
                while (r < m && board[r][j] == board[i][j]) {
                    ++count;
                    ++r;
                }
                if (count >= 3) {
                    canBeCrushed = true;
                    while (r > i) {
                        copy[--r][j] = 0;
                    }
                }
            }
        }
        board = copy;
        return canBeCrushed;
    }
    
    void drop(vector<vector<int>>& board, int m, int n) {
        for (int i = m - 1; i >= 0; --i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 0) {
                    // drop
                    int r = i, c = j;
                    while (r >= 0 && board[r][c] == 0) {
                        --r;
                    }
                    if (r >= 0) {
                        swap(board[i][j], board[r][c]);
                    }
                }
            }
        }
    }
};''',

    'find-pivot-index': '''class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 0;
        for(int x: nums) right += x;
        for(int i = 0; i < n; left += nums[i], right -= nums[i], i++) 
            if(left == right - nums[i]) return i;
        return -1;
    }
};''',

    'split-linked-list-in-parts': '''/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        vector<ListNode*>res;
        int len = 0;
        ListNode* head = new ListNode(0), *pre = root, *cur = head, *next, *p = root;
        while(p && ++len) p = p->next;
        int m = len % k, l = len / k;
        while(k--){
            cur->next = pre;
            for(int i = 0; i < l; i++) cur = cur->next;
            if(m) cur = cur->next, m--;
            next = cur->next;
            cur->next = NULL;
            res.push_back(pre);
            pre = next;
            cur = head;
        }
        return res;
    }
};''',

    'self-dividing-numbers': '''class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int>res;
        for(int i = left; i <= right; i++)
            if(isValid(i)) res.push_back(i);
        return res;
    }
    
    bool isValid(int num){
        int n = num;
        while(n){
            if(!(n % 10) || num % (n % 10)) return false;
            n /= 10;
        }
        return true;
    }
};''',

    'my-calendar-i': '''class MyCalendar {
public:
    MyCalendar() {}
    
    bool book(int start, int end) {
        for(auto& x: v)
            if(start >= x[0] && start < x[1] || end > x[0] && end <= x[1] || start < x[0] && end > x[1]) return false;
        v.push_back({start, end});
        return true;
    }

private:
    vector<vector<int>>v;
};''',

    'flood-fill': '''class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int m = image.size(), n = image[0].size();
        DFS(image, sr, sc, m, n, image[sr][sc], newColor);
        return image;
    }
    
    void DFS(vector<vector<int>>& image, int r, int c, int m, int n, int target, int newColor){
        if(r < 0 || c < 0 || r == m || c == n || image[r][c] == newColor || image[r][c] != target) return;
        image[r][c] = newColor;
        DFS(image, r + 1, c, m, n, target, newColor);
        DFS(image, r - 1, c, m, n, target, newColor);
        DFS(image, r, c + 1, m, n, target, newColor);
        DFS(image, r, c - 1, m, n, target, newColor);
    }
};''',

    'sentence-similarity': '''class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        if(words1.size() != words2.size()) return false;
        unordered_map<string, unordered_set<string>>m;
        for(auto x: pairs){
            m[x.first].insert(x.second);
            m[x.second].insert(x.first);
        }
        for(int i = 0; i < words1.size(); i++)
            if(words1[i] != words2[i] && !m[words1[i]].count(words2[i])) return false;
        return true;
    }
};''',

    'asteroid-collision': '''class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int>s;
        for(auto& x: asteroids)
            if(s.empty() || s.back() < 0 || x > 0) s.push_back(x);
            else{
                while(!s.empty() && s.back() > 0 && abs(x) > s.back()) s.pop_back();
                if(s.empty() || s.back() < 0) s.push_back(x);
                else if(abs(x) == s.back()) s.pop_back();
            }
        return s;
    }
};''',

    'daily-temperatures': '''class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int>res(n);
        stack<vector<int>>s;   // stack of <temperature, index>
        for(int i = 0; i < n; i++){
            while(!s.empty() && temperatures[i] > s.top()[0]){
                res[s.top()[1]] = i - s.top()[1];
                s.pop();
            }
            s.push({temperatures[i], i});
        }
        return res;
    }
};''',

    'delete-and-earn': '''class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        sort(nums.begin(), nums.end());
        vector<vector<int>>dp(n, vector<int>(2));
        dp[0][0] = 0;
        dp[0][1] = nums[0];
        for(int i = 1; i < n; i++){
            if(nums[i] == nums[i - 1]){
                dp[i][0] = dp[i - 1][0];
                dp[i][1] = dp[i - 1][1] + nums[i];
                continue;
            }
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = nums[i] == nums[i - 1] + 1 ? dp[i - 1][0] + nums[i] : dp[i][0] + nums[i];
        }
        return max(dp[n - 1][0], dp[n - 1][1]);
    }
};''',

    'closest-leaf-in-a-binary-tree': '''class Solution {
public:
    int findClosestLeaf(TreeNode* root, int k) {
        // Build Graph
        unordered_map<int, TreeNode*>m;
        unordered_map<int, vector<int>>g;
        buildGraph(g, m, root);
        if(g[k].size() == 1 && !m[k]->left && !m[k]->right) return k; // The nearest leaf node is the root node itself
        // BFS
        vector<int>visited(1001);
        deque<int>q;
        q.push_back(k);
        while(!q.empty()){
            int node = q.front();
            q.pop_front();
            visited[node] = 1;
            bool isEnd = true;
            for(int neigh: g[node]){
                if(!visited[neigh]){
                    q.push_back(neigh);
                    isEnd = false;
                }
            }
            if(isEnd && !m[node]->left && !m[node]->right) return node;
        }
        return 0;
    }
    
    void buildGraph(unordered_map<int, vector<int>>& g, unordered_map<int, TreeNode*>& m, TreeNode* root){
        if(!root) return;
        m[root->val] = root;
        if(root->left){
            g[root->val].push_back(root->left->val);
            g[root->left->val].push_back(root->val);
            buildGraph(g, m, root->left);
        }
        if(root->right){
            g[root->val].push_back(root->right->val);
            g[root->right->val].push_back(root->val);
            buildGraph(g, m, root->right);
        }
    }
};''',

    'min-cost-climbing-stairs': '''// Recursion: `dp[i] = min{dp[i - 1], dp[i - 2]} + cost[i];`
// A straightforward solution is:
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int>dp(n);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for(int i = 2; i < n; i++)
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
        return min(dp[n - 2], dp[n - 1]);
    }
};

// If we take a look at the solution above, we can see the result dp[i] only depends on previous 2 steps(dp[i - 1] and dp[i - 2]).
// So we can replace the 'dp' array with 2 variables.
// Here is the final solution:
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size(), a = cost[0], b = cost[1], c;
        for(int i = 2; i < n; i++, a = b, b = c)
            c = min(a, b) + cost[i];
        return min(a, b);
    }
};''',

    'largest-number-at-least-twice-of-others': '''class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int a = 0, b = 0, idx = -1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > a){
                b = a;
                a = nums[i];
                idx = i;
            }
            else if(nums[i] > b) b = nums[i];
        }
        return a >= 2 * b ? idx : -1;
    }
};''',

    'number-of-corner-rectangles': '''class Solution {
public:
    int countCornerRectangles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = i + 1; j < m; ++j) {
                int count = 0;
                for (int k = 0; k < n; ++k) {
                    if (grid[i][k] && grid[j][k]) {
                        ++count;
                    }
                }
                res += (count - 1) * count / 2;
            }
        }
        return res;
    }
};''',

    'cracking-the-safe': '''class Solution {
public:
    string crackSafe(int n, int k) {
        int target = pow(k, n);
        string res;
        for (int i = 0; i < n; ++i) {
            res += '0';
        }
        string cur = res;
        unordered_set<string>visited;
        dfs(res, target, visited, n, k, cur);
        return res;
    }
    
    bool dfs(string& res, int& target, unordered_set<string>& visited, int n, int k, string cur) {
        if (visited.count(cur)) {
            return false;
        }
        
        visited.insert(cur);
        
        if (visited.size() == target) {
            return true;
        }
        
        string next = cur.substr(1);
        
        for (int i = 0; i < k; ++i) {
            next.push_back('0' + i);
            if (!visited.count(next)) {
                res.push_back('0' + i);
                if (dfs(res, target, visited, n, k, next)) {
                    return true;
                }
                res.pop_back();
            }
            next.pop_back();
        }
        visited.erase(cur);
        return false;
    }
};''',

    'bold-words-in-string': '''class Solution {
public:
    string boldWords(vector<string>& words, string S) {
        int n = S.size();
        vector<int>v(n + 1);
        vector<int>m(n + 1);
        string res = "";
        for(auto s: words){
            auto pos = S.find(s);
            while(pos != string::npos){
                v[pos]++;
                v[pos + s.size()]--;
                pos = S.find(s, pos + 1);
            }
        }
        int pre = 0, cur = 0;
        for(int i = 0; i < n + 1; i++){
            cur = pre + v[i];
            if(pre == 0 && cur > 0) m[i] = 1;
            else if(pre > 0 && cur == 0) m[i] = -1;
            pre = cur;
        }
        for(int i = 0; i < n + 1; i++){
            if(m[i]) res += m[i] == 1 ? "<b>" : "</b>";
            if(i < n) res.push_back(S[i]);
        }
        return res;
    }
};''',

    'find-anagram-mappings': '''class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        vector<int>res;
        unordered_map<int, int>m;
        for(int i = 0; i < B.size(); i++) m[B[i]] = i;
        for(int x: A) res.push_back(m[x]);
        return res;
    }
};''',

    'partition-labels': '''// Straightforward two pointers:
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int>res;
        int maxPos = 0, pre = -1;
        for(int i = 0; i < S.size(); i++){
            for(int j = maxPos + 1; j < S.size(); j++) 
                if(S[j] == S[i]) maxPos = max(maxPos, j);
            if(i == maxPos){
                res.push_back(i - pre);
                pre = i;
            }
        }
        return res;
    }
};

// O(N)
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int>res;
        vector<int>pos(26);
        for(int i = 0; i < S.size(); i++) pos[S[i] - 'a'] = i;
        int maxPos = 0, pre = -1;
        for(int i = 0; i < S.size(); i++){
            maxPos = max(maxPos, pos[S[i] - 'a']);
            if(i == maxPos){
                res.push_back(i - pre);
                pre = i;
            }
        }
        return res;
    }
};''',

    'couples-holding-hands': '''class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        unordered_map<int, int>idx;
        int n = row.size();
        for (int i = 0; i < n; ++i) {
            idx[row[i]] = i;
        }
        int res = 0;
        for (int i = 0; i < n; i += 2) {
            if (!isCouple(row[i], row[i + 1])) {
                int val = findMyCouple(row[i]);
                swap(row[i + 1], row[idx[val]]);
                // Update idx
                idx[row[idx[val]]] = idx[val];
                idx[row[i + 1]] = i + 1;
                ++res;
            }
        }
        return res;
    }
    
    bool isCouple(int a, int b) {
        return (!(a%2) && (b == a + 1)) || (!(b%2) && (a == b + 1));
    }
    
    int findMyCouple(int x) {
        return x%2 ? x - 1 : x + 1;
    }
};''',

    'toeplitz-matrix': '''class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        for(int i = 1; i < matrix.size(); i++)
            for(int j = 1; j < matrix[0].size(); j++)
                if(matrix[i][j] != matrix[i - 1][j - 1]) return false;
        return true;
    }
};''',

    'max-chunks-to-make-sorted': '''class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int count = 0, maxDis = 0;
        for(int i = 0; i < arr.size(); i++){
            maxDis = max(maxDis, arr[i]);
            if(maxDis == i) count++;
        }
        return count;
    }
};

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int curMax = 0, n = arr.size(), res = 0;
        for (int i = 0; i < n; ++i) {
            curMax = max(curMax, arr[i]);
            if (curMax == i) {
                ++res;
            }
        }
        return res;
    }
};''',

    'jewels-and-stones': '''class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int count = 0;
        unordered_set<char>s;
        for(char c: J) s.insert(c);
        for(char c: S) if(s.count(c)) count++;
        return count;
    }
};''',

    'sliding-puzzle': '''class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        unordered_set<string>visited;
        vector<vector<int>>dst({{1,2,3}, {4,5,0}});
        string target = toString(dst);
        
        int level = 0;
        
        queue<vector<vector<int>>>cur, next;
        
        cur.push(board);
        
        while(!cur.empty()) {
            auto node = cur.front();
            cur.pop();
            
            string s = toString(node);
            
            if (s == target) {
                return level;
            }
            
            visited.insert(s);
            
            auto nextStates = nextState(node);
            
            for (auto v: nextStates) {
                string t = toString(v);
                if (!visited.count(t)) {
                    next.push(v);
                }
            }
            if (cur.empty()) {
                ++level;
                swap(cur, next);
            }
        }
        return -1;
    }
    
    vector<vector<vector<int>>> nextState(vector<vector<int>>& board) {
        vector<vector<vector<int>>>res;
        auto pos = findZero(board);
        int r = pos[0];
        int c = pos[1];
        
        int left  = c - 1;
        int right = c + 1;
        int up    = r - 1;
        int down  = r + 1;
        
        if (left >= 0) {
            swap(board[r][left], board[r][c]);
            res.push_back(board);
            swap(board[r][left], board[r][c]);
        } 
        if (right < 3) {
            swap(board[r][right], board[r][c]);
            res.push_back(board);
            swap(board[r][right], board[r][c]);
        }
        if (up >= 0) {
            swap(board[up][c], board[r][c]);
            res.push_back(board);
            swap(board[up][c], board[r][c]);
        }
        if (down < 2) {
            swap(board[down][c], board[r][c]);
            res.push_back(board);
            swap(board[down][c], board[r][c]);
        }
        return res;
    }
    
    vector<int> findZero(vector<vector<int>>& board) {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (board[i][j] == 0) {
                    return {i, j};
                }
            }
        }
    }
    
    string toString(vector<vector<int>>& v) {
        string s;
        for (auto x: v) {
            for (auto y: x) {
                s += to_string(y) + ",";
            }
        }
        return s;
    }
};''',

    'swap-adjacent-in-lr-string': '''class Solution {
public:
    bool canTransform(string start, string end) {
        int n = start.size();
        string a, b;
        vector<int>posA, posB;
        for (int i = 0; i < n; ++i) {
            if (start[i] != 'X') {
                a.push_back(start[i]);
                posA.push_back(i);
            }
            if (end[i] != 'X') {
                b.push_back(end[i]);
                posB.push_back(i);
            }
        }
        if (a.size() != b.size()) {
            return false;
        }
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] != b[i] || (a[i] == 'L' && posA[i] < posB[i] || a[i] == 'R' && posA[i] > posB[i])) {
                return false;
            }
        }
        return true;
    }
};''',

    'k-th-symbol-in-grammar': '''class Solution {
public:
    int kthGrammar(int N, int K) {
        return N == 1 ? 0 : kthGrammar(N - 1, (K + 1) / 2) ? K % 2 : !(K % 2);
    }
};''',

    'minimum-distance-between-bst-nodes': '''// Recursive
class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        int minDiff = INT_MAX;
        TreeNode* pre = NULL;
        DFS(root, pre, minDiff);
        return minDiff;
    }
    
    void DFS(TreeNode* root, TreeNode*& pre, int& minDiff){
        if(!root) return;
        DFS(root->left, pre, minDiff);
        if(pre) minDiff = min(minDiff, abs(root->val - pre->val));
        pre = root;
        DFS(root->right, pre, minDiff);
    }
};

// Non-recursive
class Solution {
public:
    int minDiffInBST(TreeNode* root) {
        int minDiff = INT_MAX;
        stack<TreeNode*>s;
        TreeNode* p = root, *pre = NULL;
        while(!s.empty() || p){
            while(p){
                s.push(p);
                p = p->left;
            }
            if(pre) minDiff = min(minDiff, abs(s.top()->val - pre->val));
            pre = s.top();
            s.pop();
            p = pre->right;
        }
        return minDiff;
    }
};''',

    'letter-case-permutation': '''class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string>res;
        DFS(S, 0, res);
        return res;
    }
    
    void DFS(string S, int pos, vector<string>& res){
        if(pos == S.size()){
            res.push_back(S);
            return;
        }
        DFS(S, pos + 1, res);
        char c = S[pos];
        if(isalpha(c)){
            S[pos] = islower(c) ? toupper(c) : tolower(c);
            DFS(S, pos + 1, res);
        }
    }
};''',

    'is-graph-bipartite': '''class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int>color(n);
        color[0] = 1;
        for(int i = 0; i < n; i++){
            auto neigh = graph[i];
            if(!color[i]) for(auto j: neigh) if(color[j]){ color[i] = -color[j]; break; }   // If un-colored, pick a color by neighbor 
            if(!color[i]) color[i] = 1;  // Empty neighbor or no colored neighbor, colored 1 as default
            for(auto j: neigh)
                if(!color[j]) color[j] = -color[i];
                else if(color[i] != -color[j]) return false;
        }
        return true;
    }
};''',

    'cheapest-flights-within-k-stops': '''// DFS + Brute Force
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        int minPrice = INT_MAX;
        vector<vector<vector<int>>>g(n);
        for(auto v: flights) g[v[0]].push_back({v[1], v[2]});
        dfs(g, src, dst, K, 0, minPrice);
        return minPrice == INT_MAX ? -1 : minPrice;
    }
    
    void dfs(vector<vector<vector<int>>>& g, int cur, int dst, int K, int price, int& minPrice){
        if(cur == dst){
            minPrice = min(minPrice, price);
            return;
        }
        if(K == -1 || price >= minPrice) return;
        for(auto v: g[cur]) dfs(g, v[0], dst, K - 1, price + v[1], minPrice);
    }
};

// BFS + Priority_queue
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<int>>g(101);
        vector<vector<int>>w(101, vector<int>(101));
        for (auto& v: flights) {
            int a = v[0];   // src
            int b = v[1];   // dst
            int c = v[2];   // weight
            g[a].push_back(b);
            w[a][b] = c;
        }
        auto comp = [](vector<int>& v1, vector<int>& v2) {
          return v1[1] > v2[1];  
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)>pq(comp);
        pq.push({src, 0, K});
        while (!pq.empty()) {
            auto v = pq.top();
            pq.pop();
            int from = v[0];
            int cost = v[1];
            int stop = v[2];
            
            if (from == dst) {
                return cost;
            }
            if (stop < 0) {
                continue;
            }
            --stop;
            for (int x: g[from]) {
                pq.push({x, cost + w[from][x], stop});
            }
        }
        return -1;
    }
};''',

    'custom-sort-string': '''class Solution {
public:
    string customSortString(string S, string T) {
        string res = "";
        vector<int>v(26);
        for(auto c: T) v[c - 'a']++;
        for(auto c: S)
            while(v[c - 'a']--) res.push_back(c);
        for(int i = 0; i < 26; i++)
            while(v[i]-- > 0) res.push_back('a' + i);
        return res;
    }
};''',

    'number-of-matching-subsequences': '''class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        int res = 0;
        vector<vector<int>>bucket(26);
        for(int i = 0; i < S.size(); i++) bucket[S[i] - 'a'].push_back(i);
        for(auto s: words){
            int pre = -1, cur = -1, i = 0;
            for(;i < s.size(); i++){
                for(auto x: bucket[s[i] - 'a']){
                    if(x > pre){
                        cur = x;
                        break;
                    }
                }
                if(cur == pre) break;
                pre = cur;
            }
            if(i == s.size()) res++;
        }
        return res;
    }
};''',

    'all-paths-from-source-to-target': '''class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>>res;
        dfs(graph, res, {}, 0);
        return res;
    }
    
    void dfs(vector<vector<int>>& graph, vector<vector<int>>& res, vector<int> path, int node){
        path.push_back(node);
        if(graph[node].size() == 0) res.push_back(path);
        for(int neigh: graph[node]) dfs(graph, res, path, neigh);
    }
};''',

    'smallest-rotation-with-highest-score': '''class Solution {
public:
    int bestRotation(vector<int>& A) {
        int n = A.size();
        vector<int>k(n);
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i - A[i]; j++) k[j]++;
            for(int j = i + 1; j <= i + n - A[i] && j < n; j++) k[j]++;
        }
        return max_element(k.begin(), k.end()) - k.begin();
    }
};''',

    'champagne-tower': '''class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        vector<double>tower((1 + 100) * 100 / 2);
        tower[0] = poured;
        for(int i = 0; i < 99; i++){
            for(int j = 0; j <= i; j++){
                int idx = index(i, j);
                if(tower[idx] > 1){
                    double remain = tower[idx] - 1;
                    tower[idx] = 1;
                    tower[index(i + 1, j)] += remain / 2;
                    tower[index(i + 1, j + 1)] += remain / 2;
                }
            }
        }
        return tower[index(query_row, query_glass)];
    }
    
    int index(int row, int col){
        return row * (row + 1) / 2 + col;
    }
};''',

    'find-eventual-safe-states': '''class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int>res;
        int n = graph.size();
        vector<int>loop(n), safe(n), visited(n);
        for(int i = 0; i < n; i++)
            if(isSafe(graph, visited, loop, safe, i)) res.push_back(i);
        return res;
    }
    
    bool isSafe(vector<vector<int>>& graph, vector<int>& visited, vector<int>& loop, vector<int>& safe, int node){
        if(safe[node]) return true;
        if(loop[node] || visited[node]) return false;
        visited[node] = 1;
        bool b = true;
        for(int neigh: graph[node]) b &= isSafe(graph, visited, loop, safe, neigh);
        visited[node] = 0;
        b ? safe[node] = 1 : loop[node] = 1;
        return b;
    }
};

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int>res;
        int n = graph.size();
        vector<int>dp(n);
        vector<int>visited(n);
        for (int i = 0; i < n; ++i) {
            if (dfs(graph, i, visited, dp)) {
                res.push_back(i);
            }
        }
        return res;
    }
    
    bool dfs(vector<vector<int>>& graph, int node, vector<int>& visited, vector<int>& dp) {
        if (dp[node]) {
            return dp[node] == 1 ? true : false;
        }
        if (visited[node]) {
            return false;
        }
        
        visited[node] = 1;
        bool isValid = true;
        for (int x : graph[node]) {
            isValid &= dfs(graph, x, visited, dp);
        }
        visited[node] = 0;
        dp[node] = isValid ? 1 : -1;
        return isValid;
    }
};''',

    'bricks-falling-when-hit': '''class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        vector<int>res;
        int m = grid.size(), n = grid[0].size();
        for (auto& v: hits) {
            int r = v[0], c = v[1], count = 0;
            grid[r][c] = 0;
            if(!reachTop(grid, r - 1, c, m, n)) {
                erase(grid, r - 1, c, m, n, count);
            }
            if(!reachTop(grid, r + 1, c, m, n)) {
                erase(grid, r + 1, c, m, n, count);
            }
            if(!reachTop(grid, r, c - 1, m, n)) {
                erase(grid, r, c - 1, m, n, count);
            }
            if(!reachTop(grid, r, c + 1, m, n)) {
                erase(grid, r, c + 1, m, n, count);
            }
            res.push_back(count);
        }
        return res;
    }
    
    bool reachTop(vector<vector<int>>& grid, int r, int c, int m, int n) {
        if (r < 0 || c < 0 || r == m || c == n || grid[r][c] == 0) {
            return false;
        }
        if (r == 0) {
            return true;
        }
        int tmp = grid[r][c];
        grid[r][c] = 0;
        bool res = reachTop(grid, r + 1, c, m, n) || reachTop(grid, r, c + 1, m, n)
                || reachTop(grid, r - 1, c, m, n) || reachTop(grid, r, c - 1, m, n);
        grid[r][c] = tmp;
        return res;
    }
    
    void erase(vector<vector<int>>& grid, int r, int c, int m, int n, int& count) {
        if (r < 0 || c < 0 || r == m || c == n || grid[r][c] == 0) {
            return;
        }
        ++count;
        grid[r][c] = 0;
        erase(grid, r + 1, c, m, n, count);
        erase(grid, r - 1, c, m, n, count);
        erase(grid, r, c + 1, m, n, count);
        erase(grid, r, c - 1, m, n, count);
    }
};''',

    'unique-morse-code-words': '''class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string>table{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        unordered_set<string>s;
        for(string x: words){
            string t = "";
            for(char c: x) t += table[c - 'a'];
            s.insert(t);
        }
        return s.size();
    }
};''',

    'split-array-with-same-average': '''class Solution {
public:
    bool splitArraySameAverage(vector<int>& A) {
        int sum = 0, n = A.size();
        for (int& x: A) {
            sum += x;
        }
        sort(A.rbegin(), A.rend());
        for (int i = 1; i <= n/2; ++i) {
            if (sum*i%n == 0 && dfs(A, 0, i, sum*i/n, n)) {
                return true;
            }
        }
        return false;
    }
    
    bool dfs(vector<int>& A, int pos, int count, int target, int& n) {
        if (count == 0) {
            return target == 0;
        }
        if (pos == n || target > A[pos] * count) {
            return false;
        }

        for (int i = pos; i < n; ++i) {
            if (target >= A[i] && dfs(A, i + 1, count - 1, target - A[i], n)) {
                return true;
            }
        }
        return false;
    }
};''',

    'number-of-lines-to-write-string': '''class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int line = 1, sum = 0;
        for(char c: S){
            sum += widths[c - 'a'];
            if(sum > 100) sum = widths[c - 'a'], line++;
        }
        return {line, sum};
    }
};''',

    'max-increase-to-keep-city-skyline': '''class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<int>rowMax(m);
        vector<int>colMax(n);
        // Store the maximum value of each row and column
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        // Sum up the difference
        int sum = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                sum += min(rowMax[i], colMax[j]) - grid[i][j];
        return sum;
    }
};''',

    'expressive-words': '''class Solution {
public:
    int expressiveWords(string S, vector<string>& words) {
        int res = 0;
        vector<char>letter;
        vector<int>count;
        for(int i = 0, index = 0; i < S.size(); index++){
            letter.push_back(S[i]);
            count.push_back(1);
            int j = i + 1;
            while(j < S.size() && S[j] == S[i]) count[index]++, j++;
            i = j;
        }
        
        for(auto s: words){
            vector<char>v;
            vector<int>c;
            bool b = true;
            int index = 0;
            for(int i = 0; i < s.size(); index++){
                v.push_back(s[i]);
                c.push_back(1);
                int j = i + 1;
                while(j < s.size() && s[j] == s[i]) c[index]++, j++;
                if(v[index] != letter[index] || (c[index] != count[index] && count[index] < 3) || c[index] > count[index]){
                    b = false;
                    break;
                }
                i = j;
            }
            if(b && index == count.size()) res++;
        }
        return res;
    }
};

class Solution {
public:
    int expressiveWords(string S, vector<string>& words) {
        int res = 0;
        for (auto& x: words) {
            if (isValid(x, S)) {
                ++res;
            }
        }
        return res;
    }
    
    bool isValid(string& x, string& y) {
        if (x.size() > y.size()) {
            return false;
        }
        
        int i = 0, j = 0, m = x.size(), n = y.size();
        while (i < m) {
            if (x[i] != y[j]) {
                return false;
            }
            
            int count1 = 1, count2 = 1;
            while (i + 1 < m && x[i] == x[i + 1]) {
                ++i;
                ++count1;
            }
            
            while(j + 1 < n && y[j] == y[j + 1]) {
                ++j;
                ++count2;
            }
            ++i;
            ++j;
            if (count1 == count2 || (count1 < count2 && count2 >= 3)) {
                continue;
            } else {
                return false;
            }
        }
        return i == m && j == n;
    }
};''',

    'binary-tree-pruning': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if(!root) return NULL;
        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);
        return (!root->val && !root->left && !root->right) ? NULL : root;
    }
};''',

    'bus-routes': '''class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        if (S == T) {
            return 0;
        }
        unordered_map<int, vector<int>>m(501);  // Stop to Bus
        int n = routes.size();
        // Build graph Stop-to-Bus
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < routes[i].size(); ++j) {
                m[routes[i][j]].push_back(i);
            }
        }
        vector<int>visitedBus(501);
        vector<int>visitedStop(1000001);
        // BFS
        queue<int>cur;
        queue<int>next;
        for (int& b: m[S]) {
            cur.push(b);
        }
        int count = 1;
        while (!cur.empty()) {
            int bus = cur.front();
            cur.pop();
            visitedBus[bus] = 1;
            for (int& s: routes[bus]) {
                if (s == T) {
                    return count;
                }
                if (visitedStop[s]) {
                   continue;
                }
                visitedStop[s] = 1;
                for (int& b: m[s]) {
                    if (!visitedBus[b]) {
                        next.push(b);
                    }
                }
            }
            
            if (cur.empty()) {
                ++count;
                swap(cur, next);
            }
        }
        return -1;
    }
};''',

    'most-common-word': '''class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_map<string, int>m;
        for(int i = 0; i < paragraph.size();){
            string s = "";
            while(i < paragraph.size() && isalpha(paragraph[i])) s.push_back(tolower(paragraph[i++]));
            while(i < paragraph.size() && !isalpha(paragraph[i])) i++;
            m[s]++;
        }
        for(auto x: banned) m[x] = 0;
        string res = "";
        int count = 0;
        for(auto x: m)
            if(x.second > count) res = x.first, count = x.second;
        return res;  
    }
};''',

    'short-encoding-of-words': '''class Solution {
private:
    struct TrieNode{
        int length;
        bool isWord;
        vector<TrieNode*>next;
        TrieNode(int x): length(x), isWord(false), next(vector<TrieNode*>(26)){}
    };
    TrieNode* root;

public:
    int minimumLengthEncoding(vector<string>& words) {
        root = new TrieNode(0);
        int count = 0;
        for(auto& s: words){
            reverse(s.begin(), s.end());
            buildTrie(s, count);
        }
        return count;
    }
    
    void buildTrie(string& s, int& count){
        auto p = root;
        bool newWord = false;
        for(int i = 0; i < s.size(); i++){
            char c = s[i];
            if(!p->next[c - 'a']){
                if(!newWord){
                    count++;
                    if(p->isWord){
                        count--;
                        count -= p->length;
                        p->isWord = false;
                    }
                    newWord = true;
                }
                p->next[c - 'a'] = new TrieNode(i + 1);
            }
            p = p->next[c - 'a'];
        }
        if(newWord){
            count += p->length;
            p->isWord = true;
        }
    }
};''',

    'shortest-distance-to-a-character': '''class Solution {
public:
    vector<int> shortestToChar(string S, char C) {
        vector<int>pos, res;
        for(int i = 0; i < S.size(); i++) if(S[i] == C) pos.push_back(i);
        for(int i = 0, p = 0; i < S.size(); i++){
            if(p < pos.size() && i == pos[p]) p++;
            res.push_back(p == 0 ? pos[0] - i : p == pos.size() ? i - pos[p - 1] : min(i - pos[p - 1], pos[p] - i));
        }
        return res;
    }
};''',

    'most-profit-assigning-work': '''class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int res = 0;
        vector<vector<int>>v;
        for(int i = 0; i < difficulty.size(); i++) v.push_back({difficulty[i], profit[i]});
        sort(v.begin(), v.end(), [](vector<int>& v1, vector<int>& v2){ return v1[0] < v2[0]; });
        int maxProfit = 0;
        for(auto& x: v){
            maxProfit = max(maxProfit, x[1]);
            x[1] = maxProfit;
        }
        for(auto& x: worker){
            int pos = upper_bound(v.begin(), v.end(), x, [](int v1, vector<int>& v2){ return v1 < v2[0]; }) - v.begin() - 1;
            if(pos >= 0) res += v[pos][1];
        }
        return res;
    }
};''',

    'positions-of-large-groups': '''class Solution {
public:
    vector<vector<int>> largeGroupPositions(string S) {
        vector<vector<int>>res;
        int l = 0, r = 0, n = S.size();
        while(l < n){
            while(r < n && S[r] == S[l]) r++;
            if(r  - l >= 3) res.push_back({l, r - 1});
            l = r;
        }
        return res;
    }
};''',

    'flipping-an-image': '''class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for(auto& x: A){
            reverse(x.begin(), x.end());
            for(auto& y: x) y ^= 1;
        }
        return A;
    }
};''',

    'sum-of-distances-in-tree': '''class Solution {
public:
    vector<int> sumOfDistancesInTree(int N, vector<vector<int>>& edges) {
        vector<vector<int>>g(N, vector<int>());
        for(auto& e: edges){
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<int>res(N), child(N), visited(N);
        dfs(g, res, child, 0, 0, visited);
        for(auto& x: visited) x = 0;
        dfs(g, res, child, 0, visited, N);
        return res;
    }
    // Sum of the distances of node 0
    void dfs(vector<vector<int>>& g, vector<int>& res, vector<int>& child, int len, int root, vector<int>& visited){
        visited[root] = 1;
        res[0] += len++;
        for(auto& x: g[root]){
            if(visited[x]) continue;
            dfs(g, res, child, len, x, visited);
            child[root] += child[x];
        }
        child[root] += 1;
    }
    // Sum of the distances of node 1 to N - 1
    void dfs(vector<vector<int>>& g, vector<int>& res, vector<int>& child, int root, vector<int>& visited, int N){
        visited[root] = 1;
        for(auto& x: g[root]){
            if(visited[x]) continue;
            res[x] = res[root] - child[x] + N - child[x];
            dfs(g, res, child, x, visited, N);
        }
    }
};''',

    'rectangle-overlap': '''class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return (min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])) && (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]));
    }
};''',

    'keys-and-rooms': '''// DFS
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int count = 0, n = rooms.size();
        vector<int>visited(n);
        dfs(rooms, 0, visited, count);
        return count == n;
    }
    
    void dfs(vector<vector<int>>& rooms, int pos, vector<int>& visited, int& count){
        if(visited[pos]) return;
        count++;
        visited[pos] = 1;
        for(auto x: rooms[pos]) dfs(rooms, x, visited, count);
    }
};

// BFS
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int count = 0, n = rooms.size();
        vector<int>visited(n);
        queue<int>q;
        q.push(0);
        while(!q.empty()){
            int x = q.front();
            q.pop();
            if(visited[x]) continue;
            visited[x] = 1;
            count++;
            for(auto neigh: rooms[x]) q.push(neigh);
        }
        return count == n;
    }
};''',

    'guess-the-word': '''/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    void findSecretWord(vector<string>& wordlist, Master& master) {
        vector<string>cur, next;
        cur = wordlist;
        for (int i = 0; i < 10; ++i) {
            int n = cur.size();
            auto word = cur[rand() % n];
            int match = master.guess(word);
            if (match == 6) {
                break;
            }
            for (auto& s: cur) {
                if (distance(s, word) == match) {
                    next.push_back(s);
                }
            }
            cur.clear();
            swap(cur, next);
        }
    }
    
    int distance(string& a, string& b) {
        int res = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] == b[i]) {
                ++res;
            }
        }
        return res;
    }
};''',

    'backspace-string-compare': '''// Two Pointers
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int i = S.size() - 1, j = T.size() - 1, countA = 0, countB = 0;
        while(i >= 0 || j >= 0){
            while(i >= 0 && (S[i] == '#' || countA > 0)) S[i--] == '#' ? ++countA : --countA;
            while(j >= 0 && (T[j] == '#' || countB > 0)) T[j--] == '#' ? ++countB : --countB;
            if(i < 0 || j < 0) return i == j;
            if(S[i--] != T[j--]) return false;
        }
        return i == j;
    }
};

// Stack
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        string a = "", b = "";
        for(auto c: S) c == '#' ? a.size() > 0 ? a.pop_back() : void() : a.push_back(c);
        for(auto c: T) c == '#' ? b.size() > 0 ? b.pop_back() : void() : b.push_back(c);
        return a == b;
    }
};

class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int i = S.size() - 1, j = T.size() - 1, count1 = 0, count2 = 0;
        while (i >= 0 || j >= 0) {
            while (i >= 0 && (S[i] == '#' || count1 > 0)) {
                if (S[i] == '#') {
                    ++count1;
                } else {
                    --count1;
                }
                --i;
            }
            
            while (j >= 0 && (T[j] == '#' || count2 > 0)) {
                if (T[j] == '#') {
                    ++count2;
                } else {
                    --count2;
                }
                --j;
            }
            
            if (i < 0 || j < 0) {
                return i == j;
            }
            
            if (S[i] != T[j]) {
                return false;
            }
            --i;
            --j;
        }
        return true;
    }
};''',

    'longest-mountain-in-array': '''class Solution {
public:
    int longestMountain(vector<int>& A) {
        int l = 0, r = 1, res = 0, n = A.size();
        bool up = true;
        while(r < n){
            if(up && r - l > 1 && A[r] < A[r - 1]) up = false;
            if(up && (A[r] <= A[r - 1]) || !up && A[r] >= A[r - 1]){
                l = up ? r : --r;
                up = true;
            }
            r++;
            if(!up && r - l > 2) res = max(res, r - l);
        }
        return res;
    }
};''',

    'hand-of-straights': '''class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        int n = hand.size();
        if(n % W) return false;
        map<int, int>m;
        for(int x: hand) m[x]++;
        auto l = m.begin();
        for(int i = 0; i < n/W; i++){
            auto r = l, t = m.end();
            advance(r, W - 1);
            for(int j = W - 1; j >= 0; j--, r--)
                if((*r).second-- <= 0 || ((*r).first - (*l).first != j)) return false;
                else if((*r).second > 0) t = r;
            if(t != m.end()) l = t;
            else advance(l, W);
        }
        return true;
    }
};''',

    'shifting-letters': '''class Solution {
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        long sum = 0;
        for(int i = S.size() - 1; i >= 0; sum += shifts[i--]) S[i] = 'a' + (S[i] - 'a' + sum + shifts[i]) % 26;
        return S;
    }
};''',

    'maximize-distance-to-closest-person': '''class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int res = -1, d = 0;
        for(auto x: seats) if(x) res = max(res, res == -1 ? d : d/2), d = 1; else d++;
        return max(res, d - 1);
    }
};''',

    'peak-index-in-a-mountain-array': '''class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int n = A.size();
        // O(n)
        for (int i = 1; i < n - 1; ++i) {
            if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
                return i;
            }
        }
        
        // O(logn)
        int l = 1, r = n - 2, mid;
        while (l <= r) {
            mid = l + (r - l)/2;
            if (A[mid] > A[mid - 1] && A[mid] > A[mid + 1]) {
                return mid;
            } else if (A[mid] > A[mid - 1]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
};''',

    'car-fleet': '''class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        int res = n;
        vector<vector<int>>cars;
        for (int i = 0; i < n; ++i) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end());
        
        vector<double>time;
        for (int i = 0; i < n; ++i) {
            time.push_back(((double)target - cars[i][0]) / cars[i][1]);
        }
        for (int i = n - 2; i >= 0; --i) {
            if (time[i] <= time[i + 1]) {
                --res;
                time[i] = time[i + 1];
            }
        }
        return res;
    }
};''',

    'exam-room': '''class ExamRoom {
public:
    ExamRoom(int N) {
        this->N = N;
    }
    
    int seat() {
        if (s.size() == 0) {
            s.insert(0);
            return 0;
        } else if (s.size() == 1) {
            int pos = *s.begin() < N/2 ? N - 1 : 0;
            s.insert(pos);
            return pos;
        } else {
            int maxDis = -1;
            int res = -1;
            if (!s.count(0)) {
                maxDis = *s.begin() - 1;
                res = 0;
            }
            auto p1 = s.begin();
            auto p2 = p1;
            ++p2;
            while (p2 != s.end()) {
                int pos = (*p2 + *p1)/2;
                int d = min(pos - *p1, *p2 - pos) - 1;
                if (d > maxDis) {
                    maxDis = d;
                    res = (*p1 + *p2)/2;
                }
                ++p1;
                ++p2;
            }
            if (!s.count(N - 1)) {
                auto e = s.end();
                --e;
                int d = N - 1 - *e - 1;
                if (d > maxDis) {
                    res = N - 1;
                }
            }
            s.insert(res);
            return res;
        }
    }
    
    void leave(int p) {
        s.erase(p);
    }
    
private:
    set<int>s;
    int N;
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */''',

    'minimum-cost-to-hire-k-workers': '''class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int K) {
        double res = INT_MAX;
        int n = quality.size();
        vector<vector<double>>workers;
        for (int i = 0; i < n; ++i) {
            workers.push_back({(double)wage[i]/quality[i], quality[i]});
        }
        sort(workers.begin(), workers.end());
        int sum = 0;
        priority_queue<int>pq;
        for (auto& x: workers) {
            sum += x[1];
            pq.push(x[1]);
            if (pq.size() > K) {
                sum -= pq.top();
                pq.pop();
            }
            if (pq.size() == K) {
                res = min(res, x[0] * sum);
            }
        }
        return res;
    }
};''',

    'buddy-strings': '''class Solution {
public:
    bool buddyStrings(string A, string B) {
        if(A.size() != B.size()) return false;
        int n = A.size(), pos = -1;
        vector<int>count(26);
        bool repeat = false, swaped = false;
        for(int i = 0; i < n; i++){
            if(A[i] != B[i]){
                if(pos == -1) pos = i;
                else if(swaped || A[pos] != B[i] || A[i] != B[pos]) return false;
                else swaped = true;
            }
            if(++count[A[i] - 'a'] > 1) repeat = true;
        }
        return swaped || repeat;
    }
};''',

    'leaf-similar-trees': '''class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>v;
        int pos = 0;
        dfs(root1, v, pos);
        pos = 0;
        return dfs(root2, v, pos);
    }
    
    bool dfs(TreeNode* p, vector<int>& v, int& pos){
        if(!p) return true;
        if(!p->left && !p->right){
            if(v.size() == pos) v.push_back(p->val);
            return v[pos++] == p->val;
        }
        return dfs(p->left, v, pos) && dfs(p->right, v, pos);
    }
};''',

    'middle-of-the-linked-list': '''class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        auto a = head, b = head;
        while(b && b->next) a = a->next, b = b->next->next;
        return a;
    }
};''',

    'uncommon-words-from-two-sentences': '''class Solution {
public:
    vector<string> uncommonFromSentences(string A, string B) {
        unordered_map<string, int>m;
        vector<string>res;
        stringstream ss(A + " " + B);
        string t;
        while(ss>>t) m[t]++;
        for(auto& x: m) if(x.second == 1) res.push_back(x.first);
        return res;
    }
};''',

    'fair-candy-swap': '''class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int sumA(0), sumB(0), half;
        unordered_set<int>s;
        for(auto& x: A) sumA += x;
        for(auto& x: B) sumB += x, s.insert(x);
        half = (sumA + sumB) / 2;
        for(auto& x: A) if(s.count(half - (sumA - x))) return {x, half - (sumA - x)};
    }
};''',

    'construct-binary-tree-from-preorder-and-postorder-traversal': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        if (pre.empty()) {
            return NULL;
        }
        
        TreeNode* root = new TreeNode(pre[0]);
        
        if(pre.size() == 1) {
            return root;
        }
        
        vector<int>preLeft, preRight, postLeft, postRight;
        int rootLeft = pre[1];
        int pos = find(post.begin(), post.end(), rootLeft) - post.begin();
        
        postLeft.assign(post.begin(), post.begin() + pos + 1);
        postRight.assign(post.begin() + pos + 1, post.end() - 1);
        preLeft.assign(pre.begin() + 1, pre.begin() + 1 + pos + 1);
        preRight.assign(pre.begin() + 1 + pos + 1, pre.end());
        
        root->left = constructFromPrePost(preLeft, postLeft);
        root->right = constructFromPrePost(preRight, postRight);
        
        return root;
    }
};''',

    'find-and-replace-pattern': '''class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string>res;
        for (auto& s: words) {
            if (isValid(s, pattern)) {
                res.push_back(s);
            }
        }
        return res;
    }
    
    bool isValid(string& a, string& b) {
        unordered_map<char, char>m, t;
        int n = a.size(), l = b.size();
        if (n != l) {
            return false;
        }
        
        for (int i = 0; i < n; ++i) {
            if (m.count(a[i]) || t.count(b[i])) {
                if (m[a[i]] == b[i] && t[b[i]] == a[i]) {
                    continue;
                } else {
                    return false;
                }
            }
            m[a[i]] = b[i];
            t[b[i]] = a[i];
        }
        return true;
    }
};

class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string>res;
        for (auto& s: words) {
            if (normalize(s) == normalize(pattern)) {
                res.push_back(s);
            }
        }
        return res;
    }
    
    string normalize(string& s) {
        unordered_map<char, char>m;
        string res;
        char c = 'a';
        for (auto& x: s) {
            if (!m.count(x)) {
                m[x] = c++;
            }
        }
        for (auto& x: s) {
            res.push_back(m[x]);
        }
        return res;
    }
};''',

    'all-possible-full-binary-trees': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int N) {
        vector<TreeNode*> res;
        if (N == 1) {
            res.push_back(new TreeNode(0));
            return res;
        }
        --N;
        for (int i = 1; i < N; i += 2) {
            auto left = allPossibleFBT(i);
            auto right = allPossibleFBT(N - i);
            for (TreeNode* l: left) {
                for (TreeNode* r: right) {
                    TreeNode* cur = new TreeNode(0);
                    cur->left = l;
                    cur->right = r;
                    res.push_back(cur);
                }
            }
        }
        return res;
    }
};''',

    'monotonic-array': '''class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        bool a(true), b(true);
        int n = A.size();
        for(int i = 0; i < n - 1 && (a || b); ++i){
            if(A[i] > A[i + 1]) a = false;
            if(A[i] < A[i + 1]) b = false;
        }
        return a || b;
    }
};''',

    'rle-iterator': '''class RLEIterator {
public:
    RLEIterator(vector<int> A) {
        for (auto x: A) {
            nums.push_back(x);
        }
    }
    
    int next(int n) {
        while (!nums.empty() && nums.front() < n ) {
            n -= nums.front();
            nums.pop_front();
            nums.pop_front();
        }
        if (nums.empty()) {
            return -1;
        }
        int count = nums.front();
        nums.pop_front();
        int res = nums.front();
        count -= n;
        if (count == 0) {a
            nums.pop_front();
        } else {
            nums.push_front(count);
        }
        return res;
    }
    
private:
    deque<int>nums;
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(A);
 * int param_1 = obj.next(n);
 */''',

    'fruit-into-baskets': '''class Solution {
public:
    int totalFruit(vector<int>& tree) {
        int i = 0, j = 0, count = 0;
        unordered_map<int, int>m;
        int res = 0;
        while (j < tree.size()) {
            if (m[tree[j]] == 0) {
                ++count;
            }
            ++m[tree[j++]];
            while (count > 2) {
                if (--m[tree[i++]] == 0) {
                    --count;
                }
            }
            res = max(res, j - i);
        }
        return res;
    }
};''',

    'online-election': '''class TopVotedCandidate {
public:
    TopVotedCandidate(vector<int> persons, vector<int> times) {
        int curLead = -1;
        unordered_map<int, int>count;
        for (int i = 0; i < times.size(); ++i) {
            count[persons[i]]++;
            if(count[persons[i]] >= count[curLead]) {
                curLead = persons[i];
            }
            m[times[i]] = curLead;
        }
    }
    
    int q(int t) {
        return (--m.upper_bound(t))->second;
    }

private:
    
    map<int, int>m;
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */''',

    'x-of-a-kind-in-a-deck-of-cards': '''class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int>m;
        int n = deck.size();
        for (int i = 0; i < n; ++i) {
            m[deck[i]]++;
        }
        int base = 0;
        for (auto& p: m) {
            base = gcd(p.second, base);
        }
        return base > 1;
    }
    
    int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
};''',

    'word-subsets': '''class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        vector<string>res;
        
        vector<int>maxCount(26);
        
        for (int i = 0; i < B.size(); ++i) {
            vector<int> v = getCount(B[i]);
            
            for (int j = 0; j < 26; ++j) {
                maxCount[j] = max(maxCount[j], v[j]);
            }
        }
        
        for (int i = 0; i < A.size(); ++i) {
            vector<int> v = getCount(A[i]);
            
            bool isValid(true);
            
            for (int j = 0; j < 26; ++j) {
                if (v[j] < maxCount[j]) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                res.push_back(A[i]);
            }
        }
        
        return res;
    }
    
    vector<int> getCount(string& s) {
        vector<int>cnt(26);
        
        for (int i = 0; i < s.size(); ++i) {
            cnt[s[i] - 'a']++;
        }
        
        return cnt;
    }
};''',

    'long-pressed-name': '''class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int a = 0, b = 0, n = name.size(), m = typed.size();
        while (a < n && b < m) {
            if (name[a++] != typed[b++]) return false;
            while (b > 0 && name[a] != typed[b] && typed[b] == typed[b - 1]) ++b;
        }
        return a == n && b == m;
    }
};''',

    'unique-email-addresses': '''class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string>res;
        
        for (const string& s: emails) {
            string e = filter(s);
            res.insert(e);
        }
        
        return res.size();
    }
    
    string filter(const string& email) {
        string res;
        int i = 0, n = email.size();
        bool ignore = false;
        for (; i < n; ++i) {
            if (email[i] == '@') {
                break;
            } else if (ignore || email[i] == '.') {
                continue;
            } else if (email[i] == '+') {
                ignore = true;
            }
            res.push_back(email[i]);
        }
        
        for (; i < n; ++i) {
            res.push_back(email[i]);
        }
        return res;
    }
};''',

    'beautiful-array': '''class Solution {
public:
    vector<int> beautifulArray(int N) {
        vector<int> res;
        for (int i = 1; i <= N; ++i) {
            res.push_back(i);
        }
        return beautify(res);
    }
    
    vector<int> beautify(vector<int>& v) {
        if (v.size() == 1) {
            return v;
        }
        vector<int> odd, even;
        for (int i = 0; i < v.size(); ++i) {
            if (i % 2) {
                odd.push_back(v[i]);
            } else {
                even.push_back(v[i]);
            }
        }
        auto L = beautify(odd);
        auto R = beautify(even);
        for (const auto& x: R) {
            L.push_back(x);
        }
        return L;
    }
};''',

    'number-of-recent-calls': '''class RecentCounter {
public:
    RecentCounter() {
        
    }
    
    int ping(int t) {
        while (!q.empty() && t - q.front() > 3000) {
            q.pop_front();
        }
        q.push_back(t);
        return q.size();
    }

private:
    deque<int>q;
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */''',

    'knight-dialer': '''class Solution {
public:
    int knightDialer(int N) {
        vector<long>dp(10, 1);
        vector<long>next(10, 1);
        vector<int>ways(10, 2);  // Number of ways we can jump from position X
        ways[5] = 0;
        ways[4] = 3;
        ways[6] = 3;
        long res = 10;
        while (--N) {
            res = 0;
            for (auto& x: dp) {
                x %= 1000000007;
            }
            for (int j = 0; j < 10; ++j) {
                res += dp[j] * ways[j];
                res %= 1000000007;
            }
            next[1] = dp[6] + dp[8];
            next[2] = dp[7] + dp[9];
            next[3] = dp[4] + dp[8];
            next[4] = dp[3] + dp[9] + dp[0];
            next[6] = dp[1] + dp[7] + dp[0];
            next[7] = dp[2] + dp[6];
            next[8] = dp[1] + dp[3];
            next[9] = dp[2] + dp[4];
            next[0] = dp[4] + dp[6];
            swap(dp, next);
        }
        return res;
    }
};''',

    'range-sum-of-bst': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        return !root ? 0 : 
               root->val < L ? rangeSumBST(root->right, L, R) : 
               root->val > R ? rangeSumBST(root->left, L, R) : root->val + rangeSumBST(root->right, L, R) + rangeSumBST(root->left, L, R);
    }
};''',

    'minimum-area-rectangle': '''class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        int minArea = 0;
        set<pair<int, int>>s;
        for (auto& p: points) {
            s.insert({p[0], p[1]});
        }
        
        for (int i = 0; i < points.size(); ++i) {
            for (int j = 0; j < points.size(); ++j) {
                auto a = points[i];
                auto b = points[j];
                
                if (a[0] == b[0] || a[1] == b[1]) {
                    continue;
                }

                pair<int, int> c = {b[0], a[1]};
                pair<int, int> d = {a[0], b[1]};
                
                if (s.count(c) && s.count(d)) {
                    int area = abs(a[1] - b[1]) * abs(b[0] - a[0]);
                    minArea = minArea ? min(minArea, area) : area;
                }
            }
        }
        return minArea;
    }
};''',

    'valid-mountain-array': '''class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        int i = 0, n = A.size();
        if (n < 3) {
            return false;
        }
        while (i < n - 1 && A[i] < A[i + 1]) {
            ++i;
        }
        if (i == 0 || i == n - 1) {
            return false;
        }
        while (i < n - 1 && A[i] > A[i + 1]) {
            ++i;
        }
        return i == n - 1;
    }
};''',

    'validate-stack-sequences': '''class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int>s1, s2;
        int m = pushed.size(), n = popped.size();
        for (int i = n - 1; i >= 0; --i) {
            s2.push(popped[i]);
        }
        
        for (int i = 0; i < m; ++i) {
            s1.push(pushed[i]);
            while (!s1.empty() && !s2.empty() && s1.top() == s2.top()) {
                s1.pop();
                s2.pop();
            }
        }
        return s2.empty();
    }
};''',

    'flip-equivalent-binary-trees': '''/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (!root1 || !root2) {
            return !root1 && !root2;
        }
        if (root1->val != root2->val) {
            return false;
        }
        return flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)
            || flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left);
    }
};''',

    'lcs': '''#include <bits/stdc++.h>

using namespace std;

vector <int> longestCommonSubsequence(vector <int> a, vector <int> b) {
    int n = a.size(), m = b.size();
    vector<int>res;
    vector<vector<int>>dp(n + 1, vector<int>(m + 1));
    dp[0][0] = 0;
    int maxlen = 0;
    for(int i = 1; i <= n; i++){
        int tmp = maxlen;
        for(int j = 1; j <= m; j++){
            dp[i][j] = a[i - 1] == b[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
            maxlen = max(maxlen, dp[i][j]);
        }
    }
    
    int r = n, c = m;
    
    while(res.size() < maxlen){
        if(dp[r][c] == dp[r - 1][c]) r--;
        else if(dp[r][c] == dp[r][c - 1]) c--;
        else{
            res.push_back(a[r - 1]);
            r--;
            c--;
        }
        
    }
    reverse(res.begin(), res.end());    
    return res;
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }
    vector<int> b(m);
    for(int b_i = 0; b_i < m; b_i++){
       cin >> b[b_i];
    }
    vector <int> result = longestCommonSubsequence(a, b);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;


    return 0;
}''',

}
