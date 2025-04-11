class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            max_words = max(max_words, word_count)
        return max_words
sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
sol =Solution()
print(sol.mostWordsFound(sentences))