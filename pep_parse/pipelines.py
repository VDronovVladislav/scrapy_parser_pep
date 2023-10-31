import datetime as dt
from collections import defaultdict

from pep_parse.constants import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.status_count = defaultdict(int)
        self.total = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        filename = f'status_summary_{now.strftime(DATETIME_FORMAT)}.csv'
        file_path = result_dir / filename

        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.status_count.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{self.total}\n')
