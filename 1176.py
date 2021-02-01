class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        pointer_s = 0
        pointer_e = 0
        T = 0
        score = 0

        def check(T, score) -> int:
            if T < lower:
                score -= 1
            elif T > upper:
                score += 1
            return score

        if k == 1:
            for T in calories:
                score = check(T, score)
        else:
            while pointer_e < k:
                T += calories[pointer_e]
                pointer_e += 1

            score = check(T, score)

            while pointer_e < len(calories):
                T += calories[pointer_e]
                T -= calories[pointer_s]
                score = check(T, score)
                pointer_e += 1
                pointer_s += 1

        return score
