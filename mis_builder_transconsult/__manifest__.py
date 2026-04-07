# Copyright 2026 Transconsult
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MIS Builder - Transconsult Reports",
    "summary": "Справки Планирано vs Реално за Transconsult",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "author": "Transconsult",
    "website": "https://github.com/OCA/mis-builder",
    "depends": ["mis_builder_budget"],
    "data": [
        "data/mis_report_style.xml",
        "data/mis_report.xml",
        "data/mis_budget_by_account.xml",
        "data/mis_report_instance.xml",
    ],
    "installable": True,
    "development_status": "Beta",
}
