import click
import tools
import utils


# Helpers
def mwl(metric, metric_price: float):
    click.echo(metric["metric_name"])

    # Retrieve currently queried tags and aggregations.
    active_metric_conf = tools.MetricsTool().get_active_metric_configurations(
        metric["metric_name"]
    )
    active_tags = active_metric_conf["attributes"]["active_tags"]
    try:
        active_aggregations = len(
            active_metric_conf["attributes"]["active_aggregations"].__dict__[
                "_data_store"
            ]["value"]
        )
    except:
        active_aggregations = 1
        click.echo("No active aggregations returned. Defaulting to 1.")

    # Estimate metric cardinality with current tagging and aggregations.
    try:
        cardinality = tools.MetricsTool().get_cardinality_estimate(
            metric["metric_name"], active_tags, active_aggregations
        )
    except:
        cardinality = None
        click.echo("Unable to estimate cardinality.")

    # Returns dictionary which corresponds to each row in the report.
    return {
        "org_name": metric["org_name"],
        "metric_name": metric["metric_name"],
        "active_tags": active_tags,
        "active_aggregations": active_aggregations,
        "current_volume": metric["avg_metric_hour"],
        "current_cost": metric["avg_metric_hour"] * metric_price,
        "mwl_volume": cardinality,
        "mwl_cost": int(cardinality) * metric_price if cardinality else None,
        "change_with_mwl": 1 - int(cardinality) / float(metric["avg_metric_hour"])
        if cardinality
        else None,
    }


# CLI
@click.group()
def cli():
    pass


@cli.command()
@click.option("--limit", help="Number of top metrics to analyze.")
@click.option("--price", help="Price per 100 Custom Metrics.")
def mwl_report(limit, price):
    top_metrics = tools.UsageMeteringTool().get_monthly_top_metrics(limit=int(limit))
    csv = [mwl(metric, metric_price=float(price) / 100) for metric in top_metrics]
    utils.write_csv(csv, "mwl_report")
