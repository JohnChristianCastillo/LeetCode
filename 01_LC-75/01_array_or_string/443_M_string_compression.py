class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        use two pointers
        l: stays at start of current letter
        r: traverses list until we find a new letter
        make sure arr[l] = letter we're currently looking at
        write count to l + 1 and above (if more than 1)

        notice we never assign l = r since r can be further down
        in a list where there are a lot of duplicates
        """

        l, r = 0, 0
        while r < len(chars):
            # very important to already set count to 1 since we only look back
            # this is to avoid dependency from l
            count = 1
            r += 1
            while r < len(chars) and chars[r-1] == chars[r]:
                count += 1
                r += 1
            # assign chars[l] to letter we're looking at, since l can be 
            # still at the beginning of the list
            chars[l] = chars[r-1]
            
            l += 1  # now we add the count character per character
            if count > 1:
                count = str(count)
                for c in count:
                    chars[l] = c
                    l += 1
        return l

