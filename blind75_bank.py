"""
Blind 75 + NeetCode 150 — extended solution bank.
Problems not already covered in solution_bank.py.
"""

BLIND75_SOLUTIONS = {
    # ─── Arrays ───────────────────────────────────────────────────
    "two-sum-ii-input-array-is-sorted": '''class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target: return [lo+1, hi+1]
            elif s < target: lo += 1
            else: hi -= 1
        return []''',

    "4sum": '''class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort(); res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                lo, hi = j+1, len(nums)-1
                while lo < hi:
                    s = nums[i]+nums[j]+nums[lo]+nums[hi]
                    if s == target:
                        res.append([nums[i],nums[j],nums[lo],nums[hi]])
                        while lo < hi and nums[lo]==nums[lo+1]: lo+=1
                        while lo < hi and nums[hi]==nums[hi-1]: hi-=1
                        lo+=1; hi-=1
                    elif s < target: lo+=1
                    else: hi-=1
        return res''',

    "maximum-points-you-can-obtain-from-cards": '''class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        total = sum(cardPoints[:k])
        res = total
        for i in range(k):
            total += cardPoints[-(i+1)] - cardPoints[k-1-i]
            res = max(res, total)
        return res''',

    "minimum-size-subarray-sum": '''class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        lo = total = 0
        res = float('inf')
        for hi in range(len(nums)):
            total += nums[hi]
            while total >= target:
                res = min(res, hi - lo + 1)
                total -= nums[lo]; lo += 1
        return 0 if res == float('inf') else res''',

    "number-of-subarrays-with-bounded-maximum": '''class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count(bound):
            res = cur = 0
            for n in nums:
                cur = cur + 1 if n <= bound else 0
                res += cur
            return res
        return count(right) - count(left - 1)''',

    "sliding-window-maximum": '''from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque(); res = []
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] < n: dq.pop()
            dq.append(i)
            if dq[0] < i - k + 1: dq.popleft()
            if i >= k - 1: res.append(nums[dq[0]])
        return res''',

    "frequency-of-the-most-frequent-element": '''class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort(); lo = res = 0; total = 0
        for hi in range(len(nums)):
            total += nums[hi]
            while nums[hi] * (hi - lo + 1) - total > k:
                total -= nums[lo]; lo += 1
            res = max(res, hi - lo + 1)
        return res''',

    "permutation-in-string": '''class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len(s2): return False
        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == need: return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            if window == need: return True
        return False''',

    "fruit-into-baskets": '''class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        from collections import defaultdict
        basket = defaultdict(int); lo = res = 0
        for hi, f in enumerate(fruits):
            basket[f] += 1
            while len(basket) > 2:
                basket[fruits[lo]] -= 1
                if basket[fruits[lo]] == 0: del basket[fruits[lo]]
                lo += 1
            res = max(res, hi - lo + 1)
        return res''',

    # ─── Strings ──────────────────────────────────────────────────
    "find-all-anagrams-in-a-string": '''class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import Counter
        need = Counter(p); window = Counter(s[:len(p)]); res = []
        if window == need: res.append(0)
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            window[s[i-len(p)]] -= 1
            if window[s[i-len(p)]] == 0: del window[s[i-len(p)]]
            if window == need: res.append(i - len(p) + 1)
        return res''',

    "longest-palindrome": '''class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s); odd = sum(v % 2 for v in c.values())
        return len(s) - odd + (1 if odd else 0)''',

    "count-and-say": '''class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            nxt = ""; i = 0
            while i < len(s):
                c = s[i]; cnt = 0
                while i < len(s) and s[i] == c: cnt += 1; i += 1
                nxt += str(cnt) + c
            s = nxt
        return s''',

    "add-binary": '''class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""; carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            s = x + y + carry
            res = str(s % 2) + res; carry = s // 2
            i -= 1; j -= 1
        return res''',

    "multiply-strings": '''class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i])-48) * (ord(num2[j])-48)
                p1, p2 = i+j, i+j+1
                total = mul + pos[p2]
                pos[p2] = total % 10; pos[p1] += total // 10
        res = "".join(str(d) for d in pos).lstrip('0')
        return res or "0"''',

    "zigzag-conversion": '''class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = [""] * numRows; row = 0; down = True
        for c in s:
            rows[row] += c
            if row == 0: down = True
            elif row == numRows - 1: down = False
            row += 1 if down else -1
        return "".join(rows)''',

    "reverse-words-in-a-string": '''class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))''',

    "implement-strstr": '''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1''',

    "text-justification": '''class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []; i = 0
        while i < len(words):
            line_len = len(words[i]); j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j]); j += 1
            line_words = words[i:j]; gaps = j - i - 1
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                space, extra = divmod(total_spaces, gaps)
                line = ""
                for k, w in enumerate(line_words[:-1]):
                    line += w + " " * (space + (1 if k < extra else 0))
                line += line_words[-1]
            res.append(line); i = j
        return res''',

    # ─── Linked Lists ──────────────────────────────────────────────
    "reverse-linked-list-ii": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head); prev = dummy
        for _ in range(left - 1): prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next; cur.next = nxt.next
            nxt.next = prev.next; prev.next = nxt
        return dummy.next''',

    "swap-nodes-in-pairs": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head); prev = dummy
        while prev.next and prev.next.next:
            a, b = prev.next, prev.next.next
            prev.next = b; a.next = b.next; b.next = a
            prev = a
        return dummy.next''',

    "rotate-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        length = 1; tail = head
        while tail.next: tail = tail.next; length += 1
        k %= length
        if k == 0: return head
        tail.next = head; cur = head
        for _ in range(length - k - 1): cur = cur.next
        new_head = cur.next; cur.next = None
        return new_head''',

    "sort-list": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        mid = slow.next; slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        dummy = cur = ListNode()
        while left and right:
            if left.val <= right.val: cur.next=left; left=left.next
            else: cur.next=right; right=right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next''',

    "merge-k-sorted-lists": '''from typing import Optional, List
import heapq
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node: heapq.heappush(heap, (node.val, i, node))
        dummy = cur = ListNode()
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node; cur = cur.next
            if node.next: heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next''',

    "reverse-nodes-in-k-group": '''from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None): self.val=val; self.next=next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head); prev_group = dummy
        while True:
            kth = self.get_kth(prev_group, k)
            if not kth: break
            group_next = kth.next
            prev, cur = kth.next, prev_group.next
            while cur != group_next:
                nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
            tmp = prev_group.next
            prev_group.next = kth; tmp.next = group_next
            prev_group = tmp
        return dummy.next
    def get_kth(self, cur, k):
        while cur and k > 0: cur = cur.next; k -= 1
        return cur''',

    # ─── Trees ────────────────────────────────────────────────────
    "binary-tree-right-side-view": '''from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []; queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(node.val)
        return res''',

    "count-good-nodes-in-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val):
            if not node: return 0
            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return res + dfs(node.left, max_val) + dfs(node.right, max_val)
        return dfs(root, root.val)''',

    "binary-tree-zigzag-level-order-traversal": '''from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []; queue = deque([root]); left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return res''',

    "path-sum-ii": '''from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path, remaining):
            if not node: return
            path.append(node.val)
            if not node.left and not node.right and remaining == node.val:
                res.append(path[:])
            else:
                dfs(node.left, path, remaining - node.val)
                dfs(node.right, path, remaining - node.val)
            path.pop()
        dfs(root, [], targetSum)
        return res''',

    "flatten-binary-tree-to-linked-list": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node: return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if node.left:
                left_tail.next = node.right
                node.right = node.left; node.left = None
            return right_tail or left_tail or node
        dfs(root)''',

    "populating-next-right-pointers-in-each-node": '''from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val=val; self.left=left; self.right=right; self.next=next
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return None
        if root.left:
            root.left.next = root.right
            if root.next: root.right.next = root.next.left
        self.connect(root.left); self.connect(root.right)
        return root''',

    "sum-root-to-leaf-numbers": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node: return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right: return curr
            return dfs(node.left, curr) + dfs(node.right, curr)
        return dfs(root, 0)''',

    "binary-search-tree-iterator": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    def _push_left(self, node):
        while node: self.stack.append(node); node = node.left
    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val
    def hasNext(self) -> bool:
        return bool(self.stack)''',

    "lowest-common-ancestor-of-a-binary-tree": '''from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right''',

    "binary-tree-preorder-traversal": '''from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []; stack = [root] if root else []
        while stack:
            node = stack.pop(); res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res''',

    "binary-tree-inorder-traversal": '''from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []; stack = []; cur = root
        while cur or stack:
            while cur: stack.append(cur); cur = cur.left
            cur = stack.pop(); res.append(cur.val); cur = cur.right
        return res''',

    "binary-tree-postorder-traversal": '''from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val=val; self.left=left; self.right=right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []; stack = [root] if root else []
        while stack:
            node = stack.pop(); res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]''',

    # ─── Graphs ───────────────────────────────────────────────────
    "surrounded-regions": '''class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O': return
            board[r][c]='S'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(m):
            dfs(r,0); dfs(r,n-1)
        for c in range(n):
            dfs(0,c); dfs(m-1,c)
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O': board[r][c]='X'
                elif board[r][c]=='S': board[r][c]='O' ''',

    "rotting-oranges": '''from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        queue=deque(); fresh=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2: queue.append((r,c,0))
                elif grid[r][c]==1: fresh+=1
        mins=0
        while queue:
            r,c,t=queue.popleft(); mins=max(mins,t)
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    grid[nr][nc]=2; fresh-=1; queue.append((nr,nc,t+1))
        return mins if fresh==0 else -1''',

    "walls-and-gates": '''from collections import deque
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        INF=2147483647; m,n=len(rooms),len(rooms[0])
        queue=deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c]==0: queue.append((r,c))
        while queue:
            r,c=queue.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and rooms[nr][nc]==INF:
                    rooms[nr][nc]=rooms[r][c]+1; queue.append((nr,nc))''',

    "network-delay-time": '''import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}
        for u,v,w in times: graph[u].append((v,w))
        dist={i:float('inf') for i in range(1,n+1)}; dist[k]=0
        heap=[(0,k)]
        while heap:
            d,u=heapq.heappop(heap)
            if d>dist[u]: continue
            for v,w in graph[u]:
                if dist[u]+w < dist[v]:
                    dist[v]=dist[u]+w; heapq.heappush(heap,(dist[v],v))
        res=max(dist.values())
        return res if res<float('inf') else -1''',

    "cheapest-flights-within-k-stops": '''class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*n; prices[src]=0
        for _ in range(k+1):
            tmp=prices[:]
            for u,v,w in flights:
                if prices[u]+w < tmp[v]: tmp[v]=prices[u]+w
            prices=tmp
        return prices[dst] if prices[dst]<float('inf') else -1''',

    "swim-in-rising-water": '''import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n=len(grid); visited=set(); heap=[(grid[0][0],0,0)]
        while heap:
            t,r,c=heapq.heappop(heap)
            if (r,c) in visited: continue
            visited.add((r,c))
            if r==n-1 and c==n-1: return t
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))''',

    "redundant-connection": '''class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent=list(range(len(edges)+1))
        def find(x):
            while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
            return x
        def union(a,b):
            a,b=find(a),find(b)
            if a==b: return False
            parent[a]=b; return True
        for a,b in edges:
            if not union(a,b): return [a,b]''',

    "min-cost-to-connect-all-points": '''import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points); visited=set(); heap=[(0,0)]; total=0
        while len(visited)<n:
            cost,i=heapq.heappop(heap)
            if i in visited: continue
            visited.add(i); total+=cost
            for j in range(n):
                if j not in visited:
                    dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    heapq.heappush(heap,(dist,j))
        return total''',

    "accounts-merge": '''class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        from collections import defaultdict
        parent={}
        def find(x):
            if x not in parent: parent[x]=x
            if parent[x]!=x: parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            parent[find(a)]=find(b)
        email_to_name={}
        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                email_to_name[email]=name
                union(acc[1],email)
        groups=defaultdict(list)
        for email in email_to_name:
            groups[find(email)].append(email)
        return [[email_to_name[root]]+sorted(emails) for root,emails in groups.items()]''',

    "number-of-islands-ii": '''class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        parent={}; count=[0]; res=[]
        def find(x):
            if parent[x]!=x: parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            a,b=find(a),find(b)
            if a!=b: parent[a]=b; count[0]-=1
        for r,c in positions:
            if (r,c) in parent: res.append(count[0]); continue
            parent[(r,c)]=(r,c); count[0]+=1
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if (nr,nc) in parent: union((r,c),(nr,nc))
            res.append(count[0])
        return res''',

    # ─── Dynamic Programming ───────────────────────────────────────
    "best-time-to-buy-and-sell-stock-with-cooldown": '''class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold=float('-inf'); sold=rest=0
        for p in prices:
            prev_sold=sold
            sold=hold+p; hold=max(hold,rest-p); rest=max(rest,prev_sold)
        return max(sold,rest)''',

    "best-time-to-buy-and-sell-stock-with-transaction-fee": '''class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold,cash=float('-inf'),0
        for p in prices:
            hold=max(hold,cash-p); cash=max(cash,hold+p-fee)
        return cash''',

    "best-time-to-buy-and-sell-stock-iii": '''class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1=buy2=float('-inf'); sell1=sell2=0
        for p in prices:
            buy1=max(buy1,-p); sell1=max(sell1,buy1+p)
            buy2=max(buy2,sell1-p); sell2=max(sell2,buy2+p)
        return sell2''',

    "best-time-to-buy-and-sell-stock-iv": '''class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices: return 0
        n=len(prices)
        if k>=n//2:
            return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
        dp=[[0]*n for _ in range(k+1)]
        for i in range(1,k+1):
            max_so_far=float('-inf')
            for j in range(1,n):
                max_so_far=max(max_so_far,dp[i-1][j-1]-prices[j-1])
                dp[i][j]=max(dp[i][j-1],prices[j]+max_so_far)
        return dp[k][-1]''',

    "burst-balloons": '''class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums=[1]+nums+[1]; n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for length in range(2,n):
            for lo in range(0,n-length):
                hi=lo+length
                for k in range(lo+1,hi):
                    dp[lo][hi]=max(dp[lo][hi],nums[lo]*nums[k]*nums[hi]+dp[lo][k]+dp[k][hi])
        return dp[0][n-1]''',

    "regular-expression-matching": '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]=='*': dp[0][j]=dp[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] in {s[i-1],'.'}: dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-2]
                    if p[j-2] in {s[i-1],'.'}: dp[i][j]=dp[i][j] or dp[i-1][j]
        return dp[m][n]''',

    "wildcard-matching": '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for j in range(1,n+1):
            if p[j-1]=='*': dp[0][j]=dp[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*': dp[i][j]=dp[i-1][j] or dp[i][j-1]
                elif p[j-1]=='?' or p[j-1]==s[i-1]: dp[i][j]=dp[i-1][j-1]
        return dp[m][n]''',

    "interleaving-string": '''class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n=len(s1),len(s2)
        if m+n!=len(s3): return False
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        for i in range(1,m+1): dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,n+1): dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or \
                          (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[m][n]''',

    "distinct-subsequences": '''class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1): dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]: dp[i][j]+=dp[i-1][j-1]
        return dp[m][n]''',

    "range-sum-query-immutable": '''class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix=[0]*(len(nums)+1)
        for i,n in enumerate(nums): self.prefix[i+1]=self.prefix[i]+n
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]''',

    "counting-bits": '''class Solution:
    def countBits(self, n: int) -> list[int]:
        dp=[0]*(n+1)
        for i in range(1,n+1): dp[i]=dp[i>>1]+(i&1)
        return dp''',

    # ─── Heap / Priority Queue ─────────────────────────────────────
    "k-closest-points-to-origin": '''import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2+p[1]**2)''',

    "hand-of-straights": '''class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        from collections import Counter
        if len(hand)%groupSize: return False
        count=Counter(hand)
        for card in sorted(count):
            if count[card]>0:
                n=count[card]
                for i in range(card,card+groupSize):
                    if count[i]<n: return False
                    count[i]-=n
        return True''',

    "merge-triplets-to-form-target-triplet": '''class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        res=[0,0,0]
        for t in triplets:
            if t[0]<=target[0] and t[1]<=target[1] and t[2]<=target[2]:
                res=[max(res[i],t[i]) for i in range(3)]
        return res==target''',

    "partition-labels": '''class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={c:i for i,c in enumerate(s)}
        res=[]; start=end=0
        for i,c in enumerate(s):
            end=max(end,last[c])
            if i==end:
                res.append(end-start+1); start=i+1
        return res''',

    "jump-game-iii": '''class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        from collections import deque
        n=len(arr); visited=set(); queue=deque([start])
        while queue:
            i=queue.popleft()
            if arr[i]==0: return True
            if i in visited: continue
            visited.add(i)
            for ni in [i+arr[i],i-arr[i]]:
                if 0<=ni<n and ni not in visited: queue.append(ni)
        return False''',

    # ─── Math / Bit Manipulation ────────────────────────────────────
    "single-number-ii": '''class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones=twos=0
        for n in nums:
            ones=(ones^n)&~twos; twos=(twos^n)&~ones
        return ones''',

    "single-number-iii": '''class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor=0
        for n in nums: xor^=n
        bit=xor&(-xor); a=b=0
        for n in nums:
            if n&bit: a^=n
            else: b^=n
        return [a,b]''',

    "bitwise-and-of-numbers-range": '''class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift=0
        while left!=right: left>>=1; right>>=1; shift+=1
        return left<<shift''',

    "rotate-image": '''class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix: row.reverse()''',

    "game-of-life": '''class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m,n=len(board),len(board[0])
        def count_live(r,c):
            cnt=0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr==0 and dc==0: continue
                    nr,nc=r+dr,c+dc
                    if 0<=nr<m and 0<=nc<n and abs(board[nr][nc])==1: cnt+=1
            return cnt
        for r in range(m):
            for c in range(n):
                live=count_live(r,c)
                if board[r][c]==1 and live not in [2,3]: board[r][c]=-1
                elif board[r][c]==0 and live==3: board[r][c]=2
        for r in range(m):
            for c in range(n):
                if board[r][c]==-1: board[r][c]=0
                elif board[r][c]==2: board[r][c]=1''',

    "happy-number": '''class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            n=sum(int(d)**2 for d in str(n))
            if n in seen: return False
            seen.add(n)
        return True''',

    "factorial-trailing-zeroes": '''class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>=5: n//=5; count+=n
        return count''',

    "excel-sheet-column-title": '''class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber:
            columnNumber-=1; res=chr(columnNumber%26+ord('A'))+res; columnNumber//=26
        return res''',

    "majority-element-ii": '''class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        c1=c2=0; n1=n2=None
        for n in nums:
            if n==n1: c1+=1
            elif n==n2: c2+=1
            elif c1==0: n1=n; c1=1
            elif c2==0: n2=n; c2=1
            else: c1-=1; c2-=1
        return [n for n in [n1,n2] if nums.count(n)>len(nums)//3]''',

    # ─── Advanced Data Structures ──────────────────────────────────
    "design-add-and-search-words-data-structure": '''class WordDictionary:
    def __init__(self): self.root={}
    def addWord(self, word: str) -> None:
        node=self.root
        for c in word: node=node.setdefault(c,{})
        node['#']=True
    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word): return '#' in node
            c=word[i]
            if c=='.':
                return any(dfs(node[ch],i+1) for ch in node if ch!='#')
            if c not in node: return False
            return dfs(node[c],i+1)
        return dfs(self.root,0)''',

    "word-search-ii": '''class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root={}
        for w in words:
            node=root
            for c in w: node=node.setdefault(c,{})
            node['#']=w
        m,n=len(board),len(board[0]); res=[]
        def dfs(r,c,node):
            if r<0 or r>=m or c<0 or c>=n: return
            ch=board[r][c]
            if ch not in node: return
            nxt=node[ch]
            if '#' in nxt: res.append(nxt.pop('#'))
            board[r][c]='#'
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]: dfs(r+dr,c+dc,nxt)
            board[r][c]=ch
        for r in range(m):
            for c in range(n): dfs(r,c,root)
        return res''',

    "all-oone-data-structure": '''class AllOne:
    def __init__(self):
        self.count={}
        self.max_count=self.min_count=0
    def inc(self,key:str)->None:
        self.count[key]=self.count.get(key,0)+1
        c=self.count[key]
        self.max_count=max(self.max_count,c)
        if self.min_count==0: self.min_count=1
    def dec(self,key:str)->None:
        if key not in self.count: return
        self.count[key]-=1
        if self.count[key]==0: del self.count[key]
        self.max_count=max(self.count.values()) if self.count else 0
        self.min_count=min(self.count.values()) if self.count else 0
    def getMaxKey(self)->str:
        return max(self.count,key=self.count.get) if self.count else ""
    def getMinKey(self)->str:
        return min(self.count,key=self.count.get) if self.count else ""''',

    "time-based-key-value-store": '''class TimeMap:
    def __init__(self): self.store={}
    def set(self,key:str,value:str,timestamp:int)->None:
        if key not in self.store: self.store[key]=[]
        self.store[key].append((timestamp,value))
    def get(self,key:str,timestamp:int)->str:
        if key not in self.store: return ""
        vals=self.store[key]; lo,hi=0,len(vals)-1; res=""
        while lo<=hi:
            mid=(lo+hi)//2
            if vals[mid][0]<=timestamp: res=vals[mid][1]; lo=mid+1
            else: hi=mid-1
        return res''',

    "insert-delete-getrandom-o1": '''import random
class RandomizedSet:
    def __init__(self): self.vals=[]; self.idx={}
    def insert(self,val:int)->bool:
        if val in self.idx: return False
        self.idx[val]=len(self.vals); self.vals.append(val); return True
    def remove(self,val:int)->bool:
        if val not in self.idx: return False
        last=self.vals[-1]; i=self.idx[val]
        self.vals[i]=last; self.idx[last]=i
        self.vals.pop(); del self.idx[val]; return True
    def getRandom(self)->int:
        return random.choice(self.vals)''',

    # ─── Greedy ───────────────────────────────────────────────────
    "gas-station": '''class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost): return -1
        tank=start=0
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0: tank=0; start=i+1
        return start''',

    "candy": '''class Solution:
    def candy(self, ratings: list[int]) -> int:
        n=len(ratings); candy=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]: candy[i]=candy[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]: candy[i]=max(candy[i],candy[i+1]+1)
        return sum(candy)''',
}
