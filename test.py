def products_value(product):
    money_sell = product[-5:]
    print(money_sell)
    # if product in request.POST:
    #     print(money_sell)
        # if money > 30:
        #     CustomUser.objects.update(money=int(money) - 30)
        # else:
        #     messages.info(request, 'У вас нет денег!')


products_value('Хлеб 30 руб')