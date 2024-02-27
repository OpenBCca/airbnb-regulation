import json
import scrapy
from scrapy import Request
from scrapy.http import Response
from airbnb_listings.items import AirBnBListingItem


class ListingSpider(scrapy.Spider):
    """
    Spider for scraping Airbnb listings.
    """
    name = "listing_spider"
    allowed_domains = ['airbnb.ca']
    start_urls = ['https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes',
                  'https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-03-01&monthly_length=3&monthly_end_date=2024-06-01&price_filter_input_type=0&channel=EXPLORE&query=Vancouver%2C%20BC&place_id=ChIJs0-pQ_FzhlQRi_OBm-qWkbs&date_picker_type=calendar&checkin=2024-02-22&checkout=2024-03-20&adults=1',
                  'https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-03-01&monthly_length=2&monthly_end_date=2024-06-01&price_filter_input_type=0&channel=EXPLORE&query=Vancouver%2C%20BC&place_id=ChIJs0-pQ_FzhlQRi_OBm-qWkbs&date_picker_type=monthly_stay&checkin=2024-02-22&checkout=2024-03-20&adults=2&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=27'
                  ]
    next_page_cursors: [str] = None

    async def parse(self, response: Response, **kwargs):
        """
        Parse method for extracting listings from the Airbnb search results page.

        Args:
            response (Response): The response object from the request.

        Yields:
            Request: A request object for each listing's details page.
        """
        script_tag = response.css('script#data-deferred-state')
        script_inner_text = script_tag.css('script::text').get()
        script_json = json.loads(script_inner_text)
        results = self._parse_listings_json(script_json)
        if ListingSpider.next_page_cursors is None:
            ListingSpider.next_page_cursors = self._get_cursors(script_json)
        for result in results:
            listing = result.get("listing", {})
            listing_id = listing.get("id")
            title = listing.get("title", "")
            name = listing.get("name", "")
            coordinate = listing.get("coordinate", "")
            latitude = coordinate.get("latitude", "")
            longitude = coordinate.get("longitude", "")
            page_url = f"https://www.airbnb.ca/rooms/{listing_id}"
            airbnb_params = {
                "airbnb_listing_id": listing_id,
                "title": title,
                "name": name,
                "latitude": latitude,
                "longitude": longitude
            }

            try:
                yield Request(url=page_url, callback=self.handle_listing,
                              meta={'airbnb_params': airbnb_params})
            except Exception as e:
                print("exception", e.args[0])

        if len(ListingSpider.next_page_cursors) != 0:
            cursor_id = ListingSpider.next_page_cursors.pop()
            next_url = f'https://www.airbnb.ca/s/Vancouver--British-Columbia--Canada/homes?cursor={cursor_id}'
            yield response.follow(next_url, callback=self.parse)

    @staticmethod
    def handle_listing(response):
        """
        Parse method for extracting details from an Airbnb listing page.

        Args:
            response (Response): The response object from the request.

         Yields:
            AirBnBListingItem: An AirBnBListingItem object containing details of an Airbnb listing.
        """
        airbnb_params = response.meta.get('airbnb_params', {})
        listing_item = AirBnBListingItem(
            airbnb_listing_id=airbnb_params.get('airbnb_listing_id'),
            title=airbnb_params.get('title'),
            name=airbnb_params.get('name'),
            latitude=airbnb_params.get('latitude'),
            longitude=airbnb_params.get('longitude')
        )

        script_tag = response.css('script#data-deferred-state')
        script_inner_text = script_tag.css('script::text').get()
        script_tag_json = json.loads(script_inner_text)

        registration_number = "Not Found"
        try:
            sections = ListingSpider._parse_listing_json(script_tag_json)
            for section in sections:
                if section.get("sectionComponentType") == "HOST_PROFILE_DEFAULT":
                    items = section.get("section", {}).get("hostFeatures", [])
                    for item in items:
                        if item.get("title") == "Registration number":
                            registration_number = item.get("subtitle", "Not found")
        except Exception as e:
            print("Exception occurred:", e)

        listing_item["registration_number"] = registration_number
        yield listing_item

    @staticmethod
    def _safe_get(data: dict, *keys, default=None):
        """
        Safely retrieve a nested value from a dictionary.

        Args:
            data (dict): The dictionary to retrieve the value from.
            keys (tuple): The keys to navigate the nested structure.
            default: The default value to return if the keys are not found.

        Returns:
            The value at the specified nested key or the default value.
        """
        try:
            for key in keys:
                data = data[key]
            return data
        except KeyError:
            return default

    @staticmethod
    def _parse_listings_json(listings_json):
        """
        Parse method for extracting listing information from a JSON object.

        Args:
            listings_json (dict): The JSON object containing the listings' information.s

        Returns:
            list: A list of listings extracted from the JSON object.
        """
        return ListingSpider._safe_get(listings_json,
                                       "niobeMinimalClientData", 0, 1, "data", "presentation", "staysSearch",
                                       "results", "searchResults", default=[])

    @staticmethod
    def _parse_listing_json(listing_json):
        """
        Parse method for extracting listing details from a JSON object.

        Args:
            listing_json (dict): The JSON object containing the listing details.

        Returns:
            list: A list of listing details extracted from the JSON object.
        """
        return ListingSpider._safe_get(listing_json, "niobeMinimalClientData", 0, 1, "data", "presentation",
                                       "stayProductDetailPage",
                                       "sections", "sections", default=[])

    @staticmethod
    def _get_cursors(script_json):
        """
        Parse method for extracting pagination cursors from a JSON object.

        Args:
            script_json (dict): The JSON object containing the pagination information.

        Returns:
            list: A list of pagination cursors extracted from the JSON object.
        """
        return ListingSpider._safe_get(script_json,
                                       "niobeMinimalClientData", 0, 1, "data", "presentation", "staysSearch",
                                       "results", "paginationInfo", "pageCursors", default=[])
