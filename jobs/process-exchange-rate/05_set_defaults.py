# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    vars = job_input.get_all_properties()
    vars["source_table"] = "exchange_rates_series"
    vars["destination_table"] = "exchange_rates_aggregates"
    job_input.set_all_properties(vars)