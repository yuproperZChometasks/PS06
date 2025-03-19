"""
сохранить данные в CSV файл без использования встроенных возможностей Scrapy, 
можyj использовать стандартный модуль Python `csv`.
"""

import scrapy
import csv

class DivansvetcsvSpider(scrapy.Spider):
    name = "divansvetcsv"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/tomsk/category/svet"]

    def __init__(self):
        # Открываем файл для записи в режиме 'write'
        self.csv_file = open('output_python.csv', mode='w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        # Записываем заголовки в CSV файл
        self.csv_writer.writerow(['name', 'price', 'url'])

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        svets = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for svet in svets:
            # Извлекаем данные
            name = svet.css('div.lsooF span::text').get()
            price = svet.css('div.pY3d2 span::text').get()
            url = svet.css('a').attrib['href']
            
            # Записываем данные в CSV файл
            self.csv_writer.writerow([name, price, url])

    def close(self, reason):
        # Закрываем CSV файл после завершения работы парсера
        self.csv_file.close()

"""
### Объяснение изменений:

1. **Импорт модуля `csv`:** Мы импортируем стандартный модуль `csv`, чтобы использовать его для записи данных в файл.

2. **Инициализация файла:** В конструкторе `__init__` мы открываем CSV файл для записи и создаем объект `csv.writer`.

3. **Запись заголовков:** Мы записываем заголовки (имя, цена, URL) в CSV файл.

4. **Запись данных:** В методе `parse` мы извлекаем данные и записываем их в CSV файл с помощью метода `writerow`.

5. **Закрытие файла:** В методе `close` мы закрываем файл, когда парсер завершает свою работу, чтобы убедиться, что все данные были корректно записаны.

### Запуск кода:

Сохраните этот код в файл, например, `divansvetcsv_spider.py`, и запустите его с помощью Scrapy, как обычно:

```bash
scrapy crawl divansvetcsv
```
"""
