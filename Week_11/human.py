class Head:
    pass


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Hand:
    def __init__(self):
        pass


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Feet:
    def __init__(self):
        pass


class Human:
    def __init__(self, torso):
        self.torso = torso

left_hand = Hand()
right_hand = Hand()
left_foot = Feet()
right_foot = Feet()
left_arm = Arm(left_hand)
right_arm = Arm(right_hand)
left_leg = Leg(left_foot)
right_leg = Leg(right_foot)
head = Head()


torso = Torso(head, left_arm, right_arm, left_leg, right_leg)

human = Human(torso)