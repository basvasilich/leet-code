# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_d = 30  # 360/12
        m_d = 6  # 360/60
        min_ratio = minutes / 60

        h_angle = hour * h_d + h_d * min_ratio
        m_angle = minutes * m_d

        angle = abs(h_angle - m_angle)

        return angle if angle <= 180 else 360 - angle