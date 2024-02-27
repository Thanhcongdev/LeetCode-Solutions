class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        word_len = len(words[0])
        words_len = len(words)
        words_map = Counter(words)
        res = []
        for i in range(word_len):
            left = i
            right = i
            cur_map = defaultdict(int)
            count = 0
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in words_map:
                    cur_map[word] += 1
                    count += 1
                    while cur_map[word] > words_map[word]:
                        cur_map[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    if count == words_len:
                        res.append(left)
                else:
                    cur_map.clear()
                    count = 0
                    left = right
        return res