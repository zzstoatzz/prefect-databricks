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
async def post_token_management_on_behalf_of_tokens(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a token on behalf of a service principal.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens?](
    https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | A on-behalf token was successfully created for the service principal. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens"  # noqa
    responses = {
        200: "A on-behalf token was successfully created for the service principal.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_token_management_tokens(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    created_by_id: str = None,
    created_by_username: str = None,
) -> Dict[str, Any]:
    """
    List all tokens belonging to a workspace or a user.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.
        created_by_id: User ID of the user that created the token.
        created_by_username: Username of the user that created the token.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/token-management/tokens?&created_by_id=%s&created_by_username=%s](
    https://{databricks_instance}/api/2.0/token-management/tokens?&created_by_id=%s&created_by_username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Tokens were successfully returned. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens"  # noqa
    responses = {
        200: "Tokens were successfully returned.",
    }

    params = {
        "created_by_id": created_by_id,
        "created_by_username": created_by_username,
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
async def delete_token_management_tokens_token_id(
    databricks_instance: str,
    token_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a token, specified by its ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        token_id: Token id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?](
    https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The token was successfully deleted. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}"  # noqa
    responses = {
        200: "The token was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_token_management_tokens_token_id(
    databricks_instance: str,
    token_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a token, specified by its ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        token_id: Token id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?](
    https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Token with specified Token ID was successfully returned. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}"  # noqa
    responses = {
        200: "Token with specified Token ID was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result
