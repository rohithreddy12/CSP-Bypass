"""
@author: moloch

Scanner issues reported by the plugin.
"""

from burp import IScanIssue


class BaseCSPIssue(IScanIssue):

    """ Just a base class with some helpful docstrings """

    def __init__(self, httpService, url, httpMessages, severity, confidence):
        """ Setters for all the getters """
        self._httpService = httpService
        self._url = url
        self._httpMessages = httpMessages
        self._severity = severity
        self._confidence = confidence

    def getUrl(self):
        """
        This method returns the URL for which the issue was generated.
        @return The URL for which the issue was generated.
        """
        return self._url

    def getIssueName(self):
        """
        This method returns the name of the issue type.
        @return The name of the issue type (e.g. "SQL injection").
        """
        raise NotImplementedError()

    def getIssueType(self):
        """
        This method returns a numeric identifier of the issue type. See the Burp
        Scanner help documentation for a listing of all the issue types.
        @return A numeric identifier of the issue type.
        """
        return 0  # https://portswigger.net/burp/help/scanner_issuetypes.html

    def getSeverity(self):
        """
        This method returns the issue severity level.
        @return The issue severity level. Expected values are "High", "Medium",
        "Low", "Information" or "False positive".
        """
        return self._severity

    def getConfidence(self):
        """
        This method returns the issue confidence level.
        @return The issue confidence level. Expected values are "Certain", "Firm"
        or "Tentative".
        """
        return self._confidence

    def getIssueBackground(self):
        """
        This method returns a background description for this type of issue.
        @return A background description for this type of issue, or
        <code>null</code> if none applies.
        """
        raise NotImplementedError()

    def getRemediationBackground(self):
        """
        This method returns a background description of the remediation for this
        type of issue.
        @return A background description of the remediation for this type of
        issue, or
        <code>null</code> if none applies.
        """
        raise NotImplementedError()

    def getIssueDetail(self):
        """
        This method returns detailed information about this specific instance of
        the issue.
        @return Detailed information about this specific instance of the issue,
        or
        <code>null</code> if none applies.
        """
        raise NotImplementedError()

    def getRemediationDetail(self):
        """
        This method returns detailed information about the remediation for this
        specific instance of the issue.
        @return Detailed information about the remediation for this specific
        instance of the issue, or
        <code>null</code> if none applies.
        """
        raise NotImplementedError()

    def getHttpMessages(self):
        """
        This method returns the HTTP messages on the basis of which the issue was
        generated.
        @return The HTTP messages on the basis of which the issue was generated.
        Note: The items in this array should be instances of
        <code>IHttpRequestResponseWithMarkers</code> if applicable, so that
        details of the relevant portions of the request and response messages are
        available.
        """
        if isinstance(self._httpMessages, list):
            return self._httpMessages
        else:
            return [self._httpMessages]

    def getHttpService(self):
        """
        This method returns the HTTP service for which the issue was generated.
        @return The HTTP service for which the issue was generated.
        """
        return self._httpService


class WildCardDirective(BaseCSPIssue):

    def getIssueName(self):
        return "Wild Card Directive"

    def getIssueBackground(self):
        return "Issue background"

    def getRemediationBackground(self):
        return "Remediation background"

    def getIssueDetail(self):
        return "Issue details"

    def getRemediationDetail(self):
        return "Remediation details"


class UnsafeContentDirective(BaseCSPIssue):

    def getIssueName(self):
        return "Unsafe Content Sources"

    def getIssueBackground(self):
        return "Issue background"

    def getRemediationBackground(self):
        return "Remediation background"

    def getIssueDetail(self):
        return "Issue details"

    def getRemediationDetail(self):
        return "Remediation details"


class InsecureContentDirective(BaseCSPIssue):

    def getIssueName(self):
        return "Insecure Content Sources"

    def getIssueBackground(self):
        return "Issue background"

    def getRemediationBackground(self):
        return "Remediation background"

    def getIssueDetail(self):
        return "Issue details"

    def getRemediationDetail(self):
        return "Remediation details"


class MissingDirective(BaseCSPIssue):

    def getIssueName(self):
        return "Missing CSP Directive"

    def getIssueBackground(self):
        return "Issue background"

    def getRemediationBackground(self):
        return "Remediation background"

    def getIssueDetail(self):
        return "Issue details"

    def getRemediationDetail(self):
        return "Remediation details"


class DeprecatedHeader(BaseCSPIssue):

    def getIssueName(self):
        return "Deprecated Header"

    def getIssueBackground(self):
        return "Issue background"

    def getRemediationBackground(self):
        return "Remediation background"

    def getIssueDetail(self):
        return "Issue details"

    def getRemediationDetail(self):
        return "Remediation details"
