"""Scrapeflow - Parallel workflow for web scraping and processing."""

from scrapeflow.executor import execute_async, Context, taskify
from scrapeflow.scrape import scrape, scrape_with_validation, scrapify
from scrapeflow.status import StatusData, Params, read_status, status_summary, url_to_key, urls_to_tasks
from scrapeflow.proxies import ProxyProvider, ProxyProviderFromList, ProxyProviderFromDict, ProxyProviderFromProxyscrape, ProxyProviderFromWebshare, ProxyProviderFromIPRoyal

__version__ = "0.1.0"

__all__ = [
    "execute_async",
    "Context", 
    "taskify",
    "scrape",
    "scrape_with_validation", 
    "scrapify",
    "StatusData",
    "Params",
    "read_status",
    "status_summary", 
    "url_to_key",
    "urls_to_tasks",
    "ProxyProvider",
    "ProxyProviderFromList",
    "ProxyProviderFromDict", 
    "ProxyProviderFromProxyscrape",
    "ProxyProviderFromWebshare",
    "ProxyProviderFromIPRoyal",
]