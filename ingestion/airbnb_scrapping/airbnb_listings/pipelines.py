# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class AirbnbListingsPipeline:
    def process_item(self, item, spider):
        return item


class AirBnbListingsDuplicatePipeLine:
    file_name = "master_data.csv"

    def __init__(self):
        self.airbnb_ids_scrapped = set()

    def open_spider(self, spider):
        """
        Need to read the file, if the file does not exit then need to inistal an empty array of ids
        :param spider:
        :return:
        """
        try:
            with open(
                    f"D:\OneDrive - BCIT\openBC\\airbnb\\airbnb-regulation\ingestion\\airbnb_scrapping\{AirBnbListingsDuplicatePipeLine.file_name}",
                    "r",
                    encoding="utf8") as file:
                read_csv_file = csv.DictReader(file)
                for row in read_csv_file:
                    row: dict
                    self.airbnb_ids_scrapped.add(row['airbnb_listing_id'])
        except FileNotFoundError as e:
            print(e)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["airbnb_listing_id"] in self.airbnb_ids_scrapped:
            raise DropItem(f"Duplicate airbnb id found: {item!r}")
        else:
            self.airbnb_ids_scrapped.add(adapter["airbnb_listing_id"])
            return item
