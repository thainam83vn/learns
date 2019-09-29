class Solution:

    def intToRoman(self, num: int) -> str:
        symbols = [
            {"roman": "M", "dec": 1000, "min": 900, "pre": "C"},
            {"roman": "D", "dec": 500, "min": 400, "pre": "C"},
            {"roman": "C", "dec": 100, "min": 90, "pre": "X"},
            {"roman": "L", "dec": 50, "min": 40, "pre": "X"},
            {"roman": "X", "dec": 10, "min": 9, "pre": "I"},
            {"roman": "V", "dec": 5, "min": 4, "pre": "I"},
            {"roman": "I", "dec": 1, "min": 0, "pre": ""},
        ]
        if num == 0:
            return ''
        if num <= 3:
            return self.intToRoman(num - 1) + 'I'

        for x in symbols:
            if num == x["dec"]:
                return x["roman"]
            elif num > x["dec"]:
                return x["roman"] + self.intToRoman(num - x["dec"])
            elif num >= x["min"]:
                return x["pre"] + x["roman"] + self.intToRoman(num - x["min"])


sol = Solution()
print(sol.intToRoman(4))
print(sol.intToRoman(11))
print(sol.intToRoman(21))
print(sol.intToRoman(199))
print(sol.intToRoman(1994))