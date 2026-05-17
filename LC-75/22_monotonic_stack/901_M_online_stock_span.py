class StockSpanner:
    """
    idea: have a stack s.t. an element is: (price, span)
    curr_span = 1
    while curr_price is higher than stk.top:
        curr_price.span = top.price.span + 1 
    
    notice that if we have a higher price, we remove all 
    smaller elements and we take over those elements' spans

    if we get another higher price we do the same
    if we get a smaller price then we know we can't pop the stack
    as there's a "wall" and thus that span is just + 1
    """

    def __init__(self):
        self.stk = []
        

    def next(self, price: int) -> int:
        curr_span = 1
        while self.stk and self.stk[-1][0] <= price:
            top_price, top_span = self.stk.pop()
            curr_span += top_span
        # then add to current stk our new element
        self.stk.append((price, curr_span))
        return curr_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)