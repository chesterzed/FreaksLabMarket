from lib2to3.fixes.fix_input import context

from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': [
        {'image': 'images/pic01.jpg',
         'name': 'Чайный столик и три стула',
         'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
         'price': 150.00},

         {'image': 'images/pic02.jpg',
         'name': 'Чайный столик и два стула',
         'description': 'Набор из стола и двух стульев в минималистическом стиле.',
         'price': 93.00},

         {'image': 'images/pic03.jpg',
         'name': 'Двухспальная кровать',
         'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
         'price': 670.00},

         {'image': 'images/pic04.jpg',
         'name': 'Кухонный стол с раковиной',
         'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
         'price': 365.00},

         {'image': 'images/pic05.jpg',
         'name': 'Кухонный стол с встройкой',
         'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
         'price': 430.00},

         {'image': 'images/pic06.jpg',
         'name': 'Угловой диван для гостинной',
         'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
         'price': 610.00},

         {'image': 'images/pic07.jpg',
         'name': 'Прикроватный столик',
         'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
         'price': 55.00},

         {'image': 'images/pic08.jpg',
         'name': 'Диван обыкновенный',
         'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
         'price': 190.00},

         {'image': 'images/pic09.jpg',
         'name': 'Стул офисный',
         'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
         'price': 30.00},

         {'image': 'images/pic10.jpg',
         'name': 'Растение',
         'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
         'price': 10.00},

         {'image': 'images/pic11.jpg',
         'name': 'Цветок стилизированный',
         'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
         'price': 15.00},

         {'image': 'images/pic12.jpg',
         'name': 'Прикроватный столик',
         'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
         'price': 25.00},
        ]
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    return render(request, "goods/product.html")