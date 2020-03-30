# https://leetcode.com/problems/meeting-rooms-ii/
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return len(intervals)

        events = []
        result = 1
        cur_result = 0
        for interval in intervals:
            si, ei = interval
            events.append((ei, 'end'))
            events.append((si, 'start'))
        events.sort(key=lambda item: item[0])

        for i, event in enumerate(events):
            event_time, event_type = event
            if event_type == 'start' and (events[i + 1][0] != event_time or events[i + 1][1] != 'end'):
                cur_result += 1
                result = max(result, cur_result)
            elif event_type == 'end' and (events[i - 1][0] != event_time or events[i - 1][1] != 'start'):
                cur_result -= 1

        return result
