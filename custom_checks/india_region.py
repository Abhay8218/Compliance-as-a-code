from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.provider.base_check import BaseProviderCheck

ALLOWED_REGIONS = ["ap-south-1", "ap-south-2"]


class AWSRegionIndiaOnly(BaseProviderCheck):
    def __init__(self):
        name = "Ensure AWS provider region is in India (data localization)"
        id = "CKV_IN_001"
        supported_provider = ["aws"]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_provider=supported_provider,
        )

    def scan_provider_conf(self, conf):
        region = conf.get("region")
        if isinstance(region, list) and region:
            region = region[0]
        if region in ALLOWED_REGIONS:
            return CheckResult.PASSED
        return CheckResult.FAILED


check = AWSRegionIndiaOnly()
