"""
LeetCode Solution Bank
~200 problems covering Easy/Medium across all major categories.
"""

SOLUTION_BANK = {
    # ─── Arrays ───────────────────────────────────────────────────
    "two-sum": '''class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []''',

    "best-time-to-buy-and-sell-stock": '''class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit''',

    "contains-duplicate": '''class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))''',

    "product-of-array-except-self": '''class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res''',

    "maximum-subarray": '''class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            max_sum = max(max_sum, curr)
        return max_sum''',

    "maximum-product-subarray": '''class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_min = cur_max = 1
        for n in nums:
            if n == 0:
                cur_min = cur_max = 1
                continue
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)
        return res''',

    "find-minimum-in-rotated-sorted-array": '''class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]''',

    "search-in-rotated-sorted-array": '''class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1''',

    "3sum": '''class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                    lo += 1; hi -= 1
                elif s < 0: lo += 1
                else: hi -= 1
        return res''',

    "container-with-most-water": '''class Solution:
    def maxArea(self, height: list[int]) -> int:
        lo, hi, res = 0, len(height) - 1, 0
        while lo < hi:
            res = max(res, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]: lo += 1
            else: hi -= 1
        return res''',

    "move-zeroes": '''class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos = 0
        for n in nums:
            if n != 0:
                nums[pos] = n
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0''',

    "majority-element": '''class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = candidate = 0
        for n in nums:
            if count == 0: candidate = n
            count += 1 if n == candidate else -1
        return candidate''',

    "rotate-array": '''class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]''',

    "missing-number": '''class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)''',

    "single-number": '''class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums: res ^= n
        return res''',

    "find-the-duplicate-number": '''class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow''',

    "sort-colors": '''class Solution:
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1''',

    "subarray-sum-equals-k": '''class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        total = res = 0
        for n in nums:
            total += n
            res += count[total - k]
            count[total] += 1
        return res''',

    "next-permutation": '''class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]: i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])''',

    "merge-intervals": '''class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res''',

    "jump-game": '''class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reach = 0
        for i, n in enumerate(nums):
            if i > reach: return False
            reach = max(reach, i + n)
        return True''',

    "spiral-matrix": '''class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res''',

    "set-matrix-zeroes": '''class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = set(); cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i); cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0''',

    "longest-consecutive-sequence": '''class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best = 0
        for n in num_set:
            if n - 1 not in num_set:
                cur = n; streak = 1
                while cur + 1 in num_set:
                    cur += 1; streak += 1
                best = max(best, streak)
        return best''',

    # ─── Strings ──────────────────────────────────────────────────
    "valid-anagram": '''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)''',

    "valid-palindrome": '''class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]''',

    "longest-substring-without-repeating-characters": '''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}; lo = res = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= lo:
                lo = seen[c] + 1
            seen[c] = i
            res = max(res, i - lo + 1)
        return res''',

    "longest-repeating-character-replacement": '''class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        lo = max_count = res = 0
        for hi, c in enumerate(s):
            count[c] += 1
            max_count = max(max_count, count[c])
            if (hi - lo + 1) - max_count > k:
                count[s[lo]] -= 1; lo += 1
            res = max(res, hi - lo + 1)
        return res''',

    "minimum-window-substring": '''class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t); missing = len(t)
        lo = start = end = 0
        for hi, c in enumerate(s, 1):
            if need[c] > 0: missing -= 1
            need[c] -= 1
            if missing == 0:
                while need[s[lo]] < 0:
                    need[s[lo]] += 1; lo += 1
                if not end or hi - lo < end - start:
                    start, end = lo, hi
                need[s[lo]] += 1; missing += 1; lo += 1
        return s[start:end]''',

    "group-anagrams": '''class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())''',

    "longest-palindromic-substring": '''class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for lo, hi in [(i, i), (i, i+1)]:
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    lo -= 1; hi += 1
                if hi - lo - 1 > len(res):
                    res = s[lo+1:hi]
        return res''',

    "palindromic-substrings": '''class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for lo, hi in [(i, i), (i, i+1)]:
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    count += 1; lo -= 1; hi += 1
        return count''',

    "encode-and-decode-strings": '''class Solution:
    def encode(self, strs: list[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> list[str]:
        res = []; i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res''',

    "reverse-string": '''class Solution:
    def reverseString(self, s: list[str]) -> None:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1; hi -= 1''',

    "roman-to-integer": '''class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i+1]]:
                result -= vals[s[i]]
            else:
                result += vals[s[i]]
        return result''',

    "longest-common-prefix": '''class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix: return ""
        return prefix''',

    "string-to-integer-atoi": '''class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-': s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit(): break
            num = num * 10 + int(c)
        num *= sign
        return max(-2**31, min(2**31 - 1, num))''',

    "count-and-say": '''class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            nxt = ""
            i = 0
            while i < len(s):
                c = s[i]; cnt = 0
                while i < len(s) and s[i] == c:
                    cnt += 1; i += 1
                nxt += str(cnt) + c
            s = nxt
        return s''',

    "fizz-buzz": '''class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1, n+1)]''',

    # ─── Linked Lists ──────────────────────────────────────────────
    "reverse-linked-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next; head.next = prev; prev = head; head = nxt
        return prev''',

    "merge-two-sorted-lists": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val: cur.next = l1; l1 = l1.next
            else: cur.next = l2; l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next''',

    "linked-list-cycle": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow == fast: return True
        return False''',

    "reorder-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next; curr.next = prev; prev = curr; curr = nxt
        l1, l2 = head, prev
        while l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2; l2.next = nxt1
            l1 = nxt1; l2 = nxt2''',

    "remove-nth-node-from-end-of-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lo = hi = dummy
        for _ in range(n + 1): hi = hi.next
        while hi:
            lo = lo.next; hi = hi.next
        lo.next = lo.next.next
        return dummy.next''',

    "copy-list-with-random-pointer": '''from typing import Optional
class Node:
    def __init__(self, x, next=None, random=None): self.val=x; self.next=next; self.random=random
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_new = {None: None}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val); cur = cur.next
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
        return old_to_new[head]''',

    "add-two-numbers": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(); carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1: val += l1.val; l1 = l1.next
            if l2: val += l2.val; l2 = l2.next
            carry, val = divmod(val, 10)
            cur.next = ListNode(val); cur = cur.next
        return dummy.next''',

    "middle-of-the-linked-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
        return slow''',

    "intersection-of-two-linked-lists": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a''',

    "palindrome-linked-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head: vals.append(head.val); head = head.next
        return vals == vals[::-1]''',

    # ─── Trees ────────────────────────────────────────────────────
    "maximum-depth-of-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))''',

    "same-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)''',

    "invert-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root''',

    "binary-tree-maximum-path-sum": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.res''',

    "binary-tree-level-order-traversal": '''from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: return []
        res = []; queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res''',

    "serialize-and-deserialize-binary-tree": '''from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Codec:
    def serialize(self, root):
        if not root: return "N"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
    def deserialize(self, data):
        vals = iter(data.split(','))
        def build():
            v = next(vals)
            if v == 'N': return None
            node = TreeNode(int(v))
            node.left = build(); node.right = build()
            return node
        return build()''',

    "subtree-of-another-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSame(self, s, t):
        if not s and not t: return True
        if not s or not t or s.val != t.val: return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)''',

    "construct-binary-tree-from-preorder-and-inorder-traversal": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root''',

    "validate-binary-search-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            if not node: return True
            if not (lo < node.val < hi): return False
            return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)
        return validate(root, float('-inf'), float('inf'))''',

    "kth-smallest-element-in-a-bst": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root: stack.append(root); root = root.left
            root = stack.pop(); k -= 1
            if k == 0: return root.val
            root = root.right''',

    "lowest-common-ancestor-of-a-binary-search-tree": '''class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val: root = root.left
            elif p.val > root.val and q.val > root.val: root = root.right
            else: return root''',

    "implement-trie-prefix-tree": '''class Trie:
    def __init__(self): self.root = {}
    def insert(self, word: str) -> None:
        node = self.root
        for c in word: node = node.setdefault(c, {})
        node['#'] = True
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True''',

    "diameter-of-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(node):
            if not node: return 0
            l, r = depth(node.left), depth(node.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        depth(root)
        return self.res''',

    "balanced-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            l, r = height(node.left), height(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1: return -1
            return 1 + max(l, r)
        return height(root) != -1''',

    "path-sum": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)''',

    # ─── Dynamic Programming ───────────────────────────────────────
    "climbing-stairs": '''class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a, b = 1, 2
        for _ in range(3, n + 1): a, b = b, a + b
        return b''',

    "coin-change": '''class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i: dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1''',

    "longest-increasing-subsequence": '''class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = []
        for n in nums:
            lo, hi = 0, len(dp)
            while lo < hi:
                mid = (lo + hi) // 2
                if dp[mid] < n: lo = mid + 1
                else: hi = mid
            if lo == len(dp): dp.append(n)
            else: dp[lo] = n
        return len(dp)''',

    "longest-common-subsequence": '''class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]''',

    "house-robber": '''class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0
        for n in nums: prev, curr = curr, max(curr, prev + n)
        return curr''',

    "house-robber-ii": '''class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_linear(arr):
            prev = curr = 0
            for n in arr: prev, curr = curr, max(curr, prev + n)
            return curr
        return max(nums[0], rob_linear(nums[1:]), rob_linear(nums[:-1]))''',

    "unique-paths": '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n): dp[j] += dp[j-1]
        return dp[-1]''',

    "jump-game-ii": '''class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = cur_end = cur_far = 0
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                jumps += 1; cur_end = cur_far
        return jumps''',

    "word-break": '''class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True; break
        return dp[-1]''',

    "decode-ways": '''class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0': dp[i] += dp[i-1]
            two = int(s[i-2:i])
            if 10 <= two <= 26: dp[i] += dp[i-2]
        return dp[-1]''',

    "partition-equal-subset-sum": '''class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp = {s + n for s in dp} | dp
        return target in dp''',

    "minimum-path-sum": '''class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0: grid[i][j] += grid[i][j-1]
                elif j == 0: grid[i][j] += grid[i-1][j]
                else: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]''',

    "triangle": '''class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in reversed(triangle[:-1]):
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i+1])
        return dp[0]''',

    "edit-distance": '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[0]; dp[0] = i
            for j in range(1, n + 1):
                tmp = dp[j]
                if word1[i-1] == word2[j-1]: dp[j] = prev
                else: dp[j] = 1 + min(prev, dp[j], dp[j-1])
                prev = tmp
        return dp[n]''',

    "maximal-square": '''class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res * res''',

    # ─── Graphs ───────────────────────────────────────────────────
    "number-of-islands": '''class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        count = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1': return
            grid[i][j] = '0'
            dfs(i+1,j); dfs(i-1,j); dfs(i,j+1); dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j); count += 1
        return count''',

    "clone-graph": '''from typing import Optional
class Node:
    def __init__(self, val=0, neighbors=None): self.val=val; self.neighbors=neighbors or []
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node: return None
        visited = {}
        def dfs(n):
            if n in visited: return visited[n]
            clone = Node(n.val); visited[n] = clone
            for nb in n.neighbors: clone.neighbors.append(dfs(nb))
            return clone
        return dfs(node)''',

    "pacific-atlantic-water-flow": '''class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            from collections import deque
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                        visited.add((nr,nc)); queue.append((nr,nc))
            return visited
        pac = bfs([(r,0) for r in range(m)] + [(0,c) for c in range(n)])
        atl = bfs([(r,n-1) for r in range(m)] + [(m-1,c) for c in range(n)])
        return [[r,c] for r,c in pac & atl]''',

    "course-schedule": '''class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: graph[b].append(a)
        visited = [0] * numCourses
        def dfs(v):
            if visited[v] == 1: return False
            if visited[v] == 2: return True
            visited[v] = 1
            for nb in graph[v]:
                if not dfs(nb): return False
            visited[v] = 2
            return True
        return all(dfs(i) for i in range(numCourses))''',

    "course-schedule-ii": '''class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: graph[b].append(a)
        visited = [0] * numCourses; order = []
        def dfs(v):
            if visited[v] == 1: return False
            if visited[v] == 2: return True
            visited[v] = 1
            for nb in graph[v]:
                if not dfs(nb): return False
            visited[v] = 2; order.append(v)
            return True
        if not all(dfs(i) for i in range(numCourses)): return []
        return order[::-1]''',

    "number-of-connected-components-in-an-undirected-graph": '''class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(a, b):
            a, b = find(a), find(b)
            if a == b: return 0
            parent[a] = b; return 1
        return n - sum(union(a, b) for a, b in edges)''',

    "graph-valid-tree": '''class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = list(range(n))
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for a, b in edges:
            a, b = find(a), find(b)
            if a == b: return False
            parent[a] = b
        return True''',

    "word-search": '''class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word): return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[k]: return False
            tmp, board[i][j] = board[i][j], '#'
            found = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            board[i][j] = tmp
            return found
        return any(dfs(i,j,0) for i in range(m) for j in range(n))''',

    "alien-dictionary": '''class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2: return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2: adj[c1].add(c2); break
        visited = {}; result = []
        def dfs(c):
            if c in visited: return visited[c]
            visited[c] = True
            for nb in adj[c]:
                if dfs(nb): return True
            visited[c] = False; result.append(c)
            return False
        for c in adj:
            if dfs(c): return ""
        return "".join(reversed(result))''',

    # ─── Binary Search ─────────────────────────────────────────────
    "binary-search": '''class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: lo = mid + 1
            else: hi = mid - 1
        return -1''',

    "first-bad-version": '''class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid): hi = mid
            else: lo = mid + 1
        return lo''',

    "search-a-2d-matrix": '''class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target: return True
            elif val < target: lo = mid + 1
            else: hi = mid - 1
        return False''',

    "koko-eating-bananas": '''import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(p / mid) for p in piles) <= h: hi = mid
            else: lo = mid + 1
        return lo''',

    "median-of-two-sorted-arrays": '''class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            max_left1  = float('-inf') if i == 0 else nums1[i-1]
            min_right1 = float('inf')  if i == m else nums1[i]
            max_left2  = float('-inf') if j == 0 else nums2[j-1]
            min_right2 = float('inf')  if j == n else nums2[j]
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                return float(max(max_left1, max_left2))
            elif max_left1 > min_right2: hi = i - 1
            else: lo = i + 1''',

    # ─── Stack / Queue ─────────────────────────────────────────────
    "valid-parentheses": '''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mapping:
                if not stack or stack[-1] != mapping[c]: return False
                stack.pop()
            else: stack.append(c)
        return not stack''',

    "min-stack": '''class MinStack:
    def __init__(self): self.stack = []; self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    def pop(self) -> None: self.stack.pop(); self.min_stack.pop()
    def top(self) -> int: return self.stack[-1]
    def getMin(self) -> int: return self.min_stack[-1]''',

    "daily-temperatures": '''class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        res = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop(); res[j] = i - j
            stack.append(i)
        return res''',

    "car-fleet": '''class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)''',

    "largest-rectangle-in-histogram": '''class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []; res = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
            stack.append((start, h))
        return res''',

    "evaluate-reverse-polish-notation": '''class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t in '+-*/':
                b, a = stack.pop(), stack.pop()
                if t == '+': stack.append(a + b)
                elif t == '-': stack.append(a - b)
                elif t == '*': stack.append(a * b)
                else: stack.append(int(a / b))
            else: stack.append(int(t))
        return stack[0]''',

    # ─── Math ──────────────────────────────────────────────────────
    "palindrome-number": '''class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x); return s == s[::-1]''',

    "count-primes": '''class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        sieve = [True] * n; sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n, i): sieve[j] = False
        return sum(sieve)''',

    "happy-number": '''class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(d)**2 for d in str(n))
            if n in seen: return False
            seen.add(n)
        return True''',

    "power-of-two": '''class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0''',

    "number-of-1-bits": '''class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")''',

    "reverse-bits": '''class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1); n >>= 1
        return res''',

    "missing-number": '''class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)''',

    "reverse-integer": '''class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if -(2**31) <= rev <= 2**31 - 1 else 0''',

    "excel-sheet-column-number": '''class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle: res = res * 26 + (ord(c) - ord('A') + 1)
        return res''',

    "sqrt": '''class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == x: return mid
            elif mid * mid < x: lo = mid + 1
            else: hi = mid - 1
        return hi''',

    # ─── Heap / Priority Queue ─────────────────────────────────────
    "top-k-frequent-elements": '''class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        return [x for x, _ in Counter(nums).most_common(k)]''',

    "find-median-from-data-stream": '''import heapq
class MedianFinder:
    def __init__(self): self.small = []; self.large = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2''',

    "kth-largest-element-in-an-array": '''class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        return heapq.nlargest(k, nums)[-1]''',

    "task-scheduler": '''class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        from collections import Counter
        counts = sorted(Counter(tasks).values(), reverse=True)
        max_count = counts[0]
        max_count_tasks = counts.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)''',

    # ─── Backtracking ──────────────────────────────────────────────
    "combination-sum": '''class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def bt(start, path, remaining):
            if remaining == 0: res.append(path[:]); return
            for i in range(start, len(candidates)):
                if candidates[i] <= remaining:
                    path.append(candidates[i])
                    bt(i, path, remaining - candidates[i])
                    path.pop()
        bt(0, [], target)
        return res''',

    "subsets": '''class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def bt(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i]); bt(i+1, path); path.pop()
        bt(0, [])
        return res''',

    "permutations": '''class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def bt(path, remaining):
            if not remaining: res.append(path[:]); return
            for i in range(len(remaining)):
                path.append(remaining[i])
                bt(path, remaining[:i] + remaining[i+1:])
                path.pop()
        bt([], nums)
        return res''',

    "letter-combinations-of-a-phone-number": '''class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def bt(i, path):
            if i == len(digits): res.append("".join(path)); return
            for c in phone[digits[i]]: path.append(c); bt(i+1, path); path.pop()
        bt(0, [])
        return res''',

    "palindrome-partitioning": '''class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        def bt(start, path):
            if start == len(s): res.append(path[:]); return
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    path.append(sub); bt(end, path); path.pop()
        bt(0, [])
        return res''',

    "n-queens": '''class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []; cols = set(); diag1 = set(); diag2 = set()
        board = [['.']*n for _ in range(n)]
        def bt(row):
            if row == n:
                res.append(["".join(r) for r in board]); return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2: continue
                cols.add(col); diag1.add(row-col); diag2.add(row+col)
                board[row][col] = 'Q'
                bt(row+1)
                cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)
                board[row][col] = '.'
        bt(0)
        return res''',

    # ─── Two Pointers ──────────────────────────────────────────────
    "two-sum-ii-input-array-is-sorted": '''class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target: return [lo+1, hi+1]
            elif s < target: lo += 1
            else: hi -= 1
        return []''',

    "trapping-rain-water": '''class Solution:
    def trap(self, height: list[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_lo = max_hi = water = 0
        while lo < hi:
            if height[lo] < height[hi]:
                if height[lo] >= max_lo: max_lo = height[lo]
                else: water += max_lo - height[lo]
                lo += 1
            else:
                if height[hi] >= max_hi: max_hi = height[hi]
                else: water += max_hi - height[hi]
                hi -= 1
        return water''',

    "remove-duplicates-from-sorted-array": '''class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]; k += 1
        return k''',

    "squares-of-a-sorted-array": '''class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lo, hi = 0, len(nums) - 1
        res = []
        while lo <= hi:
            if abs(nums[lo]) > abs(nums[hi]):
                res.append(nums[lo]**2); lo += 1
            else:
                res.append(nums[hi]**2); hi -= 1
        return res[::-1]''',

    # ─── Intervals ─────────────────────────────────────────────────
    "insert-interval": '''class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > end:
                res.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        res.append(newInterval)
        return res''',

    "non-overlapping-intervals": '''class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0; prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end: prev_end = end
            else: removed += 1
        return removed''',

    "meeting-rooms": '''class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]: return False
        return True''',

    # ─── Misc ──────────────────────────────────────────────────────
    "lru-cache": '''class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cap = capacity; self.cache = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)''',

    "number-of-1-bits": '''class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")''',

    "counting-bits": '''class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1): dp[i] = dp[i >> 1] + (i & 1)
        return dp''',

    "sum-of-two-integers": '''class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b; b = carry
        return a if b == 0 else a & mask''',

    "climbing-stairs": '''class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a, b = 1, 2
        for _ in range(3, n + 1): a, b = b, a + b
        return b''',
}
