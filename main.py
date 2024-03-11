import random


def new_card_deck(joker=False):
    """
    Creates a new deck of cards from the typical 52-card deck
    :param joker: Boolean value - if 'True', two Joker cards are added to the deck
    :return: A list of cards in a shuffled order
    """
    deck = []
    if joker:
        deck.append("Joker")
        deck.append("Joker")
    for value in range(1, 14):
        if value == 1:
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                deck.append(f"Ace of {suit}")
        elif value == 11:
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                deck.append(f"Jack of {suit}")
        elif value == 12:
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                deck.append(f"Queen of {suit}")
        elif value == 13:
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                deck.append(f"King of {suit}")
        else:
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                deck.append(f"{value} of {suit}")
    random.shuffle(deck)
    return deck


def new_tarot_deck(major=True, minor=True):
    """
    Creates a list of cards from a common tarot deck
    :param major: If 'True', the major arcana cards are included in the deck
    :param minor: If 'True', the minor arcana cards are included in the deck
    :return: A list of tarot cards, shuffled
    """
    deck = []
    major_arcana_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
                          "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel Of Fortune",
                          "Justice", "The Hanged Man", "Death", "Temperance", "Devil", "The Tower", "The Star",
                          "The Moon", "The Sun", "Judgment", "The World"]
    minor_arcana_cards = []
    for value in range(1, 15):
        if value == 1:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"Ace of {suit}")
        elif value == 11:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"Page of {suit}")
        elif value == 12:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"Knight of {suit}")
        elif value == 13:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"Queen of {suit}")
        elif value == 14:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"King of {suit}")
        else:
            for suit in ["Cups", "Pentacles", "Swords", "Wands"]:
                minor_arcana_cards.append(f"{value} of {suit}")
    if major:
        deck.extend(major_arcana_cards)
    if minor:
        deck.extend(minor_arcana_cards)
    random.shuffle(deck)
    return deck


def new_gun(bullets=1, chambers=6):
    """
    Loads a (virtual) revolver with an arbitrary number of bullets in an equally arbitrary number of chambers (Note:
    If there is an attempt to load more bullets than there are chambers, the script will use the default values of one
    'bullet' loaded into one of six 'chambers')
    :param bullets: Number of 'bullets' to load into the 'gun'
    :param chambers: Number of 'chambers' in the 'gun'
    :return: A list of Boolean values, where 'True' represents a bullet in the chamber and 'False' represents an empty
    chamber
    """
    cylinder = []
    if bullets > chambers:
        bullets = 1
        chambers = 6
    for _loop in range(bullets):
        cylinder.append(True)
    for _loop in range(chambers-bullets):
        cylinder.append(False)
    random.shuffle(cylinder)
    return cylinder


def roll(d=20, n=1):
    """
    Returns a number of random integers to replicate the rolling of dice
    :param d: Number of sides on the dice (default is 20)
    :param n: Number of dice to roll (default is 1)
    :return: A list of dice rolls, along with the sum, maximum and minimum roll
    """
    result = []
    for _loop in range(n):
        result.append(random.randint(1, d))
    return result, sum(result), max(result), min(result)


def draw(deck, n=1):
    """
    Simulates the random drawing and removal of a card from a deck
    :param deck: The list containing the deck of cards
    :param n: The number of cards to be drawn (default is 1)
    :return: A list of cards drawn
    """
    cards_drawn = []
    for _loop in range(n):
        card = random.choice(deck)
        cards_drawn.append(card)
        deck.remove(card)
    return cards_drawn


def pull_trigger(cylinder, n=1):
    """
    Simulates the game Russian Roulette
    :param cylinder: A list of Boolean values - 'True' represents the presence of a bullet in a chamber, while 'False'
    is an empty chamber
    :param n: The number of trigger pulls
    :return: A list containing the results of the trigger pulls
    """
    result = []
    for _loop in range(n):
        if len(cylinder) <= 0:
            result.append("* click * ")
        elif not cylinder[0]:
            result.append("* click *")
            cylinder.remove(cylinder[0])
        else:
            result.append("* BANG! *")
            cylinder.remove(cylinder[0])
    return result


def flip(n=1):
    """
    Simulates the flipping of a coin
    :param n: Number of coil flips
    :return: List of coin flip results, either 'Heads' or 'Tails'
    """
    result = []
    for _loop in range(n):
        result.append(random.choice(["Heads", "Tails"]))
    return result


def character_ability_roll():
    """
    Simulates the typical way of assigning ability scores in Dungeons & Dragons; four d6 die are rolled, with the three
    biggest values being summed to give the ability score
    :return: A list of six values based on the random rolls described
    """
    result = []
    for _loop in range(6):
        ability = roll(6, 4)[0]
        ability.remove(min(ability))
        result.append(sum(ability))
    return sorted(result, reverse=True)


def convert_ability_to_modifier(ability_score):
    """
    Converts an ability score to an ability modifier
    :param ability_score: The ability score (typically between 3 and 20)
    :return: The ability modifier in its raw form, as well as a formatted string with '+' where the score is positive
    """
    ability_modifier = int((ability_score - 10) / 2)
    if ability_modifier > 0:
        return ability_modifier, str(f"+{ability_modifier}")
    elif ability_modifier == 0:
        return ability_modifier, str(f" {ability_modifier}")
    else:
        return ability_modifier, str(f"{ability_modifier}")


def convert_all_to_cp(pp, gp, ep, sp, cp, split=1):
    """
    Converts all currency used in typical Dungeons & Dragons games into copper pieces, which is the lowest
    denomination - this allows for easier conversion back into larger denominations
    :param pp: Number of platinum pieces
    :param gp: Number of gold pieces
    :param ep: Number of electrum pieces
    :param sp: Number of silver pieces
    :param cp: Number of copper pieces
    :param split: Number of ways the copper pieces are to be split
    :return: A list containing the total copper pieces, the amount to be shared, and any remainder left over
    """
    total_in_cp = (cp + (sp * 10) + (ep * 50) + (gp * 100) + (pp * 1000))
    share_of_cp = total_in_cp // split
    remaining_cp = total_in_cp % split
    return total_in_cp, share_of_cp, remaining_cp


def convert_denominations(cp):
    """
    Converts the number of copper pieces back to larger denominations
    :param cp: Number of copper pieces
    :return: A list with the number of platinum, gold, electrum, silver and copper pieces respectively
    """
    if cp >= 1000:
        pp = cp // 1000
        cp = cp - (pp * 1000)
    else:
        pp = 0
    if cp >= 100:
        gp = cp // 100
        cp = cp - (gp * 100)
    else:
        gp = 0
    if cp >= 50:
        ep = cp // 50
        cp = cp - (ep * 50)
    else:
        ep = 0
    if cp >= 10:
        sp = cp // 10
        cp = cp - (sp * 10)
    else:
        sp = 0
    return pp, gp, ep, sp, cp


if __name__ == '__main__':
    card_deck = new_card_deck()
    tarot_deck = new_tarot_deck()
    gun = new_gun()
    print(pull_trigger(gun, 10))
