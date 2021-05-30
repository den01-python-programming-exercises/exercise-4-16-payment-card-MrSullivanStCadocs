def main():
    #write your code below this line
    from payment_card import PaymentCard
    PaulsCard = PaymentCard(20)
    MattsCard = PaymentCard(30)

    PaulsCard.eat_heartily()
    MattsCard.eat_affordably()

    print("Paul: " + str(PaulsCard))
    print("Matt: " + str(MattsCard))

    PaulsCard.add_money(20)
    MattsCard.eat_heartily()

    print("Paul: " + str(PaulsCard))
    print("Matt: " + str(MattsCard))

    PaulsCard.eat_affordably()
    PaulsCard.eat_affordably()
    MattsCard.add_money(50)

    print("Paul: " + str(PaulsCard))
    print("Matt: " + str(MattsCard))



if __name__ == '__main__':
    main()
