import datetime
from django.conf import settings
from backend import models
from backend.models.vulnerability import Severity
from pecoret.core.reporting import types as report_types
from pecoret.core.reporting.error import ReportError


class PentestPDFReport(report_types.PentestPDFReport):
    """
    this is an example report template based on the Hack The Box report template.
    """

    def get_context(self):
        context = super().get_context()
        context["now"] = datetime.datetime.now().strftime("%B %d, %Y")
        context["REPORT_COMPANY_INFORMATION"] = settings.REPORT_COMPANY_INFORMATION
        context["findings"] = models.Finding.objects.for_report(self.get_project())
        return context

    def get_assets(self):
        """
        get a list of report relevant assets
        :return:
        """
        assets = []
        available_assets = [models.Host, models.WebApplication, models.MobileApplication]
        for asset in available_assets:
            assets += list(asset.objects.for_project(self.get_project()))
        return assets

    def get_findings_count_for_asset(self, asset, severity=None):
        qs = asset.findings.exclude(exclude_from_report=True)
        if severity:
            qs = qs.filter(severity=Severity[severity].value)
        return qs.count()

    def get_finding_errors(self):
        errors = []
        findings = self.get_context()["findings"]
        for finding in findings:
            if not finding.proof_set.all():
                error = ReportError("Finding is missing a proof!", f"#finding-{finding.internal_id}")
                errors.append(error)
        return errors

    def get_errors(self):
        errors = self.get_finding_errors()
        if not self.report_document.report.recommendation:
            error = ReportError("Missing recommendation!", "#executive-summary-recommendation")
            errors.append(error)
        if not self.report_document.report.evaluation:
            error = ReportError("Missing evaluation!", "#executive-summary-evaluation")
            errors.append(error)
        return errors


class SingleFindingPDFReport(report_types.SingleFindingPDFReport):
    pass


class AdvisoryMarkdownExport(report_types.AdvisoryMarkdownExport):
    pass


class AdvisoryPDFExport(report_types.AdvisoryPDFExport):

    def get_context(self):
        context = super().get_context()
        context["now"] = datetime.datetime.now().strftime("%B %d, %Y")
        context["REPORT_COMPANY_INFORMATION"] = settings.REPORT_COMPANY_INFORMATION
        return context


class VulnerabilityCSVReport(report_types.VulnerabilityCSVReport):
    pass
