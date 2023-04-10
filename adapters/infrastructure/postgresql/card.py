from domain.entities.card import Card

class CardImpl:
    '''Card Interface Implementation'''
    cursor : any

    def __init__(self, cursor: any) -> None:
        self.cursor = cursor

    def save(self, card: Card) -> None:
        '''Create card'''
        create_card = """
            INSERT INTO card(id_card,exp_date,holder,number,cvv,brand)
            VALUES(%s,%s,%s,%s,%s,%s);
        """
        self.cursor.execute(create_card,(
            str(card.id_card),card.exp_date,
            card.holder,card.number,
            card.cvv,card.brand)
        )

    def list(self) -> list[Card]:
        '''Get all cards'''
        cards: list[Card] = list()
        get_card = """
            SELECT id_card,exp_date,holder,number,cvv,brand FROM card;
        """
        self.cursor.execute(get_card)
        for row in self.cursor.fetchall():
            card = Card(
               id_card=row[0],
               exp_date=row[1],
               holder=row[2],
               number=row[3],
               cvv=row[4],
               brand=row[5]
            )
            card.id_card = str(card.id_card)
            cards.append(card)
        return cards

    def detail(self, id_card: str) -> Card or None:
        '''Try get card by id'''
        get_card = """
            SELECT id_card,exp_date,holder,number,cvv,brand FROM card WHERE id_card=%s;
        """
        self.cursor.execute(get_card, (id_card,))
        rst = self.cursor.fetchone()
        if rst:
            card = Card(
                id_card=rst[0],
                exp_date=rst[1],
                holder=rst[2],
                number=rst[3],
                cvv=rst[4],
                brand=rst[5])
            card.id_card = str(card.id_card)
            return card
        return None
