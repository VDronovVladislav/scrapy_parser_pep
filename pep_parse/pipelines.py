import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        self.total = sum(self.status_count.values())
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        filename = f'status_summary_{now.strftime(DATETIME_FORMAT)}.csv'
        file_path = result_dir / filename

        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_NONE)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
            writer.writerow(['Total', self.total])
