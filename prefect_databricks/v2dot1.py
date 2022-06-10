"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from typing import TYPE_CHECKING, Any, Dict

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


@task
async def post_2dot1_jobs_create(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new job.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/create?](
    https://{databricks_instance}/api//2.1/jobs/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was created successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/create"  # noqa
    responses = {
        200: "Job was created successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_2dot1_jobs_list(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    limit: str = None,
    offset: str = None,
    expand_tasks: str = None,
) -> Dict[str, Any]:
    """
    Retrieves a list of jobs.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.
        limit: The number of jobs to return. This value must be greater than 0 and less
            or equal to 25. The default value is 20.
        offset: The offset of the first job to return, relative to the most recently
            created job.
        expand_tasks: Whether to include task and cluster details in the response.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/list?&limit=%s&offset=%s&expand_tasks=%s](
    https://{databricks_instance}/api//2.1/jobs/list?&limit=%s&offset=%s&expand_tasks=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of jobs was retrieved successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/list"  # noqa
    responses = {
        200: "List of jobs was retrieved successfully.",
    }

    params = {
        "limit": limit,
        "offset": offset,
        "expand_tasks": expand_tasks,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def get_2dot1_jobs_get(
    databricks_instance: str,
    job_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Retrieves the details for a single job.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        job_id: The canonical identifier of the job to retrieve information about. This
            field is required.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/get?&job_id=%s](
    https://{databricks_instance}/api//2.1/jobs/get?&job_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was retrieved successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/get"  # noqa
    responses = {
        200: "Job was retrieved successfully.",
    }

    params = {
        "job_id": job_id,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def post_2dot1_jobs_reset(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Overwrites all the settings for a specific job. Use the Update endpoint to
    update job settings partially.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/reset?](
    https://{databricks_instance}/api//2.1/jobs/reset?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was overwritten successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/reset"  # noqa
    responses = {
        200: "Job was overwritten successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_2dot1_jobs_update(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Add, update, or remove specific settings of an existing job. Use the Reset
    endpoint to overwrite all job settings.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/update?](
    https://{databricks_instance}/api//2.1/jobs/update?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was updated successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/update"  # noqa
    responses = {
        200: "Job was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_2dot1_jobs_delete(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Deletes a job.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/delete?](
    https://{databricks_instance}/api//2.1/jobs/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was deleted successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/delete"  # noqa
    responses = {
        200: "Job was deleted successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_2dot1_jobs_run_now(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Run a job and return the `run_id` of the triggered run.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/run-now?](
    https://{databricks_instance}/api//2.1/jobs/run-now?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was started successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/run-now"  # noqa
    responses = {
        200: "Run was started successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_2dot1_jobs_runs_submit(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Submit a one-time run. This endpoint allows you to submit a workload directly
    without creating a job. Runs submitted using this endpoint don’t display in
    the UI. Use the `jobs/runs/get` API to check the run state after the job is
    submitted.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/submit?](
    https://{databricks_instance}/api//2.1/jobs/runs/submit?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was created and started successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/submit"  # noqa
    responses = {
        200: "Run was created and started successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_2dot1_jobs_runs_list(
    databricks_instance: str,
    active_only: str,
    completed_only: str,
    job_id: str,
    offset: str,
    limit: str,
    run_type: str,
    databricks_credentials: "DatabricksCredentials",
    expand_tasks: str = None,
    start_time_from: str = None,
    start_time_to: str = None,
) -> Dict[str, Any]:
    """
    List runs in descending order by start time.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        active_only: If active_only is `true`, only active runs are included in the results;
            otherwise, lists both active and completed runs. An active
            run is a run in the `PENDING`, `RUNNING`, or `TERMINATING`.
            This field cannot be `true` when completed_only is `true`.
        completed_only: If completed_only is `true`, only completed runs are included in the
            results; otherwise, lists both active and completed runs.
            This field cannot be `true` when active_only is `true`.
        job_id: The job for which to list runs. If omitted, the Jobs service lists runs
            from all jobs.
        offset: The offset of the first run to return, relative to the most recent run.
        limit: The number of runs to return. This value must be greater than 0 and less
            than 25\. The default value is 25\. If a request specifies a
            limit of 0, the service instead uses the maximum limit.
        run_type: The type of runs to return. For a description of run types, see
            [Run](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html
            operation/JobsRunsGet).
        databricks_credentials: Credentials to use for authentication with Databricks.
        expand_tasks: Whether to include task and cluster details in the response.
        start_time_from: Show runs that started _at or after_ this value. The value must be a UTC
            timestamp in milliseconds. Can be combined with
            _start_time_to_ to filter by a time range.
        start_time_to: Show runs that started _at or before_ this value. The value must be a
            UTC timestamp in milliseconds. Can be combined with
            _start_time_from_ to filter by a time range.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/list?&active_only=%s&completed_only=%s&job_id=%s&offset=%s&limit=%s&run_type=%s&expand_tasks=%s&start_time_from=%s&start_time_to=%s](
    https://{databricks_instance}/api//2.1/jobs/runs/list?&active_only=%s&completed_only=%s&job_id=%s&offset=%s&limit=%s&run_type=%s&expand_tasks=%s&start_time_from=%s&start_time_to=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of runs was retrieved successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/list"  # noqa
    responses = {
        200: "List of runs was retrieved successfully.",
    }

    params = {
        "active_only": active_only,
        "completed_only": completed_only,
        "job_id": job_id,
        "offset": offset,
        "limit": limit,
        "run_type": run_type,
        "expand_tasks": expand_tasks,
        "start_time_from": start_time_from,
        "start_time_to": start_time_to,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def get_2dot1_jobs_runs_get(
    databricks_instance: str,
    run_id: str,
    databricks_credentials: "DatabricksCredentials",
    include_history: str = None,
) -> Dict[str, Any]:
    """
    Retrieve the metadata of a run.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        run_id: The canonical identifier of the run for which to retrieve the metadata.
            This field is required.
        databricks_credentials: Credentials to use for authentication with Databricks.
        include_history: Whether to include the repair history in the response.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/get?&run_id=%s&include_history=%s](
    https://{databricks_instance}/api//2.1/jobs/runs/get?&run_id=%s&include_history=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was retrieved successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/get"  # noqa
    responses = {
        200: "Run was retrieved successfully.",
    }

    params = {
        "run_id": run_id,
        "include_history": include_history,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def post_2dot1_jobs_runs_cancel(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Cancels a run. The run is canceled asynchronously, so when this request
    completes, the run may still be running. The run are terminated shortly. If
    the run is already in a terminal `life_cycle_state`, this method is a no-op.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/cancel?](
    https://{databricks_instance}/api//2.1/jobs/runs/cancel?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was cancelled successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/cancel"  # noqa
    responses = {
        200: "Run was cancelled successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_2dot1_jobs_runs_get_output(
    databricks_instance: str,
    run_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Retrieve the output and metadata of a run. When a notebook task returns a value
    through the dbutils.notebook.exit() call, you can use this endpoint to
    retrieve that value. Databricks restricts this API to return the first 5 MB
    of the output. To return a larger result, you can store job results in a
    cloud storage service. This endpoint validates that the run_id parameter is
    valid and returns an HTTP status code 400 if the run_id parameter is
    invalid. Runs are automatically removed after 60 days. If you to want to
    reference them beyond 60 days, you must save old run results before they
    expire. To export using the UI, see Export job run results. To export using
    the Jobs API, see Runs export.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        run_id: The canonical identifier for the run. This field is required.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/get-output?&run_id=%s](
    https://{databricks_instance}/api//2.1/jobs/runs/get-output?&run_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run output was retrieved successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/get-output"  # noqa
    responses = {
        200: "Run output was retrieved successfully.",
    }

    params = {
        "run_id": run_id,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def post_2dot1_jobs_runs_delete(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Deletes a non-active run. Returns an error if the run is active.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/delete?](
    https://{databricks_instance}/api//2.1/jobs/runs/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was deleted successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/delete"  # noqa
    responses = {
        200: "Run was deleted successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_2dot1_jobs_runs_repair(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Re-run one or more tasks. Tasks are re-run as part of the original job run, use
    the current job and task settings, and can be viewed in the history for the
    original job run.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.1/jobs/runs/repair?](
    https://{databricks_instance}/api//2.1/jobs/runs/repair?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run repair was initiated. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.1/jobs/runs/repair"  # noqa
    responses = {
        200: "Run repair was initiated.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result
