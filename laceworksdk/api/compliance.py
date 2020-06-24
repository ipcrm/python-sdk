# -*- coding: utf-8 -*-
"""
Lacework Compliance API wrapper.
"""

import json
import logging

logger = logging.getLogger(__name__)


class ComplianceAPI(object):
    """
    Lacework Compliance API.
    """

    def __init__(self, session):
        """
        Initializes the ComplianceAPI object.

        :param session: An instance of the HttpSession class

        :return ComplianceAPI object.
        """

        super(ComplianceAPI, self).__init__()

        self._session = session

    def get_latest_aws_report(self,
                              aws_account_id,
                              file_format="json",
                              report_type=None):
        """
        A method to get the latest compiance report for an AWS account.

        :param aws_account_id: A string representing which AWS Account to query.
        :param file_format: A string representing the desired file format. ("pdf" or "json")
        :param report_type: A string representing the desired report type.
            ("AWS_CIS_S3", "NIST_800-53_Rev4", "ISO_2700", "HIPAA", "SOC", or "PCI")

        :return response json
        """

        # Build the Compliance report request URI
        api_uri = "/api/v1/external/compliance/aws/GetLatestComplianceReport?" \
                  f"AWS_ACCOUNT_ID={aws_account_id}"

        if file_format:
            api_uri += f"&FILE_FORMAT={file_format}"

        if report_type:
            api_uri += f"&REPORT_TYPE={report_type}"

        response = self._session.get(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()

    def get_latest_azure_report(self,
                                azure_tenant_id,
                                azure_subscription_id,
                                file_format="json",
                                report_type=None):
        """
        A method to get the latest compiance report for an Azure tenant.

        :param azure_tenant_id: A string representing which Azure Tenant to query.
        :param azure_subscription_id: A string representing which Azure Subscription to query.
        :param file_format: A string representing the desired file format. ("pdf" or "json")
        :param report_type: A string representing the desired report type.
            ("AZURE_CIS", "AZURE_SOC", or "AZURE_PCI")

        :return response json
        """

        # Build the Compliance report request URI
        api_uri = "/api/v1/external/compliance/azure/GetLatestComplianceReport?" \
                  f"AZURE_TENANT_ID={azure_tenant_id}&AZURE_SUBS_ID={azure_subscription_id}"

        if file_format:
            api_uri += f"&FILE_FORMAT={file_format}"

        if report_type:
            api_uri += f"&REPORT_TYPE={report_type}"

        response = self._session.get(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()

    def get_latest_gcp_report(self,
                              gcp_organization_id,
                              gcp_project_id,
                              file_format="json",
                              report_type=None):
        """
        A method to get the latest compiance report for a Google Cloud organization.

        :param gcp_organization_id: A string representing which GCP Organization to query.
        :param gcp_project_id: A string representing which GCP Project to query.
        :param file_format: A string representing the desired file format. ("pdf" or "json")
        :param report_type: A string representing the desired report type.
            ("GCP_CIS", "GCP_SOC", or "GCP_PCI")

        :return response json
        """

        # Build the Compliance report request URI
        api_uri = "/api/v1/external/compliance/gcp/GetLatestComplianceReport?" \
                  f"GCP_ORG_ID={gcp_organization_id}&GCP_PROJ_ID={gcp_project_id}"

        if file_format:
            api_uri += f"&FILE_FORMAT={file_format}"

        if report_type:
            api_uri += f"&REPORT_TYPE={report_type}"

        response = self._session.get(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()

    def list_azure_subscriptions(self, azure_tenant_id):
        """
        A method to list the subscriptions in an Azure account.

        :param azure_tenant_id: A string representing which Azure Tenant to query.

        :return response json
        """

        # Build the Compliance list subscription request URI
        api_uri = "/api/v1/external/compliance/azure/ListSubscriptionsForTenant?" \
                  f"AZURE_TENANT_ID={azure_tenant_id}"

        response = self._session.get(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()

    def list_gcp_projects(self, gcp_organization_id):
        """
        A method to list the projects in a Google Cloud organization.

        :param gcp_organization_id: A string representing which GCP Organization to query.

        :return response json
        """

        # Build the Compliance list subscription request URI
        api_uri = "/api/v1/external/compliance/azure/ListSubscriptionsForTenant?" \
                  f"GCP_ORG_ID={gcp_organization_id}"

        response = self._session.get(api_uri)

        logger.debug(json.dumps(response.json(), indent=2))

        return response.json()
