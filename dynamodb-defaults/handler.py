import json


def dynamodb_defaults(event, context):
    fragment = add_defaults(event['fragment'])

    return {
      'requestId': event['requestId'],
      'status': 'success',
      'fragment': fragment
    }


def add_defaults(fragment):
    # Set to On-Demand Billing if not set
    if not fragment.get('BillingMode') and not fragment.get('ProvisionedThroughput'):
        fragment['BillingMode'] = 'PAY_PER_REQUEST'

    # Set default provisioned throughput if not provided
    if fragment.get('BillingMode') == 'PROVISIONED' and not fragment.get('ProvisionedThroughput'):
        fragment['ProvisionedThroughput'] = { 'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1 }

    # Add a stream if not set
    if not fragment.get('StreamSpecification'):
        fragment['StreamSpecification'] = { 'StreamViewType': 'NEW_IMAGE' }

    return fragment
