from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datetime import datetime


class Tool:
    def __init__(self):
        self.api_client = ApiClient(Configuration())

    def flatten(self, l):
        return [item for sublist in l for item in sublist]


class UsageMeteringTool(Tool):
    def __init__(self):
        super().__init__()
        self.usage_metering_api_client = UsageMeteringApi(self.api_client)

    def get_monthly_top_metrics(self, limit: int = 25) -> str:
        response = self.usage_metering_api_client.get_usage_top_avg_metrics(
            month=datetime.now(), limit=limit
        ).to_dict()
        return response["usage"]


class MetricsTool(Tool):
    def __init__(self):
        super().__init__()
        self.metrics_api_client = MetricsApi(self.api_client)

    def get_active_metric_configurations(self, metric_name: str):
        response = self.metrics_api_client.list_active_metric_configurations(
            metric_name
        )
        return response["data"]

    def get_cardinality_estimate(
        self, metric_name: str, active_tags: list[str], active_aggregations: int
    ):
        response = self.metrics_api_client.estimate_metrics_output_series(
            filter_groups=",".join(active_tags),
            filter_num_aggregations=active_aggregations,
            metric_name=metric_name,
        )
        return response["data"]["attributes"]["estimated_output_series"]
