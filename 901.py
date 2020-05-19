# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.h = []

    def next(self, price: int) -> int:
        count = 1

        if len(self.h) == 0:
            self.h.append((price, 1))
            return 1
        else:

            last_price, last_span = self.h[-1]

            if last_price <= price:
                next_price = last_price
                next_span = last_span

                while next_price <= price:
                    count += next_span
                    if count <= len(self.h):
                        next_price, next_span = self.h[-1 * count]
                    else:
                        break

                self.h.append((price, count))

                return count
            else:
                self.h.append((price, 1))
                return 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
