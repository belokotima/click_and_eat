new ymaps.Placemark([address['lat'], address['lon']], {
// Зададим содержимое заголовка балуна.
// <img src=\"' + rest['logo'] + '\" height="100" width="100" style="border-radius: 50%">
        balloonContentHeader: '<h2 class="uk-text-light" style="margin-bottom: 0"><a>' + rest['title'] + '</a></h2>',
// Зададим содержимое основной части балуна.
        balloonContentBody: body,
// Зададим содержимое нижней части балуна.
        balloonContentFooter: 'Часы работы: ' + rest['open_time'] + ' - ' + rest['close_time'],
// Зададим содержимое всплывающей подсказки.
        hintContent: rest['title']
    },
    {
        iconLayout: circleLayout,
// Описываем фигуру активной области "Круг".
        iconShape: {
            type: 'Circle',
// Круг описывается в виде центра и радиуса
            coordinates: [0, 0],
            radius: 27
        }
    })