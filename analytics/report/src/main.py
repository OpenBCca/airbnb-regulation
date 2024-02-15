from listing_store import ListingStore
from report_generator import ReportGenerator 

class ReportGenerationService:
    def __init__(self, report_generator,listing_store, report_store, policy_evaluator):
        self.report_generator = report_generator
        self.listing_store = listing_store
        self.report_store = report_store
        self.policy_evaluator = policy_evaluator
        self.evaluated_data_collection = {}

    def evaluate_and_generate_report(self, listing_id):
        data = self.listing_store.get_items_from_mock_store()
        evaluated_data = self.policy_evaluator.evaluate(data)
        self.evaluated_data_collection[listing_id] = evaluated_data
        report = self.report_generator.generate_report(self.evaluated_data_collection)
        filename = f"report_{listing_id}.{self.report_generator.output_format}"
        self.report_store.save_report(report, filename)

listing_store = ListingStore('mock') 
report_generator = ReportGenerator('html') 
report_store = ReportStore()  
policy_evaluator = PolicyEvaluator()  

service = ReportGenerationService(report_generator, listing_store, report_store, policy_evaluator)
service.evaluate_and_generate_report('1')  # Generate a report for listing with ID '1'