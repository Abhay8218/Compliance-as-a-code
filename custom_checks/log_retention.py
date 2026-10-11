from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class CloudWatchRetention180(BaseResourceCheck):
    def __init__(self):
        name = "Ensure CloudWatch log groups retain logs for at least 180 days (CERT-In)"
        id = "CKV_IN_002"
        supported_resources = ["aws_cloudwatch_log_group"]
        categories = [CheckCategories.LOGGING]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_resources=supported_resources,
        )

    def scan_resource_conf(self, conf):
        days = conf.get("retention_in_days")
        if isinstance(days, list) and days:
            days = days[0]
        if days is None:
            return CheckResult.PASSED  # no setting means logs never expire
        try:
            days = int(days)
        except (TypeError, ValueError):
            return CheckResult.UNKNOWN  # e.g. a variable we can't resolve
        if days == 0 or days >= 180:
            return CheckResult.PASSED
        return CheckResult.FAILED


check = CloudWatchRetention180()
