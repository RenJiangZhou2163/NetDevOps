"""Nautobot development configuration file."""

# pylint: disable=invalid-envvar-default
import os
import sys

from nautobot.core.settings import *  # noqa: F403  # pylint: disable=wildcard-import,unused-wildcard-import
from nautobot.core.settings_funcs import parse_redis_connection, is_truthy

#
# Debug
#

DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", False))

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

#
# Logging
#

LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

#
# Redis
#

# Redis Cacheops
CACHEOPS_REDIS = parse_redis_connection(redis_database=1)

#
# Celery settings are not defined here because they can be overloaded with
# environment variables. By default they use `CACHES["default"]["LOCATION"]`.
#

# Enable installed plugins. Add the name of each plugin to the list.
PLUGINS = [
    "nautobot_device_onboarding",
    "nautobot_circuit_maintenance",
    "nautobot_data_validation_engine",
    "nautobot_capacity_metrics",
    "nautobot_golden_config",
    "nautobot_plugin_nornir",
    "nautobot_ssot",
    "nautobot_device_lifecycle_mgmt",
    "nautobot_firewall_models",
    "nautobot_bgp_models",
    "nautobot_floor_plan",
    "nautobot_design_builder",
    # "nautobot_ui_plugin",     # 当前版本不适配Nautobot2.3.x
    "nautobot_type_reapply",
]

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
    "nautobot_device_onboarding": {
        "create_platform_if_missing": True,
        "create_manufacturer_if_missing": True,
        "create_device_type_if_missing": True,
        "create_device_role_if_missing": True,
        "default_device_role": "network",
    },
    "nautobot_bgp_models": {},
    "nautobot_device_lifecycle_mgmt": {
        "barchart_bar_width": float(os.environ.get("BARCHART_BAR_WIDTH", 0.1)),
        "barchart_width": int(os.environ.get("BARCHART_WIDTH", 12)),
        "barchart_height": int(os.environ.get("BARCHART_HEIGHT", 5)),
    },
    "nautobot_firewall_models": {},
    "nautobot_ssot": {},
    "nautobot_circuit_maintenance": {
        "raw_notification_initial_days_since": 100,
        "raw_notification_size": 16384,
        "dashboard_n_days": 30,
        "overlap_job_exclude_no_impact": False,
        "notification_sources": []
    },
    "nautobot_data_validation_engine": {},
    "nautobot_capacity_metrics": {
        "app_metrics": {
            "models": {
                "dcim": {"Site": True, "Rack": True, "Device": True},
                "ipam": {"IPAddress": True, "Prefix": True},
             },
             "jobs": True,
             "queues": True,
             "versions": {
               "basic": True,
               "plugins": True,
            }
        }
    },
    "nautobot_golden_config": {
        "per_feature_bar_width": 0.15,
        "per_feature_width": 13,
        "per_feature_height": 4,
        "enable_backup": True,
        "enable_compliance": True,
        "enable_intended": True,
        "enable_sotagg": True,
        "sot_agg_transposer": None,
        "enable_postprocessing": False,
        "postprocessing_callables": [],
        "postprocessing_subscribed": [],
        "platform_slug_map": None,
    },
    "nautobot_plugin_nornir": {
        "nornir_settings": {
            "credentials": "nautobot_plugin_nornir.plugins.credentials.env_vars.CredentialsEnvVars",
            "runner": {
                "plugin": "threaded",
                "options": {
                    "num_workers": 20,
                },
            },
        },
    }
}