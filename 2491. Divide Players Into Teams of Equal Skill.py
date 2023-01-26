class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        prev_cnt = skill[left] + skill[right]
        ans = 0

        while right < len(skill) and left < right:
            cnt = skill[left] + skill[right]
            
            if cnt != prev_cnt:
                return -1
            else:
                ans += skill[left] * skill[right]
            
            prev_cnt = cnt
            left += 1
            right -= 1

        return ans
