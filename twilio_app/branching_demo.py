from django_twilio.decorators import twilio_view
from .views import gather, say_words


def get_valid_digit(request):
    digit = request.POST.get('Digits', '1')
    # For this demo only 1 or 2 are valid. Return 1, if invalid selection.
    if digit != '2':
        digit = '1'
    return digit


@twilio_view
def gather_branch(request):
    words = "Press 1 for Branch A, Press 2 for Branch B"
    handler_url_name = "process_branch"
    return gather(request, words=words, handler_url_name=handler_url_name)


@twilio_view
def process_branch(request):
    redirect = {'1': gather_branch_a, '2': gather_branch_b}
    digit = get_valid_digit(request)
    function = redirect[digit]
    return function(request)


@twilio_view
def gather_branch_a(request):
    words = "Branch A - Press 1 to hang up, Press 2 for greeting"
    handler_url_name = "process_branch_a"
    return gather(request, words=words, handler_url_name=handler_url_name)


@twilio_view
def process_branch_a(request):
    phrases = {'1': 'Branch A - Goodbye', '2': 'Branch A - Hello monkey'}
    digit = get_valid_digit(request)
    return say_words(request, words=phrases[digit])


@twilio_view
def gather_branch_b(request):
    words = "Branch B - Press 1 to hang up, Press 2 for greeting"
    handler_url_name = "process_branch_b"
    return gather(request, words=words, handler_url_name=handler_url_name)


@twilio_view
def process_branch_b(request):
    phrases = {'1': 'Branch B - Goodbye', '2': 'Branch B - Hello monkey'}
    digit = get_valid_digit(request)
    return say_words(request, words=phrases[digit])
