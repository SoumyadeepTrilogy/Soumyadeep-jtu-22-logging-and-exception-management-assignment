import os

# AWS credential constants
ALS_AWS_SECRET_KEY = os.getenv("ALS_AWS_SECRET_KEY")
ALS_AWS_ACCESS_KEY = os.getenv("ALS_AWS_ACCESS_KEY")
ALS_AWS_REGION = os.getenv("ALS_AWS_REGION_NAME", "us-east-1")
ALS_AWS_ACCOUNT = os.getenv("ALS_AWS_ACCOUNT", "082830052325")

# DDB Constants
DB_TABLE_NAME = os.getenv("ALS_DDB_TABLE_NAME", "auto-lead-scoring")
DEALER_DB_TABLE = os.getenv("ALS_DEALER_DDB_TABLE_NAME", "als-dealer-table")

# HYU Endpoint Constants
HYU_DEALER_ENDPOINT_NAME = os.getenv('HYU_DEALER_ENDPOINT_NAME')
HYU_NO_DEALER_ENDPOINT_NAME = os.getenv('HYU_NO_DEALER_ENDPOINT_NAME')

# BMW Endpoint Constants
BMW_DEALER_ENDPOINT_NAME = os.getenv('BMW_DEALER_ENDPOINT_NAME')

# MASERATI Endpoint Constants
MAS_DEALER_ENDPOINT_NAME = os.getenv('MAS_DEALER_ENDPOINT_NAME')

# General Model Constants
GEN_DEALER_ENDPOINT_NAME = os.getenv('GEN_DEALER_ENDPOINT_NAME')

# Admin Constants
SUPPORTED_OEMS = ["hyundai", "bmw", "maserati"]
DEFAULT_OEM_LIMIT = os.getenv("DEFAULT_OEM_LIMIT", "0.036779455840587616")
# Data Tool 3rd Party Service Constants
ALS_DATA_TOOL_REQUEST_KEY = os.getenv('ALS_DATA_TOOL_REQUEST_KEY')
ALS_DATA_TOOL_SERVICE_URL = os.getenv('ALS_DATA_TOOL_SERVICE_URL')
ALS_DATA_TOOL_PHONE_VERIFY_METHOD = os.getenv('ALS_DATA_TOOL_PHONE_VERIFY_METHOD')
ALS_DATA_TOOL_EMAIL_VERIFY_METHOD = os.getenv('ALS_DATA_TOOL_EMAIL_VERIFY_METHOD')

# Numverify Constants
NUM_VERIFY_ACCESS_KEY = os.getenv('NUM_VERIFY_ACCESS_KEY')
NUM_VERIFY_URL = os.getenv('NUM_VERIFY_URL')

# Towerdata Constants
TOWER_DATA_URL = os.getenv('TOWER_DATA_URL')
TOWER_DATA_API_KEY = os.getenv('TOWER_DATA_API_KEY')

# S3 bucket for lead dumping
S3_BUCKET_NAME = os.getenv("ALS_QUICKSIGHT_BUCKET_NAME", "auto-lead-scoring-quicksight")

# Cognito Constants
ALS_USER_POOL_ID = os.getenv('ALS_USER_POOL_ID')
# Quicksight Dashboards

PROVIDER_DASHBOARD_ID = os.getenv('PROVIDER_DASHBOARD', "ceb3c69c-707d-4709-a072-89745bfea377")
OEM_DASHBOARD_ID = os.getenv('OEM_DASHBOARD', "c504a613-a3d1-48ad-9212-73552e7c0b69")
ADMIN_DASHBOARD_ID = os.getenv('ADMIN_DASHBOARD', "92e96960-d42e-4f12-9910-0448c1e08fd6")

DASHBOARD_ARN = {
    "3PL": f"arn:aws:quicksight:us-east-1:{ALS_AWS_ACCOUNT}:dashboard/{PROVIDER_DASHBOARD_ID}",
    "OEM": f"arn:aws:quicksight:us-east-1:{ALS_AWS_ACCOUNT}:dashboard/{OEM_DASHBOARD_ID}",
    "ADMIN": f"arn:aws:quicksight:us-east-1:{ALS_AWS_ACCOUNT}:dashboard/{ADMIN_DASHBOARD_ID}"
}

SESSION_LIFETIME = 600

# Constant Median Data Values
DEALER_RATING = "4.678555302965422"
LIFETIMEREVIEWS = "228.7548938307518"
RECOMMENDED = "95.71456599706488"
DEALER_SCR = "5.348490632243166"
DEALER_OCR = "8.918993057558286"
EMAILDOMAINCAT_RATIO = "0.04438530340664647"
LEAD_PROVIDERSERVICE_RATION = "0.044290802250891076"

HOUSEHOLD_INCOME = 55319.39
POPULATION_DENSITY = 3585.81

# SQS Queue
SQS_QUEUE_NAME = os.getenv('SQS_QUEUE_NAME', 'auto-lead-scoring')

# TTL
LEAD_ITEM_TTL = 120
OEM_ITEM_TTL = 30
