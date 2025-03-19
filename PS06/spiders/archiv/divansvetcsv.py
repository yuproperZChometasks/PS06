"""
Сохранить спарсенные данные в CSV файл, 
воспользоваться встроенными возможностями Scrapy. изменения в ваш код и добавить настройки для экспортирования 
данных в CSV. Вот обновленный код:
"""
import scrapy

class DivansvetcsvSpider(scrapy.Spider):
    name = "divansvetcsv"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/tomsk/category/svet"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        svets = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for svet in svets:
            yield {
                # Ссылки и теги получаем с помощью консоли на сайте 
                'name': svet.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': svet.css('div.pY3d2 span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                'url': svet.css('a').attrib['href']
            }

# Для запуска парсера и сохранения данных в CSV файл, используйте следующую команду в терминале:
# scrapy crawl divansvetcsv -o output.csv

"""
### Инструкция по запуску:

1. Сохраните этот код в файл, например, `divansvetcsv_spider.py`.
2. Перейдите в директорию вашего проекта Scrapy.
3. Запустите команду в терминале:
"""
   # ```bash
   # scrapy crawl divansvetcsv -o output.csv
   # ```
"""
Эта команда создаст файл `output.csv` в текущей директории, в который будут сохранены спарсенные данные с сайта. 
Если файла не существует, Scrapy создаст его автоматически. Если файл уже есть, то он будет перезаписан."
"""