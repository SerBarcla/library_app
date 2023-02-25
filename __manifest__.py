{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Batlang",
    "category": "Services/Library",    
    "license": "AGPL-3",
    "website": "https://www.datalabs.space",
    "version": "16.0.1.0",
    "depends": ["base"],
    "application": True,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menu.xml",
    ]
    
}