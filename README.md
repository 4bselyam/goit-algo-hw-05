### Висновок

Проведене тестування ефективності алгоритмів пошуку підрядка Бойєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на двох текстових файлах (стаття 1 та стаття 2) показало, що алгоритм Бойєра-Мура є найбільш ефективним для пошуку як існуючих, так і вигаданих підрядків. Нижче наведені результати часу виконання для кожного алгоритму в секундах:

#### Стаття 1

- Існуючий підрядок ("алгоритмів"):

  - Бойєр-Мур: 0.00215 сек
  - Кнут-Морріс-Пратт: 0.00965 сек
  - Рабін-Карп: 0.00662 сек

- Вигаданий підрядок ("неіснуючийпідрядок"):
  - Бойєр-Мур: 0.04437 сек
  - Кнут-Морріс-Пратт: 0.57862 сек
  - Рабін-Карп: 0.37817 сек

#### Стаття 2

- Існуючий підрядок ("системи"):

  - Бойєр-Мур: 0.00075 сек
  - Кнут-Морріс-Пратт: 0.00278 сек
  - Рабін-Карп: 0.00205 сек

- Вигаданий підрядок ("неіснуючийпідрядок"):
  - Бойєр-Мур: 0.11814 сек
  - Кнут-Морріс-Пратт: 0.75235 сек
  - Рабін-Карп: 0.53037 сек

На основі отриманих даних можна зробити висновок, що алгоритм Бойєра-Мура демонструє найкращі результати в обох випадках. Він є найшвидшим для пошуку існуючих підрядків і значно перевершує інші алгоритми при пошуку вигаданих підрядків. Це робить алгоритм Бойєра-Мура найкращим вибором для завдань пошуку підрядків у великих текстах, де ефективність є критично важливою.
