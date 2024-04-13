## Критерии выполнения заданий

* Результат задания залили на GitHub и сдали в виде ссылки на репозиторий.

### Задание 1

Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD,
задействовав модуль django.forms.

Условия для пользователей:

* могут создавать новые продукты,
* не могут создавать продукты с запрещенными словами в названии и описании.

Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы
нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.


> Для настройки валидации внутри формы определите методы `clean` для полей (например, `clean_name()`). При наличии
> запрещенных слов — выбрасывайте ошибку `forms.ValidationError()` с соответствующим сообщением. Если валидация проходит
> успешно, возвращайте cleaned_data.

### Задание 2

Добавьте новую модель «Версия», которая должна содержать следующие поля:

* продукт,
* номер версии,
* название версии,
* признак текущей версии.

При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

> Признак текущей версии — булево поле, является ли версия для продукта текущей для отображения на сайте или нет.
> Для отображения активной версии расширьте метод`get_context_data()`
> контроллера списка продуктов, получите данные о версиях продукта и выберите текущую (активную) версию для продукта.

### Задание 3

Добавьте реализацию работы с формами для версий продукта.

> При стилизации формы методом `__init__` можно создать класс-миксин для сокращения дублирования кода.
> Для стилизации булевого поля используйте специальный стиль — `form-check-input`.