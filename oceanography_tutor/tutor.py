from datetime import timedelta, date

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.last_reviewed = None

class Tutor:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Add a new flashcard to the tutor."""
        self.cards.append(card)

    def review_cards(self):
        """Review all cards and update their last reviewed date."""
        for card in self.cards:
            if card.last_reviewed is None or (date.today() - card.last_reviewed).days > 7:
                # Simulate user answering a question
                card.answered_correctly = True
                card.last_reviewed = date.today()

    def get_next_card(self):
        """Get the next card to review, based on last reviewed date."""
        today = date.today()
        tomorrow = today + timedelta(days=1)
        return next((card for card in self.cards if (tomorrow - card.last_reviewed).days > 7), None)

def main():
    tutor = Tutor()

    # Example usage:
    card1 = Card("What is the tide?", "The rise and fall of sea level due to gravitational forces.")
    card2 = Card("What is salinity?", "The concentration of dissolved salts in seawater.")

    tutor.add_card(card1)
    tutor.add_card(card2)

    tutor.review_cards()

    next_card = tutor.get_next_card()
    if next_card:
        print(f"Next card: {next_card.question}")
    else:
        print("No cards to review")

if __name__ == "__main__":
    main()
