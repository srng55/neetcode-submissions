class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize !=0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card,0) + 1

        for card in sorted(count):

            while count[card] > 0:

                for i in range(card, card + groupSize):

                    if count.get(i,0) == 0:
                        return False

                    count[i] -=1

        return True