from behave import *


@when('user accesses {url}')
def access_url(context, url):
    context.response = context.test.client.get(url, follow=True)


@when('user selects visualization type {vis}')
def select_vis(context, vis):
    context.vis_type = vis


@when('user types in dataset {dataset_handle}')
def select_dataset(context, dataset_handle):
    context.dataset_handle = dataset_handle


@then('user is redirected to {url}')
def is_on_page(context, url):
    context.test.assertRedirects(response=context.response, expected_url=url)


@given('user is logged in with username {user} and password {pw}')
def user_login(context, user, pw):
    context.test.client.login(username=user, password=pw)


@when('user clicks visualize')
def request_visualize(context):
    context.response = context.test.client.post('/app/visualize/', {'visualization_type': context.vis_type, 'dataset': context.dataset_handle})


@then('display {page}')
def check_page(context, page):
    if page == 'visualization':
        context.test.assertTemplateUsed(context.response, 'showviz.html')
    elif page == 'error':
        print(context.response.content.decode())
        context.test.assertTemplateUsed(context.response, 'errorviz.html')
