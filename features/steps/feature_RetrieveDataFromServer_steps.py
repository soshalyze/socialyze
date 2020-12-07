from behave import *

@when('user select {site_name}')
def site_select(context, site_name):
      context.site_name = site_name

@when('user selects content {content_type}')
def site_select(context, content_type):
      context.content_type = content_type

@when('user enter {site_user}')
def site_select(context, site_user):
      context.site_user = site_user

@when('user enters {instance_limit}')
def site_select(context, instance_limit):
      context.instance_limit = instance_limit

@when('send fetch request')
def fetch_request(context):
    context.response = context.test.client.post('/app/fetch/', {'site_name': context.site_name,
                                                                'content_type': context.content_type,
                                                                'site_user': context.site_user,
                                                                'instance_limit': context.instance_limit})



